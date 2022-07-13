#API key olBq4Nu1OCe2w0DAEmFos7GWp
#API key secret oZpyJdHbfWriQ85n8QdkDlTozv1C6kDSf6eM74IdcKmb7MAnLY
#Accses token 3081048181-MdAAUVmp0qAHKSpUt0pkyQrNIrpmB5LcZGtgN71
#Accses token secret VKd18oZ3kT4GCnCiImIL7CPTK5E7rCIeBtDGsM8w4SYml

pip install tweepy
import tweepy

from datetime import datetime,timezone

import pytz

import pandas as pd

# Twitter APIの認証設定
# 取得したキーを格納
api_key = "olBq4Nu1OCe2w0DAEmFos7GWp"
api_secret = "oZpyJdHbfWriQ85n8QdkDlTozv1C6kDSf6eM74IdcKmb7MAnLY"
access_key = "3081048181-MdAAUVmp0qAHKSpUt0pkyQrNIrpmB5LcZGtgN71"
access_secret = "VKd18oZ3kT4GCnCiImIL7CPTK5E7rCIeBtDGsM8w4SYml"

# Tweepy設定
# インスタンスの作成
auth = tweepy.OAuthHandler(api_key, api_secret) # Twitter API認証
auth.set_access_token(access_key, access_secret)# アクセストークン設定
#　”wait_on_rate_limit = True”　利用制限にひっかかた時に必要時間待機する
api = tweepy.API(auth ,wait_on_rate_limit = True)

# 検索条件の設定
# ワードの間に半角スペースで２つのワードが検索できる
search_word = '会社行きたくない'
item_number = 50

#検索条件を元にツイートを抽出
tweets = tweepy.Cursor(api.search_tweets, q = search_word, lang = 'ja').items()


#関数:　UTCをJSTに変換する
def change_time_JST(u_time):
    #イギリスのtimezoneを設定するために再定義する
    utc_time = datetime(u_time.year, u_time.month,u_time.day, \
    u_time.hour,u_time.minute,u_time.second, tzinfo=timezone.utc)
    #タイムゾーンを日本時刻に変換
    jst_time = utc_time.astimezone(pytz.timezone("Asia/Tokyo"))
    # 文字列で返す
    str_time = jst_time.strftime("%Y-%m-%d_%H:%M:%S")
    return str_time

#抽出したデータから必要な情報を取り出す
#取得したツイートを一つずつ取り出して必要な情報をtweet_dataに格納する
tw_data = []

for tweet in tweets:
    #ツイート時刻とユーザのアカウント作成時刻を日本時刻にする
    tweet_time = change_time_JST(tweet.created_at)
    create_account_time = change_time_JST(tweet.user.created_at)
    #tweet_dataの配列に取得したい情報を入れていく
    if tweet.favorite_count >= 1:

        tw_data.append([
        tweet_time,
        tweet.text,
        tweet.favorite_count

                       ])

#取り出したデータをpandasのDataFrameに変換
#CSVファイルに出力するときの列の名前を定義
labels = [
    'ツイート時刻',
    'ツイート本文',
    'いいね数'
    ]

#tw_dataのリストをpandasのDataFrameに変換
df = pd.DataFrame(tw_data,columns=labels)

#CSVファイルに出力する
#CSVファイルの名前を決める
file_name='tw_data_会社行きたくない0711.csv'

#CSVファイルを出力する
df.to_csv(file_name,encoding='utf-8-sig',index=False)
