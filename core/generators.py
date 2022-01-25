from email.mime import image
import imp
from typing import Any, Union
from qrcode.image.pil import PilImage
import qrcode


def generate_default(data: Any) -> Union[PilImage, Any]:
    image = qrcode.make(data=data)
    return image


def generate_custom(data: any, version: int, error_correction: int, box_size: int, border: int, optimize_image: bool) -> Union[PilImage, Any]:
    _qrcode = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border
    )
    _qrcode.add_data(data, optimize=20 if optimize_image else 0)
    _qrcode.make()
    return _qrcode.make_image()
