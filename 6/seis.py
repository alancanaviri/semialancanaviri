def verificar(cad):
	dig=0
	car=0
	for c in cad:
		if c>='0' and c<='9':
			dig=dig+1
		else:
			if c>='a' and c<='z':
				car=car+1
	print ('letras:',car)
	print ('digitos:',dig)		
verificar("!hola$mundo 123456")
