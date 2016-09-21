import praw
import Obot
import time
import pyimgur
import urllib.parse
import string
import random
import ctypes



print('Loging in')
r = praw.Reddit(Obot.app_id)
print('Logged in user agent: ' + Obot.app_usa)
print('Setting Oauth app info')
r.set_oauth_app_info(Obot.app_id, Obot.app_secret, Obot.app_uri)
print('Oauth set!')
print('Refreshing access Information')
r.refresh_access_information(Obot.app_refresh)

im = pyimgur.Imgur(Obot.client_id, Obot.client_secret)

def id_gen(size=9, chars=string.ascii_uppercase + string.digits):  #Create random ID
    return ''.join(random.choice(chars) for _ in range(size))




while True:


    ass = 'ass and titties'
    submissions = r.get_subreddit('pics').get_random_submission()
    url = urllib.parse.unquote(submissions.url)
    jpg = 'jpg'
    imgur = 'imgur'
    if jpg in url and imgur in url:
        newurl = url.split('/')[-1].split('.')[0]
        im.get_image(newurl).download(path="C:\\Users\\KEVIN\\Pictures\\Pyimgur", name=id_gen(), overwrite=False, size=None)
        time.sleep(30)









