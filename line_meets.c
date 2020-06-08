# include <stdio.h>
 int main()
{
    int t,i;
    scanf("%d",&t);
    while (t--)
    {  float m1,m2;
      int a[4],b[4];
      for(i=0;i<4;i++)
      scanf("%d",&a[i]);
      for(i=0;i<4;i++)
      scanf("%d",&b[i]);
      m1=(a[3]-a[1])/(a[2]-a[0]);
      m2=(b[3]-b[1])/(b[2]-b[0]);
      if(m1==m2)
      printf("0");
      else
      printf("1");
    }
    return 0;
}