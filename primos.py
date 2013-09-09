x = int(raw_input('numero:'))

for i in range(2, x):
	if x % i == 0:
		print 'No es primo'
		exit(0)
	else:
		pass

print 'Si es primo'
