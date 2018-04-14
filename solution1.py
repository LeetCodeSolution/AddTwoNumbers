import re

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, node1, node2):
        """
        :type node1: ListNode
        :type node2: ListNode
        :rtype: ListNode
        """
        first_node, last_node = None, None
        up = 0
        while node1 and node2:
            val1 = node1.val
            val2 = node2.val
            result = val1 + val2 + up
            if result >= 10:
                up = 1
                result -= 10
            else:
                up = 0
            node1 = node1.next
            node2 = node2.next
            
            node = ListNode(result)
            if not first_node:
                first_node = node
            if last_node:
                last_node.next = node
            last_node = node
        
        extra = node1 if node1 else node2
        
        while extra:
            result = extra.val + up
            if result >= 10:
                up = 1
                result -= 10
            else:
                up = 0
            node = ListNode(result)
            if last_node:
                last_node.next = node
            last_node = node
            extra = extra.next
        
        if up == 1:
            node = ListNode(up)
            if last_node:
                last_node.next = node
        return first_node


def output_node_chain(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def get_node_chain(expression):
    expression_numbers = expression.split('->')
    last_node, first_node = None, None
    for expression_number in expression_numbers:
        node = ListNode(int(expression_number))
        if not last_node:
            first_node = node
        if last_node:
            last_node.next = node
        last_node = node
    return first_node



expression = input()
expression = expression.replace(' ', '')
result = re.split('\((.*?)\)', expression)
expression1, expression2 = result[1], result[3]
node1, node2 = get_node_chain(expression1), get_node_chain(expression2)
s = Solution()
node = s.addTwoNumbers(node1, node2)
print(output_node_chain(node))
