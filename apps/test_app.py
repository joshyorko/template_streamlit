import datetime

import streamlit as st
from pandas import read_csv

from scripts.utils import get_files, to_excel


def app():
  # ---- MAINPAGE ----
  st.title('Test App 1 Dashboard')
  st.markdown("##")

  # ---- SIDEBAR ---
  st.sidebar.title('Report Parameters')
  Test1 = st.sidebar.date_input("Test1",datetime.date(2021, 8, 18))
  Test2 = st.sidebar.date_input("Test2",datetime.date(2021, 8, 19))
  Test3Input = st.sidebar.selectbox('Test Input',('Input1','Input2'))
  out_file = st.sidebar.text_input('Output File Name')
  TestIncrementNumber = st.sidebar.number_input('Insert Increment Values',value=5)
  TestIncrementNumber = st.sidebar.number_input('Insert Increment Values (Increments of 1)')
  
  
  uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files=True)

  if st.sidebar.button('Run Report'):
        with st.spinner('Report Executing...'):
          zoneIds = get_files(uploaded_files)
          st.info(f"Zones Found [ {len(zoneIds)}]")
          st.info(f'Granularity [ **_{TestIncrementNumber}_** ] minutes')
          st.info(f'Test3Input [ **_{Test3Input}_** ]')
          st.info(f'Test1 Date [ **_{Test1}_** ]')
          st.info(f'Test2 Date [ **_{Test2}_** ]')
        #df = read_csv('test.csv')
        #df = df.reset_index().drop(columns=['index'])
        #df['Actual AttTest2 %'] = df['Actual AttTest2 %'].astype(str)
        #df_xlsx = to_excel(df)
        #st.download_button(label='📥 Download Current Result',data=df_xlsx ,file_name= f'{out_file}.xlsx')
        #st.dataframe(df)
        #st.success('Report Completed')
        #csv1 = convert_df(df)
        #st.download_button("📥 Press to Download",csv1,f"occupancy_report_{out_file}.csv","text/csv",key='download-csv')
