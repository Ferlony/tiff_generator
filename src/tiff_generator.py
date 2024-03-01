from typing import Union
from pathlib import Path

from PIL import Image
from imageio.core.request import Request
from imageio.plugins.tifffile_v3 import TifffilePlugin
import magic
import imageio.v3 as iio


class TiffGenerator:

    def __init__(self, padding_right=50, padding_top=50) -> None:
        self.__padding = (padding_right, padding_top)

    @property
    def padding(self) -> tuple[int, int]:
        return self.__padding

    @staticmethod
    def __check_if_allowed_file_format(file_path: Union[str, Path]) -> bool:
        return True if "image" == magic.from_file(file_path, mime=True)[:5] else False

    @staticmethod
    def __generate_tiff(images: list, out: str) -> None:
        ndimages = []
        for image in images:
            ndimages.append(iio.imread(image))

        with TifffilePlugin(Request(uri=(out + 'Result.tif'), mode='w')) as tiff_plugin:
            tiff_plugin.write(ndimage=ndimages,
                              resolutionunit='INCH',
                              compression='LZW',
                              predictor=True,
                              photometric='rgb',
                              subfiletype=0
            )

    @staticmethod
    def __max_size_in_images(images: list) -> tuple[int, int]:
        x_images = []
        y_images = []

        for each in images:
            image = Image.open(each)
            x, y = image.size
            x_images.append(x)
            y_images.append(y)

        return (max(x_images), max(y_images))

    def __create_blank_image(self, images: list, rows: int, columns: int) -> Image.Image:
        max_x, max_y = self.__max_size_in_images(images)
        res_x = (max_x + self.padding[0]) * rows + self.padding[0]
        res_y = (max_y + self.padding[1]) * columns + self.padding[1]

        return Image.new('RGB', (res_x, res_y), color='white')

    def __create_image_table(self, images: list, out: str, rows_in_res: int) -> None:
        rows = len(images) // rows_in_res
        columns = len(images) // rows

        image_table = self.__create_blank_image(images, rows, columns)

        x_offset = 0 + self.padding[0]
        y_offset = 0 + self.padding[1]
        row_item_counter = 0

        for each in images:

            image_data = iio.imread(each)
            x, y = Image.open(each).size

            image_table.paste(Image.fromarray(image_data), (x_offset, y_offset))

            if row_item_counter < rows - 1:
                x_offset += x + self.padding[0]
                row_item_counter += 1

            else:
                row_item_counter = 0
                x_offset = 0 + self.padding[0]
                y_offset += y + self.padding[1]

        image_table.save(out + 'Result.tif', compression="tiff_lzw")

    def __get_allowed_files_in_dir(self, dir_path: str) -> list:
        allowed_files = []
        for each in Path(dir_path).iterdir():
            if self.__check_if_allowed_file_format(each):
                allowed_files.append(each)

        return allowed_files

    def generate_tiff(self, dirs: list, out: str, rows: Union[None, int]) -> None:
        images = []
        for dir_path in dirs:
            images.extend(self.__get_allowed_files_in_dir(dir_path))

        if rows:
            self.__create_image_table(images, out, rows)
        else:
            self.__generate_tiff(images, out)
        return
