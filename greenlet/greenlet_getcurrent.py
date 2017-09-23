import greenlet

def test1(x, y):
    print "current test1 greenlet id:", id(greenlet.getcurrent()), "parent greenlet id:", id(greenlet.getcurrent().parent)
    z = gr2.switch(x + y)
    print "back z: ", z

def test2(u):
    print "current test2 greenlet id:", id(greenlet.getcurrent()), "parent greenlet id:", id(greenlet.getcurrent().parent)
    return "haha, test2 returned!"

gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)
print "main greenlet id: ", id(greenlet.getcurrent()), "gr1 id: ", id(gr1), "gr2 id: ", id(gr2)
print gr1.switch("begin from", "gr1")   

#output result:
#main greenlet id:  139876429176176 gr1 id:  139876429176016 gr2 id:  139876429176656
#current test1 greenlet id: 139876429176016 parent greenlet id: 139876429176176
#current test2 greenlet id: 139876429176656 parent greenlet id: 139876429176176
#haha, test2 returned!
