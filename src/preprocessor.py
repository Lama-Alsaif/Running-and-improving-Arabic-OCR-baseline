# -*- coding: utf-8 -*-

'''
This module contains methods for the preprocessing of the image 

author:Lama Alsaif
date:22/03/2023

'''
import logging
from PIL import Image
import cv2
from datetime import date



logging.basicConfig(
    filename="../logs/results-"+date.today().strftime("%B %d, %Y")+".log",
    level=logging.INFO,
    filemode='w',
    format="%(name)s - %(levelname)s - %(message)s"
)

class preprocessor:

    def __init__(self) -> None:
        pass

    def preprocess_data(self,img_path:str) ->str:
        '''
        The aim of this function is to start preprocessing the image before passing it to the model 

        Args:
            img_path:(str) this attribute represents passed image path.

        Returns:
            img_path_binarized:(str) final preprocessing step 
        '''
        try:
            assert isinstance(img_path,str)


            img_path_format=self.change_format(img_path)
            img_path_dpi=self.change_dpi(img_path_format)
            img_path_binarized=self.binarize(img_path_dpi)

            
            
            logging.info(f'SUCCESS at preprocess_data method: the image with the "{img_path}" path')
            return img_path_binarized

        except Exception as e:
            logging.error(f'ERROR at preprocess_data method: the error is ==> {e}.')
            return e

    

    def change_format(self,img_path:str) ->str :

        '''
        The aim of this function is to change the image format to JPEG to remove the possibility of having an alpha channel 

        Args:
            img_path:(str) this attribute represents passed image path.
        Returns:
            img_path_format:(str) path of the new image if image changing format is a success
        '''
        try:

            im1 = Image.open(img_path)
            im1.save('..\\assets\\processed_image_steps\\1_processed_img_format.tiff')
            im = '..\\assets\\processed_image_steps\\1_processed_img_format.tiff'
           
            logging.info(f'SUCCESS at change_format method: for this image path "{img_path}".')
            return im 
        except Exception as e:
                logging.error(f'ERROR at change_format method: for this image path "{img_path}", the error is ==> {e}.')
                raise False


    
    def change_dpi(self,img_path:str) ->bool:

        '''
        The aim of this function is to change the image dpi to 600  

        Args:
            img_path:(str) this attribute represents passed image path.
        Returns:
            img_path_dpi:(str) path of the new image with the 600 dpi 
        '''

        try:

            im1 = Image.open(img_path)
            im1.save("..\\assets\\processed_image_steps\\2_processed_img_dpi.tiff", dpi=(600,600))
           
            logging.info(f'SUCCESS at change_dpi method: for this image path "{img_path}".')
            return True
        except Exception as e:
                logging.error(f'ERROR at change_dpi method: for this image path "{img_path}", the error is ==> {e}.')
                raise False

    def binarize(self,img_path)->str:
        
        '''
        The aim of this function is binarize the image   

        Args:
            img_path:(str) this attribute represents passed image path.
        Returns:
            img_path_binarized:(str) path of the new binarized image 
        '''
        
        try:
            im = cv2.imread('..\\assets\\processed_image_steps\\1_processed_img_format.tiff')

            th, im_th = cv2.threshold(im, 128, 255, cv2.THRESH_BINARY)

            th, im_th_tz = cv2.threshold(im, 128, 255, cv2.THRESH_TOZERO)


            im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

            th, im_gray_th_otsu = cv2.threshold(im_gray, 128, 192, cv2.THRESH_OTSU)

            cv2.imwrite('..\\assets\\processed_image_steps\\3-processed_img_binar.tiff', im_gray_th_otsu)
            img='..\\assets\\processed_image_steps\\3-processed_img_binar.tiff'

            logging.info(f'SUCCESS at binarize method: for this image path "{img_path}".')
            return img
        except Exception as e:
                logging.error(f'ERROR at change_dpi method: for this image path "{img_path}", the error is ==> {e}.')
                raise e