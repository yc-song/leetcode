 '''
If using python sorting library, there's the problem of not being able to figure out
which characters were adjacent at first.
'''
from collections import deque
l='baaaba'
def main(s:str):
    s = list(s)
    same_queue = deque()
    diff_queue = deque()
    s_sorted = list()
    i=1
    if s[0]==s[1]:
        same_queue.append(s[0])
    else: diff_queue.append(s[0])
    for i in range(1, len(s) - 1, 1):
        if s[i] == s[i + 1] or s[i] == s[i-1]:
            same_queue.append(s[i])
        else:
            diff_queue.append(s[i])
    if s[len(s) - 1] == s[len(s) - 2]:
        same_queue.append(s[len(s) - 1])
    else:
        diff_queue.append(s[len(s) - 1])
    print("1", same_queue, diff_queue)

    while same_queue and i:
        s_sorted.append(same_queue.popleft())
        print("2", same_queue,diff_queue, s_sorted)

        if diff_queue :
            print("2-1", diff_queue)

            if diff_queue[0]!=s_sorted[-1]:
                s_sorted.append(diff_queue.popleft())


        else: i=0
        print("3", same_queue,diff_queue,s_sorted)

    if same_queue:
        return ""

    elif diff_queue:
        while diff_queue:

            s_sorted.append(diff_queue.popleft())
            print("4", same_queue, diff_queue, s_sorted)
        return ''.join(s_sorted)
    else: return ''.join(s_sorted)

print(main(l))Reorganize String