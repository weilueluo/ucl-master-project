from pprint import pprint

from ml.datasets import create_inference_dataloaders
from ml.models import create_inference_model
from ml.options import create_inference_options


def main():
    name = 'pix2pix'
    opt = create_inference_options(name)
    inference_loader = create_inference_dataloaders(opt, name)
    model = create_inference_model(opt, inference_loader, name)

    print(str(opt))
    print('Inference started')
    model.inference()
    print('Inference finished')


if __name__ == '__main__':
    main()
