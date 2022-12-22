import streamlit as st 
import pandas as pd
import altair as alt
from streamlit_option_menu import option_menu
import time
import copy
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

# cahce for storing csv file uploaded 
@st.cache(allow_output_mutation=True)
def mainp(ap):
  app = copy.deepcopy(ap)
  return app
# file uploader to make the user upload the csv
ap = st.file_uploader(label = 'File should be .csv', type='.csv', accept_multiple_files=False,)
# passing the file uploaded to the mainp function in order to save it in the cache 
uploa = mainp(ap) 



# if clause to check if the file is uploaded if true then read the file and show the radio buttons with charts
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
  # title
  st.title('googleplay Application')
  # delete $ from the price column (for converting to float pourpose )
  playStore['Price'] = playStore['Price'].str.replace('$', '')
  # delete Everyone from the price column (for converting to float pourpose )
  playStore['Price'] = playStore['Price'].str.replace('Everyone', '0')
  # delete M from the Reviews column (for converting to float pourpose )
  playStore['Reviews'] = playStore['Reviews'].str.replace('M', '')
    # delete + from the Installs column (for converting to float pourpose )
  playStore['Installs'] = playStore['Installs'].str.replace('+','')
    # delete , from the Installs column (for converting to float pourpose )
  playStore['Installs'] = playStore['Installs'].str.replace('Free','0')
   # delete Free from the Installs column (for converting to float pourpose )
  playStore['Installs'] = playStore['Installs'].str.replace(',','')
  # droping the outliers of Rating column
  playStore.drop(playStore[playStore['Rating'] == 19. ].index, inplace=True)
  # droping NAN columns
  playStore.dropna(inplace=True)
  # converting the Price, Reviews and Installs to float 
  playStore = playStore.astype({'Price':float,'Reviews':float,'Installs':float})
  # selectbox to select the genere of the app in order to use the selected genere in the radio buttons of the charts
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
  # the else if statement if the file is not uploaded b the user show this markdown 
elif ap is None:
  st.markdown('# `Please Upload Google Play Dataset`')


