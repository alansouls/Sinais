import numpy as np

def getNE(yList,uList,n,m):
	N = len(yList)
	yList = np.asarray(yList)
	uList = np.asarray(uList)
	y = np.zeros((N-1,n))
	for i in range(0,N-1):
		for j in range(0,n):
			if(N-n >= 0):
				y[i,j] = -yList[i-j]
			else:
				y[i,j] = 0
	u = np.zeros((N-1,m))
	for i in range(0,N-1):
		for j in range(0,m):
			if(N-m >= 0):
				u[i,j] = -uList[i-j]
			else:
				u[i,j] = 0
	print(y)
	Y = yList[1:]
	Y = Y.reshape(N-1,1)
	print(Y)
	print(u)			
	X = np.zeros((N-1,n+m))
	for i in range(0,n+m):
		for j in range(0,N-1):
			if i < n:
				X[j,i] = y[j,0]
			else:
				X[j,i] = u[j,0]

	
	print(X)
	print(Y)
	teta = np.linalg.inv(np.transpose(X)@X)@np.transpose(X)@Y
	print(teta)
	print("ERRO:")
	print(Y-X@teta)



getNE(list(range(0,5)),list(range(1,6)),1,1)