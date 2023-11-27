# Pill Image Classification By Using Stacking Ensemble Method

## Overview
Welcome to the Pill Image Classification By Using Stacking Ensemble Method Project repository. This project focuses on advancing the accuracy and reliability of pill identification systems through deep learning techniques. The primary exploration involves the implementation and comparison of various deep learning models, including ResNet50, Inception-V3, and MobileNet. The study specifically investigates the efficacy of ensemble methods, such as stacking and weighted average ensembles, aiming to contribute to the improvement of pill image classification systems in the healthcare and pharmaceutical domains.

## Table of Contents
1. [Introduction](#introduction)
2. [Methodology](#methodology)
3. [Results and Discussion](#results-and-discussion)
4. [Conclusion](#conclusion)


## Introduction
Problem Statement:
- 30.5% of medication error occurs in the emergency department of HUSM, Kelantan (Shitu et al., 2020)
- Human factors play a crucial role in the occurrence of medication errors (Mekonnen et al., 2018)
- 66.3% of errors in medicine identification due to the prevalence of look-alike alphabetical names of drugs (Tseng et al., 2018)

Research Questions:
- How to choose an appropriate pill image classification method?
- How effective is implementing the stacking ensemble method in machine learning methodology to classify pill images?
- How will the stacking ensemble method compare to other algorithms and ensemble method?

Research Objectives:
- To review the different kinds of methodologies related to the classification of medical images with journal and article literature by June 2023.
- To design and train an ensemble model to evaluate the best accuracy for classifying pill images by November 2023.
- To perform benchmarking of the proposed ensemble model comparing to results of other researchers by November 2023.


## Methodology
Based on the OSEMN framework by Hilary Mason and Chris Wiggins:
- Obtain, Scrub, Explore, Model, and iNterpret

The original model was translated to a more relevant format as below:
![image](https://github.com/faisalmadd/Pill-Image-Classification-By-Using-Stacking-Ensemble-Method/assets/84001348/6015ed49-384f-4bcf-997a-e0ade80fdf5a)

Data Aquisition:
- Dataset used: "Pharmaceutical Drugs and Vitamins Synthetic Images“ dataset from Kaggle
- Link: https://www.kaggle.com/datasets/vencerlanz09/pharmaceutical-drugs-and-vitamins-synthetic-images/data
- Consists of 10,000 images of pills, categorized into ten distinct classes
![image](https://github.com/faisalmadd/Pill-Image-Classification-By-Using-Stacking-Ensemble-Method/assets/84001348/2e4a6620-73d8-48c5-aca3-6f8b99b7d6a3)

Data cleaning:
- images that are faulty or incomplete were eliminated
- image formats were standardized to handle any inconsistencies or anomalies
- manual check was carried out to locate and eliminate any images that are irrelevant
- data augmentation techniques including rotation, scaling, and flipping were utilized to increase the dataset size to 20,000 images

Model Training:
- ResNet50, Inception-V3, and MobileNet base models were trained
- the base models were saved as .h5 files
- individual base learners aggregated using a stacking ensemble technique, using a meta model
- individual base learners aggregated using a bagging ensemble technique, using an Average() layer and WeightedAverageLayer(), respectively
- all models trained for 10 epochs

Results and Evaluation:
- performance was assessed using diverse metrics such as accuracy, precision, sensitivity, and F1 score
- evaluate computational efficiency and resource utilization of the stacking ensemble model
- confusion matrix were generated
- stacking ensemble model’s performance was compared to other ensemble models
- outcomes were evaluated against the findings documented in previous research

## Results and Discussion
- Inception-V3 outperformed the other base models with the highest test accuracy of 96.15%.
- MobileNet outperformed the other models in terms of training and prediction time of 4 Hours 8 Mins, and 32 seconds respectively.
- The proposed stacking ensemble model significantly outperforms the individual base models and related work with 98.80% accuracy. It also excelled in terms of precision, sensitivity, and F1-score.
- The proposed stacking ensemble model was the most time-efficient among the ensemble methods.
- Training time is influenced by the hardware configuration

## Conclusion
Research Contribution:
- Provides practical solutions for image classification in healthcare & pharmaceutical domains.
- Addresses existing gaps in the field by providing a rigorous comparative analysis by using more performance metrics for evaluation. 
- This research could also encourage other researchers to explore ensemble techniques for image classification and provide insights into the trade-offs between accuracy and training time.

Future Work:
- Focus on gathering larger and more diverse datasets.
- Adapting the research findings to real-time applications.
- Focus on improving the model's robustness against adversarial attacks 




