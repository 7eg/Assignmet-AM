import altair as alt
import pandas as pd
import streamlit as st 
import matplotlib.pyplot as plt
st.set_page_config(
  page_title="Assignment", )

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

# Disable the maximum row size which is 5k because the dataset we use is 10k rows
alt.data_transformers.disable_max_rows()
st.markdown('### Choose color for the text')
# color picker 
selected_color = st.color_picker('','#8E3E3E')
# cahce for storing color picked 
@st.cache
def defColor(cl):
  pl = cl
  return pl

colo = defColor(selected_color)

# Intro
st.title('`Google Play Store Apps`')
st.markdown('### Web scraped data of 10k Play Store apps for analysing the Android market.')
st.markdown(f"<span style='color: {colo}'>The Google Play Store Apps dataset on Kaggle is a collection of data on over 10,000 mobile applications from the Google Play Store. The data was collected in August 2018, and includes information on each app's rating, category, number of reviews, and size. The dataset is useful for anyone interested in analyzing mobile app trends or building predictive models for app success.</span>", unsafe_allow_html=True)
st.subheader('**`The dataset consist of the below 13 columns:`** ')
st.markdown(f"<span style='color: {colo}'>1 - App - The name of the app.'</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: {colo}'>2 - Category - The category the app belongs to, such as Games, Education, or Finance.</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: {colo}'>3 - Rating - The app's overall user rating, on a scale of 1 to 5.</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: {colo}'>4 - Reviews - The number of user reviews the app has received.</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: {colo}'>5 - Size - The size of the app, in megabytes.</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: {colo}'>6 - Installs - The number of times the app has been downloaded.</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: {colo}'>7 - Type - Whether the app is free or paid.</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: {colo}'>8 - Price - The price of the app, if it is paid.</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: {colo}'>9 - Content Rating - The age group the app is intended for, such as Everyone or Teen.</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: {colo}'>10 - Genres - The genres the app belongs to, such as Arcade or Strategy.</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: {colo}'>11 - Last Updated - The date when the app was last updated on the Play Store.</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: {colo}'>12 - Current Ver - The current version of the app.</span>", unsafe_allow_html=True)
st.markdown(f"<span style='color: {colo}'>13 - Android Ver - The minimum required Android version for the app.</span>", unsafe_allow_html=True)
# Findings 
st.subheader('`Findings`')
st.write(f"""<span style='color: {colo}'>
By exploring the category field in the dataset, it could be determined which categories of apps are the most popular among users. For example,
it might be found that games and social networking apps are among the most popular categories, while productivity and education apps are less popular. 
This information could be useful for app developers and marketers who are looking to target specific categories of users with their apps.</span>""", unsafe_allow_html=True)
st.write('\n')
st.write(f"""<span style='color: {colo}'>
the distribution of app ratings. By examining the rating field, 
it could be determined which apps have the highest and lowest ratings among users.
This information could be used to identify trends in app quality over time,
as well as identify apps that have consistently high or low ratings. 
This could be useful for app developers who are looking to improve the quality of their apps,
as well as users who are looking for high-quality apps to download.</span>""", unsafe_allow_html=True)
st.write('\n')

st.write(f"""<span style='color: {colo}'>Overall, the Google Play Store Apps dataset contains a wealth of information about the apps available in the Google Play Store,
and there are many potential findings that could be uncovered by analyzing this data. Whether you are an app developer,
a marketer, or simply interested in the app ecosystem, this dataset offers a wealth of insights and opportunities for exploration.
</span>""", unsafe_allow_html=True)


