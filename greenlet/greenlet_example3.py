import greenlet

def test1(x, y):
    z = gr2.switch(x + y)
    print('test1', z)

def test2(u):
    print('test2', u)
    gr1.switch('arg', 'in', 'test2')

gr1 = greenlet.greenlet(test1)
gr2 = greenlet.greenlet(test2)
print gr1.switch("hello", "world")

#output
#('test2', 'helloworld')
#('test1', ('arg', 'in', 'test2'))
#None
