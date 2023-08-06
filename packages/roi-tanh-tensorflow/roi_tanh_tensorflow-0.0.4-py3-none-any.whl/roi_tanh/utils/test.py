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


color_correspondance = {
    0: [0, 0, 0],
    1: [50, 50, 0],
    2: [150, 50, 0],
    3: [50, 150, 0],
    4: [0, 50, 150],
    5: [50, 0, 150],
    6: [0, 150, 50],
    7: [150, 0, 50],
    8: [250, 250, 250],
    9: [250, 0, 0],
    10: [0, 250, 0],
    11: [0, 0, 250],
    12: [0, 250, 250],
    13: [250, 250, 0],
    14: [250, 0, 250],
    15: [100, 0, 100],
    16: [100, 100, 100],
    17: [0, 100, 0],
    18: [100, 0, 100],
    255: [200, 100, 0],
}


def convert_labels_in_image(lbls: np.ndarray) -> np.ndarray:
    global color_correspondance
    shape = list(lbls.shape)
    shape[-1] = 3
    output = np.zeros(shape=shape)
    for i in range(lbls.shape[-1]):
        output[np.where(lbls[..., i] >= 0.9)] = color_correspondance[i]
    return output


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
    cv2.imwrite(
        os.path.join(os.getcwd(), "unit_test", "new_label.png"),
        convert_labels_in_image(lbls=new_label),
    )
