from email.mime import image
import imp
from typing import Any, Union
from qrcode.image.pil import PilImage
import qrcode




def generate_default(data: Any) -> Union[PilImage, Any]:
    image = qrcode.make(data=data)
    return image