import random
import time

todo = ["send email to boss" , "homework" , "repair Ps5"]

print("Welcome to the mighty to-do list")

while True:
    print("1 - show my to-do's")
    print("2 - add a new to-do")
    print("3 - delete a to-do")
    print("4 - exit")


    action = input("what action do you want to fulfill?")

    if action == "1":
        print(todo)
        input("enter to continue!")


    elif action == "2":
        new_todo = input("insert new to-do: ")
        todo.append(new_todo)
        print("new to-do has been added!")
        input("enter to continue!")

    elif action == "3":
        print("to-do list: ", todo)
        remove_todo = input("which to-do do you want to delete?: ")
        if remove_todo in todo:
            todo.remove(remove_todo)
            print("deleted!")
            input("enter to continue!")
        else:
            print("to-do was not found!")
            input("enter to continue!")
            

    elif action == "4":
        print("goodbye!")
        quit()





