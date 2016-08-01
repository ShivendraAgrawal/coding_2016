def print_ll(A, print_till = 10):
    to_print = True
    count = 0
    while to_print:
        if A:
            print(A.val)

            count += 1
            if count == print_till:
                break

            A = A.next
            if A == None:
                break
        else:
            break

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def has_cycle(A):
    slow = A
    if slow == None:
        return False

    fast = slow.next
    if fast == None:
        return False

    while 1:
        if slow == fast:
            # print("Node with %d part of cycle" % slow.val)
            return True

        slow = slow.next
        if slow == None:
            return False

        fast_intermediate = fast.next
        if fast_intermediate == None:
            return False
        fast = fast_intermediate.next
        if fast == None:
            return False

def find_cycle_length(A):
    cycle_found = False
    slow = A
    fast = slow.next
    length = 0

    while 1:
        if slow == fast:
            if cycle_found:
                return length
            else:
                length = 0
                cycle_found = True

        length += 1
        slow = slow.next
        fast_intermediate = fast.next
        fast = fast_intermediate.next

def find_cycle_start(A, cycle_length):
    former = A
    latter = former
    loop_till = cycle_length

    while loop_till > 0:
        latter = latter.next
        loop_till -= 1

    while 1:
        if former == latter:
            return former

        former = former.next
        latter = latter.next

def cycle(A):
    cycle_present = has_cycle(A)

    if cycle_present:
        # print('Cycle found !!')

        cycle_length = find_cycle_length(A)
        # print('Cycle length = ' + str(cycle_length))

        cycle_start = find_cycle_start(A, cycle_length)
        # print('Cycle starts at node with value = ' + str(cycle_start.val))
        return cycle_start

    return None



a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
f = ListNode(6)
g = ListNode(7)
h = ListNode(8)
i = ListNode(9)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g
g.next = h
h.next = i
i.next = f

# a = ListNode(1)
# a.next = a



print_ll(a)
print
print_ll(cycle(a))