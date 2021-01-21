class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)  
        cur = dummy  
        
        while l1 and l2:#check if values exist at each node  
            if l1.val <= l2.val:  
                cur.next = l1  
                l1 = l1.next  
            else:  
                cur.next = l2  
                l2 = l2.next  
            cur = cur.next  
        
        cur.next = l1 or l2    #add either l1 or l2
        return dummy.next
