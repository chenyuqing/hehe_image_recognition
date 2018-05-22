# coding: utf-8

#########
# train.txt 是训练集
# test.txt 是测试集
# val.txt 是验证集
# trainval.txt 是训练和验证集

# trainval占总数据集的50%，test占总数据集的50%
# train占trainval的50%，val占trainval的50%
#####
import os,random

# read the filenames from a file
dirname = './Annotations'
files = [f[:-4] for f in os.listdir(dirname) if f[-4:].lower() == '.xml']

# random divide  
trainval = random.sample(files, len(files)//2)
test = [f for f in files if f not in trainval]

# random divide 
train = random.sample(trainval, len(trainval)//2)
val = [f for f in trainval if f not in train]

# save to txt file
def list2txt(arr, fname):
    with open(fname+'.txt', 'w') as f:
        for a in arr:
            f.write(a+'\n')

list2txt(trainval, 'trainval')
list2txt(test, 'test')
list2txt(train, 'train')
list2txt(val, 'val')

