import streamlit
import pandas
# import requests
import snowflake.connector
# from urllib.error import URLError

streamlit.title("Zena's Amazing Catalog")

#connect Snowflake
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake2"])
my_cur = my_cnx.cursor()
#execute color
my_cur.execute("SELECT * from catalog_for_website") # COLOR_OR_STYLE
colours = my_cur.fetchall()

streamlit.text(colours)
streamlit.dataframe(colours)

df = pandas.DataFrame(colours)
streamlit.text(df)

# streamlit.selectbox('Choose colour:', list(colours))


streamlit.text('our warm')



my_cnx.close() 
