from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os 
from dotenv import load_dotenv
load_dotenv()

slack_scraper_token = os.getenv('slack_scraper_token')
channel_id=os.getenv("channel_id")


image_path='./image.png'
image_path1='./image1.png'
image_paths='./images.png'
# image_path2= './image2.png'

# Set the path to the file you want to send
file_path = r"LinkedIn_jobs.csv"
file_path1= r"LinkedIn_jobs.xlsx"
file_list= [file_path,file_path1,image_path,image_path1, image_paths]

# #Setting up an Automated Text
message ="LinkedIn Jobs"

# Initialize the Slack WebClient
client = WebClient(token=slack_scraper_token)

def send_message():
     try:
        response = client.chat_postMessage(
            channel=channel_id,
            text = message
        )
        if response["ok"]:
            print("File uploaded successfully.")
        else:
            print("Failed to upload file.")
     except SlackApiError as e:
         print(f"Error uploading file: {e.response['error']}")


#Function to send the file
def send_file():
     for element in file_list:
        response =client.files_upload_v2(
        channel = channel_id,
        file= element,
            )
        if response['ok']:
            print (f"File sent successful")
        
        else:
            print(f"Error sending file ")
        