from abc import ABC

from ml.options.base import BaseTrainOptions, BaseInferenceOptions


class Pix2pixOptions(ABC):
    def __init__(self):
        super().__init__()

    @property
    def tag(self):
        return 'pix2pix-sketch-simplification-NO_WEIGHT_MAP-CONTENT_LOSS'


class Pix2pixInferenceOptions(BaseInferenceOptions):

    def __init__(self):
        super().__init__()
        self.input_images_path = r'sketch_simplification/test'
        self.output_images_path = 'noghost_sketch_simplification_WEIGHT_MAP'
        self.image_size = 512
        self.a_to_b = True
        self.batch_size = 8
        self.num_workers = 4

        self.generator_config = _generator_config()
        self.discriminator_config = _discriminator_config()

    @property
    def tag(self):
        return 'pix2pix-noghost-inference-sketch-simplification-WEIGHT_MAP'

    @property
    def inference_run_id(self):
        return 'pix2pix-sketch-simplification-NORMAL-2022-09-07-Wednesday-16h-09m-49s'

    @property
    def inference_run_tag(self):
        return 'final'


class Pix2pixTrainOptions(Pix2pixOptions, BaseTrainOptions):

    def __init__(self):
        super().__init__()

        # Training
        self.batch_size = 8
        self.run_id = 'pix2pix-sketch-simplification-MSE-DILATE-CONTENT_LOSS-2022-09-08-Thursday-14h-26m-24s'
        self.start_epoch = 401
        self.end_epoch = 500
        self.eval_freq = 50
        self.log_freq = 5
        self.save_freq = 50
        self.batch_log_freq = 0

        # Dataset
        # weight map * 100: pix2pix-sketch-simplification-weight-map-2022-09-06-Tuesday-03h-04m-14s
        # weight map * 10: pix2pix-sketch-simplification-weight-map-2022-09-06-Tuesday-09h-42m-18s
        # weight map + content loss: pix2pix-sketch-simplification-weight-map-content-loss-2022-09-06-Tuesday-15h-39m-22s
        # weight map + content loss + dilate: pix2pix-sketch-simplification-weight-map-content-loss-dilate-2022-09-06-Tuesday-21h-58m-50s

        # pix2pix-sketch-simplification-NORMAL-2022-09-07-Wednesday-16h-09m-49s + weightmap
        # pix2pix-sketch-simplification-CONTENT_LOSS-2022-09-07-Wednesday-19h-44m-34s + weightmap
        # pix2pix-sketch-simplification-CONTENT_LOSS-DILATE-2022-09-07-Wednesday-23h-16m-58s + weightmap
        # pix2pix-sketch-simplification-DILATE-2022-09-07-Wednesday-13h-35m-26s + weightmap
        # pix2pix-sketch-simplification-MSE-2022-09-08-Thursday-10h-28m-04s
        # pix2pix-sketch-simplification-NO_WEIGHT_MAP-CONTENT_LOSS-2022-09-08-Thursday-18h-11m-45s

        # pix2pix-sketch-simplification-NO-WEIGHT-MAP-2022-09-08-Thursday-10h-16m-21s
        self.dataset_root = './sketch_simplification'
        self.a_to_b = True
        self.random_jitter = True
        self.random_mirror = True
        self.random_rotate = True

        self.weight_map = True
        self.dilate = True
        self.content_loss = True
        self.mse_loss = True
        # self.resume_ckpt_file = 'pix2pix-sketch-simplification-DILATE-2022-09-07-Wednesday-13h-35m-26s'

        # Model
        self.generator_config = _generator_config()
        self.discriminator_config = _discriminator_config()

        # Optimizer
        self.lr = 0.0002
        self.optimizer_beta1 = 0.5
        self.optimizer_beta2 = 0.999
        self.init_gain = 0.02
        self.weight_decay = 0
        self.decay_epochs = 100

        # Loss
        self.l1_lambda = 100.0  # encourage l1 distance to actual output
        self.d_loss_factor = 0.5  # slow down discriminator learning

        # transforms
        self.VGG16_PATH = 'vgg16-397923af.pth'
        self.a_to_b = True
        self.image_size = 512


def _discriminator_config():
    return {
        'in_channels': 1 * 2,  # conditionalGAN takes both real and fake image
        'blocks': [
            # {
            #     'filters': 512,
            # },
            {
                'filters': 256,
            },
            {
                'filters': 128,
            },
            {
                'filters': 64,
            },
            {
                'filters': 32,
            },
            {
                'filters': 16,
            },
            # {
            #     'filters': 4,
            # },
        ]
    }


def _generator_config():
    return {
        'in_channels': 1,
        'out_channels': 1,
        'blocks': [
            {
                'filters': 32,
                'dropout': False,
                'skip_connection': False
            },
            {
                'filters': 64,
                'dropout': False,
                'skip_connection': True
            },
            {
                'filters': 128,
                'dropout': False,
                'skip_connection': True
            },
            # {
            #     'filters': 128,
            #     'dropout': False,
            #     'skip_connection': True
            # },
            {
                'filters': 256,
                'dropout': False,
                'skip_connection': True
            },
            # {
            #     'filters': 256,
            #     'dropout': False,
            #     'skip_connection': True
            # },
            {
                'filters': 512,
                'dropout': True,
                'skip_connection': True
            },
            {
                'filters': 1024,
                'dropout': True,
                'skip_connection': True
            },
        ]
    }
