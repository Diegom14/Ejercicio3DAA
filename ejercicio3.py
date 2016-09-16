import timeit

def minimo(A):				
	lo	=	1
	hi	=	len(A)	-2
	mid = len(A)//2
			
	while lo+1 != mid:
		if A[lo-1]	>	A[lo]	and	A[lo]	<	A[lo+1]:
			return lo
		if A[hi-1]	>	A[hi]	and	A[hi]	<	A[hi+1]:
			return hi
		lo = lo+1	 
		hi = hi-1
	return "no hay minimo"



j=raw_input('Ingresar nombre de archivo a probar sin extension(input): ')
archivo = open('%s.txt'%j, 'r')
A = []
for linea in archivo:
	 numero = int(linea)
	 A.append(numero)
archivo.close()
print "todo va bien"
a = minimo(A)
print "todo va bien"
#print a
times = 1   
tiempo = timeit.Timer(lambda: minimo(A), "")
tiempof = tiempo.repeat(times, 1)
print tiempof