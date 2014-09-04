def ValorCadena(a,b):
	a1=len(a)
	a2=len(b)
	if a1 != a2:
		if a1<a2:
			return b
		else:
			if	a1 > a2:
				return a
	else:
		return a+b
r=ValorCadena("ALAN","CANAVIRI")
print r