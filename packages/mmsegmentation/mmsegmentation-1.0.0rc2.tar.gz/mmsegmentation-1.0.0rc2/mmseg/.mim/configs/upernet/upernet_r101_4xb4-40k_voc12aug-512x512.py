_base_ = './upernet_r50_4xb4-40k_voc12aug-512x512.py'
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101))
