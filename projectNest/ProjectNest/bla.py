bla = 0.1

def func():
    global bla
    bla += .1
    print bla
    if bla < 111.1:
        print 'Threat'
    else:
        print 'Chilled'

while True:
    func()
        
       
    
