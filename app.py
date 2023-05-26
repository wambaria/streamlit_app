
import pandas as pd 
import numpy as np
import pickle as pkl  
import streamlit as st  
from PIL import Image as img  
    
# loading in the model to predict on the data  
pickle_in1 = open('classifier.pkl', 'rb')  
classifier = pkl.load(pickle_in1)  
    
def welcome():  
    return 'welcome you all'  
    
# here, we will define the function which will make the prediction using the      # data which the user have imported  
def prediction(sepal_length1, sepal_width1, petal_length1, petal_width1):    
     
    prediction = classifier.predict(  
        [[sepal_length1, sepal_width1, petal_length1, petal_width1]])  
    print(prediction)  
    return prediction  
        
    
# Here, this is the main function in which we will be defining our webpage   
def main():  
      # Now, we will give the title to out web page  
    st.title("Iris Flower Prediction")  
        
    # Now, we will be defining some of the frontend elements of our web            # page like the colour of background and fonts and font size, the padding and    # the text to be displayed  
    html_temp = """  
    <div style = "background-colour: #FFFF00; padding: 16px">  
    <h1 style = "color: #000000; text-align: centre; "> Streamlit Iris Flower Classifier ML App   
     </h1>  
    </div>  
    """  
        
    # Now, this line will allow us to display the front-end aspects we have   
    # defined in the earlier  
    st.markdown(html_temp, unsafe_allow_html = True)  
        
    # Here, the following lines will create the text boxes in which the user can     # enter the data which is required for making the prediction  
    sepal_length1 = st.text_input ("Sepal Length ", " Type Here")  
    sepal_width1 = st.text_input ("Sepal Width ", " Type Here")  
    petal_length1 = st.text_input ("Petal Length ", " Type Here")  
    petal_width1 = st.text_input ("Petal Width ", " Type Here")  
    result = " "  
        
    # here, the below line will ensure that whenever the button named 'Predict' # is clicked, the prediction function that is defined earlier is called for making   # the prediction and it will also store it in the variable result  
    if st.button ("Predict"):  
        result = prediction (sepal_length1, sepal_width1, petal_length1, petal_width1)  
    st.success ('The output of the above is {}'.format(result))  
if __name__== '__main__':  
    main()  