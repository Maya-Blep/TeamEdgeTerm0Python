#********************************************************************
 #                                                                 
 #  Team Edge List Mini-project: THE SHOPPING LIST HELPER
 # 
 #  This project prompts users using input() to prompt users
 #  to add (or remove) items from a shopping list. It starts empty
 #  and each time the program is run it asks you to either add or 
 #  remove an item from the list. It also updates the user of its
 #  contents. The shopping list also checks to see if an item 
 #  is already present in the list and prevents you from adding it
 #  again, giving feedback along the way. 
 # 
 # ***************************************************************/

active = True
shopping_list=[]
print("Welcome to Shopping List! 🌟")

welcome_message = "Hi! I'm your shopping assistant, Maya! Let me take your order. 😚 \n You can type 'add milk' to add milk to your shopping list. \n or you can type 'remove milk' to remove it. \n"

print(welcome_message)


#-->Todo: declare a shopping_list list


def prompt_user():
    
    reply = input("What do you want to add or remove? 🥰 >>  ")

    return reply


def check_answer(ans):
    input = ans.split()
    if input[0] == "add":
        add_item(input[1])
    elif input[0] == "remove":
        remove_item(input[1])
#fprint(ans)

#this function can take in a string and store it in an array

def add_item(item): 
    shopping_list.append(item)

def remove_item(item):
    shopping_list.remove(item)

while active:

    check_answer(prompt_user()) 
    print(shopping_list)

#this makes the program continously prompt and check response while the boolean 'active' returns True
