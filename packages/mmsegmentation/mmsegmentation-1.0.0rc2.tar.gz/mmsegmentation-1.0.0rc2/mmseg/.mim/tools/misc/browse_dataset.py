# Copyright (c) OpenMMLab. All rights reserved.
import argparse
import os.path as osp

from mmengine import Config, DictAction
from mmengine.utils import ProgressBar

from mmseg.registry import DATASETS, VISUALIZERS
from mmseg.utils import register_all_modules


def parse_args():
    parser = argparse.ArgumentParser(description='Browse a dataset')
    parser.add_argument('config', help='train config file path')
    parser.add_argument(
        '--output-dir',
        default=None,
        type=str,
        help='If there is no display interface, you can save it')
    parser.add_argument('--not-show', default=False, action='store_true')
    parser.add_argument(
        '--show-interval',
        type=float,
        default=2,
        help='the interval of show (s)')
    parser.add_argument(
        '--cfg-options',
        nargs='+',
        action=DictAction,
        help='override some settings in the used config, the key-value pair '
        'in xxx=yyy format will be merged into config file. If the value to '
        'be overwritten is a list, it should be like key="[a,b]" or key=a,b '
        'It also allows nested list/tuple values, e.g. key="[(a,b),(c,d)]" '
        'Note that the quotation marks are necessary and that no white space '
        'is allowed.')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    cfg = Config.fromfile(args.config)
    if args.cfg_options is not None:
        cfg.merge_from_dict(args.cfg_options)

    # register all modules in mmseg into the registries
    register_all_modules()

    dataset = DATASETS.build(cfg.train_dataloader.dataset)
    cfg.visualizer['save_dir'] = args.output_dir
    visualizer = VISUALIZERS.build(cfg.visualizer)
    visualizer.dataset_meta = dataset.METAINFO

    progress_bar = ProgressBar(len(dataset))
    for item in dataset:
        img = item['inputs'].permute(1, 2, 0).numpy()
        data_sample = item['data_samples'].numpy()
        img_path = osp.basename(item['data_samples'].img_path)

        img = img[..., [2, 1, 0]]  # bgr to rgb

        visualizer.add_datasample(
            osp.basename(img_path),
            img,
            data_sample,
            show=not args.not_show,
            wait_time=args.show_interval)

        progress_bar.update()


if __name__ == '__main__':
    main()
