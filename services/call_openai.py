from openai import OpenAI
import streamlit as st

# Function to call OpenAI DALL·E for image generation
def get_image_openai(prompt):
    try:
        # Set your OpenAI API key here (replace 'your-api-key' with your actual key)
        api_keys = st.secrets['OPEN_AI_APIKEY']['OPEN_AI_APIKEY']

        client = OpenAI(api_key=api_keys)

        # Request to DALL·E model to generate an image
        response = client.images.generate(
            model="dall-e-2",
            prompt=prompt,
            n=1,  # Number of images to generate
            size="1024x1024"  # Image size (adjust as needed)
        )

        # Get the URL of the generated image
        image_url = response.data[0].url
        return image_url

    except Exception as e:
        print(f"Error occurred: {e}")
        return None
