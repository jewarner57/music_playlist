from LinkedList import LinkedList

print("Hello World")

list = LinkedList()

list.append("Item2")
list.prepend("Test")
list.append("last item")
list.prepend("first item")

list.printList()
list.delete_from_tail()
list.printList()

print(list.find("Test"))
print(list.find("last item"))
