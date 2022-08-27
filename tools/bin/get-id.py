#!/usr/bin/env python
"""
Script for generating puzzle ID.
"""

# --- Imports

# External packages
import shortuuid
import typer


# --- Main program

def main() -> None:
    """
    Generate puzzle ID.
    """
    typer.echo(shortuuid.uuid())


# --- Run app

if __name__ == "__main__":
    typer.run(main)
