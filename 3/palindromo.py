def palindromo(cad):
	aux=""
	i=len(cad)-1
	while(i>=0):
		aux=aux+cad[i]
		i=i-1
	if aux==cad:
		return "true"
	else:
		return "false"
print palindromo("oruro")