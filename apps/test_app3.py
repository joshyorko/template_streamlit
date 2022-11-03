import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from pivottablejs import pivot_ui


def app():
  
  # ---- MAINPAGE ----
  st.title('Test App 3 Dashboard')
  st.markdown("##")
  df = pd.read_csv('apps/pivotfootball.csv')
  t = pivot_ui(df)
  with open(t.src) as t:
    components.html(t.read(), width=1500, height=600, scrolling=True)