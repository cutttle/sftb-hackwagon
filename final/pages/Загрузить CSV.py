import numpy as np
import pandas as pd

from utils import *

from catboost import CatBoostRegressor
from model import Predicter
st.set_page_config(initial_sidebar_state="collapsed")


st.markdown("Загрузить CSV файл")
st.sidebar.markdown("# Загрузить CSV файл")

add_bg_from_local('1693new.png')

st.columns(2)
st.columns(2)
st.columns(2)
st.columns(2)
st.columns(2)

def plotly_to_pdf(fig, filename):
    import plotly.io as pio
    pio.write_image(fig, filename)


# if mode is csv
# add file uploader
file = st.file_uploader('', type='csv')
if file is not None:
    df = pd.read_csv(file)
    if 'y' in df.columns:
        df = df.drop('y', axis=1)
    m = st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #FF7314;
        color:#00ff00;
    }
    div.stButton > button:hover {
        background-color: #8A2432;
        color:#00ff00;
        }
    </style>""", unsafe_allow_html=True)

    ab = st.columns([2, 1, 2])
    if ab[1].button('Предсказать 👌👌'):
        model = Predicter()
        y_pred = abs(model.predict(df))
        # y_pred = [np.random.randint(1, 100) for i in range(len(df))]
        df.insert(0, 'y', y_pred)
        # st.write(df)
        ab = st.columns([2, 1, 1])
        am = st.markdown("""
        <style>
        div.stDownloadButton > button:first-child {
            background-color: #FF7314;
            color:#ffff00;
        }
        div.stDownloadButton > button:hover {
            background-color: #8A2432;
            color:#00ffff;
            }
        </style>""", unsafe_allow_html=True)
        ab[0].download_button(
            label="Скачать предсказанные времена",
            data=pd.DataFrame(df).to_csv(index=False),
            file_name='large_df.csv',
            mime='text/csv',
        )
        # save to csv
        df.to_csv('tmp.csv', index=False)
        url = '/Показать_графики'
        ab[2].markdown(f'''
        <a href="{url}"><button style="background-color:#FF7314; color:White; font-size: 20px; border-radius: 5px; border: 1px solid #FF7314; padding: -10px 11px; text-align: left; text-decoration: none; display: inline-block; margin: 0px -50px; cursor: pointer;">Показать информацию</button></a>
        ''',
                      unsafe_allow_html=True)

        # plot y_pred with plotly
