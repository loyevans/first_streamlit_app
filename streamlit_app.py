import streamlit
import pandas
import requests

# main menu
streamlit.title('My New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
# smoothie header
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#read csv with pandas from url
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# change index to fruit name
my_fruit_list = my_fruit_list.set_index('Fruit')
# let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# fruit list data frame
streamlit.dataframe(fruits_to_show)
#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
# removed response code streamlit.text(fruityvice_response)
streamlit.text(fruityvice_response.json())
