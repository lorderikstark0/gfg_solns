def lookandSay(n):
	if(n==1):
		return "1"
	if(n==2):
		return "11"

	s="11"
	for i in range(3,n+1):
		s +='$'
		l=len(s)
		cnt=1
		tmp=""
		for j in range(1,l):
			if(s[j]!=s[j-1]):
				tmp+=str(cnt+0)
				tmp +=s[j-1]
				cnt=1
			else:
				cnt+=1
		s=tmp
	return s

if __name__=='__main__':
	t=int(input())
	while(t>0):
		n=int(input())
		print(lookandSay(n))
		t=t-1

