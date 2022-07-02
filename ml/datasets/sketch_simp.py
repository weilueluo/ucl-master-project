import os
import random

import cv2 as cv
from torchvision.transforms import transforms

from ml.datasets import BaseDataset
from ml.datasets.augmentation import rotate_crop_max_cv, FixedRandomResizedCrop, flip_horizontal_cv
from ml.file_utils import get_all_image_paths
from ml.options.sketch_simp import SketchSimpInferenceOptions, SketchSimpTrainOptions


class SketchSimpDataset(BaseDataset):
    def __init__(self, opt, root):
        super().__init__(opt)
        self.paths = sorted(get_all_image_paths(root))
        self.a_to_b = opt.a_to_b
        self.transform = transforms.Compose([
            transforms.Resize(size=opt.image_size),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ])

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, i):
        A, B = self._split_image_pil(self._read_im_pil(self.paths[i]))
        A, B = A.convert('L'), B.convert('L')
        A, B = self.transform(A), self.transform(B)
        return (A, B) if self.a_to_b else (B, A)


class SketchSimpInferenceDataset(SketchSimpDataset):

    def __init__(self, opt: SketchSimpInferenceOptions):
        super().__init__(opt, opt.input_images_path)


class SketchSimpTestDataset(SketchSimpDataset):
    def __init__(self, opt: SketchSimpTrainOptions):
        root = os.path.join(opt.dataset_root, opt.dataset_test_folder)
        super().__init__(opt, root)


class SketchSimpTrainDataset(BaseDataset):
    def __init__(self, opt: SketchSimpTrainOptions):
        super().__init__(opt)
        root = os.path.join(opt.dataset_root, opt.dataset_train_folder)
        self.paths = sorted(get_all_image_paths(root))
        self.a_to_b = opt.a_to_b
        self.opt = opt

    def __len__(self):
        return len(self.paths)

    def __getitem__(self, i):
        A, B = self._split_image_cv(self._read_im_cv(self.paths[i]))
        A, B = cv.cvtColor(A, cv.COLOR_RGB2GRAY), cv.cvtColor(B, cv.COLOR_RGB2GRAY)

        if random.random() < 0.1:
            A, B = B, B  # encourage model to not change cleaned image

        flip = random.random() < 0.5
        rotate_deg = random.randint(0, 180)

        transform1 = transforms.Compose([
            transforms.Lambda(lambda im: rotate_crop_max_cv(im, rotate_deg)),
            transforms.Lambda(lambda im: flip_horizontal_cv(im, flip)),
        ])

        A, B = transform1(A), transform1(B)

        transform2 = transforms.Compose([
            transforms.ToTensor(),
            FixedRandomResizedCrop(A.shape[1], A.shape[0], self.opt.image_size, scale=(0.3, 1.0), ratio=(1, 1)),
            transforms.Normalize(0.5, 0.5),
        ])

        A, B = transform2(A), transform2(B)

        return (A, B) if self.a_to_b else (B, A)
