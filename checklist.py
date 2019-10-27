#Create our Checklist
checklist = list()

#CREATE
def create(item):
    checklist.append(item)

#READ
def read(index):
    return checklist[int(index)]

#UPDATE
def update(index, item):
    checklist[index] = item

#DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index=0
    for list_item in checklist:
        # print(str(index) + list_item)
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    for input_item in checklist:
        print("√ " + input_item)

def select(function_code):
    # add item
    if function_code == "A":
        input_item = user_input("Input item:")
        create(input_item)
        mark_completed(input_item)

    # Read item
    # elif function_code == "R":
    #     item_index = user_input("Index Number?")
    #
    #     # Remember that item_index must actually exist or our program will crash.
    #     print(read(item_index))

    # Print all items
    elif function_code == "P":
        list_all_items()

    #Update all items
    elif function_code == "U":
        #print full list of all items
        list_all_items()
        #ask which item to change
        item_index = user_input("Which Item? > ")
        #
        print(read(item_index))
        confirm_item_index = user_input("Is this correct? Y/N")
        if confirm_item_index == "Y":
            def update(index, item):
                checklist[item_index] = item

    #Delete/destroy
    elif function_code == "D":
        list_all_items()

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False
    # Catch all
    else:
        print("Unknown Option")
    return True

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

running = True
while running:
    selection = user_input(
        "Press A to add to list, P to display list and Q to quit")
    running = select(selection)

# def test():
    # create("purple sox")
    # create("red cloak")
    #
    # print(read(0))
    # print(read(1))
    #
    # update(0, "purple socks")
    #
    # destroy(1)
    #
    # print(read(0))
    # # Call your new function with the appropriate value
    # select("C")
    # # View the results
    # list_all_items()
    # # Call function with new value
    # select("R")
    # # View results
    # list_all_items()
    # # Continue until all code is run
    # list_all_items()
    #
    # user_value = user_input("Please Enter a value:")
    # print(user_value)

# test()
