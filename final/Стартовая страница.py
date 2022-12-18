import streamlit as st
from utils import *
st.set_page_config(initial_sidebar_state="collapsed",layout='wide', page_title="Стартовая страница", page_icon="🌍")
# st.title('Wagon Hackathon.')
st.columns(2)
st.columns(2)
st.columns(2)
st.columns(2)
st.columns(2)
st.columns(2)
st.columns(2)
st.columns(2)
st.columns(2)
st.columns(2)
st.columns(2)
st.columns(2)




# add subheader and text
# st.text('''
# Разработанный веб-сервис позволяет как ввести данные о поездах вручную,
# так и загрузить csv файл с информацией о поездах
# и раcсчитать примерное время в движении.''')

add_bg_from_local('1691_without_button.png')
url = '/Ввести_вручную'
for i in range(0, 21):
    res = st.columns(1)

col4, col5, col6 = st.columns([1, 2, 1])

col6.markdown(f'''
<a href="{url}"><button style="background-color:#FF7314; color:White; font-size: 40px; border-radius: 10px; border: 3px solid #FF7314; padding: -15px 1112px; text-align: left; text-decoration: none; display: inline-block; margin: -30px -100px; cursor: pointer;">ПОЛУЧИТЬ ПРОГНОЗ</button></a>
''',
              unsafe_allow_html=True)
# invisible button
