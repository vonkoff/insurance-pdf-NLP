import dropbox
import os
import time

# Get your Dropbox access token from the Dropbox website.
ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

# Create a Dropbox client object.
client = dropbox.Dropbox(ACCESS_TOKEN)

# Get the path to the "PDF Insurance" folder.
PDF_INSURANCE_FOLDER_PATH = "/PDF Insurance"

# Create a Cloud Pub/Sub topic.
topic_name = "pdf-insurance"

# Create a Cloud Pub/Sub subscription.
subscription_name = "pdf-insurance-subscription"

# Subscribe to the topic.
client.subscribe(topic_name, subscription_name)

# Define a function to handle messages from the Cloud Pub/Sub subscription.
def on_message(message):
    # Get the file path from the message.
    file_path = message.data

    # Send the file to Document AI.
    send_pdf_to_document_ai(file_path)

# Register the function to handle messages from the Cloud Pub/Sub subscription.
client.register_message_handler(on_message)

# Create a Cloud Pub/Sub pull request.
pull_request = client.create_pull_request(subscription_name, 5)

# Start the Cloud Pub/Sub subscription.
client.start_subscription(subscription_name)

# Wait for messages from the Cloud Pub/Sub subscription.
client.wait_for_messages()
