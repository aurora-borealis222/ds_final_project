import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine('postgresql://salariesdb_owner:fvjJWZ0I5Rri@ep-bitter-morning-a2e4mkvk.eu-central-1.aws.neon.tech/salariesdb')

@st.cache_data
def get_salaries():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM salaries.salaries"))

    return pd.DataFrame(result)

@st.cache_data
def get_salaries_real():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM salaries.salaries_real"))

    return pd.DataFrame(result)

@st.cache_data
def get_inflation():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM salaries.inflation"))

    return pd.DataFrame(result)

@st.cache_data
def get_inflation_influence():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM salaries.inflation_influence"))

    return pd.DataFrame(result)

@st.cache_data
def get_salaries_real_and_gdp():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM salaries.salaries_real_and_gdp"))

    return pd.DataFrame(result)