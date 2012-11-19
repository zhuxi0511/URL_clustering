#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;

const int N = 200005;
int rank[N], sa[N], X[N], Y[N], highet[N], in[N];
int bucket[N];

void cal highet(int n)
{
    int j,k=0;
    for(int i=1;i<=n;++i)rank[sa[i]]=i;
    for(int i=0;i<n;highet[rank[i++]]=k)
        for (k ? k--: 0, j = sa[rank[i] - 1]; in[i + k] == in[j + k]; k++);
}

bool cmp(int *r, int a, int b, int len)
{
    return (r[a] == r[b] && r[a + len] == r[b + len]);
}

void deal_suffix(int n, int m = 256)
{
    int len,p,*x=X,*y=Y;
    memset( bucket, 0, sizeof(int) * (m + 1));
    for (int i = 0; i < n; ++i) bucket[ x[i] = in[i] ]++;
    for(int i=1;i<m;++i)bucket[i]+=bucket[i-1];
    for(int i=n-1;i>=0;--i)sa[--bucket[x[i]]]=i;
    for(len=1,p=1;p<n;m=p,len*=2)
    {
        p = 0;
        for(int i=n-len;i<n;++i)y[p++]= i;
        for(int i=0;i<n;++i)if(sa[i]>= len ) y[p++] = sa[i] - len;
        memset( bucket, 0, sizeof(int) * (m + 1) );
        for (int i = 0; i < n; ++i) bucket[ x[y[i]] ]++;
        for (int i = 1; i < m; ++i) bucket[i] += bucket[i - 1];
        for (int i = n - 1; i >= 0; --i) sa[ --bucket[ x[y[i]] ] ] = y[i];
        swap(x, y);
        x[sa[0]] = 0;
        p = 1;
        for (int i = 1; i < n; ++i) x[sa[i]] = cmp(y, sa[i-1], sa[i], len) ? p - 1: p++;
    }
    calhighet(n-1);
}

int main()
{
    int xxx[1000] = [1,2,3,4,3,2,3,4,5,3,1,3,0];
    in = xxx;
    deal_suffix(13)
    return 0;
}
