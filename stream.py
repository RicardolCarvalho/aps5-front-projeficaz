import streamlit as st
import requests

URL = "https://www.streamlit.io/"

st.session_state['page'] = st.session_state.get('page', 'Cadastro_usuario')
page = st.sidebar.selectbox("Menu", [])
if page != st.session_state['page']:
    st.session_state['page'] = page