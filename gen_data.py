import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
np.random.seed(2019)
from copy import deepcopy

print(len(sys.argv))
if len(sys.argv) < 2:
    noise_dim = 100
    noise_scale = 10
elif len(sys.argv) == 2:
    noise_dim = 100
    noise_scale = int(sys.argv[1])
else:
    noise_dim = int(sys.argv[1])
    noise_scale = int(sys.argv[2])

ihdp_train = np.load('./data/IHDP/ihdp_npci_1-1000.train.npz')
ihdp_test = np.load('./data/IHDP/ihdp_npci_1-1000.test.npz')

new_ihdp_train_x = ihdp_train['x']
new_ihdp_test_x = ihdp_test['x']

new_ihdp_train_x = np.concatenate((new_ihdp_train_x, noise_scale*np.random.randn(672, noise_dim, 1000)),axis=1).astype(np.half)
new_ihdp_test_x = np.concatenate((new_ihdp_test_x, noise_scale*np.random.randn(75, noise_dim, 1000)),axis=1).astype(np.half)

np.savez('./data/IHDP/{}times_noisy_{}_ihdp_npci_1-1000.train.npz'.format(noise_scale, noise_dim),
         x=new_ihdp_train_x,t=ihdp_train['t'],yf=ihdp_train['yf'],ycf=ihdp_train['ycf'],
         mu0=ihdp_train['mu0'], mu1=ihdp_train['mu1'])
np.savez('./data/IHDP/{}times_noisy_{}_ihdp_npci_1-1000.test.npz'.format(noise_scale, noise_dim),
         x=new_ihdp_test_x, t=ihdp_test['t'],yf=ihdp_test['yf'],ycf=ihdp_test['ycf'],
         mu0=ihdp_test['mu0'], mu1=ihdp_test['mu1'])

jobs_train = np.load('./data/JOBS/jobs.train.npz')
jobs_test = np.load('./data/JOBS/jobs.test.npz')

new_jobs_train_x_100 = jobs_train['x']
new_jobs_test_x_100 = jobs_test['x']

new_jobs_train_x_100 = np.concatenate((new_jobs_train_x_100, noise_scale*np.random.randn(2569, noise_dim, 10)),axis=1).astype(np.half)
new_jobs_test_x_100 = np.concatenate((new_jobs_test_x_100, noise_scale*np.random.randn(643, noise_dim, 10)),axis=1).astype(np.half)

np.savez('./data/JOBS/{}times_noisy_{}_jobs.train.npz'.format(noise_scale, noise_dim),
         x=new_jobs_train_x_100,t=jobs_train['t'],yf=jobs_train['yf'],e=jobs_train['e'])
np.savez('./data/JOBS/{}times_noisy_{}_jobs.test.npz'.format(noise_scale, noise_dim),
         x=new_jobs_test_x_100,t=jobs_test['t'],yf=jobs_test['yf'],e=jobs_test['e'])

twins_train = np.load('./data/TWINS/twins_1-10.train.npz')
twins_test = np.load('./data/TWINS/twins_1-10.test.npz')

new_twins_train_x_100 = twins_train['x']
new_twins_test_x_100 = twins_test['x']

new_twins_train_x_100 = np.concatenate((new_twins_train_x_100, noise_scale*np.random.randn(4868, noise_dim, 100)),axis=1).astype(np.half)
new_twins_test_x_100 = np.concatenate((new_twins_test_x_100, noise_scale*np.random.randn(541, noise_dim, 100)),axis=1).astype(np.half)

np.savez('./data/TWINS/{}times_noisy_{}_twins_1-10.train.npz'.format(noise_scale, noise_dim),
         x=new_twins_train_x_100,t=twins_train['t'],yf=twins_train['yf'],ycf=twins_train['ycf'])
np.savez('./data/TWINS/{}times_noisy_{}_twins_1-10.test.npz'.format(noise_scale, noise_dim),
         x=new_twins_test_x_100,t=twins_test['t'],yf=twins_test['yf'],ycf=twins_test['ycf'])
