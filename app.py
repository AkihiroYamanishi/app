import streamlit as st
import requests
import transformers

# Set the LINE API endpoint
LINE_API_ENDPOINT = "https://api.line.me/v2/bot/message/reply"

# Get the LINE access token
LINE_ACCESS_TOKEN = "lHM1G3h54yfPos/iBAidDmsSSOAibMN7FpwXG285jWrinDeKC5/cQnoOWG7trZ5lbbeyTB3kp9jdVr8hy8fXlwWr23xuC0FhMQtVLiBkflYf8HiHI+WA4SFUcMrAyiSyd1wivwnna6FC4p9NFTdGGQdB04t89/1O/w1cDnyilFU="

# Load the ChatGPT model
model = transformers.AutoModelForSeq2SeqLM.from_pretrained("facebook/bart-base")

# Create a function to send a message to the LINE app
def send_message(message):
    # Create a request body
    request_body = {
        "to": "1661055658",
        "messages": [
            {
                "type": "text",
                "text": message
            }
        ]
    }

    # Send the request
    response = requests.post(LINE_API_ENDPOINT, headers={"Authorization": "Bearer {}".format(LINE_ACCESS_TOKEN)}, data=request_body)

    # Check the response status code
    if response.status_code == 200:
        return True
    else:
        return False

# Create a Streamlit app
st.title("LINE Bot")

# Get the user input
message = st.text_input("Enter your message:")

# Generate a response from ChatGPT
response = model.generate(text=message, max_length=50)

# Send the response to the LINE app
if send_message(response):
    st.success("Message sent successfully!")
else:
    st.error("Error sending message!")