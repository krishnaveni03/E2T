import streamlit as st
from googletrans import Translator

# Function to translate text to the specified language
def translate_text(text, dest_lang):
    translator = Translator()
    translated_text = translator.translate(text, dest=dest_lang).text
    return translated_text

# Streamlit App
def main():
    st.title("Language Translator")

    page = st.sidebar.selectbox("Select a page", ["Home", "Translation"])

    if page == "Home":
        st.header("Welcome to Language Translator!")
        st.write("This app translates text from one language to another.")

    elif page == "Translation":
        st.header("Translate Text")

        input_text = st.text_area("Enter text to translate:")
        dest_lang = st.selectbox("Select language to translate to:", ["Tamil", "French", "German", "Spanish", "Chinese (Simplified)"])

        if st.button("Translate"):
            translated_text = translate_text(input_text, dest_lang.lower())
            st.success("Translated Text:")
            st.write(translated_text)

if __name__ == "__main__":
    main()
