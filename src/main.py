# -*- coding: utf-8 -*-

'''
This module is responsilbe for preprosseing the images and running the Tesseract OCR model on the processed images 

author:Lama Alsaif
date:22/03/2023

'''

from preprocessor import preprocessor
from model_runner import model_runner


class runner:

    def __init__(self,preprocessor,model_runner,img_path) -> None:
        self.preprocessor=preprocessor
        self.model_runner=model_runner
        self.img_path=img_path

    def start_model(self) ->None:
        '''
        The aim of this function is to start prepreprocessing then running the model
        '''

        # for key in self.keywords:
        preprocessed_img= self.preprocessor.preprocess_data(self.img_path)

        result= self.model_runner.run_model(preprocessed_img)


if __name__ =="__main__":
    preprocessor=preprocessor()
    model_runner = model_runner()
    runner=runner(preprocessor,model_runner,"..\\assets\\normal\\1.jpeg") #change path here to the desired image location 
    runner.start_model()

