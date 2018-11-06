import numpy as np

def getNE(yList,uList,n,m):
	N = len(yList)
	yList = np.asarray(yList)
	uList = np.asarray(uList)
	y = np.zeros((N,n))
	for i in range(0,N):
		for j in range(0,n):
			if(N-n >= 0):
				y[i,j] = -yList[i-j]
			else:
				y[i,j] = 0
	u = np.zeros((N,m))
	for i in range(0,N):
		for j in range(0,m):
			if(N-m >= 0):
				u[i,j] = -uList[i-j]
			else:
				u[i,j] = 0
	print(y)
	print(u)			
	X = np.zeros((N,n+m))
	for i in range(0,n+m):
		for j in range(0,N):
			if i < n:
				X[j,i] = y[j,0]
			else:
				X[j,i] = u[j,0]

	
	print(X)
	teta = np.linalg.inv(np.transpose(X)@X)@np.transpose(X)@y




getNE(list(range(0,5)),list(range(1,6)),1,1)