# streamlit_app.py

import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect
from collections.abc import Iterable
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# Create a connection object.

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
def run_table():
	credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
	)
	conn = connect(credentials=credentials)

	@st.cache(ttl=600)
	def run_query(query):
		rows = conn.execute(query, headers=1)
		rows = rows.fetchall()
		return rows

	sheet_url = st.secrets["private_gsheets_url"]
	sheet2_url = st.secrets["private_ghseets2_url"]

	sheet1_data = run_query(f'SELECT * FROM "{sheet_url}"')
	sheet2_data = run_query(f'SELECT * FROM "{sheet2_url}"')

	

	st.write("Personal Info")
	df = pd.DataFrame(sheet1_data)
	df["age"] = df["age"].astype(int)
	df["activity_level"] = df["activity_level"].fillna(0)
	df = df.dropna()
	st.table(df)

	st.write("Game Data")
	ds = pd.DataFrame(sheet2_data)
	st.table(ds)

	


