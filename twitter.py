import twitter

#api = twitter.Api(consumer_key = 'consumer_key',consumer_secret = 'consumer_secret', access_token_key = 'access_token', access_token_secret = 'access_token_secret')
#print api.VerifyCredentials()["id":16133,"location":"Philadelphia","name":"bear"]


api = twitter.Api()
statuses = api.GetUserTimeline('HarvardGSD')
print [s.text for s in statuses]
