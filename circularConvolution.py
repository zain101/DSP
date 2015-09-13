#!/usr/bin/env python

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
		tmp = getCol(tmp)
		k=0
	return mat

def getCol(tmp):
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


if __name__ == "__main__":
	x = getMatrix("Give value for X");
	h = getMatrix("Give value for  H");
	print "X(n) =",x,"H(n) =", h
	x, h = checkAndPadd(x, h)
	print "After padding:"
	print "Convoution of ","X(n) =",x, " and H(n) =", h
	mat  = genCircularMat(x)
	print "\n"
	j = 0;
	print "Multiplication os these 2 matrix:"
	for i in mat:
		print i,"   [", h[j],"]"
		j = j+1
	print "\n"
	print "The resultant Y(N) ==>", multiple1(mat, h)
