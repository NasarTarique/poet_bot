import tweepy
import json
import get_poem

client = open('client_secret.json',)
client_dictionary = json.load(client)
auth = tweepy.OAuthHandler(client_dictionary['consumer_key'], client_dictionary['consumer_secret'])
auth.set_access_token(client_dictionary['access token'],client_dictionary['access token secret'])
api = tweepy.API(auth)

poem = get_poem.get_poem()

str = poem['poem_title'] +'\n'+'\n'+'by'+poem['author_name'] +'\n' +'\n'
count_chars = len(poem['poem_title']) + len(poem['author_name'])+ 6
poemparts = []
list = poem['poem'].splitlines()
for x in list:
    if x==list[len(list)-1]:
        str = str+'\n'+x
        poemparts.append(str)
    if (len(x)+count_chars)<140:
        str = str+'\n'+x
        count_chars = count_chars+len(x)
    else:
        poemparts.append(str)
        str=''
        count_chars=0


if len(poemparts)==1:
    api.update_status(poemparts[0])
    print("tweeted")
else:
    api.update_status(poemparts[0])
    status_list = api.user_timeline('PoetBot2')
    tweetid = status_list[0].id
    for x in range(1,len(poemparts)):
        status_list = api.user_timeline('PoetBot2')
        tweetid = status_list[0].id
        api.update_status(status = poemparts[x], in_reply_to_status_id = tweetid, auto_populate_reply_metadata=True)




