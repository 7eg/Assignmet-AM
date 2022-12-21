import streamlit as st 
import pandas as pd
import altair as alt
from streamlit_option_menu import option_menu
import colorsys
import time
import copy

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


@st.cache(allow_output_mutation=True)
def mainp(ap):
  app = copy.deepcopy(ap)
  return app

ap = st.file_uploader(label = 'File should be .csv', type='.csv', accept_multiple_files=False,)

uploa = mainp(ap) 




if ap is not None:
  playStore = pd.read_csv(ap)
  def convert_df(df):
    return df.to_csv().encode('utf-8')

  csv = convert_df(playStore)

  st.download_button(
      label="Download CSV file",
      data=csv,
      file_name='googlePlayStore.csv',
      mime='text/csv',
  )

  st.title('googleplay Application')
  playStore['Price'] = playStore['Price'].str.replace('$', '')
  playStore['Price'] = playStore['Price'].str.replace('Everyone', '0')
  playStore['Reviews'] = playStore['Reviews'].str.replace('M', '')
  playStore['Installs'] = playStore['Installs'].str.replace('+','')
  playStore['Installs'] = playStore['Installs'].str.replace('Free','0')
  playStore['Installs'] = playStore['Installs'].str.replace(',','')
  playStore.drop(playStore[playStore['Rating'] == 19. ].index, inplace=True)
  playStore.dropna(inplace=True)
  playStore = playStore.astype({'Price':float,'Reviews':float,'Installs':float})
  playStoreApp = st.selectbox("Select app Genre of the App", playStore['Genres'].unique())
  st.write(playStoreApp)
  plot_type = st.radio("select the plot type",['scatter','line','histogram','Bar','Binned Heatmap'])
  if plot_type == 'scatter':
    pl = alt.Chart(playStore[playStore['Genres'] == playStoreApp],width=800, height=600).mark_circle().encode(
      x = 'Reviews',
      y = 'Installs',
      color='App:N',
      tooltip = ['Reviews','Installs','App']
  ).interactive()
  elif plot_type == 'histogram':
    pl = alt.Chart(playStore[playStore['Genres'] == playStoreApp],width=800, height=600).mark_bar().encode(
      x = 'Reviews',
      y = 'count()',
       color='App:N',
      tooltip = ['Reviews','App']
  ).interactive()
  elif plot_type == 'Bar':
    pl = alt.Chart(playStore[playStore['Genres'] == playStoreApp],width=800, height=600).mark_bar().encode(
      x = 'Reviews',
      y = 'App',
       color='App:N',
      tooltip = ['Reviews','App']
  ).interactive()
  elif plot_type == 'Binned Heatmap':
    pl =alt.Chart(playStore[playStore['Genres'] == playStoreApp],width=800, height=600).mark_rect().encode(
    alt.X('Rating:Q', bin=alt.Bin(maxbins=60)),
    alt.Y('Reviews:Q', bin=alt.Bin(maxbins=40)),
    alt.Color('Rating:Q', scale=alt.Scale(scheme='greenblue')),
      tooltip=['App','Rating','Genres']
).interactive()
  else :
    pl = alt.Chart(playStore[playStore['Genres'] == playStoreApp],width=800, height=600).mark_line().encode(
      x = 'Reviews',
      y = 'Installs',

      tooltip = ['Reviews','Installs','App']
  ).interactive()
  st.altair_chart(pl)
elif ap is None:
  st.markdown('# `Please Upload Google Play Dataset`')


