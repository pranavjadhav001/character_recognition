import cv2
import numpy as np
from keras.models import load_model
from config import chars

class Recognizer:
	def __init__(self, model_path):
		self.model = load_model(model_path,compile=False)
		self.char_dict = dict(zip(range(len(chars)), chars))
		print(self.char_dict)
	
	def normImg(self, char_img):
		char_img = cv2.resize(char_img, (32, 32))
		char_img = cv2.cvtColor(char_img, cv2.COLOR_BGR2GRAY)
		char_img = char_img/255.0
		return char_img

	def predictChar(self, char_img):
		norm_img = self.normImg(char_img)
		result = self.model.predict(np.expand_dims(norm_img, axis=(0,-1)))
		return self.char_dict[np.argmax(result[0])]

	def batchPredictChar(self, char_imgs):
		batch_imgs = np.empty(shape=(len(char_imgs),32,32),dtype=np.float32)
		for cnt,i in enumerate(char_imgs):
			batch_imgs[cnt,] = self.normImg(i)
		result = self.model.predict(np.expand_dims(batch_imgs, axis=-1))
		char_result = [self.char_dict[np.argmax(i)] for i in result]
		return char_result


