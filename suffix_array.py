import variable
from consts import * 

def find_root(p):
    if variable.father[p] == p:
        return p
    variable.father[p] = find_root(variable.father[p])
    return variable.father[p]

def init_father(urls):
    variable.father = [ i for i in range(len(urls)) ]

def init(n):
    variable.rank = [0] * (n + 1)
    variable.sa = [0] * (n + 1)
    variable.highet = [0] * (n + 1)

def calhighet(n):
    j = k = 0
    for i in range(1, n + 1):
        variable.rank[ variable.sa[i] ] = i
    for i in range(0, n):
        if k != 0:
            k -= 1
        else:
            k = 0
        j = variable.sa[variable.rank[i] - 1]
        while variable.need_deal[i + k][0] == variable.need_deal[j + k][0]:
            k += 1
        variable.highet[variable.rank[i]] = k

def cmp(r, a, b, plen):
    return (r[a] == r[b] and r[a + plen] == r[b + plen])

def deal_suffix(n, m = 256):
    variable.need_deal.append((SIGN_MINIMUM_TO_NUMBER, -1))
    init(n)
    plen = p = 0
    x = [0] * (n + 1)
    y = [0] * (n + 1)
    bucket = [0] * (m + 1)
    for i in range(n):
        x[i] = variable.need_deal[i][0]
        bucket[x[i]] += 1
    for i in range(1, m):
        bucket[i] += bucket[i - 1]
    for i in range(n - 1, -1, -1):
        bucket[ x[i] ] -= 1
        variable.sa[ bucket[ x[i] ] ] = i
    plen = p = 1
    while p < n:
        p = 0
        for i in range(n - plen, n):
            y[p] = i
            p += 1
        for i in range(n):
            if variable.sa[i] >= plen:
                y[p] = variable.sa[i] - plen
                p += 1
        bucket = [0] * (m + 1)
        for i in range(0, n):
            bucket[ x[y[i]] ] += 1
        for i in range(1, m):
            bucket[i] += bucket[i - 1]
        for i in range(n - 1, -1, -1):
            bucket[ x[y[i]] ] -= 1
            variable.sa[ bucket[ x[y[i]] ] ] = y[i]
        x, y = y, x
        x[variable.sa[0]] = 0
        p = 1
        for i in range(1, n):
            if cmp(y, variable.sa[i - 1], variable.sa[i], plen):
                x[variable.sa[i]] = p - 1
            else:
                x[variable.sa[i]] = p
                p += 1
        m = p
        plen *= 2
    calhighet(n - 1)

def make_group(threshold):
    group_start = False
    need_group = set()
    for i in range(2, len(variable.highet)):
        highet = variable.highet[i]
        sa = variable.sa[i]
        suffix = variable.need_deal[sa]
        if highet and suffix[0] > 1:
            if group_start:
                if highet >= threshold and (1, -1,) not in variable.need_deal[sa:sa + threshold]:
                    pre_suffix = variable.need_deal[variable.sa[i - 1]]
                    root_now = find_root(suffix[1])
                    root_pre = find_root(pre_suffix[1])
                    need_group.add(pre_suffix[1])
                    need_group.add(suffix[1])
                    if root_pre != root_now:
                        variable.father[root_now] = root_pre
                else:
                    group_start = False
            else:
                if highet >= threshold and (1, -1,) not in variable.need_deal[sa:sa + threshold]:
                    group_start = True
                    pre_suffix = variable.need_deal[variable.sa[i - 1]]
                    root_now = find_root(suffix[1])
                    root_pre = find_root(pre_suffix[1])
                    need_group.add(pre_suffix[1])
                    need_group.add(suffix[1])
                    if root_pre != root_now:
                        variable.father[root_now] = root_pre

    groups = list()
    for url_num in need_group:
        groups.append( (find_root(url_num), url_num) )

    groups.sort(key=lambda x:x[1])
    #print groups
    #print len(groups)

    groups.sort(key=lambda x:x[0])

    result = list()
    for i in range(len(groups)):
        if i == 0:
            result.append([groups[i][1]])
        else:
            if groups[i][0] == groups[i - 1][0]:
                result[len(result) - 1].append(groups[i][1])
            else:
                result.append([groups[i][1]])

    return result



if __name__ == '__main__':
    variable.need_deal = [1,2,3,4,3,2,3,4,5,3,1,3,0]
    init(12)
    deal_suffix(13)
    print variable.rank
    print variable.sa
    print variable.highet
