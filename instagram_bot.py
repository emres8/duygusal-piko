import time
from instagrapi import Client

SAD_TAGS = ["#Türkiye", "#Güncel", "#Haber", "#Spor", "#Sad", "#Sadedit", "#kesfet", "#keşfet"]

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.client = self.login_to_instagram()

    def login_to_instagram(self):
        cl = Client()

        try:
            cl.login(self.username, self.password)
            return cl
        except Exception as e:
            print(f"An error occurred during login: {str(e)}")
            return None

    def get_latest_clip_from_user(self, user_id):
        """Retrieve the latest clip from a specified user."""
        try:
            threads = self.client.direct_threads()
            for thread in threads:
                user_messages = [
                    message for message in thread.messages
                    if message.user_id == user_id and message.item_type == 'clip'
                ]
                user_messages.sort(key=lambda msg: msg.timestamp, reverse=True)
                if user_messages:
                    return user_messages[0]
        except Exception as e:
            print(f"An error occurred while retrieving the latest clip: {str(e)}")
        return None

    def post_video_to_instagram(self, video_path, tags=[]):
        """Post the downloaded clip to Instagram with a caption and tags."""
        try:
            full_caption = f"{' '.join(tags)}"
            self.client.video_upload(video_path, full_caption)
            print("Video posted successfully!")
        except Exception as e:
            print(f"An error occurred while posting the video: {str(e)}")

    def download_video_from_clip(self, clip):
        """Download the video from the given clip."""
        try:
            timestamp = int(time.time())
            video_path = f"latest_clip_{timestamp}.mp4"
            return self.client.video_download_by_url(clip.clip.video_url, video_path)
        except Exception as e:
            print(f"An error occurred while downloading the clip: {str(e)}")
