1 #include <cstdio>
2 #include <cstring>
3 #include <algorithm>
4 #include <iostream>
5 using namespace std;
6
7 const int N = 200005;
8 int rank[N], sa[N], X[N], Y[N], highet[N], in[N];
9 int bucket[N];
10
11 void calhighet(int n)
12 {
13 intj,k=0;
14 for(inti=1;i<=n;++i)rank[sa[i]]=i;
15 for(inti=0;i<n;highet[rank[i++]]=k)
16 for (k ? k--: 0, j = sa[rank[i] - 1]; in[i + k] == in[j + k]; k++);
17 }
18
19 bool cmp(int *r, int a, int b, int len)
20 {
21 return (r[a] == r[b] && r[a + len] == r[b + len]);
22 }
23
24 void deal_suffix(int n, int m = 256)
25 {
26 intlen,p,*x=X,*y=Y;
27 memset( bucket, 0, sizeof(int) * (m + 1));
28 for (int i = 0; i < n; ++i) bucket[ x[i] = in[i] ]++;
29 for(inti=1;i<m;++i)bucket[i]+=bucket[i-1];
30 for(inti=n-1;i>=0;--i)sa[--bucket[x[i]]]=i;
31 for(len=1,p=1;p<n;m=p,len*=2)
32 {
33 p = 0;
34 for(inti=n-len;i<n;++i)y[p++]= i;
35 for(inti=0;i<n;++i)if(sa[i]>= len ) y[p++] = sa[i] - len;
36 memset( bucket, 0, sizeof(int) * (m + 1) );
37 for (int i = 0; i < n; ++i) bucket[ x[y[i]] ]++;
38 for (int i = 1; i < m; ++i) bucket[i] += bucket[i - 1];
39 for (int i = n - 1; i >= 0; --i) sa[ --bucket[ x[y[i]] ] ] = y[i];
40 swap(x, y);
41 x[sa[0]] = 0;
42 p = 1;
43 for (int i = 1; i < n; ++i) x[sa[i]] = cmp(y, sa[i-1], sa[i], len) ? p -
1: p++;
44 }
45 calhighet(n-1);
46 }
