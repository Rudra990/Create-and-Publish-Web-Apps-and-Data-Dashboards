import streamlit as st
import pandas

data = {'Series_1':[1,2,3],
        'Series_2':[4,52,53]
}

df = pandas.DataFrame(data)


st.title('Our First Streamlit App')
st.subheader('Introducing Streamlit in Automate Everything with Python')

st.write('''This is my first web app using streamlit
Enjoy it!!! 
''')

st.write(df)
st.line_chart(df)

myslider = st.slider('Celsius')
st.write(myslide, 'in Fahrenheit is',myslider  * 9/5 +32)
