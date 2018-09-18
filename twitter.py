import tweepy

consumer_key = "Tdge4a6konBvh9FEhui3aoYPZ"
consumer_secret = "7owY8wMRFGH71pAKxaauboDNIpJZU0Bzpcb9AiDMvvWef2RpDG"
access_token = "834100303897231360-ezMd7Jm44XMI66WFpf5oUFuRyyxaZcB"
access_token_secret = "xtzaAh6Hr2AbvCgWoCkqhpnNnbat21rA4EbegDVIjNSrn"
auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api =tweepy.API(auth)
user1 =api.get_user(raw_input("Enter the first twitter profile: "))
name1=user1.name
tweets1=user1.statuses_count
following1=user1.friends_count
followers1=user1.followers_count
likes1=user1.favourites_count
print ("Profile @",name1,", TWEETS",tweets1,", FOLLOWING",following1,", FOLLOWERS",followers1,", LIKES",likes1)


user2 =api.get_user(raw_input("Enter the second twitter profile: "))
name2=user2.name
tweets2=user2.statuses_count
following2=user2.friends_count
followers2=user2.followers_count
likes2=user2.favourites_count
print("Profile @,name2,", TWEETS,tweets2,", FOLLOWING,following2,", FOLLOWERS,followers2,", LIKES",likes2)

score1=0
score2=0
if tweets1>tweets2:
	score1=score1 +1
elif tweets1<tweets2:
	score2=score2 +1
if following1>following2:
	score1=score1 +1
elif following1<following2:
	score2=score2 +1
if followers1>followers2:
	score1=score1 +1
elif followers1<followers2:
	score2=score2 +1
if likes1>likes2:
	score1=score1 +1
elif likes1<likes2:
	score2=score2 +1
print("THE FINAL SCORE IS"),
print(score1),
print("-"),
print(score2)


