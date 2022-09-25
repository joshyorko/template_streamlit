import streamlit as st
import datetime

def app():
  # ---- MAINPAGE ----
  st.title('Sample Report Input Form 2')
  st.markdown("##")

  # ---- SIDEBAR ---
  st.sidebar.title('Report Parameters')
  start = st.sidebar.date_input("Enter Start Date",datetime.date(2021, 8, 18))

  
  uploaded_files = st.sidebar.file_uploader("Choose a CSV file", accept_multiple_files=True)

  
        #csv1 = convert_df(df)
        #st.download_button("📥 Press to Download",csv1,f"occupancy_report_{out_file}.csv","text/csv",key='download-csv')
