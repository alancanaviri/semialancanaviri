def lista(inicio,fin):
	lista=[]
	pares=[]
	while(inicio<=fin):
		lista.append(inicio)
		inicio=inicio+1
	for i in lista:
		if i%2==0:
			pares.append(i)
	print lista
	print pares
		
	
a=input()
b=input()
lista(a,b)