lado1 = input('Digite primero: ')
lado2 = input('Digite segundo lado: ')
lado3 = input('Digite tercero lado: ')
if lado1 + lado2 > lado3:
	if lado1 == lado2 and lado1 == lado3:
		print ('equilatero')
	elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3: 
		print ('isosceles') 
	elif lado1 != lado2 and lado3 or lado2 != lado1 and lado3 or lado1 != lado3: 
		print ('escaleno')
else: 
	print ('los valores no formam um Triangulo') 