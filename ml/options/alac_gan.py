from ml.options.base import BaseTrainOptions
from ml.options.pix2pix import Pix2pixOptions


class AlacGANTrainOptions(BaseTrainOptions):

    @property
    def tag(self):
        return 'alacGAN-train'

    def __init__(self):
        super().__init__()

        # Training
        self.batch_size = 16
        self.start_epoch = 1
        self.end_epoch = 60
        self.eval_freq = 5
        self.log_freq = 1
        self.save_freq = 1
        self.batch_log_freq = 100

        # Dataset
        self.dataset_root = './alacgan_colorization_data'
        self.a_to_b = True

        # Optimizer
        self.lr = 0.0002
