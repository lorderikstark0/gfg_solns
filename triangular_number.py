
def triangular(num):
	if(num<0):
		return False
	sum ,n =0,1 
	while(sum <=num):
		sum =sum+n
		if(sum==num):
			return True 
		n=n+1
	return False 


def main():
	t=int(input())
	while(t>0):
		n=int(input())
		if(triangular(n)):
			print(1)
		else:
			print(0)
		t=t-1
if __name__=='__main__':
	main()