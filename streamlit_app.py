import streamlit as st
import numpy as np
import pandas as pd


solar_bd = pd.read_csv("/Users/junKa/Documents/db-prueba-dash.csv")


st.title('Solar Temperature Variations Relative to A “Quiet Sun” Day In August 2008')

st.write(pd.DataFrame({
    'first column': solar_bd.Date,
    'second column': solar_bd.Irradiance,
    'third column': solar_bd.Wavelength
}))

chart_data = pd.DataFrame(
     pd.to_datetime(solar_bd.Date),
     solar_bd.Irradiance)
st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe1'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)



df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)


