from time import sleep

#Event manager
eventListeners = {}

def fireEvent(name):
    #trigger the event(name) handler
    print("eventListeners: event:%s, value:%s\n" % (name, eventListeners[name]))
    eventListeners[name]()

def useEvent(func):
    def call(*args, **kws):
	generator = func(*args, **kws)
	eventName = next(generator)
	def resume():
            try:
		next(generator)
	    except StopIteration:
		pass
	print("Register an event!")
	eventListeners[eventName] = resume
    return call

#test
#firstly call next(testWork), return click
#secondly call it, return clicked
@useEvent
def testWork():
    print("="*50)
    print("Waitting click!")
    yield "click"
    print("clicked!")

if __name__ == '__main__':
    testWork()
    sleep(3)
    fireEvent("click")
    
