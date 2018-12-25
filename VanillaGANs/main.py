from collections import OrderedDict

import numpy as np
import time

import torch
import torch.nn as nn
import torch.optim as optim

from torchvision.utils import save_image

import torch.nn.functional as F

#load mnist dataset and define network
from torchvision import datasets, transforms

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

#Define a transform to normalize the data
transform = transforms.Compose([transforms.ToTensor()])

#Download and load the training data
trainset = datasets.MNIST('MNIST_data/', download=True, train= True, transform = transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=128, shuffle=True)

testset = datasets.MNIST('MNIST_data/', download=False, train=False, transform = transform)
testloader = torch.utils.data.DataLoader(testset, batch_size = 64, shuffle=False)

from network import discriminator, generator
from util import get_optimizer
from train import run_vanilla_gan

NOISE_DIM=96

'''Discriminator'''
D = discriminator().to(device)

'''Generator'''
G = generator(NOISE_DIM).to(device)

'''Optimizers'''
D_solver = get_optimizer(D)
G_solver = get_optimizer(G)

'''run training'''
run_vanilla_gan(D, G, D_solver, G_solver, trainloader, num_epochs=20)
