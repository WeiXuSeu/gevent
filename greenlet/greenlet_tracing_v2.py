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
    print "test_greenlet_tracing id %s, gr1 id %s, gr2 id %s" % (id(main), id(gr1), id(gr2))
    oldtrace = greenlet.settrace(callback)
    try:
	gr1.switch()
    except:
	print "Exception"
    finally:
	#greenlet.settrace(oldtrace)
	print "test_greenlet_tracing finished!"

print "main id: ", id(greenlet.getcurrent())
test_greenlet_tracing()

#result output:
#main id:  139849268931952
#test_greenlet_tracing id 139849268931952, gr1 id 139849268931792, gr2 id 139849268932432
#switch from 139849268931952 to 139849268931792
#switch from 139849268931792 to 139849268932432
#throw from 139849268932432 to 139849268931952
#Exception
#test_greenlet_tracing finished!
#throw from 139849268931952 to 139849268931792
#switch from 139849268931792 to 139849268931952

#question? :how does exception in last two line happen
