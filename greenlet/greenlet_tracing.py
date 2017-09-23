import greenlet

def test_greenlet_tracing():
    def callback(event, args):
        print event, 'from', id(args[0]), 'to', id(args[1])

    def dummy():
        gr2.switch()

    def dummyException():
	raise Exception("Except in coroutine!")

    main = greenlet.getcurrent()
    gr1 = greenlet.greenlet(dummy)
    gr2 = greenlet.greenlet(dummyException)
    print "main id %s, gr1 id %s, gr2 id %s" % (id(main), id(gr1), id(gr2))
    oldtrace = greenlet.settrace(callback)
    try:
	gr1.switch()
    except:
	print "Exception"
    finally:
	greenlet.settrace(oldtrace)

test_greenlet_tracing()

#main id 139671050739056, gr1 id 139671050738896, gr2 id 139671050739536
#switch from 139671050739056 to 139671050738896
#throw from 139671050738896 to 139671050739056
#Exception
#process finished!
