import streamlit as st
from pandas import read_csv

from scripts.utils import get_files,to_excel

import datetime

def app():
  # ---- MAINPAGE ----
  st.title('Sample Report Input Form')
  st.markdown("##")

  # ---- SIDEBAR ---
  st.sidebar.title('Report Parameters')
  start = st.sidebar.date_input("Enter Start Date",datetime.date(2021, 8, 18))
  end = st.sidebar.date_input("Enter End Date",datetime.date(2021, 8, 19))
  timezone = st.sidebar.selectbox('Enter Timezone',('Central','Eastern'))
  out_file = st.sidebar.text_input('Output File Name')
  granularity = st.sidebar.number_input('Insert Granularity',value=5)
  time_after_class = st.sidebar.number_input('Time After Class Start (Increments of 1)')
  
  
  uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files=True)

  if st.sidebar.button('Run Report'):
        with st.spinner('Report Executing...'):
          zoneIds = get_files(uploaded_files)
          st.info(f"Zones Found [ {len(zoneIds)}]")
          st.info(f'Granularity [ **_{granularity}_** ] minutes')
          st.info(f'TimeZone [ **_{timezone}_** ]')
          st.info(f'Start Date [ **_{start}_** ]')
          st.info(f'End Date [ **_{end}_** ]')
        df = read_csv('test.csv')
        df = df.reset_index().drop(columns=['index'])
        df['Actual Attend %'] = df['Actual Attend %'].astype(str)
        df_xlsx = to_excel(df)
        st.download_button(label='📥 Download Current Result',data=df_xlsx ,file_name= f'{out_file}.xlsx')
        st.dataframe(df)
        st.success('Report Completed')
        #csv1 = convert_df(df)
        #st.download_button("📥 Press to Download",csv1,f"occupancy_report_{out_file}.csv","text/csv",key='download-csv')
