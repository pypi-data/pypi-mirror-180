from .grid_sampler import bilinear_sampler
import tensorflow as tf
from skimage import transform as trans
import numpy as np
from typing import Tuple, Optional


def atanh(x: tf.Tensor) -> tf.Tensor:
    """
    Implements the atanh function

    Args:
        x: tensor to activate element-wise.
    """
    return 0.5 * tf.math.log((1 + x) / (1 - x))


def apply_mat_tensor(coords: np.ndarray, matrix: np.ndarray) -> np.ndarray:
    """
    Applies the matrix tensor to the coordinates

    Args:
        coords: array of coordinates to modify
        matrix: matrix array for coords change
    """
    matrix.astype(np.float32)
    coords = np.array(coords, copy=False, ndmin=2)
    perm = np.arange(len(coords.shape))
    perm[0] = 1
    perm[1] = 0
    x, y = np.transpose(coords, axes=perm)
    src = np.stack([x, y, np.ones_like(x)], axis=0)
    dst = src.T @ matrix.T
    dst[dst[:, 2] == 0, 2] = np.finfo(float).eps
    dst[:, :2] /= dst[:, 2:3]
    return dst[:, :2]


def boxes2landmark(boxes):
    """
    converts boxes to landmarks from which we will derive the similarity transform

    Args:
        boxes: bounding box of the face
    """
    landmarks = []
    for i in range(boxes.shape[0] - 1):
        cen_x = (boxes[i][0] + boxes[i][2]) / 2.0
        cen_y = (boxes[i][1] + boxes[i][3]) / 2.0
        landmarks.append((cen_x, cen_y))
    mouth1 = (boxes[3][0], boxes[3][3])
    landmarks.append(mouth1)
    mouth2 = (boxes[3][2], boxes[3][3])
    landmarks.append(mouth2)
    return np.array(landmarks)


def get_warped_coords(
    corrds: np.ndarray,
    tform: trans.SimilarityTransform,
    tform2: trans.SimilarityTransform,
) -> tf.Tensor:
    """
    computes the warped coordinates using tanh roi

    Args:
        corrds: initial coordinates
        tform: first transformation to apply
        tform2: second transformation to apply
    """
    matrix1 = np.linalg.inv(tform.params)
    matrix2 = tform2.params
    grid = apply_mat_tensor(
        atanh(tf.clip_by_value(apply_mat_tensor(corrds, matrix2), -0.9999, 0.9999)),
        matrix1,
    )
    return grid


def get_inversed_coords(
    corrds: np.ndarray,
    tform: trans.SimilarityTransform,
    tform2: trans.SimilarityTransform,
) -> tf.Tensor:
    """
    computes the warped coordinates using inverted tanh roi

    Args:
        corrds: initial coordinates
        tform: first transformation to apply
        tform2: second transformation to apply
    """
    matrix1 = tform.params
    matrix2 = np.linalg.inv(tform2.params)
    grid = apply_mat_tensor(tf.math.tanh(apply_mat_tensor(corrds, matrix1)), matrix2)
    return grid


def get_coords(
    tform: trans.SimilarityTransform,
    tform2: trans.SimilarityTransform,
    out_shape: Tuple[int],
    mode: str = "warp",
) -> tf.Tensor:
    """
    extract coords

    Args:
        out_shape: shape of the output
        tform: first transformation to apply
        tform2: second transformation to apply
        mode: mode to use for the method
    """
    cols, rows = out_shape[0], out_shape[1]
    tf_coords = np.indices((cols, rows), dtype=np.float32).reshape(2, -1).T
    if mode == "warp":
        tf_coords = get_warped_coords(
            tf_coords,
            tform=tform,
            tform2=tform2,
        )
    elif mode == "inverse":
        tf_coords = get_inversed_coords(
            tf_coords,
            tform=tform,
            tform2=tform2,
        )
    tf_coords = tf.transpose(
        tf.reshape(tf.transpose(tf_coords), (-1, cols, rows)), perm=(0, 2, 1)
    )
    return tf_coords


def coords2grid(coords: tf.Tensor, in_image_shape: Tuple[int]) -> tf.Tensor:
    """
    converts coords to grip for grid sampling

    Args:
        coords: coordiantes to convert
        in_image_shape: image shape
    """
    ih, iw = in_image_shape[0], in_image_shape[1]
    coords = (2 * coords) / tf.expand_dims(
        tf.expand_dims((tf.stack([np.float32(ih) - 1, np.float32(iw) - 1])), axis=-1),
        axis=-1,
    ) - 1
    grid = tf.expand_dims(tf.transpose(coords, (1, 2, 0)), axis=0)
    return grid


def FastTanhWarping(
    image: tf.Tensor, boxes: np.ndarray, output_size: Optional[Tuple[int]] = None
):
    """
    applies fast tanh warping using skimage transforms

    Args:
        boxes: bounding box of the face
        output_size: size of the output iamge
    """
    tform = trans.SimilarityTransform()
    dst = np.array([[-0.25, -0.1], [0.25, -0.1], [0.0, 0.1], [-0.15, 0.4], [0.15, 0.4]])
    tform2 = trans.SimilarityTransform(
        scale=1.0 / 256.0, rotation=0, translation=(-1, -1)
    )
    landmarks = boxes2landmark(boxes=boxes)
    tform.estimate(landmarks, dst)
    if output_size is None:
        output_size = np.array(image).shape
    corrds = get_coords(tform, tform2, output_size, mode="warp")
    grid = coords2grid(corrds, np.array(image).shape)
    warped_image = bilinear_sampler(
        img=np.expand_dims(image, axis=0), x=grid[..., 0], y=grid[..., 1]
    )
    return warped_image
