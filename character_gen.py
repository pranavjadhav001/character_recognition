'''script to generate new digital data for a character'''
import cv2
from PIL import ImageFont,ImageDraw,Image
import glob
import os
import random
import argparse

class CharacterGen:
    def __init__(self,character,save_folder,font_folder_path,font_min_size,font_max_size):
        self.character = character
        self.font_folder_path = font_folder_path
        self.folder = save_folder
        if not os.path.exists(self.folder):
            os.mkdir(self.folder)
        self.font_min_size = font_min_size
        self.font_max_size = font_max_size

    def create_canvas(self,width,height):
        '''returns plain background image to write text on , background color'''
        canvas_shape = (width,height)
        canvas_bg = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        canvas = Image.new(mode="RGB", size=canvas_shape, color=canvas_bg)
        return canvas, canvas_bg

    def create_char(self,font_name):
        font = ImageFont.truetype(font_name,random.randint(self.font_min_size,self.font_max_size))
        w,h = font.getsize(self.character)
        canvas,canvas_bg = self.create_canvas(w+int((w/2)), h+int((h/4)))
        draw_txt = ImageDraw.Draw(canvas)
        text_fg = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        while text_fg == canvas_bg:
            text_fg = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw_txt.text((int(w/4),0), self.character, fill=text_fg, font=font)
        return canvas

    def create_multiple(self,samples):
        '''fn to create bulk images'''
        font_paths = glob.glob(os.path.join(self.font_folder_path, '*.ttf'))
        for cnt in range(samples):
            #canvas, canvas_bg = self.create_canvas()
            image = self.create_char(random.choices(font_paths)[0])
            image.save(os.path.join(self.folder, str(cnt))+'.png')

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    PARSER.add_argument('--char', help='character',type=str)
    PARSER.add_argument('--save_folder', help='generated folder storage',type=str)
    PARSER.add_argument('--font_folder', help='font folder',type=str)
    PARSER.add_argument('--font_min_size', help='font min size',type=int,default=10)
    PARSER.add_argument('--font_max_size', help='font max size',type=int,default=10)
    PARSER.add_argument('--samples', help='no. of samples',type=int,default=10)
    #PARSER.add_argument('--center_x', help='font min size',type=int,default=10)
    #PARSER.add_argument('--center_y', help='font min size',type=int,default=10)
    ARGS = PARSER.parse_args()
    generator = CharacterGen(ARGS.char,ARGS.save_folder,ARGS.font_folder,\
        ARGS.font_min_size,ARGS.font_max_size)
    generator.create_multiple(samples=ARGS.samples)