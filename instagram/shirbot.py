"""
What does this quickstart script aim to do?
- This is my template which includes the new QS system.
    It includes a randomizer for my hashtags... with every run, it selects 10
    random hashtags from the list.
NOTES:
- I am using the bot headless on my vServer and proxy into a Raspberry PI I
have at home, to always use my home IP to connect to Instagram.
    In my comments, I always ask for feedback, use more than 4 words and
    always have emojis.
    My comments work very well, as I get a lot of feedback to my posts and
    profile visits since I use this tactic.
    As I target mainly active accounts, I use two unfollow methods. 
    The first will unfollow everyone who did not follow back within 12h.
    The second one will unfollow the followers within 24h.
"""

# !/usr/bin/python2.7
import random
from instapy import InstaPy
from instapy import smart_run

# get a session!
#session = InstaPy(username='****', password='****', headless_browser=True)
session = InstaPy(username='****', password='*****')

# let's go! :>
with smart_run(session):
    hashtags = ['پول', 'ثروت', 'ثروتمندان',
                'کارآفرین',
                'افغانستان', 'هرات', 'کابل',
                'پروان', 'تهران',
                'استارتاپ', 'استارتاپ دیلی', 'کارآفرینی',
                'وب سایت',
                'مدریت', 'رهبری', 'خوشی', 'آریانا',
                'برنامه نویسی',
                'کرپتوکرنسی', 'بیت کوین', 'بیل ', 'گیتس',
                'جیف',
                'بیزوس', 'بامیان', 'دایکندی', 'پولدار', 'تکنولوژی',
                'پولی', 'پولخوش',
                'کار', 'آینده', 'تکنالوژی', 'بورس', 'مارکتنگ', 'بورسیه', 'صنعت', 
                'تجارت', 'الکترونیک',
                'فقیر', 'آینده سازان', 'مدریت',
                'پرداخت', 'بانک',
                'آنلاین', 'فروش', 'مهارت', 'انگیزشی', 'انگیزه', 'هدف', 'برنامه',
                'موبایل', 'جاغوری', 'کسب و کار', 'کسب', 'مثبت', 'انرژی', 
                'پیشه']
    random.shuffle(hashtags)
    my_hashtags = hashtags[:10]

    # general settings
    session.set_dont_like(['غمگین', 'بارانی', 'ساده'])
    session.set_do_follow(enabled=True, percentage=50, times=1)
    session.set_do_comment(enabled=True, percentage=50)
    session.set_comments([
                            u'آیا میخواهید اولین ملیاردر خانواده تان باشید؟ :heart_eyes: پس حتما '
                            u'از صفحه ما دیدن کنید',
                            u'موفقیت شما آرزوی ماست :heart_eyes: از صفحه خودتان هم دیدن کنید '
                            u'به خانواده ملیاردر ها بپیوندید :wink:',
                            u'داستان های موفقیت را در صفحه ما ببنید :heart_eyes: حتما خوش تان خواهد آمد '
                            u'پس لایک و فالو هم یاد تان نرود',
                            u'از موفقیت دیگران باید درس گرفت :heart_eyes: این درس ها در پیچ ما می باشد ',
                            u'پولدار ها چگونه پول پارو می کنند؟  ',
                            u'جواب در پیج ما است :wink:',
                            u'همه از پیج ما دیدن کردن :heart_eyes: شما هم ببنید ',
                            u'اگر در بخش کارآفرینی علاقه دارید پس پیچ ما را فالو کنید :wink:',
                            u'شرکت های بزرگ انترنتی چگونه بجود آمدن؟ :heart_eyes: جواب را در پیج ما ببنید '
                            u'انسان های موفق چگونه به این موقعیت رسیدن؟  در پیج ما ببنید :wink:',
                            u'چگونه کسب کارهای اینترنتی  به وجود آمدن 💰',
                            u'زندگی نامه افراد موفق دنیا :wink:',
                            u'چگونه از انترنت کسب درآمد کنیم؟ جواب در پیج ما است :money_with_wings:',
                            u'زندگی ثروتمندترین شخص دنیا در پیج ما ببنید :money_mouth_face:',
                            u'راز ملیاردر های خود ساخته را در پیج ما ببنید 😻 💰',
                            u'ثروت مندان و راز آنها 😻 💰 در پیچ ما ببنید',
                            u'ثروت مندان و راز آنها 😻 💰 چگونه از آنها یاد بگریم',
                            u'ثروت مندان و راز آنها 😻 💰 چگونه از آنها کاپی برداری کنیم',
                            u'آیا میدانی دنیا دست کیست؟ جواب در پیج ما است 🦸‍♂️',
                            u'زندگی نامه افراد موفق دنیا در پیج ما 🧐 🌐 💟 ',
                            u'به خانواده ملیاردر های آینده بیاید 🤑 💰',
                            u'آیا میخواهید اولین ملیاردر خانواده تون باشید؟'
                            u'پس حتما از پیج ما دیدن کنید 🥇 :money_with_wings:',
                            u'آینده به کدام سمت روان است؟ جواب در پیج ما ببنید',
                            u'رهبران چگونه رهبری می کند؟ :superhero: :superhero_man: :supervillain_woman:',
                            u'از رهبران دنیا چی میشه آموخت؟ در پیچ ما ببنید 💗 😍 🥇 ',
                            ],
                        media='Photo')
    session.set_do_like(True, percentage=50)
    session.set_delimit_liking(enabled=True, max_likes=100, min_likes=0)
    session.set_delimit_commenting(enabled=True, max_comments=20, min_comments=0)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    max_following=2000,
                                    min_followers=50,
                                    min_following=50)

    session.set_quota_supervisor(enabled=True,
                                sleep_after=["likes", "follows"],
                                sleepyhead=True, stochastic_flow=True,
                                notify_me=True,
                                peak_likes_hourly=200,
                                peak_likes_daily=585,
                                peak_comments_hourly=80,
                                peak_comments_daily=182,
                                peak_follows_hourly=48,
                                peak_follows_daily=None,
                                peak_unfollows_hourly=35,
                                peak_unfollows_daily=402,
                                peak_server_calls_hourly=None,
                                peak_server_calls_daily=4700)

    session.set_user_interact(amount=10, randomize=True, percentage=80)

    # activity
    session.like_by_tags(my_hashtags, amount=90, media=None)
    session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="nonfollowers",
                            style="FIFO",
                        #    unfollow_after=12 * 60 * 60, sleep_delay=501)
                           unfollow_after=186 * 60 * 60, sleep_delay=501)
    session.unfollow_users(amount=500, instapy_followed_enabled=True, instapy_followed_param="all",
                        #    style="FIFO", unfollow_after=24 * 60 * 60,
                           style="FIFO", unfollow_after=360 * 60 * 60,
                            sleep_delay=501)

    """ Joining Engagement Pods...
    """
    session.join_pods(topic='sports', engagement_mode='no_comments')
