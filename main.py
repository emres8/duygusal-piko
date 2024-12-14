
from dotenv import load_dotenv
import os
from instagram_bot import InstagramBot, SAD_TAGS

def main():
    load_dotenv()
    username = os.getenv('INSTAGRAM_USERNAME')
    password = os.getenv('INSTAGRAM_PASSWORD')

    bot = InstagramBot(username, password)
    if bot.client:
        user_id = bot.client.user_id_from_username('emresafter8')
        latest_clip = bot.get_latest_clip_from_user(user_id)
        video_path = bot.download_video_from_clip(latest_clip)
        bot.post_video_to_instagram(video_path, SAD_TAGS)

if __name__ == "__main__":
    main()