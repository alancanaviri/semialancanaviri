def primo(n):
	i=2
	while i<n:
		if(n%i==0):
			return 0
		i=i+1
	return 1
def suma(n):
	i=0
	p=2
	suma=0
	while i<n:
		if primo(p)==1:
			suma=suma+p
			i=i+1
		p=p+1
	print suma
suma(4)