from LinkedList import LinkedList

print("\nMusic Playlist")
print("--------------")
print('Powered by LinkedList\u2122 technology.')
print("--------------")


list = LinkedList()

list.append("1")
list.append("2")
list.append("3")
list.append("6")
list.append("4")

list.printList()
list.reverse()
list.printList()

# list.printList()
# list.delete_from_tail()
# list.printList()

# print(list.find("Test"))
# print(list.find("last item"))
# print(list.delete("Test"))
# print(list.find("Test"))
