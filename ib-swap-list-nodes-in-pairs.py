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

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def swapPairs(self, A):
        head = A
        i = head
        i_next = i.next


        if i_next == None:
            return head

        swap = i_next.next
        i_next.next = i
        i.next = swap
        head = i_next

        previous = i


        while 1:
            i = i.next

            if i == None:
                break

            i_next = i.next

            if i_next == None:
                break

            swap = i_next.next
            i_next.next = i
            i.next = swap

            if previous != None:
                previous.next = i_next
                previous = i

        return head






s = Solution()
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

print_ll(a)
print
print_ll(s.swapPairs(a))


