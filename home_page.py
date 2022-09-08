import streamlit as st 
import pandas as pd 

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
from wordcloud import WordCloud
import pygsheets
import pandas as pd
import random
from google.oauth2 import service_account
from gsheetsdb import connect
from datetime import date
gc = pygsheets.authorize(service_file='./key/key.json')


def run_home_page():
	#setting profile coloumns
	profile_info= {
		'profile_id':[],
		'name':[],
		'age':[],
		'contact' :[],
		'activity_level':[],
		'date':[]
				}

	#convert columns to data frame
	ds = pd.DataFrame(profile_info)

	#open sheet
	sh = gc.open('test_sheet')

	#select work sheet and write dataframe
	#select the first sheet 
	wks = sh[0]
	#update the first sheet with df, starting at cell B2. 
	if 'regist' not in st.session_state:
		st.session_state['regist'] = False
	# wks.set_dataframe(ds,(1,1))
	def profile_writer(name,age,contact):
		row_count = len(wks.get_all_records()) + 2
		id=row_count-1
		activity_level = ""
		now_date = str(date.today())
		data1=[id,name,age,contact,activity_level,now_date]
		wks.append_table(data1,start='2')
	


	form1 = st.empty()
	if st.session_state['regist'] == False:
		with form1.form(key="reg_form"):
			st.title("Registartion")
			st.subheader("Enter the details")
			name = st.text_input("Enter Your Name")
			contact = st.text_input("Enter Your number")
			age = st.slider("Enter your age")
			sub = st.form_submit_button("Submit",on_click=profile_writer(name,age,contact))
			if sub:
				st.write("Written to DB")
				form1.empty()
				st.session_state['regist'] = True

	


