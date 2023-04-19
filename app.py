import streamlit as st 

st.title('title of your application')
st.markdown('**bold text**')

st.sidebar.title('title of the sidebar')
st.sidebar.markdown('markdown *text* in the **sidebar**')

agree = st.checkbox('I agree')
if agree: 
    st.write('Great!')
    st.markdown('this is markdown **text!**')

agree_sidebar = st.sidebar.checkbox('side bar checkbox')
if agree_sidebar: 
    st.write('side bar checked')
    st.sidebar.write('side bar checked')
    
