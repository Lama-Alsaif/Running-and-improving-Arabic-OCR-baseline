# -*- coding: utf-8 -*-

'''
This module contains methods for the preprocessing of the image 

author:Lama Alsaif
date:22/03/2023

'''
import logging
import cv2
import mahotas
from PIL import Image
from PIL import ImageFilter
from pylab import gray, imshow, show
from datetime import date
from skimage import color
from skimage import io


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
            final_img:(str) final preprocessing step 
        '''
        try:
            assert isinstance(img_path,str)

            #image pre-proccessing steps
            img_path_format=self.change_format(img_path)
            img_path_dpi=self.change_dpi(img_path_format)
            # img_path_norma=self.img_normalization(img_path)
            img_path_sharp=self.img_sharp(img_path_dpi)
            img_path_otsu=self.otsu_method_img(img_path_sharp)
            img_path_skeleton = self.skeletonisation(img_path_otsu)
            final_img = self.gery_imag(img_path_skeleton)
            # final_img=self.binarize(img_path_grey)


            
            
            logging.info(f'SUCCESS at preprocess_data method: the image with the "{img_path}" path')
            return final_img

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

   
    


    def change_dpi(self,img_path:str) ->str:

        '''
        The aim of this function is to change the image dpi to 350  

        Args:
            img_path:(str) this attribute represents passed image path.
        Returns:
            img_path_dpi:(str) path of the new image with the 350 dpi 
        '''

        try:

            im1 = Image.open(img_path)
            im1.save("..\\assets\\processed_image_steps\\2_processed_img_dpi.tiff", dpi=(350,350))
            im = '..\\assets\\processed_image_steps\\2_processed_img_dpi.tiff'
           
            logging.info(f'SUCCESS at change_dpi method: for this image path "{img_path}".')
            return im
        except Exception as e:
                logging.error(f'ERROR at change_dpi method: for this image path "{img_path}", the error is ==> {e}.')
                raise e



    def img_normalization(self,img_path:str) ->str:
        '''
        The aim of this function is to normalise the image

        Args:
            img_path:(str) this attribute represents passed image path.
        Returns:
            img_path_dpi:(str) path of the new image with the 600 dpi 
        '''

        try:

            img1 = cv2.imread(img_path)
            # Normalize the image
            img1 = cv2.normalize(img1, None, 0, 1.0,
            cv2.NORM_MINMAX, dtype=cv2.CV_32F)
            cv2.imwrite("..\\assets\\processed_image_steps\\3_processed_normaliz.tiff",img1)
            im = '..\\assets\\processed_image_steps\\3_processed_normaliz.tiff'
           
            logging.info(f'SUCCESS at img_normalization method: for this image path "{img_path}".')
            return im
        except Exception as e:
                logging.error(f'ERROR at img_normalization method: for this image path "{img_path}", the error is ==> {e}.')
                raise e

    def img_sharp(self,img_path)->str:
        '''
        The aim of this function is to sharpn the image 

        Args:
            img_path:(str) this attribute represents passed image path.
        Returns:
            img_path_sharp:(str) path of the new sharpend image 
        '''
        try:
            im1 = Image.open(img_path);

            # Apply sharp filter
            im1 = im1.filter(ImageFilter.SHARPEN);
            im1 = im1.filter(ImageFilter.SHARPEN);
            im1.save('..\\assets\\processed_image_steps\\4_processed_sharp.tiff')
            img = '..\\assets\\processed_image_steps\\4_processed_sharp.tiff'
            logging.info(f'SUCCESS at img_sharp method: for this image path "{img_path}".')
            return img
        except Exception as e:
            logging.error(f'ERROR at img_sharp method: for this image path "{img_path}", the error is ==> {e}.')
            raise e


    def otsu_method_img(self,img_path)->str:
        '''
        The aim of this function is to use  otsu_method on the image

        Args:
            img_path:(str) this attribute represents passed image path.
        Returns:
            img_path_otsu:(str) path of the image with otsu method applied
        '''
        try:
            img1 =mahotas.imread(img_path)
            # filtering image
            img1 = img1.max(2)
            
            # otsu method
            T_otsu = mahotas.otsu(img1)  
            
            # image values should be greater than otsu value
            img1 = img1 > T_otsu

            mahotas.imsave('..\\assets\\processed_image_steps\\5_processed_otsu.tiff', img1)
            img = '..\\assets\\processed_image_steps\\5_processed_otsu.tiff'
            logging.info(f'SUCCESS at otsu_method_img method: for this image path "{img_path}".')
            return img
        except Exception as e:
                logging.error(f'ERROR at otsu_method_img method: for this image path "{img_path}", the error is ==> {e}.')
                raise e

    def skeletonisation(self,img_path)->str:
        '''
        The aim of this function is to Skeletonise the image

        Args:
            img_path:(str) this attribute represents passed image path.
        Returns:
            img_path_skeleton:(str) path of the Skeletonised image 
        '''
        try:
            img1 =mahotas.imread(img_path)
            # Skeletonisation by thinning
            img1 = mahotas.thin(img1)
            mahotas.imsave('..\\assets\\processed_image_steps\\6_processed_skeleton.tiff',img1)
            img = '..\\assets\\processed_image_steps\\6_processed_skeleton.tiff'
            logging.info(f'SUCCESS at skeletonisation method: for this image path "{img_path}".')
            return img
        except Exception as e:
            logging.error(f'ERROR at skeletonisation method: for this image path "{img_path}", the error is ==> {e}.')
            raise e


    def gery_imag(self,img_path)->str:
            '''
            The aim of this function is to Skeletonise the image

            Args:
                img_path:(str) this attribute represents passed image path.
            Returns:
                img_path_grey:(str) path of the grey image 
            '''
            try:
                img1 = cv2.imread(img_path)
                img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
                cv2.imwrite('..\\assets\\processed_image_steps\\7_processed_grey.tiff',img1)
                img = '..\\assets\\processed_image_steps\\7_processed_grey.tiff'
                logging.info(f'SUCCESS at gery_imag method: for this image path "{img_path}".')
                return img
            except Exception as e:
                logging.error(f'ERROR at gery_imag method: for this image path "{img_path}", the error is ==> {e}.')
                raise e
    

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
                logging.error(f'ERROR at binarize method: for this image path "{img_path}", the error is ==> {e}.')
                raise e