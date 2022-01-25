from typing import Union
from cv2 import QRCodeDetector, imread


def decode_qr_code(image_file_path: str) -> Union[bool, tuple]:
    image = imread(filename=image_file_path)
    value, points, straight_code = QRCodeDetector().detectAndDecode(image)
    if points is None:
        return False
    return (value, points, straight_code)
