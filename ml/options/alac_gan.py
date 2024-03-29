from ml.options.base import BaseTrainOptions, BaseInferenceOptions


class AlacGANInferenceOptions(BaseInferenceOptions):

    def __init__(self):
        super().__init__()
        # self.input_images_path = r'./colorization/test'
        self.input_images_path = r'colorization/test'
        self.output_images_path = 'noghost_colorization_output_new'
        self.image_size = 512
        self.a_to_b = True
        self.batch_size = 8
        self.num_workers = 4
        self.hint_mask = True
        self.hint_multiplier = 1
        self.custom_color = None  # red: (235, 64, 52), yellow: (252, 186, 3), blue: (66, 135, 245)
        self.limit = None  # limit on the inference dataset

    @property
    def tag(self):
        return 'alacgan-noghost-inference'

    @property
    def inference_run_id(self):
        # return 'alacGAN-train-2022-07-02-Saturday-12h-25m-53s'  # fine tuned
        return 'alacGAN-noghost-colorization-finetune-2022-09-04-Sunday-16h-54m-10s'  # new fine-tuned
        # return 'alacGAN-train-2022-06-29-Wednesday-17h-23m-26s'  # pretrained

    @property
    def inference_run_tag(self):
        return 'final'


class AlacGANTrainOptions(BaseTrainOptions):

    @property
    def tag(self):
        return 'alacGAN-noghost-colorization-finetune'

    def __init__(self):
        super().__init__()

        # Model
        self.use_hint = True
        self.mask_all = True

        # Training
        self.batch_size = 8
        self.start_epoch = 1
        self.end_epoch = 10
        self.eval_freq = 5
        self.log_freq = 1
        self.save_freq = 5
        self.batch_log_freq = 0
        self.resume_ckpt_file = 'alacGAN-train-2022-06-29-Wednesday-17h-23m-26s_final.ckpt'

        # Dataset
        self.image_size = 512
        self.dataset_root = './colorization'
        self.a_to_b = True
        self.make_fake_hint = True
        self.in_channels = 1
        self.out_channels = 3

        # Optimizer
        self.lr = 0.00002

        # Scheduler
        self.scheduler_step_size = 20
        self.scheduler_gamma = 1.0

        # Backbones checkpoint
        self.VGG16_PATH = 'vgg16-397923af.pth'
        self.I2V_PATH = 'i2v.pth'
