# -*- coding: utf-8 -*-

'''
code for running and improving Tesseract OCR for arabic and english

author:Lama Alsaif
date:22/03/2023

'''

import logging
import cv2
import pytesseract
import arabic_reshaper
from bidi.algorithm import get_display
from datetime import date




logging.basicConfig(
    filename="../logs/results-"+date.today().strftime("%B %d, %Y")+".log",
    level=logging.INFO,
    filemode='w',
    format="%(name)s - %(levelname)s - %(message)s"
)


class model_runner:

    def __init__(self) -> None:
        pass



    def run_model(self,preprocessed_img:str) ->str:
            '''
            The aim of this function is to start preprocessing the image before passing it to the model 

            Args:
                preprocessed_img:(str) this attribute represents passed image path.

            Returns:
                result:(str) true if preprocessing is a success
            '''
            try:
                assert isinstance(preprocessed_img,str)

                #location of the Tesseract to connect it to pytesseract
                pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

                img  = cv2.imread(preprocessed_img)


                text = pytesseract.image_to_string(img,lang='eng+ara')
                text = arabic_reshaper.reshape(text)
                text = get_display(text, base_dir = 'L')
                print(arabic_reshaper.reshape(text))
                
                logging.info(f'SUCCESS at change_dpi method: for this image path "{preprocessed_img}".')
                return True


            except Exception as e:
                logging.error(f'ERROR at preprocess_data method: the error is ==> {e}.')
                return False