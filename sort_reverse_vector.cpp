#include <bits/stdc++.h>
using namespace std;
#define pb push_back 


vector<int> sortVector(vector<int>&v){
	return sort(v.begin(),v.end());
}

vector<int> reverseVector(vector<int>& v){
	return reverse(v.begin(),v.end());
}
int main(){
	int t;
	cin >> t;
	while(t-->0){
		int n ;
		cin >> n;
		vector<int> arr;
		for(int i=0;i<n;i++){
			int p;
			cin >> p;
			arr.pb(p);
		}
	}
	return 0;
}