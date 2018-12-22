#include<bits/stdc++.h>
using namespace std;
int a[101][101];
int main()
{
int n;
cin>>n;
for(int i=1;i<=n;i++)
for(int j=1;j<=n;j++)
	cin>>a[i][j];
 
int s = 0,ss=0;
for(int i=1;i<=n;i++)
for(int j=1;j<=n;j++)
	if(a[i][j]<=50)
		s+=1;
	if(a[i-1][j]>50|| a[i+1][j]>50 ||a[i][j-1]>50 || a[i][j+1]>50 || i==1 || j==n || j==1 || j==n)
	{
		ss+=1
	} 
cout<<s<<" "<<ss<<endl;

return 0;
}