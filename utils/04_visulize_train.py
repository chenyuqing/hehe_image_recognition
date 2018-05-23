#!/usr/bin/env python  
import os, io
import sys  
import numpy as np  
import matplotlib.pyplot as plt  
import pylab  
from pylab import figure, show, legend  
from mpl_toolkits.axes_grid1 import host_subplot  

def plot_train_loss(iters, loss, label, ylabel):
	host = host_subplot(111)  
	plt.subplots_adjust(right=0.8) # ajust the right boundary of the plot window  
	#par1 = host.twinx()  
	# set labels  
	host.set_xlabel("iterations")  
	host.set_ylabel(ylabel)  
	#par1.set_ylabel("validation accuracy")  
	  
	# plot curves  
	p1, = host.plot(iters, loss, label=label)  

	host.legend(loc=1)  
	  
	# set label color  
	host.axis["left"].label.set_color(p1.get_color())  
	host.set_xlim([min(iters), max(iters)+20])  
	host.set_ylim([min(loss), max(loss)+0.05])  
	  
	plt.draw()  
	plt.show()

import argparse
def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='Faster R-CNN training loss curves')
    parser.add_argument('--train_method', dest='train_method', help = 'alt_opt or end2end', default='alt_opt')
    parser.add_argument('--filename', dest='filename', default=None)

    args = parser.parse_args()
    return args


if __name__ == '__main__':
	args = parse_args()

	filename = args.filename
	train_method = args.train_method
	if filename == None:
		print('No specified filename to be set')
		exit()

	# fp = io.open('faster_rcnn_end2end_VGG16_--set_EXP_DIR_vgg_RNG_SEED_42.txt.2018-05-22_16-44-26.train', 'r',encoding='UTF-8') 
	fp = io.open(filename, 'r',encoding='UTF-8')
	lines = fp.readlines()[1:]
	iters = []
	loss = []
	if train_method == "alt_opt":
		long_iters = []
		long_loss = []
		for p in lines:
			# print(p.encode('ascii', 'ignore').split()[0])
			# print(p.encode('ascii', 'ignore').split()[2])
			iters.append(int(p.encode('ascii', 'ignore').split()[0]))
			loss.append(float(p.encode('ascii', 'ignore').split()[2]))

			# alt-opt training
			if len(iters) > 2 and iters[-1] < iters[-2]:
				iters.pop()
				loss.pop()
				# plot_train_loss(iters, loss)
				long_iters.append(iters)
				long_loss.append(loss)
				iters = []
				loss = []
				continue
		long_iters.append(iters)
		long_loss.append(loss)

		plot_train_loss(long_iters[0], long_loss[0], "train RPN loss", "Stage 1 RPN loss")
		plot_train_loss(long_iters[1], long_loss[1], "train fast RCNN loss", "Stage 1 fast RCNN loss")
		plot_train_loss(long_iters[2], long_loss[2], "train RPN loss", "Stage 2 RPN loss")
		plot_train_loss(long_iters[3], long_loss[3], "train fast RCNN loss", "Stage 2 fast RCNN loss")
	else:
		for p in lines:
			# print(p.encode('ascii', 'ignore').split()[0])
			# print(p.encode('ascii', 'ignore').split()[2])
			iters.append(int(p.encode('ascii', 'ignore').split()[0]))
			loss.append(float(p.encode('ascii', 'ignore').split()[2]))
		# end2end training
		plot_train_loss(iters, loss, 'Training loss(sum of 4 loss)', 'Training loss')

	# print(type(iters[0]))
	# print(iters)
	# print(loss)

	fp.close()


