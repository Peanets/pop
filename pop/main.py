# -*- coding: utf-8 -*-
import os
import sys
import click
from controller import Controller

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

pass_controller = click.make_pass_decorator(Controller)
cmd_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),'commands'))

class ComplexCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = []
        for dirname, dirnames, filenames in os.walk(cmd_folder):
            for subdirname in dirnames:
                for filename in os.listdir(os.path.join(dirname, subdirname)):
                    if filename[0:-3]==subdirname:
                        rv.append(filename[0:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        try:
            if sys.version_info[0] == 2:
                name = name.encode('ascii', 'replace')
            mod = __import__('pop.commands.'+name+'.' + name,
                             None, None, ['cli'])
        except ImportError:
            raise
        return mod.cli

@click.command(cls=ComplexCLI, context_settings=CONTEXT_SETTINGS)
@click.option('-home', envvar='HOME', default='')
@click.option('-pop_home', envvar='POP_HOME', default='.pop')
@click.option('-project_home', envvar='POP_PROJECT_HOME', default='Projects')
@click.option('-v', '--verbose', is_flag=True, help='Enables verbose mode.')
@click.pass_context
def cli(ctx, home, pop_home, project_home, verbose):
    ctx.obj = Controller(ctx, home, pop_home, project_home, verbose);