import streamlit as st
import pandas as pd
# import requests
import snowflake.connector
# from urllib.error import URLError

st.title("Zena's Amazing Catalog")

#connect Snowflake
my_cnx = snowflake.connector.connect(**st.secrets["snowflake2"])
my_cur = my_cnx.cursor()
#execute color
my_cur.execute("SELECT COLOR_OR_STYLE, PRICE from catalog_for_website")
colours = my_cur.fetchall()

# st.text('--data from Snowflake')
# st.text(colours)
# st.text('--Put data into st.dataframe')
# st.dataframe(colours)
# df2 = st.dataframe(colours)
# st.text(df2)
st.text('--Put data into pd.DataFrame')
df = pd.DataFrame(colours)
# st.text(df)
st.write(df)

st.text('--df0 values tolist')
color_list = df[0].values.tolist()
st.text(color_list)
st.dataframe(color_list)
st.write(color_list)
# st.text('--test df2 values tolist')
# color_list2 = df2[0].values.tolist()

st.text('--selectbox')
sel_col2 = st.selectbox('Choose colour:', list(colours))
st.text('-- selectbox df - color_list')
sel_col = st.selectbox('Choose colour:', list(color_list))
# st.text('-- selectbox df2')
# st.selectbox('Choose colour:', list(df2))

# st.text('multiselect colour')
# st.multiselect("Pick colour:", list(colours) )
# st.text('multiselect colour df')
# st.multiselect("Pick colour:", list(df) )
 
#caption - pict_desc
st.write('our warm, comf', sel_col, 'sweatuit')
st.write('our warm, comf', sel_col2, 'sweatuit')
pict_desc = ('our warm, comf ' + sel_col + ' sweatuit')
st.write(pict_desc)

#execute pict
my_cur.execute("SELECT DIRECT_URL from catalog_for_website where COLOR_OR_STYLE = '"+sel_col+"' ")
pict_url = my_cur.fetchone()

# pict_url = 'https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/royal_blue_sweatsuit.png/' , 
st.image( pict_url , caption=pict_desc)

my_cnx.close() 
