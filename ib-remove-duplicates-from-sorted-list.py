def print_ll(A):
    to_print = True
    while to_print:
        if A:
            print(A.val)
            A = A.next
            if A == None:
                break
        else:
            break

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def removeDuplicates(A):
    i = A
    if i == None:
        return A

    i_next = i.next
    if i_next == None:
        return A

    while 1:
        removed = False
        if i.val == i_next.val:
            i.next = i_next.next
            removed = True

        if not removed:
            i = i.next
            if i == None:
                return A

        i_next = i.next
        if i_next == None:
            return A


a = ListNode(1)
b = ListNode(1)
c = ListNode(3)
d = ListNode(3)
e = ListNode(6)
f = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print_ll(a)
print
print_ll(removeDuplicates(a))