# Running-and-improving-Arabic-OCR-baseline
The repository is created to upload the code for the second phase of Thiqahs interview  

## About 

In this project, I used [tessaract OCR](https://github.com/tesseract-ocr/tesseract#about) and did some image pre-processing as recommended by tessaract [documentation](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html) to improve the results produced by the model I also included a training file with synthetic data produced using [TextRecognitionDataGenerator](https://github.com/Belval/TextRecognitionDataGenerator) repository to train the model in it to further improve the results for especially the Arabic language 

## How to run 

You should start off by downloading the tessaract engine from their [official website](https://tesseract-ocr.github.io/tessdoc/Installation.html) and should follow the steps for your operating system 

During installation, you will be presented with same as the image below it allows you to add more components. Arabic should be included in the Additional language and script data.

![image of the page](https://github.com/Lama-Alsaif/Running-and-improving-Arabic-OCR-baseline/tree/main/readme_assets/1.png)

also, remember the location of this folder of the image below since we are going to use it in our code later and if you are a windows user it is prefered to not change it so you do not have to change the code later.

![image of the page](https://github.com/Lama-Alsaif/Running-and-improving-Arabic-OCR-baseline/tree/main/readme_assets/2.png)

after the installation is completed create clone the current repository by 

```
git clone https://github.com/Lama-Alsaif/Running-and-improving-Arabic-OCR-baseline.git
```

then open it up with your favorite editor and go to ```src/main.py``` 
and change the location of ```pytesseract.pytesseract.tesseract_cmd ``` variable to the location you have installed tessaract OCR in 
(if you are a windows user and keep it in its default location you can skip this step)

when you are done with this step I would recommend creating a venv environment by going to the repository path and opening up the terminal and typing 

```
python -m venv env
```
this creates a env folder where the new environment will be stored 

then type

``` 
&env/Scripts/Activate.ps1
```

or if the above command did not work type

```
env/Scripts/activate.bat
```
this will activate the evnviorment and you should see the (env) at the begging of your commend line, like the picture below 

![image of the cmd with (env)](https://github.com/Lama-Alsaif/Running-and-improving-Arabic-OCR-baseline/tree/main/readme_assets/3.png)

finally type  
```
 pip install -r requirements.txt
```
to download all the required libraries including pytesseract which is used to link pytesseract with python

the last step now is to  run ```main.py``` to run the code 



