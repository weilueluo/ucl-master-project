from abc import ABC

from ml.options.base import BaseTrainOptions


class Pix2pixOptions(ABC):
    def __init__(self):
        super().__init__()

    @property
    def tag(self):
        return 'pix2pix-pretrain-colorization'


class Pix2pixTrainOptions(Pix2pixOptions, BaseTrainOptions):

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
        self.dataset_dir = './alacgan_colorization_data'
        self.a_to_b = True

        # Model
        self.generator_config = _generator_config()
        self.discriminator_config = _discriminator_config()

        # Optimizer
        self.lr = 0.0002
        self.optimizer_beta1 = 0.5
        self.optimizer_beta2 = 0.999
        self.init_gain = 0.02
        self.weight_decay = 0
        self.decay_epochs = 10

        # Loss
        self.l1_lambda = 100.0  # encourage l1 distance to actual output
        self.d_loss_factor = 0.5  # slow down discriminator learning

        # transforms
        self.random_jitter = True
        self.random_mirror = True


def _discriminator_config():
    return {
        'in_channels': 3 * 2,  # conditionalGAN takes both real and fake image
        'blocks': [
            # {
            #     'filters': 512,
            # },
            # {
            #     'filters': 512,
            # },
            {
                'filters': 512,
            },
            {
                'filters': 512,
            },
            {
                'filters': 256,
            },
            {
                'filters': 128,
            },
            {
                'filters': 64,
            },
        ]
    }


def _generator_config():
    return {
        'in_channels': 3,
        'out_channels': 3,
        'blocks': [
            {
                'filters': 64,
                'dropout': False,
                'skip_connection': False
            },
            {
                'filters': 128,
                'dropout': False,
                'skip_connection': True
            },
            {
                'filters': 256,
                'dropout': False,
                'skip_connection': True
            },
            {
                'filters': 512,
                'dropout': False,
                'skip_connection': True
            },
            {
                'filters': 512,
                'dropout': True,
                'skip_connection': True
            },
            {
                'filters': 512,
                'dropout': True,
                'skip_connection': True
            },
            # {
            #     'filters': 512,
            #     'dropout': True,
            #     'skip_connection': True
            # },
            # {
            #     'filters': 512,
            #     'dropout': True,
            #     'skip_connection': True
            # },
        ]
    }
