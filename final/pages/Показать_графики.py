import pandas as pd
import streamlit as st
import plotly.graph_objects as go
st.set_page_config(initial_sidebar_state="collapsed")

df = pd.read_csv('tmp.csv')


fig = go.Figure()
# label axis
fig.update_layout(
    xaxis_title="Обьект",
    yaxis_title="Время в движении",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#7f7f7f"
    )
)
# add data
fig.add_trace(go.Scatter(x=df.index, y=df['y'], mode='markers', name='Время в движении'))

# add points data
# fig.add_trace(go.Scatter(x=df['date_depart_year'], y=df['y'], , name='Время в движении'))
# add title
fig.update_layout(title_text='                                                                                                     Время в движении')
# show figure
st.plotly_chart(fig)
st.table(df)