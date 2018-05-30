# -*- coding: utf-8 -*-

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
import os
import pandas as pd

def data_aug(data_dir, cate_list, nb_aug):
	train = []
	for category_id, category in enumerate(cate_list):
	    for file in os.listdir(os.path.join(data_dir, category)):
	        train.append(['train/{}/{}'.format(category, file), category_id, category])
	train = pd.DataFrame(train, columns=['file', 'category_id', 'category'])

	datagen = ImageDataGenerator(
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest')

	for filepath,filename in zip(train.file, train.category):
    print(filepath,filename)
    img = load_img('input/'+filepath)  # this is a PIL image
    x = img_to_array(img)  # this is a Numpy array with shape (3, 150, 150)
    x = x.reshape((1,) + x.shape)  # this is a Numpy array with shape (1, 3, 150, 150)

    # the .flow() command below generates batches of randomly transformed images
    # and saves the results to the `preview/` directory
    i = 0
    for batch in datagen.flow(x, batch_size=1,
                              save_to_dir='input/train_aug/'+filename, save_prefix=filename, save_format='jpeg'):
        i += 1
        if i > nb_aug:
            break  # otherwise the generator would loop indefi