#!/usr/bin/env python3
# -*- coding: utf8 -*-

import os
from pathlib import Path
from typing import Union

import click
import sh
from epprint import epprint


class chdir:
    def __init__(
        self,
        path,
        *,
        verbose: Union[bool, int, float],
        unwrite: bool = False,
    ):
        self.verbose = verbose
        self.orig_path = Path(os.getcwd())
        self.path = Path(os.fsdecode(path)).resolve()
        self.unwrite = unwrite

    def __enter__(self):
        os.chdir(self.path)
        if self.verbose:
            epprint(f"{self.path=}")
        if self.unwrite:
            sh.chmod("+w", ".")

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.unwrite:
            sh.chmod("-w", ".")
        os.chdir(self.orig_path)


@click.command()
@click.argument("path", type=str, nargs=1)
@click.option("--verbose", is_flag=True)
@click.pass_context
def cli(
    ctx,
    path: str,
    verbose: Union[bool, int, float],
):

    with chdir(path, verbose=verbose):
        os.system("pwd")
        os.system("ls -al")

    os.system("pwd")
