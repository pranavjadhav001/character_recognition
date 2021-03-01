'''script to create bulk digital data for multiple chars'''
import glob
import os
import random
from character_gen import CharacterGen

chars = ['0','1','2','3','4','5','6','7','8','9',\
		'A','B','C','D','E','F','G','H','I','J','K','L',\
		'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
		'a','b','c','d','e','f','g','h','i','j','k','l','m','n',\
		'o','p','q','r','s','t','u','v','w','x','y','z']
print(len(chars))
for i in chars:
	generator = CharacterGen(i,'custom_data/'+i,'new_fonts',10,100)
	generator.create_multiple(samples=2000)

