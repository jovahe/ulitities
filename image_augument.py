"""



"""

import keras
import sys
import PIL

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
datagen = ImageDataGenerator(
         rotation_range=30,
         #width_shift_range=0.2,
         #height_shift_range=0.2,
         shear_range=0.2,
         zoom_range=0.2,
         horizontal_flip=True,
         vertical_flip=True,
         fill_mode='constant')

img = load_img('/home/scrs/test/dataA/storage_tank_696.jpg')
#print (img.size)
x = img_to_array(img)
#print (x.shape)
x = x.reshape((1,) + x.shape)
#print (x.shape)
#exit(0)

i = 0
for batch in datagen.flow(x,
                          batch_size = 1,
                          save_to_dir = '/home/scrs/test/dataA/pre',
                          save_prefix = 'storage_tank_696',
                          save_format = 'png'):
    i +=1
    break
    #if i>1:
        #break


print ("OK")