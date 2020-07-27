import praw
import textwrap
import secret

from PIL import Image,ImageFont,ImageDraw
from instabot import Bot

reddit = praw.Reddit(client_id=secret.cid,
                     client_secret=secret.csecret,
                     password=secret.rdpwd,
                     user_agent="R2IBot",
                     username=secret.rduname)

hot_posts = reddit.subreddit('LifeProTips').top('day')
hot_posts = list(hot_posts)
title = hot_posts[0].title

BACKGROUND = (38, 50, 56)
FOREGROUND = (207, 216, 220)
img = Image.new('RGBA',(900,900),BACKGROUND)
font = ImageFont.truetype("Recursive-Regular-CASL=0-CRSV=1-MONO=0-slnt=0.ttf",40)
w,h = font.getsize(title)

draw = ImageDraw.Draw(img)
image_width, image_height = img.size
y_text = 350
lines = textwrap.wrap(title,width=40)
for line in lines:
    line_width, line_height = font.getsize(line)
    draw.text(((image_width - line_width) / 2, y_text),line, font=font, fill=FOREGROUND)
    y_text += line_height

rgb_im = img.convert('RGB')
rgb_im.save('final.jpg')

bot = Bot()
bot.login(username=secret.iguname, password=secret.igpwd)
bot.upload_photo("final.jpg",caption="Beep Bop I'm a bot")