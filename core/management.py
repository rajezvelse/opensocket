import functools
import os
import pkgutil
import sys
from collections import defaultdict
from difflib import get_close_matches
from importlib import import_module

from core.BaseCommand import BaseCommand

DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def find_commands(command_dir):
    """
    Given a path to a commands directory, return a list of all the command
    names that are available.
    """
    return [name for _, name, is_pkg in pkgutil.iter_modules([command_dir])
            if not is_pkg and not name.startswith('_')]


def load_command_class(name, prog):
    module = import_module('commands.%s' % (name,))
    return module.Command(prog)


@functools.lru_cache(maxsize=None)
def get_commands():
    commands_dir = os.path.join(DIR, 'commands')

    return find_commands(commands_dir)


class ManagementUtility:
    """
    Encapsulate the logic of the django-admin and manage.py utilities.
    """

    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]

    def fetch_command(self, subcommand, prog):

        commands = get_commands()

        if subcommand not in commands:
            sys.stderr.write('Unknown command: %r\n' % subcommand)
            sys.exit(1)

        klass = load_command_class(subcommand, prog)
        return klass

    def execute(self):
        """
        Given the command-line arguments, figure out which subcommand is being
        run, create a parser appropriate to that command, and run it.
        """
        try:
            subcommand = self.argv[1]
        except IndexError:
            subcommand = '--help'  # Display help if no arguments were given.

        if subcommand == '--help' or subcommand == '-h':
            commands = get_commands()

            print(
                "\n\33[32mType '{} help <subcommand>' for help on a specific subcommand.\33[0m \n\nAvailable subcommands:".format(os.path.basename(self.argv[0])))
            print("\33[33m")
            for c in commands:
                print("  -", c)

            print("\33[0m")
        else:
            cmd = self.fetch_command(subcommand, prog="{} {}".format(os.path.basename(self.argv[0]), self.argv[1]))
            return cmd.run_from_argv(self.argv[2:])


def execute_from_command_line(argv=None):
    """Run a ManagementUtility."""
    utility = ManagementUtility(argv)
    utility.execute()
