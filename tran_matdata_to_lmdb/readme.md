 to transform the augmentation data to lmdb 
 these codes are from https://github.com/junyuseu/ResNet-on-Cifar10,and I change a little to fix with the mat file.
 firstly run the aug_convert_cifar10_lmdb.py,then the aug_pad_cifar10.py,at last the aug_compute_mean.py
 for test the resnet,mean.npy is need,use convert_mean.py to transform mean.binaryproto to mean.npy
