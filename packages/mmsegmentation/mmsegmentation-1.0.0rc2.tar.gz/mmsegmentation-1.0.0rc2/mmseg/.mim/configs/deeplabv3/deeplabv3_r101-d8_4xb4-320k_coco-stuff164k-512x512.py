_base_ = './deeplabv3_r50-d8_4xb4-320k_coco-stuff164k-512x512.py'
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101))
