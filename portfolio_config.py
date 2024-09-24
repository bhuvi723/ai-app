import streamlit as st
import json

with open('portfolio_info.json', 'r') as f:
    portfolio_data = json.load(f)

# st.set_page_config(page_title=f"{portfolio_data['info_keys']['name']} | My Portfolio", page_icon=":rocket:", layout="wide")

keys = list(portfolio_data[list(portfolio_data.keys())[1]])[0]
print(keys)