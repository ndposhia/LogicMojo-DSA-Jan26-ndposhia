# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    dummy = SinglyLinkedListNode(0)
    current = dummy

    while head1 and head2:
        if head1.data > head2.data:
            current.next = head2
            head2=head2.next
        else:
            current.next = head1
            head1=head1.next
        current=current.next
        
    if head1:
        current.next = head1
    elif head2:
        current.next = head2

    return dummy.next
