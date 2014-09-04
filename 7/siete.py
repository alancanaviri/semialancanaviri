def secuencia1(n):
	i=1
	inc=1
	while i>0:
		print str(i)*i
		if i==n:
			inc=-1
		i=i+inc
secuencia1(5)