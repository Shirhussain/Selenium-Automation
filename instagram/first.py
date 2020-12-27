from instapy import InstaPy
# from requests.sessions import session

session = InstaPy(username="*****", password="*****")

# session.like_by_tags(["پول", "ثروت", "میلیون", "ملیاردر", "کارآفرین"], amount=5)
session.login()
session.like_by_tags(["ثروت", "کارآفرین", "پول"], amount=5)
session.set_dont_like(["غمگنی", "بارانی"])
session.set_do_follow(True, percentage=50)
session.set_do_comment(True, percentage=50)
session.set_comments(["Nice!", "Sweet!", "Beautiful :heart_eyes:"])
# session.set_quota_supervisor(enabled=True, peak_comments_daily=240, peak_comments_hourly=21)
# این را بخاطر گذاشتم که افراد بالای ۸۵۰۰ فالور دارد هیچ وقت فالو بک نمی دهد
# session.set_relationship_bounds(enabled=True, max_followers=8500)
# https://realpython.com/instagram-bot-python-instapy/
# session.set_use_clarifai(enabled=True, api_key='<your_api_key>')
# session.clarifai_check_img_for(['nsfw'])
session.end()
