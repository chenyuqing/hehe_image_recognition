#!/usr/bin/env python  
import os, io
import sys  
import numpy as np  
import matplotlib.pyplot as plt  
import pylab  
from pylab import figure, show, legend  
from mpl_toolkits.axes_grid1 import host_subplot  

def plot_train_loss(iters, loss):
	host = host_subplot(111)  
	plt.subplots_adjust(right=0.8) # ajust the right boundary of the plot window  
	#par1 = host.twinx()  
	# set labels  
	host.set_xlabel("iterations")  
	host.set_ylabel("RPN loss")  
	#par1.set_ylabel("validation accuracy")  
	  
	# plot curves  
	p1, = host.plot(iters, loss, label="train RPN loss")  

	host.legend(loc=1)  
	  
	# set label color  
	host.axis["left"].label.set_color(p1.get_color())  
	host.set_xlim([min(iters), max(iters)+20])  
	host.set_ylim([min(loss), max(loss)+0.05])  
	  
	plt.draw()  
	plt.show()

fp = io.open('faster_rcnn_end2end_VGG16_--set_EXP_DIR_vgg_RNG_SEED_42.txt.2018-05-22_16-44-26.train', 'r',encoding='UTF-8') 
iters = []
loss = []
lines = fp.readlines()[1:]
for p in lines:
	# print(p.encode('ascii', 'ignore').split()[0])
	# print(p.encode('ascii', 'ignore').split()[2])
	iters.append(int(p.encode('ascii', 'ignore').split()[0]))
	loss.append(float(p.encode('ascii', 'ignore').split()[2]))

	# alt-opt training
	# if len(iters) > 2 and iters[-1] < iters[-2]:
	# 	iters.pop()
	# 	loss.pop()
	# 	plot_train_loss(iters, loss)
	# 	iters = []
	# 	loss = []
	# 	continue
# end2end training
plot_train_loss(iters, loss)

# print(type(iters[0]))
# print(iters)
# print(loss)

fp.close()


