
# Core Pkgs
from select import select
import streamlit as st 
import streamlit.components.v1 as stc 
from home_page import run_home_page
from eda_app import run_table
from ml_app import run_cap
from Recom import run_rec
from streamlit_option_menu import option_menu
import time

st.sidebar.title("AIMES")
# 1=sidebar menu, 2=horizontal menu,3=Recommendation, 4=horizontal menu w/ custom menu
EXAMPLE_NO = 1

    
registered = False
def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Activity Info", "Display Table","Visualizations","Recommendations","Game Stats"],  # required
                icons=["house", "book", "table","bar-chart","person","joystick"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected

    if example == 2:
        # 2. horizontal menu w/o custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Activity Info", "Display Table","Graphs","Recommendations","Game Stats"],  # required
            icons=["house", "excercise", "table","graph","arrow","game"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected

    if example == 3:
        
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Activity Info", "Display Table","Graphs","Recommendations","Game Stats"],  # required
            icons=["house", "excercise", "table","graph","arrow","game"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected
	
    if example == 4:
        
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Activity Info", "Display Table","Graphs","Recommendations","Game Stats"],  # required
            icons=["house", "excercise", "table","graph","arrow","game"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )
        return selected
	

    if example == 5:
        # 2. horizontal menu with custom style
        selected = option_menu(
            menu_title=None,  # required
            options=["Home", "Activity Info", "Display Table","Graphs","Recommendations","Game Stats"],  # required
            icons=["house", "excercise", "table","graph","arrow","game"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
            styles={
                "container": {"padding": "0!important", "background-color": "#fafafa"},
                "icon": {"color": "orange", "font-size": "25px"},
                "nav-link": {
                    "font-size": "25px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#eee",
                },
                "nav-link-selected": {"background-color": "green"},
            },
        )
        return selected

	


selected = streamlit_menu(example=EXAMPLE_NO)
if selected == "Home":
	run_home_page()
elif selected == "Activity Info":
	run_cap()
elif selected == "Recommendations":
	run_rec()
elif selected == "Display Table":
    run_table()


	



