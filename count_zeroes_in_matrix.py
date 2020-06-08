
def countZeroes(arr,n):
	count=0
	for i in range(n):
		for j in range(n):
			if(arr[i][j]==0):
				count=count+1
	return count 




if __name__=='__main__':
	t=int(input())
	for i in range(t):
		n=int(input().strip())
		arr=list(map(int ,input().strip().split()))
		matrix =[[0 for i in range(n)]for j in range(n)]
		k=0
		for i in range(n):
			for j in range(n):
				matrix[i][j]=arr[k]
				k+=1
		print(countZeroes(matrix,n))