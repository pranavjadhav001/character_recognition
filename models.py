import keras
import keras.backend as K
K.set_image_data_format('channels_last')
import argparse
from keras.applications.densenet import DenseNet121

def get_model(arch_name='densenet',input_shape=(32,32,1),classes=67):
	if arch_name == 'densenet':
		model = keras.applications.DenseNet121(include_top=True,weights=None,
	    		input_shape=input_shape,
	    		classes=classes)

	elif arch_name == 'resnet':
		model = keras.applications.ResNet50(include_top=True,weights=None,
    		input_shape=input_shape,
    		classes=classes)

	elif arch_name == 'mobilenet':
		model = keras.applications.MobileNet(include_top=True,weights=None,
    		input_shape=input_shape,
    		classes=classes)

	elif arch_name == 'vgg':
		model = keras.applications.VGG16(include_top=True,weights=None,
    		input_shape=input_shape,
    		classes=classes)

	else:
		print('arch_name not found')
		model =  None

	return model
