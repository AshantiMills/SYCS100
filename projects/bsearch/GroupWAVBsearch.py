#Hezekiah
#Michelle
#Sacha
#Eboni
#Ashanti
#Tyler


list = [1,2,64,78,79,80,100,121,144,387,4000]
x = 387
def bsearch(list,x):
	if list != None:
		hi = len(list)
		lo = 0
		n = (hi+lo)/2
		a = 0
		while list[n] != x and a < len(list):
			if list[n] < x:
				lo = n
			elif list[n] > x:
				hi = n
			n = (hi+lo)/2
			a += 1
		
		if list[n] == x:
			print n
		else:
			print -1
	else:
		print -1	
bsearch(list,x)
