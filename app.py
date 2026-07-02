import streamlit as st
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Page setup
st.set_page_config(
    page_title="AI Vision Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Vision Assistant")

st.write("Upload an image and ask any question about it.")

# Upload image
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_container_width=True)

    question = st.text_input("Ask your question")

    if st.button("Get Answer"):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            with st.spinner("Thinking..."):

                response = model.generate_content(
                    [question, image]
                )

            st.subheader("Answer")

            st.success(response.text)