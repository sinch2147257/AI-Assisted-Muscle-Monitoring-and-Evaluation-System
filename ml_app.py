import subprocess
import sys
import streamlit as st
import random
import pygsheets
def run_cap():
	def start_capture():
		subprocess.run([f"{sys.executable}", "activity_check.py"])
	stress_button = st.button("Activate Stress Monitor",key="monitor")
	cap_button = st.button("Start Capturing",key="capsforactivity")
	
	if cap_button:
		start_capture()

	gc = pygsheets.authorize(service_file='./key/key.json')
	sh = gc.open('test_sheet')
	wks = sh[0]
	current_row_count = len(wks.get_all_records()) + 1
	cell_addr = "E"+str(current_row_count)
	print(cell_addr)
	value = wks.get_value(cell_addr)
	stress_level = random.randint(0,5)
	def write_on_bar():
		with st.sidebar:
			my_bar = st.progress(0)
			if value=="Low":
				my_bar.progress(25)
				st.write("Activity: Low")
			elif value=="Medium":
				my_bar.progress(50)
				st.write("Activity: Medium")
			else:
				my_bar.progress(100)
				st.write("Activity: High")
			if stress_level==3:
				st.write("Stress Level: High")
			else:
				st.write("Stress Level: Low")
	if len(value)!=0:
		write_on_bar()
		
run_cap()
