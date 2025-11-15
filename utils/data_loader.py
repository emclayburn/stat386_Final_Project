import pandas as pd
import streamlit as st

@st.cache_data
def load_team_data(path="all_teams.csv"):
    return pd.read_csv(path)

@st.cache_data
def load_goalie_data(path="data/goalies_allseasons.csv"):
    return pd.read_csv(path)
