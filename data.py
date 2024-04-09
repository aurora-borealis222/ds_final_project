import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# engine = create_engine('postgresql://salariesdb_owner:fvjJWZ0I5Rri@ep-bitter-morning-a2e4mkvk.eu-central-1.aws.neon.tech/salariesdb')

connection = st.connection("postgresql", type="sql")

@st.cache_data
def get_salaries():
    result = connection.query("SELECT * FROM salaries.salaries")
    return pd.DataFrame(result)

@st.cache_data
def get_salaries_real():
    result = connection.query("SELECT * FROM salaries.salaries_real")
    return pd.DataFrame(result)

@st.cache_data
def get_inflation():
    result = connection.query("SELECT * FROM salaries.inflation")
    return pd.DataFrame(result)

@st.cache_data
def get_inflation_influence():
    result = connection.query("SELECT * FROM salaries.inflation_influence")
    return pd.DataFrame(result)

@st.cache_data
def get_salaries_real_and_gdp():
    result = connection.query("SELECT * FROM salaries.salaries_real_and_gdp")
    return pd.DataFrame(result)