from typing import Tuple
import os

if __name__ == "__main__":
    os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

    import argparse

    parser = argparse.ArgumentParser(
        usage=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--logger",
        nargs="?",
        type=str,
        default="logs.log",
        help="path to save the logs",
    )
    parser.add_argument(
        "--unit_test",
        action="store_true",
        default=False,
        help="run the unit test",
    )
    args = parser.parse_args()
    from .utils.getlogger import get_logger

    logger = get_logger(log_file=args.logger)
else:
    logger = None
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from .utils.packages import check_packages
from .warping.warping import TanhWarping

check_packages(logger=logger)
import tensorflow as tf
import numpy as np


def apply_roi_tanh_warping(
    image: np.ndarray, label: np.ndarray, size: Tuple[int]
) -> Tuple[tf.Tensor, tf.Tensor]:
    """
    applies a warping to an example pair

    Args:
        image: images to rectify
        label: one hot labels
        size: output target size
    """
    return TanhWarping(image=image, label=label, size=size)


if __name__ == "__main__":
    if args.unit_test:
        from .utils.test import run_a_unit_test, save_example_pair

        image, label = run_a_unit_test()
        new_image, new_label = apply_roi_tanh_warping(
            image=image, label=label, size=(622, 639)
        )
        save_example_pair(new_image=new_image, new_label=new_label)
    from .utils.clear import remove_chache_folders

    remove_chache_folders()
