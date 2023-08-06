# import files
import argparse
from os import system, popen
from os.path import isfile, isdir, abspath, dirname
from shutil import rmtree
from sys import exit, stderr


# functions
error_log = stderr.write


def error(message):
    global parser
    error_log(f"usage: {parser.usage}\n"
              f"{parser.prog}: error: {message}")


def check_arg():
    global argv, parser

    if not argv.file:
        argv = parser.parse_args(("-h",))
        exit(0)

    if not isfile(argv.file):
        error(f'"{argv.file}" is not a file')
        exit(1)

    if not isdir(argv.dir):
        error(f'"{argv.dir} is not a directory')


# create parser
parser = argparse.ArgumentParser(prog="pypyd", usage="pypyd  <file> -d <dir>")
parser.add_argument("file", help="file to change")
parser.add_argument("-d", "--dir", help="out dir", const=None)
argv = parser.parse_args()
if argv.dir is None:
    argv.dir = dirname(argv.file)

argv.file = abspath(argv.file)
argv.dir = abspath(argv.dir)
# check argv
check_arg()

_cwd = popen("cd").read()
system(f"cd {argv.dir}")
with open("setup.pypyd.py", "w") as f:
    f.write(
        f"from setuptools import setup\n"
        f"from Cython.Build import cythonize\n"
        f"setup(\n"
        f'    ext_modules=cythonize(r"{argv.file}")\n'
        f")"
        )
system("python setup.pypyd.py build_ext --inplace")

system("del test.c")
rmtree(r".\build")
system(f"cd {_cwd}")
system("del test.c")
rmtree(r".\build")
system(f"cd {_cwd}")
