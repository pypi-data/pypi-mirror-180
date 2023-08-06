from .fastwarping import FastTanhWarping
from typing import Tuple, List
import tensorflow as tf
import numpy as np
from PIL import Image


def labels2boxes(
    input: np.ndarray,
    left_eye_class: List[int] = [2, 4],
    right_eye_class: List[int] = [3, 5],
    nose_class: List[int] = [6],
    mouth_class: List[int] = [7, 8, 9],
) -> tf.Tensor:
    """
    extracts bbox from labels

    Args:
        input: input labels
        left_eye_class: class indices associated with the left eye
        right_eye_class: class indices associated with the right eye
        nose_class: class indices associated with the nose
        mouth_class: class indices associated with the mouth
    """
    images = np.transpose(input, axes=(2, 0, 1))
    leye_image = np.sum(images[left_eye_class], axis=0)
    reye_image = np.sum(images[right_eye_class], axis=0)
    nose_image = np.sum(images[nose_class], axis=0)
    mouth_image = np.sum(images[mouth_class], axis=0)
    leye = Image.fromarray(leye_image).getbbox()
    reye = Image.fromarray(reye_image).getbbox()
    nose = Image.fromarray(nose_image).getbbox()
    mouth = Image.fromarray(mouth_image).getbbox()
    if leye is None:
        leye = [0, 0, 0, 0]
    if reye is None:
        reye = [0, 0, 0, 0]
    if nose is None:
        nose = [0, 0, 0, 0]
    if mouth is None:
        mouth = [0, 0, 0, 0]
    boxes = np.array((leye, reye, nose, mouth))
    assert boxes.shape == (4, 4)
    return boxes


def sharpen_labels(label: tf.Tensor) -> tf.Tensor:
    """
    ensures that the labels are ones an zeros

    Args:
        label: one hot labels (bilinear)
    """
    return tf.math.round(tf.nn.softmax(logits=label, axis=-1))


def TanhWarping(
    image: np.ndarray, label: np.ndarray, size: Tuple[int]
) -> Tuple[tf.Tensor, tf.Tensor]:
    """
    apply tanh warping based on
    https://openaccess.thecvf.com/content_CVPR_2019/papers/Lin_Face_Parsing_With_RoI_Tanh-Warping_CVPR_2019_paper.pdf

    Args:
        image: images to rectify
        label: one hot labels
        size: output target size
    """
    boxes = labels2boxes(np.array(label))
    warped_image = FastTanhWarping(image=image, boxes=boxes, output_size=size)
    warped_labels = FastTanhWarping(image=label, boxes=boxes, output_size=size)
    warped_labels = sharpen_labels(warped_labels)
    return warped_image, warped_labels
