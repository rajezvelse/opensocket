import sys
import argparse


class BaseCommand:
    description = "Base command"

    def __init__(self, prog):
        self.parser = argparse.ArgumentParser(description=self.description, prog=prog)

    def create_args(self):
        return

    def validate_args(self, *args):
        return self.parser.parse_args(*args)

    def execute(self, **kwargs):
        print(kwargs)

    def run_from_argv(self, *args):
        self.create_args()
        args = self.validate_args(*args)

        return self.execute(**vars(args))
