import instaloader
import subprocess


L = instaloader.Instaloader(save_metadata=False, post_metadata_txt_pattern='')

USER="username/email/phone_no"
PASSWORD="instapassword"
TARGET="stories"

L.login(USER, PASSWORD)

profile = L.check_profile_id("elliavrram")



for story in L.get_stories(userids=str(profile)):
    for item in story.get_items():
        L.download_storyitem(item, TARGET)
subprocess.Popen('explorer "{0}"'.format(TARGET))


# 3181029899
# 353276743
