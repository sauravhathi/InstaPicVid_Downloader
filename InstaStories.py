import instaloader
import subprocess


L = instaloader.Instaloader(save_metadata=False, post_metadata_txt_pattern='')

USER="saurav_hathi"
PASSWORD="@sauravhathi$680$118"
TARGET="stories"

L.login(USER, PASSWORD)

profile = L.check_profile_id("akshaykumar")

for story in L.get_stories(userids=str(profile.userid)):
    for item in story.get_items():
        L.download_storyitem(item, TARGET)
subprocess.Popen('explorer "{0}"'.format(TARGET))