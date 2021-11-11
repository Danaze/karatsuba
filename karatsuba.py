# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:12:07 2021

@author: daaze
"""

def karatsuba(x,y):
	"""
	Function to multiply 2 numbers in a more efficient manner
	Prameters: (x,y) - inputs to be multiplied
	Returns the product x * Y using recursive karatsuba algorithm
	"""
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		nby2 = n // 2
		
		a = x // 10**(nby2)
		b = x % 10**(nby2)
		c = y // 10**(nby2)
		d = y % 10**(nby2)
		
		ac = karatsuba(a,c)
		bd = karatsuba(b,d)
		ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
        
        # this little trick, writing n as 2*nby2 takes care of both even and odd n
		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

		return prod
