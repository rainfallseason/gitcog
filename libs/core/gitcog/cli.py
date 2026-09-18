import argparse
import logging

from rich.console import Console
from rich.logging import RichHandler


def parser_init() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
                    prog="gitcog",
                    description="Generate config files from toml")
    return parser

def read_available_plugins() -> dict:
    from pathlib import Path

    import tomllib
    source_dir = Path(__file__).resolve().parent
    asset_path = source_dir / "assets" / "known_plugins.toml"
    with open(asset_path, mode="rb") as plugin_data:
        data = tomllib.load(plugin_data)
    return data

def main():
    logging.basicConfig(level="INFO", handlers=[RichHandler(rich_tracebacks=True)])
    parser = parser_init()
    parser.print_help()
