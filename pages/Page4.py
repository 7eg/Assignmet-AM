import altair as alt
import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
import plotly.express as px
# the foother for showing names Abdulaziz and Muhannad
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


playStore = pd.read_csv('googleplaystore.csv')
playStore['Price'] = playStore['Price'].str.replace('$', '')
playStore['Price'] = playStore['Price'].str.replace('Everyone', '0')
playStore['Reviews'] = playStore['Reviews'].str.replace('M', '')
playStore = playStore.astype({'Price':float,'Reviews':float})
playStore.drop(playStore[playStore['Rating'] == 19. ].index, inplace=True)
playStore.dropna(inplace=True)
# converting the Last Updated column from Object to date 
playStore["Last Updated"] = pd.to_datetime(playStore["Last Updated"], format="%B %d, %Y")
# getting the year only column 
playStore["Year"] = playStore["Last Updated"].dt.year


# sub header 
st.subheader('Pie plot of a sample data of 10 apps and their Rating')
st.markdown('#### Column = Rating & App')
# getting sample of data 10 rows for the following pie chart
sampledata  = playStore.head(10).copy()
fig, ax = plt.subplots()
explode = (0, 0, 0.4, 0,0,0,0,0,0,0.4)  
ax.pie(sampledata['Rating'], labels=sampledata['App'],explode=explode,
        shadow=True, startangle=90,autopct='%1.1f%%')
# showing the chart
st.pyplot(fig)

# sub header 
st.subheader('Bubble Chart of a sample data of 30 apps ')
st.markdown('#### Column = Review & Installs')
# Bubble chart 
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
# showing the bubble chart
fig

# showing balloons 
st.balloons()
