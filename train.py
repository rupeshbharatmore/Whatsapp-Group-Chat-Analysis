


def update(node,start,end,ind,val):
    #print(start,end,ind,val,"ddddddd")
    if start == end:
        arr[start] = val
        tree[node] = arr[start]
    else:

        mid = start+(end-start)//2
        if start<=ind<=mid:
            update(2*node,start,mid,ind,val)
        else:
            update(2*node+1,mid+1,end,ind,val)
        tree[node] = max(tree[2*node],tree[2*node+1])

def build(node,start,end):
    if start == end:
        tree[node] = arr[start]
    else:
        mid = start+(end-start)//2
        build(2*node,start,mid)
        build(2*node+1,mid+1,end)
        tree[node] = max(tree[2*node],tree[2*node+1])
    
def query(node,start,end,l,r):
    #print(start,end,l,r)
    if end<l or r<start:return float("-inf")
    if start == end:
        return tree[node]
    elif(l<=start and end<=r):
        return tree[node]
    else:
        mid = start+(end-start)//2
        left= query(2*node,start,mid,l,r)
        right = query(2*node+1,mid+1,end,l,r)
        return max(left,right)

n,m = map(int(input().split()))
arr =[ 0]
for _ in range(pow(2,n)):
    arr.append(int(input()))

tree = [0]*(4*n)
build(1,1,n)
#print(tree)
q = int(input())
for _ in range(q):
    p,b = map(int,input().split())
    update(1,1,pow(2,n),p,b)
    print(tree[1])
    