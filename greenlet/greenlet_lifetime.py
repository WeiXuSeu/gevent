from greenlet import greenlet 

def test1():
    gr2.switch(1)
    print "test1 finished!"

def test2(x):
    print "test2 begin: ", x
    z = gr1.switch()
    print "test2 finished: ", z

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
print "gr1 is dead?: %s, gr2 is dead?: %s" % (gr1.dead, gr2.dead)
gr2.switch()
print "gr1 is dead?: %s, gr2 is dead?: %s" % (gr1.dead, gr2.dead)
print gr2.switch(10)


#test2 begin:  1
#test1 finished!
#gr1 is dead?: True, gr2 is dead?: False
#test2 finished:  ()
#gr1 is dead?: True, gr2 is dead?: True
#10

#如果试图再次switch到一个已经是dead状态的greenlet会怎么样呢，事实上会切换到其parent greenlet。
