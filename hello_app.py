

import streamlit as st
import altair as alt
import re
import pandas as pd
import numpy as np




def write_to_file(file_name, data_dict): # takes the dictionary and save it file with newlines
    with open(file_name, "w") as f:
        f.write(str(data_dict))

def read_from_file(file_name): # read the file and gives dictionary
    with open(file_name, "r") as f:
        data_text = f.read()
        data_dict = eval(data_text)
        return data_dict


pass_code = 'yo'
if st.text_input('enter the code') == pass_code:
    
    
    file_name = 'data_dict.txt'
    data_dict = read_from_file(file_name)
    
    
    
    title = st.text_input("What do you want to write about ?")
    
    body = st.text_area("Start .... ", height=200, max_chars=None)
    
    if st.button("save entry "):
        try:
            data_x = body + '\n' + data_dict[title]
            data_dict.pop(title,None)
            data_dict[title] = data_x
            
        except:
            data_dict[title] = body
        write_to_file(file_name, data_dict)
        
    
    if st.button("read previous entries "):
        st.write(dict(reversed(list(data_dict.items())))) # show the dictionary in reverse order
    
    
    
    
    
    
    
    
    
    
    
    
