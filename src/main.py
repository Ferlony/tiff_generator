from os import (sep, path, getcwd, chdir, mkdir)
from pathlib import Path
import argparse

from tiff_generator import TiffGenerator


def normalize_path(dir_path):
    dir_path = dir_path if path.isabs(dir_path) else path.abspath(dir_path)
    dir_path = dir_path if dir_path[-1] == sep else dir_path + sep
    return dir_path


def get_out_path() -> str:
    default_cwd = getcwd()
    chdir(Path(str(Path(__file__).parent.resolve()) + f"{sep}..{sep}"))
    out_path = str(getcwd()) + f"{sep}out{sep}"
    chdir(default_cwd)
    return out_path


def main(**kwargs):
    dirs = list(map(normalize_path, kwargs["dirs"]))
    out = normalize_path(kwargs["out"])
    rows = kwargs["rows"]

    if not path.exists(out):
        raise FileNotFoundError

    TiffGenerator().generate_tiff(dirs, out, rows)
    return


if __name__ == "__main__":

    DEFAULT_OUT_PATH = get_out_path()

    if not path.exists(DEFAULT_OUT_PATH):
        mkdir(DEFAULT_OUT_PATH)

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument(
        "-d",
        "--dirs",
        required=True,
        nargs="+",
        help="Provide relative or absolute path to dirs with images to get their union in tiff\n"\
             "Usage: -d ./dir1 /home/user/dir2 OR --dirs=./dir1 /home/user/dir2"
    )

    arg_parser.add_argument(
        "-r",
        "--rows",
        type=int,
        required=False,
        nargs="?",
        action="store",
        default=None,
        help="Use to generate singlepage tiff file from images\n"\
             "Usage: -r 2 OR --rows=3"
    )

    arg_parser.add_argument(
        "-o",
        "--out",
        type=str,
        required=False,
        nargs="?",
        action="store",
        default=DEFAULT_OUT_PATH,
        help="Used to set output\n"\
             "By default puts into out in project root\n"\
             "Usage: -o ./dir1 OR --out=/home/user/dir2"
    )

    pargs = arg_parser.parse_args()
    main(dirs=pargs.dirs, out=pargs.out, rows=pargs.rows)
