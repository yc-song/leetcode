
def __partition(l:list, start:int, end:int, idx_list:list)->int:
    j=start
    for i in range(start+1, end+1):
        if l[i]>l[start]:
            j+=1
            l[j],l[i]=l[i],l[j]
            idx_list[j],idx_list[i]=idx_list[i],idx_list[j]
    idx_list[start],idx_list[j]=idx_list[j],idx_list[start]
    l[start],l[j]=l[j],l[start]
    return j

def __quicksorthelp(l:list, start:int, end:int, idx_list:list)->None:
    if start<end:
        q=__partition(l,start,end, idx_list)
        __quicksorthelp(l,start,q-1, idx_list)
        __quicksorthelp(l,q+1, end, idx_list)
        return
    else: return

def quicksort(l:list)->(list,list):
    idx_list=[None]*len(l)
    medal=[None]*len(l)
    for i in range(len(l)): ## change to idx_list soon after
        idx_list[i]=i
    __quicksorthelp(l,0,len(l)-1, idx_list)
    for j in range(len(l)):
        if j ==0:
            medal[idx_list[j]]="Gold Medal"
        elif j==1:
            medal[idx_list[j]] = "Silver Medal"
        elif j == 2:
            medal[idx_list[j]] = "Bronze Medal"
        else: medal[idx_list[j]]=str(j+1)
    return medal


l=[10,3,8,9,4]
print(quicksort(l))

