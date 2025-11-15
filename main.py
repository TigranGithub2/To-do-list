import random
import time

todo = ["send email to boss" , "homework" , "repair Ps5"]

print("Welcome to the mighty to do list")

while True:
    print("1 - show my todo's")
    print("2 - add a new todo")
    print("3 - delete a todo")
    print("4 - exit")


    action = input("what action do you want to fulfill?")

    if action == "1":
        print(todo)
        input("enter to continue!")


    elif action == "2":
        new_todo = input("insert new todo: ")
        todo.append(new_todo)
        print("new todo has been added!")
        input("enter to continue!")

    elif action == "3":
        print("todo list: ", todo)
        remove_todo = input("which word do you want to delete?: ")
        if remove_todo in todo:
            todo.remove(remove_todo)
            print("deleted!")
            input("enter to continue!")
        else:
            print("todo was not found!")
            input("enter to continue!")
            

    elif action == "4":
        print("goodbye!")
        quit()







