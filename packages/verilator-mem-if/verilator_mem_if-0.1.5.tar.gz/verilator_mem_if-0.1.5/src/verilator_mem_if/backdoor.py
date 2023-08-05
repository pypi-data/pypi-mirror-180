# Copyright IDEX Biometrics
# Licensed under the MIT License, see LICENSE
# SPDX-License-Identifier: MIT

import sys
import argparse
import logging
from pathlib import Path
from contextlib import contextmanager
from intelhex import IntelHex
from veriloghex import VerilogHex
from bincopy import BinFile

from .backdoor_memory_interface import BackdoorMemoryInterface
from . import __version__

LOG = logging.getLogger()
logging.basicConfig(format="%(levelname)s:%(name)s: %(message)s")

class IllegalFormatError(Exception):
    pass

@contextmanager
def file_or_stdout(file):
    if file is None:
        yield sys.stdout
    else:
        with Path(file).open('w') as f:
            yield f
            

def int_from_dec_or_hex_string(astring):
    """Converts string decimal or hex arguments to int. """
    try:
        return int(astring,0)
    except ValueError:
        raise argparse.ArgumentError("expecting a hex string or integer for the address")


def get_format(hexfile):
    try:
        return {
            '.vmem': 'verilog',
            '.hex' : 'intel',
            '.ihex': 'intel'
        }[hexfile.suffix]
    except KeyError:
        raise IllegalFormatError(
            f"suffix '{hexfile.suffix}' of file '{hexfile.name}' does not match a supported file format: [.vmem, .hex, .ihex]"
        )


def load(args):
    """Load memory from file. """

    hexfile = Path(args.filename)
    format = args.format or get_format(hexfile)

    with BackdoorMemoryInterface(args.hostname, args.port) as bd:
        hex = BinFile(hexfile.name) if format == 'intel' else VerilogHex(hexfile.name)
        for address,data in hex:
            bd.write_memory_block8(address,data)


def dump(args):
    """Dump memory contents to STDOUT or file. """

    with BackdoorMemoryInterface(args.hostname, args.port) as bd:
        data = bd.read_memory_block8(args.address, args.size)
    
    with file_or_stdout(args.output) as f:
        if args.format == "verilog":
            vmem = VerilogHex(data, offset=args.address)
            a = vmem.tovmem()
            f.write(a)
        elif args.format in ['intel', 'hex']:
            ihex = IntelHex()
            ihex.frombytes(data)
            if args.format == 'hex':
                ihex.dump(f)
            else:
                ihex.tofile(f, 'hex')
        else:
            raise ValueError(f"invalid format '{args.format}'")

def init(args):
    """Initialize a RAM with a specific byte value. """

    with BackdoorMemoryInterface(args.hostname, args.port) as bd:
        # The BackdoorMemoryInterface has a maximum payload size of 32KB so
        # we split anything larger into chunks.
        chunk_size = 2**15
        chunks = args.size // chunk_size
        if args.size % chunk_size:
            raise ValueError("sizes that are not multiples of 32KB unsupported")
        address = args.address
        for _ in range(chunks):
            bd.write_memory_block8(
                address,
                bytearray([args.init_value] * chunk_size)
            )
            address += chunk_size


formatter = lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=80, width=200)

def parse_args():
    parser = argparse.ArgumentParser(
        description="A script for loading and dumping memory",
        formatter_class=formatter
    )
    subparsers = parser.add_subparsers()

    # Global options
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
        help="display the version"
    )
    parser.add_argument(
        "--hostname", 
        default="localhost", 
        type=str, 
        help="specify the hostname to connect to (default: %(default)s)"
    )
    parser.add_argument(
        "--port",
        default=5557,
        type=int,
        help="specify the port (default: %(default)s)"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="enable verbose printing"
    )


    # init subparser
    parser_init = subparsers.add_parser(
        "init",
        help="initialize a memory with a fixed byte value"
    )
    parser_init.add_argument(
        "--init-value",
        type=int_from_dec_or_hex_string,
        default="0xff",
        help="byte value to use for flash initialization (default: %(default)s)"
    )
    parser_init.add_argument(
        "--address",
        default=0x800000,
        type=int_from_dec_or_hex_string,
        help="specify the start address of the memory region (default: %(default)s)"
    )
    parser_init.add_argument(
        "--size",
        default=0x80000,
        type=int_from_dec_or_hex_string,
        help="specify the size of the memory in bytes (default: %(default)s)"
    )
    parser_init.set_defaults(func=init)


    # load subparser
    parser_load = subparsers.add_parser(
        "load",
        help="load memory from a file (supported formats are Verilog hex and Intel hex)"
    )
    parser_load.add_argument(
        "filename",
        help="specify the input file name (format auto-detected with .vmem and .[i]hex file extensions)"
    )
    parser_load.add_argument(
        "-f",
        "--format",
        choices=["intel", "verilog"],
        help="override the file type detection"
    )
    parser_load.set_defaults(func=load)


    # dump parser
    parser_dump = subparsers.add_parser(
        "dump",
        help="dump memory to a file or stdout (supported formats are hexdump, Intel hex and Verilog hex)"
    )
    parser_dump.add_argument(
        "address",
        type=int_from_dec_or_hex_string,
        help="memory address to dump"
    )
    parser_dump.add_argument(
        "size",
        type=int,
        help="number of bytes to dump"
    )
    parser_dump.add_argument(
        "-f",
        "--format",
        default="hex",
        choices=["hex", "intel", "verilog"],
        help="the dump format to use (default: %(default)s)"
    )
    parser_dump.add_argument(
        "--vmem-width",
        type=int,
        default=32,
        choices=[8, 16, 32, 64, 128],
        help="specify the bit width for VMEM output (default: %(default)s)"
    )
    parser_dump.add_argument(
        "-o",
        "--output",
        type=str,
        default=None,
        help="dump to a file instead of STDOUT"
    )
    parser_dump.set_defaults(func=dump)

    args = parser.parse_args()

    if hasattr(args, "func"):
        return args
    if hasattr(args, "subparser"):
        args.subparser.print_help()
    else:
        parser.print_help()
        return None

def main():
    args = parse_args()
    if not args:
        exit(0)

    level = logging.DEBUG if args.debug else logging.INFO
    LOG.setLevel(level)
    
    args.func(args)

if __name__ == "__main__":
    main()