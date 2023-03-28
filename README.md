# Running-and-improving-Arabic-OCR-baseline
The repository is created to upload the code for the second phase of Thiqahs interview  

## About 

In this project, I used [tessaract OCR](https://github.com/tesseract-ocr/tesseract#about) and did some image pre-processing as recommended by tessaract [documentation](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html) to improve the results produced by the model I also included a training file with synthetic data produced using [TextRecognitionDataGenerator](https://github.com/Belval/TextRecognitionDataGenerator) repository to train the model in it to further improve the results for especially the Arabic language 

## How to run 

You should start off by downloading the tessaract engine from their [official website](https://tesseract-ocr.github.io/tessdoc/Installation.html) and should follow the steps for your operating system 

During installation, you will be presented with a page that allows you to add more components. Arabic should be included in the Additional language and script data.

![image of the page](https://github.com/Lama-Alsaif/Running-and-improving-Arabic-OCR-baseline/tree/main/readme_assets/1.png)






