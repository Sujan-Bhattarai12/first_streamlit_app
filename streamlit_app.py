import streamlit
streamlit.title("My parents healthy diner")

streamlit.header("Breakfast Menu")
streamlit.text(" 🥣  Omega 3 and Blueberry Oatmeal")
streamlit.text(" 🥗  Kale, Spinach & Rocket Smoothie")
streamlit.text(" 🐔  Hard-Boidled Free-range egg")
streamlit.text(" 🥑🍞 Avocado Toast")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

#set the index
#my_fruit_list = my_fruit_list.set_index('Fruit')

#selector pane
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])


# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]

##show the dataframe
#streamlit.dataframe(fruits_to_show)

