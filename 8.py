print("Введите число в десятичной СС:")
try:
	a = int(input())
except ValueError:
	print("invalid data")
	exit()	

print("Введите основание СС (2 или 8):")
try:
	base = int(input())
except ValueError:
	Print("invalid data")
	exit()

def base_2(a):
	b = bin(abs(a))
	b1 = b[2::]
	if a >= 0:
		print("Заданное Вами число в двоичной системе: ", b1)
		exit()	
	else:
		print("Заданное Вами число в двоичной системе ","-",b1, sep="")

def base_8(a):
	d =  oct(abs(a))
	d1 = d[2::]
	if a >= 0:
		print("Заданное Вами число в восьмеричной системе: ",d1)
		exit()
	else:
		print("Заданное Вами число в восьмеричной системе: ","-",d1, sep="")	
	
if base == 2:
	base_2(a)
	exit()
else:	
	if base == 8:
		base_8(a)
		exit() 
	else:
		print("invalid data")	