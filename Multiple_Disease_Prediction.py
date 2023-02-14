# -*- coding: utf-8 -*-
"""
Created on Sun May  8 21:01:15 2022

@author: siddhardhan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

breast_cancer_model = pickle.load(open('breast_cancer_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinson's Prediction',
                           'Breast Cancer Diagnostics'],
                          icons=['activity','heart','person','virus2'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmewz7Or8Lg624lDbvbdvjz9XtR147p7v37w&usqp=CAU", width=300)
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuU9a2n9s4TQo5YL6zaIlsBbnEIhwFVwejkg&usqp=CAU");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('**Number of Pregnancies**')
        
    with col2:
        Glucose = st.text_input('**Glucose Level**')
    
    with col3:
        BloodPressure = st.text_input('**Blood Pressure value**')
    
    with col1:
        SkinThickness = st.text_input('**Skin Thickness value**')
    
    with col2:
        Insulin = st.text_input('**Insulin Level**')
    
    with col3:
        BMI = st.text_input('**BMI value**')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('**Diabetes Pedigree Function value**')
    
    with col2:
        Age = st.text_input('**Age of the Person**')
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = '**The person is Diabetic**'
        else:
          diab_diagnosis = '**The person is not Diabetic**'
        
    st.success(diab_diagnosis)




# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRGbs_BElRUVufk2nfoPnUIvtV3L_uKD9jXEg&usqp=CAU", width=300)
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcThbr1aGMfHfY-tDM7_wFtlr9fWxzuIUnbRJw&usqp=CAU");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('**Age**')
        
    with col2:
        sex = st.text_input('**Sex**')
        
    with col3:
        cp = st.text_input('**Chest Pain types**')
        
    with col1:
        trestbps = st.text_input('**Resting Blood Pressure**')
        
    with col2:
        chol = st.text_input('**Serum Cholestoral in mg/dl**')
        
    with col3:
        fbs = st.text_input('**Fasting Blood Sugar > 120 mg/dl**')
        
    with col1:
        restecg = st.text_input('**Resting Electrocardiographic results**')
        
    with col2:
        thalach = st.text_input('**Maximum Heart Rate achieved**')
        
    with col3:
        exang = st.text_input('**Exercise Induced Angina**')
        
    with col1:
        oldpeak = st.text_input('**ST depression induced by exercise**')
        
    with col2:
        slope = st.text_input('**Slope of peak exercise ST segment**')
        
    with col3:
        ca = st.text_input('**Major vessels colored by flourosopy**')
        
    with col1:
        thal = st.text_input('**thal: 0 = normal;  1 = fixed defect;  2 = reversable defect**')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = '**The person is having heart disease**'
        else:
          heart_diagnosis = '**The person does not have any heart disease**'
        
    st.success(heart_diagnosis)
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):

    st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTIiqfhVS1oCp-7K5O4YFTQj92MYzfBLca9MA&usqp=CAU", width=300)    
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("data:image/jpeg;base64,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");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('**MDVP:Fo(Hz)**')
        
    with col2:
        fhi = st.text_input('**MDVP:Fhi(Hz)**')
        
    with col3:
        flo = st.text_input('**MDVP:Flo(Hz)**')
        
    with col4:
        Jitter_percent = st.text_input('**MDVP:Jitter(%)**')
        
    with col5:
        Jitter_Abs = st.text_input('**MDVP:Jitter(Abs)**')
        
    with col1:
        RAP = st.text_input('**MDVP:RAP**')
        
    with col2:
        PPQ = st.text_input('**MDVP:PPQ**')
        
    with col3:
        DDP = st.text_input('**Jitter:DDP**')
        
    with col4:
        Shimmer = st.text_input('**MDVP:Shimmer**')
        
    with col5:
        Shimmer_dB = st.text_input('**MDVP:Shimmer(dB)**')
        
    with col1:
        APQ3 = st.text_input('**Shimmer:APQ3**')
        
    with col2:
        APQ5 = st.text_input('**Shimmer:APQ5**')
        
    with col3:
        APQ = st.text_input('**MDVP:APQ**')
        
    with col4:
        DDA = st.text_input('**Shimmer:DDA**')
        
    with col5:
        NHR = st.text_input('**NHR**')
        
    with col1:
        HNR = st.text_input('**HNR**')
        
    with col2:
        RPDE = st.text_input('**RPDE**')
        
    with col3:
        DFA = st.text_input('**DFA**')
        
    with col4:
        spread1 = st.text_input('**spread1**')
        
    with col5:
        spread2 = st.text_input('**spread2**')
        
    with col1:
        D2 = st.text_input('**D2**')
        
    with col2:
        PPE = st.text_input('**PPE**')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "**The person has Parkinson's disease**"
        else:
          parkinsons_diagnosis = "**The person does not have Parkinson's disease**"
        
    st.success(parkinsons_diagnosis)



# Breast Cancer Prediction Page
if (selected == "Breast Cancer Diagnostics"):
    
    st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQl7UYk7IYPEqxd40IqAt0slUDT3x2Lz6NaaA&usqp=CAU", width=300)
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://wallpaper.dog/large/20431729.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
    # page title
    st.title("Breast Cancer Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        radius_mean = st.text_input('**Mean Radius**')
        
    with col2:
        texture_mean = st.text_input('**Mean Texture**')
        
    with col3:
        perimeter_mean = st.text_input('**Mean Perimeter**')
        
    with col4:
        area_mean = st.text_input('**Mean Area**')
        
    with col5:
        smoothness_mean = st.text_input('**Mean Smoothness**')
        
    with col1:
        compactness_mean = st.text_input('**Mean Compactness**')
        
    with col2:
        concavity_mean = st.text_input('**Mean Concavity**')  
        
    with col3:
        concave_points_mean = st.text_input('**Mean Concave Points**')
        
    with col4:
        symmetry_mean = st.text_input('**Mean Symmetry**')
        
    with col5:
       fractal_dimension_mean = st.text_input('**Mean Fractal Dimension**')
        
    with col1:
        radius_error = st.text_input('**Radius Error**')
        
    with col2:
        texture_error = st.text_input('**Texture Error**')
        
    with col3:
        perimeter_error = st.text_input('**Perimeter Error**')
        
    with col4:
        area_error = st.text_input('**Area Error**')
        
    with col5:
        smoothness_error = st.text_input('**Smoothness Error**')
        
    with col1:
        compactness_error = st.text_input('**Compactness Error**')
        
    with col2:
        concavity_error = st.text_input('**Concavity Error**')
        
    with col3:
        concave_points_error = st.text_input('**Concave Points Error**')
        
    with col4:
        symmetry_error = st.text_input('**Symmetry Error**')
        
    with col5:
        fractal_dimension_error = st.text_input('**Fractal Dimension Error**')
        
    with col1:
        radius_worst = st.text_input('**Worst Radius**')
        
    with col2:
        texture_worst = st.text_input('**Worst Texture**')
        
    with col3:
        perimeter_worst = st.text_input('**Worst Perimeter**')
        
    with col4:
        area_worst = st.text_input('**Worst Area**')
        
    with col5:
        smoothness_worst = st.text_input('**Worst Smoothness**')
    
    with col1:
        compactness_worst = st.text_input('**Worst Compactness**')
        
    with col2:
        concavity_worst = st.text_input('**Worst Concavity**')
        
    with col3:
        concave_points_worst = st.text_input('**Worst Concave Points**')
        
    with col4:
        symmetry_worst = st.text_input('**Worst Symmetry**')
        
    with col5:
        fractal_dimension_worst = st.text_input('**Worst Fractal Dimension**')    
        
    
    
    # code for Prediction
    breast_cancer_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Breast Cancer Result"):
        breast_cancer__prediction = breast_cancer_model.predict([[radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean, 
                                                                  radius_error, texture_error, perimeter_error, area_error, smoothness_error, compactness_error, concavity_error, concave_points_error, symmetry_error, fractal_dimension_error, 
                                                                  radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst, compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst]])                          
        
        if (breast_cancer__prediction[0] == 1):
          breast_cancer_diagnosis = "**The Breast cancer is Benign**"
        else:
          breast_cancer_diagnosis = "**The Breast Cancer is Malignant**"
        
    st.success(breast_cancer_diagnosis)
