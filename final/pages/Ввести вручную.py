import numpy as np
import pandas as pd
import streamlit as st
from model import Predicter
from utils import *

st.set_page_config(initial_sidebar_state="collapsed", layout='wide')
# st.markdown("# Ввести данные о поездах вручную️")
col = st.columns(7)
col = st.columns(7)
col = st.columns(7)
col = st.columns(7)
col = st.columns(7)
col = st.columns(7)
add_bg_from_local('16922.png')
# set color text to black
st.markdown(
    """
<style>
p {
    color: black;
}
</style>
""",
    unsafe_allow_html=True,
)

# create manual input with layout
col = st.columns(7)
col2 = st.columns(7)
col3 = st.columns(7)
# You can use a column just like st.sidebar:

st_code_snd = col[0].text_input('id станции отправления', value='wagonwagonwagontutu:)wagon')
st_code_rsv = col[1].text_input('id станции назначения', value='wagondigitalnewyearrailway:)happy')
date_depart_year = col[2].selectbox('год отправления   ', [2019, 2020, 2021, 2022], index=2)
date_depart_month = col[3].selectbox('месяц отправления', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], index=11 )
date_depart_week = col[4].selectbox('неделя отправления', [1,2,3,4,5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52], index=49)
date_depart_day = col[5].selectbox('день отправления', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31], index=30)
date_depart_hour = col[6].selectbox('час отправления', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], index=23)

fr_id = col2[0].text_input('id груза', value=3390)
route_type = col2[1].selectbox('тип отправки', [4.0,1.0, 2.0], index=0)
is_load = col2[2].selectbox('признак гружёности', [1, 0], index=1)
rod = col2[3].selectbox('род подвижного состава', [4,2], index=1)
common_ch = col2[4].selectbox('id характеристики ', [11.0,2.0], index=0)
vidsobst = col2[5].selectbox('вид собственности', [102.0, 2.0], index=0)
distance = int(col2[6].text_input('расстояние рейса', int(32.0)))

snd_org_id = col3[0].text_input('id грузоотправителя', value=2)
rsv_org_id = col3[1].text_input('id грузополучателя', value=3)
snd_roadid = col3[2].selectbox('id дороги отправления', [1,2], index=1)
rsv_roadid = col3[3].selectbox('id дороги назначения', [1,2], index=1)
snd_dp_id = col3[4].text_input('id региона отправления', value=3)
rsv_dp_id = col3[5].text_input('id региона назначения', value=4)
y_pred = col3[6].text_input('Ожидаемое время, ч', value=5)

# create dataframe
data = {'st_code_snd': [st_code_snd],
        'st_code_rsv': [st_code_rsv],
        'date_depart_year': [date_depart_year],
        'date_depart_month': [date_depart_month],
        'date_depart_week': [date_depart_week],
        'date_depart_day': [date_depart_day], 'date_depart_hour': [date_depart_hour],
        'fr_id': [fr_id], 'route_type': [route_type], 'is_load': [is_load], 'rod': [rod], 'common_ch': [common_ch],
        'vidsobst': [vidsobst], 'distance': [distance], 'snd_org_id': [snd_org_id], 'rsv_org_id': [rsv_org_id],
        'snd_roadid': [snd_roadid], 'rsv_roadid': [rsv_roadid], 'snd_dp_id': [snd_dp_id], 'rsv_dp_id': [rsv_dp_id]}

df = pd.DataFrame(data)
# st.table(pd.DataFrame(data))

# predict
if st.button('Предсказать'):
    model = Predicter()
    y_pred = model.predict(df)
    # print(y_pred)
    # df.insert(0, 'y', y_pred)
    # append to dataframe
    # add y_pred col to the beginning of the dataframe
    # y_pred = [np.random.randint(1, 100) for i in range(len(df))]
    # write text Ожидаемое время

    # increase text size
    st.markdown(f'<p style="font-size: 20px;font-color: red">Ожидаемое время в пути для рейса из <b>{st_code_snd}</b> до <b>{st_code_rsv}</b> составит <u>{str(y_pred[0])[:6]}</u> ч.</p>', unsafe_allow_html=True)
    df.insert(0, 'y', y_pred)
    # st.write(df)
    # st.table(pd.DataFrame(df))




