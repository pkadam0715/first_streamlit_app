import streamlit 

streamlit.title('God is Great')

streamlit.title('Breakfast Menu')
streamlit.header('Morning Breakfast')
streamlit.text('🥗 poha, Upma and Idli Samber')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥑🍞 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
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

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# take the json version of response and normalize it 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as a table 
streamlit.dataframe(fruityvice_normalized)

#Add a Text Entry Box and Send the Input to Fruityvice as Part of the API Call

# New section to display fruityvice API Response
streamlit.header('Fruityvice Fruit Advice!')

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
