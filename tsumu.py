import tweepy
from config import *

# 認証
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# つぶやく画像ファイルを指定
# 偶数：クールな画像
# 奇数：ぽやぽや画像
# imgディレクトリ配下の最大数以内で、乱数を生成
# 偶数と奇数を交互に
# ログとか一時ファイルとかに、最後につぶやいた画像ファイル名をつぶやいても良いかも？

# 画像ツイート
api.update_status_with_media(filename='img/1.jpg',status="")