#!/usr/bin/env python3
# -*- coding: utf8 -*-

# pylint: disable=C0111  # docstrings are always outdated and wrong
# pylint: disable=W0511  # todo is encouraged
# pylint: disable=C0301  # line too long
# pylint: disable=R0902  # too many instance attributes
# pylint: disable=C0302  # too many lines in module
# pylint: disable=C0103  # single letter var names, func name too descriptive
# pylint: disable=R0911  # too many return statements
# pylint: disable=R0912  # too many branches
# pylint: disable=R0915  # too many statements
# pylint: disable=R0913  # too many arguments
# pylint: disable=R1702  # too many nested blocks
# pylint: disable=R0914  # too many local variables
# pylint: disable=R0903  # too few public methods
# pylint: disable=E1101  # no member for base
# pylint: disable=W0201  # attribute defined outside __init__
# pylint: disable=R0916  # Too many boolean expressions in if statement


import os
#import sys
from pathlib import Path

import click
from asserttool import eprint
from asserttool import ic


class chdir():
    def __init__(self, path):
        self.orig_path = Path(os.getcwd())
        self.path = Path(os.fsdecode(path)).resolve()

    def __enter__(self):
        os.chdir(self.path)
        #ic(self.path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.orig_path)


@click.command()
@click.argument("path", type=str, nargs=1)
@click.option('--verbose', is_flag=True)
@click.option('--debug', is_flag=True)
@click.pass_context
def cli(ctx,
        path,
        verbose: bool,
        debug: bool,):

    ctx.ensure_object(dict)
    ctx.obj['verbose'] = verbose
    ctx.obj['debug'] = debug
    with chdir(path):
        os.system('pwd')
        os.system("ls -al")

    os.system('pwd')


