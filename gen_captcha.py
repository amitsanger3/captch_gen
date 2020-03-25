from itertools import permutations, combinations
from captcha.image import ImageCaptcha
import numpy as np
import os


def get_str(x):
    """
    Create string from tuple of integers
    :param x: Tuple
        tuple of integers
    :return: str
        string form of integers
    """
    return "".join([str(i) for i in x])


def digit_captcha(width, height, num_list, font_path, font_size=[22,23,24,25,26,27,28]):
    """
    Creates captcha of permutations of 4 digits in the range of num_list as save them as
    .png format of your desired location.
    :param width: int
        width of captcha image
    :param height: int
        height of captcha image
    :param num_list: array
        array of integers you want in captcha's text
    :param font_path: str
        directory path where you saved you fonts in .ttf files.
        Some of the I used can be downloaded from:
        https://drive.google.com/drive/folders/1GavwXoNFVTiWd4zuC3m7ayGut8kuEViR?usp=sharing
    :param font_size: array
        array of integers
    :return: None
    """

    fonts_name = os.listdir(font_path) # list of all fonts name in string form
    font_list = [font_path+i for i in fonts_name]  # joining path + fonts file
  
#     num_list = np.arange(0, 10)
    captch_strings = list(permutations(num_list,4))
    n = 1
    for string in captch_strings:
        # Fonts sizes must takes small so that the text comfortably comes within the
        # image otherwise you can get error
        img = ImageCaptcha(width=160, height=35, fonts=font_list, font_sizes=font_size)
        
        img_name = get_str(string)
        
        gen_img = img.generate_image(str(img_name))

        dst = '../DATA/CAPTCHAS2/'+img_name+'.png'  # destination folder; where captchas need to save
        img.write(img_name, dst)

        if n % 100 == 0:
            print(((len(captch_strings)-n)/len(captch_strings))*100, "% REMAINING")
        n += 1


x = np.arange(0, 10)
digit_captcha(width, height, x)

