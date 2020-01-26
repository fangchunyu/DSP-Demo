from easydict import EasyDict as edict

# from configs.config_brain import *
from configs.config_u2os import *
# from configs.config_celegans import *

config = edict()
config.TRAIN = edict()
config.VALID = edict()

config.archi1 = archi1
config.archi2 = archi2
config.loss   = loss

config.TRAIN.ckpt_saving_interval = 10
config.TRAIN.batch_size = 2
config.TRAIN.beta1 = 0.9
config.TRAIN.n_epoch = 500
config.TRAIN.decay_every = 50
config.TRAIN.lr_decay = 0.5
config.TRAIN.conv_kernel = 3
config.TRAIN.learning_rate_init = 1e-4


config.factor = factor
config.TRAIN.img_size_lr = train_img_size_lr
config.TRAIN.img_size_hr = train_img_size_hr
config.using_batch_norm  = using_batch_norm
config.label = label


## if use multi-gpu training
config.TRAIN.num_gpus = 3
## if use single-gpu training  
config.TRAIN.device_id = 0

config.TRAIN.using_mixed_precision = False

config.TRAIN.using_edge_loss = False
config.TRAIN.using_grad_loss = False

config.TRAIN.lr_img_path = train_lr_img_path
config.TRAIN.hr_img_path = train_hr_img_path
config.TRAIN.mr_img_path = train_mr_img_path

config.TRAIN.test_data_path = train_test_data_path
config.TRAIN.valid_lr_path = train_valid_lr_path  # valid on_the_fly 

config.TRAIN.test_saving_path = "sample/test/{}/".format(label)
config.TRAIN.ckpt_dir = "checkpoint/{}/".format(label)
config.TRAIN.log_dir = "log/{}/".format(label)

config.VALID.lr_img_path = valid_lr_img_path
config.VALID.lr_img_size = valid_lr_img_size # [depth, height, width, channels]
config.VALID.saving_path = "{}/{}/".format(config.VALID.lr_img_path, label)
# config.VALID.saving_path = "H:/{}/".format(label)