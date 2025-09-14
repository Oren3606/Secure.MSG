"""
Pass arguments from terminal emulator for launch

Usage:
secmsg [e | l | c] [options]
more info with `secmsg -h`
"""
from argparse import ArgumentParser

parser = ArgumentParser(
    prog="Secure.MSG",
    usage="secmsg [establish | link | configure] [options]",
    epilog="Secure.MSG is a secure messaging platform",
    description="Secure decentralized messaging platform"
)

parser.add_argument("mode",
                    choices=["establish", "e", "link", "l", "configure", "c"],
                    help="Mode of operation")

parser.add_argument("target",
                    nargs="?",
                    type=str,
                    help="Target for connecting to a session")

parser.add_argument("--username", "-u",
                    type=str,
                    help="Username for session")

parser.add_argument("--savefile", "-s",
                    nargs="?",
                    const=True,
                    type=str,
                    help="File for saving session. Leave empty for automatic name")

cli_args = parser.parse_args()
