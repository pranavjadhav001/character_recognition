'''script to create bulk digital data for multiple chars'''
import glob
import os
import random
from character_gen import CharacterGen
from config import chars
import argparse

if __name__ == "__main__":
	PARSER = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	PARSER.add_argument('--folder', help='target folder which will have char folders',type=str)
	ARGS = PARSER.parse_args()
	if not os.path.exists(ARGS.folder):
		os.mkdir(ARGS.folder)
	for cnt,i in enumerate(chars):
		generator = CharacterGen(i,os.path.join(ARGS.folder,'Sample0'+str(cnt+1)),'new_fonts',10,100)
		generator.create_multiple(samples=100)
