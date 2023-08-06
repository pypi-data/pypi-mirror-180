import os
from PIL import Image
import numpy as np
import sys

import torch
import torch.nn.functional as F
import torchvision.transforms as transforms

sys.path.append('features/item_cut')
from u2net.networks import U2NET
from u2net.base_dataset import Normalize_image
from u2net.saving_utils import load_checkpoint_mgpu

DEVICE = 'cpu'

CHECKPOINT_PATH = 'features/models/cloth_segm_u2net_latest.pth'


class ClothesSegmentation():
    def __init__(self,):
        transforms_list = []
        transforms_list += [transforms.ToTensor()]
        transforms_list += [Normalize_image(0.5, 0.5)]
        self.transform_rgb = transforms.Compose(transforms_list)

        self.net = U2NET(in_ch=3, out_ch=4)
        self.net = load_checkpoint_mgpu(self.net, CHECKPOINT_PATH)
        self.net = self.net.to(DEVICE)
        self.net = self.net.eval()

    def detect(self, image):
        img = Image.open(image).convert('RGB')
        image_tensor = self.transform_rgb(img)
        image_tensor = torch.unsqueeze(image_tensor, 0)
        
        output_tensor = self.net(image_tensor.to(DEVICE))
        output_tensor = F.log_softmax(output_tensor[0], dim=1)
        output_tensor = torch.max(output_tensor, dim=1, keepdim=True)[1]
        output_tensor = torch.squeeze(output_tensor, dim=0)
        output_tensor = torch.squeeze(output_tensor, dim=0)
        output_arr = output_tensor.cpu().numpy()

        alist = [output_arr[0,:-1], output_arr[:-1,-1], output_arr[-1,::-1], output_arr[-2:0:-1,0]]

        map_dict = {1 : "Cut", 2 : "Cut", 3 : "Cut"}
# top - 1, low - 2, full - 3
        for border in alist:
            elements = set(border)
            elements = list(elements)
            if elements[-1] != 0:
                return output_arr, map_dict[elements[-1]]

        return output_arr, "No cut"