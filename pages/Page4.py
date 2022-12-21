import altair as alt
import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import plotly.express as px
st.markdown(
"""
<style>
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    text-align: center;
}
</style>
<div class="footer">
    Created by <b><i>Abdulaziz</i></b> and <b><i>Muhannad</i></b>
</div>
""",
unsafe_allow_html=True,
)
alt.data_transformers.disable_max_rows()
st.title('Data Analized')


playStore = pd.read_csv('assignment/googleplaystore.csv')
playStore['Price'] = playStore['Price'].str.replace('$', '')
playStore['Price'] = playStore['Price'].str.replace('Everyone', '0')
playStore['Reviews'] = playStore['Reviews'].str.replace('M', '')
playStore = playStore.astype({'Price':float,'Reviews':float})
playStore.drop(playStore[playStore['Rating'] == 19. ].index, inplace=True)
playStore.dropna(inplace=True)
playStore["Last Updated"] = pd.to_datetime(playStore["Last Updated"], format="%B %d, %Y")
playStore["Year"] = playStore["Last Updated"].dt.year



st.subheader('Pie plot of a sample data of 10 apps and their Rating')
st.markdown('#### Column = Rating & App')
sampledata  = playStore.head(10).copy()
fig, ax = plt.subplots()
explode = (0, 0, 0.4, 0,0,0,0,0,0,0.4)  
ax.pie(sampledata['Rating'], labels=sampledata['App'],explode=explode,
        shadow=True, startangle=90,autopct='%1.1f%%')
st.pyplot(fig)


st.subheader('Bubble Chart of a sample data of 30 apps ')
st.markdown('#### Column = Review & Installs')
fig = px.scatter(
    playStore.head(30),
    x="Reviews",
    y="Installs",
    size="Reviews",
    color="App",
    hover_name="App",
    log_x=True,
    size_max=60,
)
fig
st.balloons()
