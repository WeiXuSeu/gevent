import greenlet

def test1(x, y):
    try:
        z = gr2.switch(x + y)
    except Exception:
        print 'Catch exception in test1!'

def test2(u):
    assert False

gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)
try:
    gr1.switch("come from", "gr1")
except:
    print "Catch exception in main"

#result output:
#Catch exception in main
