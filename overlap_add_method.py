#!/usr/bin/env python
import copy

def getMatrix(msg):
	print msg
	x =  raw_input() ;
	x = x.split();
	x = convToNum(x);
	return  x

def convToNum(x):
	t = []
	for i in x:
		t.append(int(i))
	return t


def checkAndPadd(x, h):
	if(len(x) < len(h)):
		n =  len(h) -len(x)
		for i in range(0, n):
			x.append(0)
	elif(len(h) < len(x)):
		n = len(x) - len(h)
		for i in range(0, n):
			h.append(0)
	return x, h

def genCircularMat(x):
    mat = []
    tmp = []
    for i in range(0, len(x)):
    		mat.append([])
    for i in  range(0, len(x)):
    	for j in range(0, len(x)):
    		mat[i].append(0)
    tmp = x
    k = 0
    for i in range(0, len(x)):
    	for j in range(0, len(x)):
    		mat[j][i] = tmp[k]
    		k = k+1
    	tmp = getCol(tmp, x)
    	k=0
    return mat

def getCol(tmp, x):
	n = tmp.pop()
	x.insert(0, n)
	return tmp

def multiple1(mat, h):
	a = []
	for  i in range(0, len(h)):
		a.append(mul(mat[i], h))
	return a

def mul(m, h):
	sum = 0;
	for i in range(0, len(h)):
		sum = sum + (m[i]*h[i])
	return sum

def genrateSubsequence(x, m, l):
    a = len(x)
    xx = a
    b = a%l
    if (b !=0):
        a = a - b
        a = a + l
        b = range(0,a)
        a, b = checkAndPadd(x, b)
        p = 0
        q = l
        r , s, xx= [], [], len(a)
    else:
        p = 0
        q = l
        r , s = [], []
    for i in range(0, xx/l):
        a = (x[p:q]) + [0]*(m-1)
        p, q = q, q+q
        s.append(a)
        r = copy.copy(a)
        a = []
    return s

def organise(z, n ):
	j =1
	for i in range(0, len(z)):
		tmp1 = z[n-1] + z[n]
		z.insert(n, tmp1)
		z.pop(n+1)
		z.pop(n-1)
		n = n*2 - j
		j = j+1
		if(n >= len(z)):
			break
	return z
if __name__ == "__main__":
    x = getMatrix("Give value for X");
    h = getMatrix("Give value for  H");
    l = input("Give the value for l: ")
    m = len(h)
    n = l+m-1
    s = genrateSubsequence(x, m, l)
    t = []
    print "X(n) =",x,"H(n) =", h
    print "The subsequence are: "
    for i in s:
        print i
    x, h = checkAndPadd(s[0], h)
    for k in range(0, len(s)):
        mat = []
        print "\n\n#########################FOR Y[",k,"]";
        print "Convoution of ","X(n) =",s[k], " and H(n) =", h
        mat  = genCircularMat(s[k])
        print "\n"
        j = 0;
        print "Multiplication os these 2 matrix:"
        for i in mat:
        	print i,"   [", h[j],"]"
        	j = j+1
        print "\n"
        z = multiple1(mat, h)
        print "Y(",k,") is ==>", z
        t.append(z)
	z = []
	for i in t:
		z = z + i
	print "z = ", z


    print "\nThe resultant Y(N) is ==>", organise(z, n)
