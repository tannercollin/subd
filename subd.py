from time import sleep
from instapush import App

apisecret = open('apisecret.txt').read().strip()

app = App('566f99bea4c48aba38ea4fe7', apisecret)

print '>' + apisecret + '<'

while True:
    app.notify(event_name='newpost', trackers={'title': 'Hello world!'})
    print "Notification sent."
    sleep(10)
