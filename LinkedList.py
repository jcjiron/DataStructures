

class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


def print_list(head):
    finalString = ""
    current = head
    while current is not None:
        finalString += str(current.val) + "->"
        current = current.next
    
    finalString += "None"
    print(finalString)


def reverse_list(head):
    prev = None
    current = head

    while current is not None:
        next = current.next
        
        current.next = prev

        prev = current
        current = next

    return prev

keys = [1,2,3,4,5]

currNode = None
for i in reversed(range(len(keys))):
    currNode = Node(keys[i], currNode)

print_list(currNode)

reversedList = reverse_list(currNode)
print_list(reversedList)










