from LinkedList import LinkedList

print("\nMusic Playlist")
print("--------------")
print('Powered by LinkedList\u2122 technology.')
print("--------------")

LinkedList = LinkedList()
commandList = ["append", "prepend",
               "find", "reverse", "delete", "print", "exit"]
stopProgram = False

while not stopProgram:
    print("--------------")
    print("Enter a command: append, prepend, find, reverse, delete, print, exit")
    command = input().lower()
    while command not in commandList:
        print("Enter a valid command")
        command = input().lower()

    if command == "append":
        print("enter song name")
        name = input().lower()
        LinkedList.append(name)

    if command == "prepend":
        print("enter song name")
        name = input().lower()
        LinkedList.prepend(name)

    if command == "find":
        print("enter song name to find")
        name = input().lower()
        print(f'Song Found: {LinkedList.find(name)}')

    if command == "reverse":
        LinkedList.reverse()

    if command == "delete":
        print("enter song name to delete")
        name = input().lower()

        if name == LinkedList.tail:
            LinkedList.delete_from_tail()
        else:
            LinkedList.delete(name)

    if command == "print":
        print("--------------")
        LinkedList.printList()

    if command == "exit":
        print("exiting...")
        stopProgram = True
