# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    temp1 = llist1
    temp2 = llist2
    len1 = 0
    len2 = 0
    
    while temp1.next:
        len1+=1
        temp1=temp1.next
        
    while temp2.next:
        len2+=1
        temp2=temp2.next
    
    temp1 = llist1
    temp2 = llist2
    
    if len1!=len2:
        return False
    else:
        while temp1.next:
            if temp1.data != temp2.data:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
    return True
