import argparse
import logging
import sys

from rich.console import Console
from rich.logging import RichHandler

if sys.version_info >= (3, 15): # Refer to PEP 810
    import lazy_import
else:
    import lazy_loader

    pathlib = lazy_loader.load("pathlib")

    ruamel = lazy_loader.load("ruamel")
    tomllib = lazy_loader.load("tomllib")




def parser_init() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
                    prog="gitcog",
                    description="Generate config files from toml")
    parser.add_argument("-l", "--load", metavar="PACKAGE", help="Load ", required=True)
    parser.add_argument("-p", "--path", metavar="file", help="Load from this path", required=True)
    parser.add_argument("--allow-unnoficial-package", action="store_true", help="You should NOT use this option") # これは--no-preserve-rootと同じ趣旨の安全策 これがなければERRORに投げて終了、あったらWARNINGで警告
    return parser

def read_available_plugins() -> dict:
    source_dir = pathlib.Path(__file__).resolve().parent
    asset_path = source_dir / "assets" / "known_plugins.toml"
    with open(asset_path, mode="rb") as plugin_data:
        data = tomllib.load(plugin_data)
    return data

# def parse_config(allow_yaml: bool) -> dict:
#     if allow_yaml:
#         do_something

# def check_filetype(path):
#     do_something ファイルタイプがtomlかyamlかそれ以外かを確かめよう

def main():
    logging.basicConfig(level="INFO", handlers=[RichHandler(rich_tracebacks=True)])
    parser = parser_init()
    parser.print_help()

main()