_base_ = './fcn-d6_r50-d16_4xb2-80k_cityscapes-769x769.py'
model = dict(pretrained='torchvision://resnet50', backbone=dict(type='ResNet'))
