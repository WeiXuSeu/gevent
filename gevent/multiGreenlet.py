import gevent

def beep(interval):
    print("Beep %s" % interval)
    gevent.sleep(interval)

for i in range(10):
    gevent.spawn(beep, i)

beep(20)
