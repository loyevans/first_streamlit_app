import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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


#create repeatable code block function
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
    
#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:
        back_from_function = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(back_from_function)
except URLError as e:
    streamlit.error()

# pause while tshoot
streamlit.stop()
# snowflake connection
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# 4th exercise
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
# add another fruit input box
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding', add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from streamlit')")


# 1st exercise with snowflake connector 
#-- my_cur.execute("select current_user(), current_account(), current_region()")
#-- my_cur.execute("select current_user(), current_account(), current_region()")
#-- my_data_row = my_cur.fetchone()
#-- streamlit.text("Hellow from Snowflake:")
#-- streamlit.text(my_data_row)
# 2nd exercise with snowflake connector
#-- my_cur.execute("select * from fruit_load_list")
#-- my_data_row = my_cur.fetchone()
#-- streamlit.text("The fruit load list contains:")
#-- streamlit.text(my_data_row)
# 3rd exercise with snowflake connector
#-- my_cur.execute("select * from fruit_load_list")
#-- my_data_row = my_cur.fetchone()
#-- streamlit.header("The fruit load list contains:")
#-- streamlit.dataframe(my_data_row)
