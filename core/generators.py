from email.mime import image
import imp
from typing import Any, Union
from qrcode.image.pil import PilImage
import qrcode


def generate_default(data: Any) -> Union[PilImage, Any]:
    image = qrcode.make(data=data)
    return image


def generate_custom(data: any, version: int = 1, error_correction: int = qrcode.ERROR_CORRECT_L, box_size: int = 10, border: int = 4,
                    optimize_image: bool = True, background_color: tuple(int, int, int) = (250, 250, 250),
                    foreground_color: tuple(int, int, int) = (0, 0, 0)) -> Union[PilImage, Any]:
    _qrcode = qrcode.QRCode(
        version=version, error_correction=error_correction, box_size=box_size, border=border)
    _qrcode.add_data(data, optimize=20 if optimize_image else 0)
    _qrcode.make()
    return _qrcode.make_image(back_color=background_color, fill_color=foreground_color)
