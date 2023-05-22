import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

import streamlit 

streamlit.title('God is Great')

streamlit.title('Breakfast Menu')
streamlit.header('Morning Breakfast')
streamlit.text('🥗 poha, Upma and Idli Samber')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥑🍞 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page
streamlit.dataframe(my_fruit_list)

#Choose the Fruit Name Column as the Index
my_fruit_list = my_fruit_list.set_index('Fruit')

#Choose a Few Fruits to Set a Good Example
streamlit.multiselect("Pick Some Fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(my_fruit_list)

# New section to display fruityvice API Response
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

streamlit.header("Fruityvice Fruit Advice!")
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")

# take the json version of response and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table 
streamlit.dataframe(fruityvice_normalized)

#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# take the json version of response and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table 
streamlit.dataframe(fruityvice_normalized)

#Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call

# New section to display fruityvice API Response
streamlit.header('Fruityvice Fruit Advice!')

fruit_choice = streamlit.text_input('What fruit would you like information about?','kiwi')
streamlit.write('The user entered ', fruit_choice)

#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# take the json version of response and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table 
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)

my_data_row = my_cur.fetchone()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)

my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

#allow the end user to add a fruit to the list 
add_my_fruit = streamlit.text_input('what food would you like to add?')
streamlit.write('Thanks for adding', add_my_fruit)

#don't run anything past here while we troubleshoot
#streamlit.stop()

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_rows)

# New section to display fruityvice API Response

streamlit.header('Fruityvice Fruit Advice!')
try:
    fruit_choice = streamlit.text_input('what fruit would you like information about?')
    streamlit.write('The user entered ', fruit_choice)

if not fruit_choice:
    streamlit.error("please select a fruit to get information.")
else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
except URLError as e:
    streamlit.error()
    
#create the repeatable code block (called a function)
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#New section to display fruityvice API Response
#streamlit.header('Fruityvice Fruit Advice!')
#try:
    #fruit_choice = streamlit.text_input ('what fruit would you like information about?')
    #if not fruit_choice:
        #streamlit.error("please select a fruit to get information.")
    #else:
        #back_from_function = get_fruityvice_data(fruit_choice)
        #streamlit.dataframe(back_from_function)
    
