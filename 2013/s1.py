import sys

s = input()
c= s
while 1:
	c = str(int(c)+1)

	l = list(c)
	p = True
	for x in l:
		if l.count(x) > 1:
			p = False
			break
	
	if p:
		print(c)
		sys.exit()