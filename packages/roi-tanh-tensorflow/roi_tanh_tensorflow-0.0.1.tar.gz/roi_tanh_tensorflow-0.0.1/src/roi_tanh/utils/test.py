import tensorflow as tf
import numpy as np
from typing import Tuple
import cv2
import sys
import os


class labelConvertor_helen:
    def __init__(self):
        super(labelConvertor_helen, self).__init__()
        self.correspondance = {
            0: "unknown",
            1: "unknown",
            2: "unknown",
            3: "unknown",
            4: "unknown",
            5: "unknown",
            6: "unknown",
            7: "unknown",
            8: "unknown",
            9: "unknown",
            10: "unknown",
            11: "unknown",
        }

    def __call__(self, map: tf.Tensor) -> tf.Tensor:
        map[np.where(map >= 11)] = -1

        return tf.one_hot(map, depth=len(self.correspondance) - 1).numpy()


mask_convertor = labelConvertor_helen()


def decode_image(image_path: str, ismask: bool) -> np.ndarray:
    """
    load and converts an iamge or label

    Args:
        image_path: path to file
        ismask: boolean to know if we are dealing with a label or not
    """
    if ismask:
        decoded_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    else:
        decoded_image = cv2.imread(image_path)
    if decoded_image is None:
        print(image_path, "error")
        sys.exit()
    if ismask:
        global mask_convertor
        image = decoded_image.astype(np.uint8)
        image[np.where(image >= 11)] = -1
        image = mask_convertor(image)
    else:
        image = decoded_image.astype(np.float32)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)
    return image


def run_a_unit_test() -> Tuple[np.ndarray, np.ndarray]:
    """
    collects an example for unit testing
    """
    return (
        decode_image(
            image_path=os.path.join(os.getcwd(), "unit_test", "2546515404_1_image.jpg"),
            ismask=False,
        ),
        decode_image(
            image_path=os.path.join(os.getcwd(), "unit_test", "2546515404_1_label.png"),
            ismask=True,
        ),
    )


def save_example_pair(new_image: np.ndarray, new_label: np.ndarray) -> None:
    """
    save the warped images and corresponding labels

    Args:
        new_image: image to save
        new_label: warped label to save
    """
    if not isinstance(new_image, np.ndarray):
        new_image = new_image.numpy()
    if not isinstance(new_label, np.ndarray):
        new_label = new_label.numpy()
    cv2.imwrite(
        os.path.join(os.getcwd(), "unit_test", "new_image.jpg"),
        cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB),
    )
