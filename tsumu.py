import tweepy
import os 
import glob
import random
from config import *

# 認証
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# 実行ディレクトリへ移動
tsumu_exec_dir = '/home/otokura/tsumugi_bot'
os.chdir(tsumu_exec_dir)

# 最後につぶやいた画像ファイル名のログ
tsumu_log = './tsumu.log'

# 現在の画像数を取得
tsumu_max = len(glob.glob('./img/*/*'))

# ファイルがあるか確認
if os.path.isfile(tsumu_log):
  # ファイルがあった場合、最後につぶやいた画像番号を取得
  with open(tsumu_log,mode='r') as tsumu_read:
    tsumu_last = int(tsumu_read.read())

  # 前回が偶数の場合、奇数の
  # 奇数の場合、偶数の乱数を生成する
  if(tsumu_last % 2 == 0):
    tsumu_number = random.randrange(1,tsumu_max,2)
  else:
    tsumu_number = random.randrange(2,tsumu_max,2)
else:
  # ファイルが無い場合、初回起動と見做しつぶやく画像を全体から決定する
  tsumu_number = random.randrange(1,tsumu_max)

# 決定された画像番号に応じて画像ファイルのフルパスを指定する
if(tsumu_number % 2 == 0):
  tsumu_img = './img/poyapoya/' + str(tsumu_number) + '.jpg'
else:
  tsumu_img = './img/cool/' + str(tsumu_number) + '.jpg'

# 画像ツイート
api.update_status_with_media(filename=str(tsumu_img),status="")

# 最後につぶやいた画像番号をログファイルへ記録する
with open(tsumu_log, mode='w') as tsumu_write:
  tsumu_write.write(str(tsumu_number))

