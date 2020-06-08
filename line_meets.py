'''
given the slopes of two lines find if they meet
 just chceck if 
 tan theta of them are equal or not 
 if qual they they are parallel and never meet
 '''


def meets(li1,li2):
	'''
	sl1 =(li1[3]-li1[1])//(li1[2]-li1[0])
	sl2 =(li2[3]-li2[1])//(li2[2]-li2[0])

	if(sl1==sl2):
		return 0
	else:
		return 1
	'''
	###need to also handle div by 0 exception 
	
	if (li[2]-li[0]!=0 or li2[2]-li2[0]!=0):
		sl1 =(li1[3]-li1[1])//(li1[2]-li1[0])
		sl2 =(li2[3]-li2[1])//(li2[2]-li2[0])

		if(sl1==sl2):
			return 0
		else:
			return 1
	elif(li2[2]-li2[0]==0):
		return 0
	elif(li1[2]-li1[0]==0):
		return 0		

def main():
	t=int(input())
	while(t>0):
		li1=[int(x) for x in input().split() ]
		li2=[int(x) for x in input().split() ]
		print(meets(li1,li2))
		t=t-1



if __name__=='__main__':
	main()