# Etherium Blockchain phishing detection using KNN algorithm

<p align="center">
  <img src="https://github.com/chartingshow/documentation/blob/master/assets/images/etherium-blockchain-phishing-detection/header.png" width="450" />
  <h2 align="center">Ether Phishing Classifier</h2>
</p>

## Description

The major blochains have been implicated in problems related to cyberattacks, scams, ponzi and pishing, the latter associated with at least 50% of cybercrime in the etherium network. this application uses a dataset of transactions in the etherium blockhain to classify by means of a KNN algorithm those that are pishing (the scope of this application is limited to the samples obtained from the dataset).

## About

<img src="https://github.com/chartingshow/documentation/blob/master/assets/images/etherium-blockchain-phishing-detection/1.gif" width="600" height="338"/>

Allows you to retrain the algorithm in real time by changing the hyperparameters and then see the impact on the ranking performance.

<img src="https://github.com/chartingshow/documentation/blob/master/assets/images/etherium-blockchain-phishing-detection/2.gif" width="600" height="338"/>

New samples can be used to be classified by the previously trained model.

<img src="https://github.com/chartingshow/documentation/blob/master/assets/images/etherium-blockchain-phishing-detection/3.gif" width="600" height="338"/>

## Download

This app can be downloaded from drive:

https://drive.google.com/file/d/1Gm_UUo8ijopbgOrRNGiTIbtPXzdn0_Or/view?usp=share_link

**Usage**: simply double-click on the Ether_Phishing_Classifier.exe file and follow the on-screen instructions.

## Known issues

- when executing, the dataset preprocessing procedure is carried out, and the KNN training, so it may take time to open depending on your system specs.
- The file weight is 230mb due to the compression of the required data science libraries.

## Libs used:

- scikit-learn==1.2.1
- numpy==1.24.2
- requests==2.28.2
- matplotlib==3.7.0
- pandas==1.5.3
- seaborn==0.12.2
- PyQt5==5.15.4
