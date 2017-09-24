from greenlet import greenlet, getcurrent
from time import sleep

#Create a event, and listeners listen for it (using set), use fire() to trigger listeners
class Event(object):
    def __init__(self, name):
	self.name = name
	self.listeners = set()

    def listen(self, listener):
	self.listeners.add(listener)

    def fire(self):
	for listener in self.listeners:
            listener()

class EventManager(object):
    def __init__(self):
	self.events = {}
    
    #register an event and related event handler (Event)
    def register(self, name):
	self.events[name] = Event(name)
    
    def fire(self, name):
	self.events[name].fire()
    
    #hang up the current greenlet, register it to a specific event(event_name)
    #switch to parent greenlet
    def await(self, event_name):
	self.events[event_name].listen(getcurrent().switch)
	getcurrent().parent.switch()
    
    #create a greenlet for func
    def use(self, func):
	return greenlet(func).switch

manager = EventManager()
manager.register("click")

@manager.use
def test(name):
    print "=" * 50
    print "%s waiting for click" % name
    manager.await("click")
    print "clicked!!"

if __name__ == "__main__":
    test("micro_thread")
    print "do many other works..."
    sleep(3)
    print "done... now trigger click event."
    manager.fire("click")
