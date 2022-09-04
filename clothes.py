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
my_cur.execute("SELECT COLOR_OR_STYLE from catalog_for_website") # to jest zaimportowane ze snowflake jako tupla
colours = my_cur.fetchall() #colours to tupla

streamlit.text('data from Snowflake')
streamlit.text(colours)

streamlit.text('Put data into st.dataframe')
streamlit.dataframe(colours)
streammlit.text(print(colours))
 
streamlit.text('Put data into pd.DataFrame')
df = pandas.DataFrame(colours)
streamlit.text(df)

# streamlit.selectbox('Choose colour:', list(colours))


streamlit.text('our warm, comf /pink/ sweatuit')



my_cnx.close() 
