from pycricbuzz import Cricbuzz
import json
import time
from twilio.rest import TwilioRestClient
client = TwilioRestClient("AC0b85724324030f71484dd878fd6ec27f", "f700b474f7f686b2ad88ffcaa73118b6")

def buzz():
	c = Cricbuzz()
	matches = c.matches()
	h=c.livescore(['4'])
	print(h)
	result=[]
	l=[]
	l.append(h['matchinfo']['status'])
	l.append(h['batting']['team'])
	l.append(h['batting']['score'][0]['overs']+"overs")
	l.append(h['batting']['score'][0]['runs']+"/"+h['batting']['score'][0]['wickets'])

	#l.append(h['bowling']['team'])
	#l.append(h['bowling']['score'][0]['overs']+"overs")
	#l.append(h['bowling']['score'][0]['runs']+"/"+h['bowling']['score'][0]['wickets'])


	summary=" ".join(l)

	batting=[]
	for i in range(len(h['batting']['batsman'])):
		batting.append(h['batting']['batsman'][i]['name'])
		batting.append(h['batting']['batsman'][i]['runs']+"("+h['batting']['batsman'][i]['balls']+")")
	
	m=" ".join(batting)	
	bowling=[]
	for i in range((len(h['bowling']['bowler']))):
		bowling.append(h['bowling']['bowler'][i]['name'])
		bowling.append(h['bowling']['bowler'][i]['overs']+"overs")
		bowling.append(h['bowling']['bowler'][i]['runs']+"runs")
		bowling.append(h['bowling']['bowler'][i]['wickets']+"wickets")
	bow=" ".join(bowling)

	com_list=[]
	com=c.commentary(['1'])
	for i in range(2):
		com_list.append(com['commentary'][i])
	
	result.append(summary)
	result.append(m)
	result.append(bow)
	result.append("\n".join(com_list))
	return(result)








	
while(True):
	only=buzz()
	print(only)
	client.messages.create(to="+919978762997", from_="+14847274317",body=only[0])
	client.messages.create(to="+919978762997", from_="+14847274317",body=only[1])
	client.messages.create(to="+919978762997", from_="+14847274317",body=only[2])
	
	
	
	time.sleep(1)	



# we import the Twilio client from the dependency we just installed


# the following line needs your Twilio Account SID and Auth Token


# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
#pabba 9978762997
#client.messages.create(to="+919898272433", from_="+14847274317",body=a)