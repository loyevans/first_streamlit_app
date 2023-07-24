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
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# removed response code - streamlit.text(fruityvice_response)
# removed basic json body response - streamlit.text(fruityvice_response.json())
#take response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output to the screen as a table
streamlit.dataframe(fruityvice_normalized)
