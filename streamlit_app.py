import streamlit as st
import pandas as pd
from pinotdb import connect
##import plotly-express as px
from datetime import datetime
import time

st.set_page_config(page_title="Engagement User Dashboard", layout="wide")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

# ##Connect to Pinot
# conn = connect(host='http://54.179.19.243/', port=8099, path='/query/sql', scheme='http'"New Text Document.txt")

# # Query the date
# curs = conn. cursor ()
# query = """
# SELECT CATEGORY, COUNT(USERID) as PageViews
# FROM Consolidate
# GROUP BY CATEGORY
# LIMIT 200
# """

# curs.execute (query)
# df_summary = pd.DataFrame(curs, coluans=[iten(0) for Iten in curs.desceiption])

