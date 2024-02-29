from typing import Union
from pathlib import Path

import magic
from imageio.plugins.tifffile_v3 import TifffilePlugin
import imageio.v3 as iio
import imageio.core.request


class TiffGenerator:

    @staticmethod
    def __generate_tiff(images: list, out: str) -> None:
        tiff_plugin = TifffilePlugin(imageio.core.request.Request(uri=(out + 'Result.tif'), mode='w'))
        for image in images:
            tiff_plugin.write(ndimage=iio.imread(image), contiguous=True)

    @staticmethod
    def __check_if_allowed_file_format(file_path: Union[str, Path]) -> bool:
        return True if "image/" == magic.from_file(file_path, mime=True)[:6] else False

    def __get_allowed_files_in_dir(self, dir_path: str) -> list:
        allowed_files = []
        for each in Path(dir_path).iterdir():
            if self.__check_if_allowed_file_format(each):
                allowed_files.append(each)

        return allowed_files

    def generate_tiff(self, dirs: list, out: str) -> None:
        images: list = []
        for dir_path in dirs:
            images.extend(self.__get_allowed_files_in_dir(dir_path))
        self.__generate_tiff(images, out)
        return
