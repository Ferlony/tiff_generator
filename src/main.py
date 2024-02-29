from os import sep, path
import argparse

from tiff_generator import TiffGenerator


def normalize_path(dir_path):
    dir_path = dir_path if path.isabs(dir_path) else path.abspath(dir_path)
    dir_path = dir_path if dir_path[-1] == sep else dir_path + sep
    return dir_path


def main(**kwargs):
    dirs = list(map(normalize_path, kwargs["dirs"]))
    out = normalize_path(kwargs["out"])

    TiffGenerator().generate_tiff(dirs, out)
    return


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument(
        "-d",
        "--dirs",
        required=True,
        nargs="+",
        help="Provide relative or absolute path to dirs with images to get their union in tiff\n"\
             "Usage: -d ./dir1 /home/user/dir2 / --dirs=./dir1 /home/user/dir2"
    )

    arg_parser.add_argument(
        "-o",
        "--out",
        type=str,
        required=False,
        nargs="?",
        action="store",
        default=f"..{sep}out{sep}",
        help="Used to set output\n"\
             "By default puts into out in project root\n"\
             "Usage: -o ./dir1 / --out=/home/user/dir2"
    )

    pargs = arg_parser.parse_args()
    main(dirs=pargs.dirs, out=pargs.out)
