class computer:
    def __init__(k,c,r,s,v):
        k.c = c
        k.r = r
        k.s = s
        k.v = v
    def configuration(p):
        print("Configuration is = ", p.c , p.r , p.s,p.v)

com1 = computer('I5 PC',16,1024 ,3)
com2 = computer('Ryzen PC', 32 , 2048,6)
com3 = computer('Ryzen PC- ssd', 32 , 320,'NA')

com1.configuration()
com2.configuration()
com3.configuration()






