from collections import deque

def adjust(q, new_entry):
    while(len(q) > 0 and q[-1] < new_entry ):
        q.pop()
    q.append(new_entry)
    return q

def slidingMaximum(A, B):
    answer = []
    start = A[:B]
    q = deque([A[0]])

    for i in start[1:B]:
        q = adjust(q, i)
    answer.append(q[0])

    for i in range(B, len(A)):
        tail_last_window = A[i - B]
        new_to_window = A[i]

        if tail_last_window == q[0]:
            q.popleft()
            q = adjust(q, new_to_window)
            answer.append(q[0])
        else:
            q = adjust(q, new_to_window)
            answer.append(q[0])
    return answer



A = (1, 3, -1, -3, 5, 3, 6, 7)
# A = (7,2,1,6)
B = 1

print(slidingMaximum(A, B))