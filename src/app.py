import streamlit as st

from password_generators import (MemorablePasswordGenerator, PinGenerator,
                                 RandomPasswordGenerator)


st.title("🔐Password Generator")
st.divider()
col1, col2 = st.columns(2)

with col1:
    password_type = st.radio(
        "Choose The Password Type : ",
        ("Pin", "Random Password", "Memorable Password")
    )
    st.divider()
    if password_type == 'Pin':
        length = st.slider("Length", min_value=4, max_value=20, value=8)
        password = PinGenerator(length=length)
    elif password_type == 'Random Password':
        length = st.slider("Length", min_value=8, max_value=50, value=12)
        include_numbers = st.toggle("Include Numbers")
        include_symbols = st.toggle("Include Symbols")
        password = RandomPasswordGenerator(length=length, include_digits=include_numbers, include_symbols=include_symbols)
    elif password_type == 'Memorable Password':
        num_of_words = st.slider("Number of words", min_value=3, max_value=12, value=5)
        password = MemorablePasswordGenerator(length=num_of_words)
    
    generate = st.button("Generate Password", type='primary')


with col2 :
    st.header("Password : ")
    if generate:
        password = password.generate()
        st.subheader(fr'  ```{password}```  ')
        st.success("Password generated successfully!")