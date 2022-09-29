import streamlit
import pandas
import requests
import snowflake.connector

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach, & Rocket Smoothie')
streamlit.text('🐔 Hard-Boilded Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

#New Section to display the fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')

#add instruction and picker for the user
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)

#take the JSON version of the response and normalises it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)


#do not run any code past this point 
streamlist.stop()
import snowflake.connector

#Connecting to Snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * FROM fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)

#add instruction and picker for the user
add_fruit = streamlit.text_input('What fruit would you like to add?','Jackfruit')
streamlit.write('Thanks for adding  ', add_fruit)
my_cur.execute("INSERT INTO fruit_load_list VALUES ('from streamlist')")
addfruit_response = requests.get("https://fruityvice.com/api/fruit/"+ add_fruit)

