
def __partition(l:list, start:int, end:int)->int:
    j=start
    for i in range(start+1, end+1):
        if l[i]>l[start]:
            j+=1
            l[j],l[i]=l[i],l[j]
    l[start],l[j]=l[j],l[start]
    print(start, end, j,  l)
    return j

def __quicksorthelp(l:list, start:int, end:int)->None:
    if start<end:
        q=__partition(l,start,end)
        __quicksorthelp(l,start,q-1)
        __quicksorthelp(l,q+1,end)
        return
    else: return

def quicksort(l:list)->None:
    __quicksorthelp(l,0,len(l)-1)
    return l
l=[5,3,2,0,9]
quicksort(l)

#
# def test(l:list):
#     l[0],l[2]=l[2],l[0]
# l=deque([1,2,3,4])
# test(l)
# print(l)
