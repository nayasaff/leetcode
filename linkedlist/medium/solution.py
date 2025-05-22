class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
Algorithm :
1. Iterate over all values of two linked list
2. Add two numbers and store carry 
3. Store value of sum in new linked list
4. Get next node in linked list
5. Check of any carry to add it to new linked list
Time complexity : O(N), Space complexity O(N)
"""

def addTwoNumbers(self, l1, l2):

        result = ListNode()
        remainder = 0
        while l1 or l2:


            value1 = l1.val if l1 is not None else 0
            value2 = l2.val if l2 is not None else 0
            sum = value1 + value2 + remainder 
            remainder = sum // 10

            val = val % 10
            result = ListNode(val, result)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if(remainder != 0) :
            result = ListNode(remainder, result)

        prev = None
        while result:
                next_node = result.next   # save next node
                result.next = prev        # reverse the link
                prev = result             # move prev forward
                result = next_node        # move current forward

        return prev