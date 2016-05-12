def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def text2num(message):
	a=list(message)

	i=0

	b=a
	d=[]
	e=[]
	f=[]


	for i in range(len(a)):

	    if ord(a[i])==32:
	        e.append(d)
	        d=[]

	    d.append(ord(a[i]))

	for i in range(1,len(e)):
	    e[i].remove(32)

	for i in range(len(e)):
	    x=0
	    for j in range(len(e[i])):
	        
	        c=x
	        x=(c*256)+e[i][j]
	    f.append(x)
	return f

def encrypt(message, n, e):
	encoded = text2num(message)
	encrypted = []
	for m in encoded:
		c = (m**e)%n
		encrypted.append(c)
	return encrypted

p = 203956878356401977405765866929034577280193993314348263094772646453283062722701277632936616063144088173312372882677123879538709400158306567338328279154499698366071906766440037074217117805690872792848149112022286332144876183376326512083574821647933992961249917319836219304274280243803104015000563790123
q = 319705304701141539155720137200974664666792526059405792539680974929469783512821793995613718943171723765238853752439032835985158829038528214925658918372196742089464683960239919950882355844766055365179937610326127675178857306260955550407044463370239890187189750909036833976197804646589380690779463976173
n = p*q
phi = (p-1)*(q-1)
e = 7
d = modinv(e, phi)

message = "xkcd dot com slash 538 "

code = encrypt(message, n, e)
murray = open('murray_code.txt', 'w')
murray.write('code : ')
murray.write(str(code)) 
murray.write('\n')
murray.write('n = %s' % str(n))
murray.write('\n')
murray.write('e = %s' % str(e))



