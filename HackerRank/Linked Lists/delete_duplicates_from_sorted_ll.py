#
# Complete the 'removeDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def removeDuplicates(llist):
    temp1= llist
    
    while temp1.next:
        if temp1.data == temp1.next.data:
            temp1.next = temp1.next.next
            continue
        temp1=temp1.next
    return llist
