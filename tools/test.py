#!/usr/bin/env python3
"""
Tests a spoj solution.
"""

# TODO
# - time execution
# - run several times
# - set executable bit on command if it doesn't already have it.
# - diff, if any


import sys
import argparse
import subprocess
from io import StringIO
import itertools


def parse_options(args):
    parser = argparse.ArgumentParser(description='Tests a spoj solution.')
    parser.add_argument('command', type=str,
                        help='The script that implements the spoj solution.\nMust be executable, read input from stdin and print output to stdout.')
    parser.add_argument('input_file', type=str,
                        help='Input file for the spoj solution')
    parser.add_argument('expected_output_file', type=str,
                        help='File with the expected output for the spoj solution, given input_file')
    parser.add_argument('-v', '--verbose', action='store_true', default=False,
                        help='Verbose output')
    parsed = parser.parse_args(args)
    return parsed


def main(args):
    options = parse_options(args)

    call = subprocess.Popen([options.command], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = call.communicate(open(options.input_file, "rb").read())
    stdout = stdout.strip()
    stderr = stderr.strip()

    if options.verbose and stdout:
        print("Output:\n{}\n\nEnd of output.".format(stdout))
    if stderr:
        print("Error output:\n{}\n\nEnd of error output".format(stderr))

    if call.returncode != 0:
        print("Command '{}' returned non-zero ({}):".format(command), call.returncode)
        return call.returncode

    expected = open(options.expected_output_file, "rb").read()
    match = stdout.strip() == expected.strip()

    if not match:
        print("Expected and actual output don't match!")
        print("Expected:")
        print(expected.decode())
        print("Actual:")
        print(stdout.decode())
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
