from ml.options import BaseTrainOptions
from ml.options.base import BaseInferenceOptions


class SketchSimpTrainOptions(BaseTrainOptions):

    def __init__(self):
        super().__init__()
        # Training
        self.batch_size = 4
        self.start_epoch = 1
        self.end_epoch = 250_000
        self.eval_freq = 10_000
        self.log_freq = 1_000
        self.save_freq = 10_000
        self.batch_log_freq = 0
        # Optimizer
        self.opt_step_size = 200_000
        self.opt_gamma = 0.1

        # Dataset
        self.dataset_root = 'sketch_simp_pretrain_data'
        self.a_to_b = True

        # Optimizer
        self.lr = 0.0002

    @property
    def tag(self):
        return 'sketch-simp-train'


class SketchSimpInferenceOptions(BaseInferenceOptions):
    @property
    def inference_run_id(self):
        return 'SketchSimpInferenceOptionsRunID'

    def __init__(self):
        super().__init__()

    @property
    def tag(self):
        return 'sketch-simp-inference'
