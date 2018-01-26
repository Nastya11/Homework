lst=[1,2]
f=0
while f<4000000:
	f=lst[-1]+lst[-2]
	lst.append(f)
	
M=[x for x in lst if x%2==0]
print ('list: ',M)
print ('sum =',sum(M))
