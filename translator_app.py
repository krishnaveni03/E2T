import streamlit as st
from googletrans import Translator

# Function to translate text from English to Tamil
def translate_to_tamil(text):
    translator = Translator()
    translated_text = translator.translate(text, src='en', dest='ta').text
    return translated_text

# Streamlit App
def main():
    st.title("English to Tamil Translator")
    page = st.sidebar.selectbox("Select a page", ["Home", "Translation"])

    if page == "Home":
        st.header("Welcome to English to Tamil Translator!")
        st.write("This app translates English text to Tamil.")
        st.image("pic.png", caption="Optional caption for the image", use_column_width=True)

    elif page == "Translation":
        st.header("Translate English to Tamil")
        input_text = st.text_area("Enter English text to translate:")

        if st.button("Translate"):
            translated_text = translate_to_tamil(input_text)
            st.success("Translated Text:")
            st.write(translated_text)

if __name__ == "__main__":
    main()
