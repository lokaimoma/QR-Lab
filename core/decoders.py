from typing import Union, List
from cv2 import QRCodeDetector, imread
from pyzbar.pyzbar import decode, Decoded
from PIL import Image


# cv2 lib doesn't work in some cases. Left it for reference purposes.
def decode_qr_code(image_file_path: str) -> Union[bool, tuple]:
    image = imread(filename=image_file_path)
    value, points, straight_code = QRCodeDetector().detectAndDecode(image)
    if points is None:
        return False
    return (value, points, straight_code)


def decode_qr_code_(image_file_path: str) -> List[Decoded]:
    return decode(Image.open(image_file_path))