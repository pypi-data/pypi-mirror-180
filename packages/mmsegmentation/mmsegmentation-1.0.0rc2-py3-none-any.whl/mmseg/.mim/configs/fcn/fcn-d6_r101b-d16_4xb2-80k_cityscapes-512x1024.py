_base_ = './fcn-d6_r50-d16_4xb2-80k_cityscapes-512x1024.py'
model = dict(
    pretrained='torchvision://resnet101',
    backbone=dict(type='ResNet', depth=101))
