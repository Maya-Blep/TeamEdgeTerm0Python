

# -------------------------------------------- 

	# You've just learned about variables, conditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you get the bill. 

	# How do you think restaurants automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you eat out, you have the option to order one or multiple items.
	# What kind of items are available to order? There's usually a menu.
	# Allow your user to order a drink, meal, and dessert.

	# At the end of the order, the receipt comes and you have to calculate the total cost:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a receipt with:
        #1. the items you ordered and their cost 
	#2. a total for your order before tax
	#3. a total for your order after tax
	#4. the amount of your tip 
	#5. the total including tax and tip

# -------------------------------------------- 


# -------------------------------------------- 

# Part 1:
# Let's start by creating the variables we'll need to keep track of the user's order
# as well as TAX and tip

# Remember: Your user should be able to order at least 3 items (a drink, meal, and dessert item). 

# --------------------------------------------

#Maya's Bubbling Boba:
#Matcha Boba Milk Tea: 5.25
#Strawberry Boba Milk: 5.25
#Brown Sugar Boba Milk: 5.05
#Taro Boba Milk Tea: 5.25
#California Rolls: 4.15
#Tuna Nigiri: 4.10
#Shrimp Onigiri: 4.30
#Orange Chicken: 3.45
#Rice: 3.40
#Black Bean Noodles: 4.10
#Rainbow Crepe Cake Slice: 5.99 
#Chocolate Filled Churro: 4.25
#Strawberry Shortcake Slice: 5.99
#Macarons: 4.25
#Ice Cream: 3.05

from socket import if_nameindex


food_price = 0
drink_price = 0
food_price2 = 0
food_price3 = 0
food_price4 = 0



# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------


print("MENU")
print("Drinks")
print("♡~~~~~~~~~~♡")

print("1. Matcha Boba Milk Tea 🧋 $5.25")
print("2. Strawberry Boba Milk 🧋 $5.25")
print("3. Brown Sugar Boba Milk 🧋 $5.05")
print("4. Taro Boba Milk Tea 🧋 $5.25")
print("Meals")
print("♡~~~~~~~~~~♡")
print("6. California Rolls 🍣 $4.15")
print("7. Tuna Nigiri 🍣 $4.10")
print("8. Shrimp Onigiri 🍙 $4.30")
print("9. Orange Chicken 🍗 $3.45")
print("10. Rice 🍚 $3.40")
print("11. Black Bean Noodles 🍜 $4.10")
print("Desserts")
print("♡~~~~~~~~~~♡")
print("13. Rainbow Crepe Cake Slice 🍰 $5.99")
print("14. Chocolate Filled Churro $4.25")
print("15. Strawberry  Shortcake Slice 🍰 $5.99")
print("16.  Macarons $4.25 🍪")
print("17. Ice Cream $3.05 🍦")

print("Hi! Welcome to Maya's Bubbling Boba~💜")



# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?

# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------


drink = int(input("What drink would you like to order? (Pick  1-4. If you don't wan't anything from here, type 5)"))
if drink == 1:
		print("You picked Matcha Boba Milk Tea! Matcha slayss! 😌")
elif drink == 2:
		print("You picked Strawberry Boba Milk! Yum! 😋")
elif drink == 3:
		print("You picked Brown Sugar Boba Milk! I LOVE that flavor! 💕")
elif drink == 4:
		print("You picked Taro Boba Milk Tea! Good choice! 😚")
elif drink == 5:
		print("No drink? That's okay! 👍")
else:
	print("I need a number! 😶")

if drink == 1:
	drink_price = food_price + 5.25
elif drink == 2:
	drink_price = food_price + 5.25
elif drink == 3:
	drink_price = food_price + 5.05
elif drink == 4:
	drink_price = food_price + 5.25
elif drink == 5:
	drink_price = food_price + 0.00


meal = int(input("What meal would you like to order? (Pick 6-11! If you don't want anything from here, type 12)"))
if meal == 6:
	print("You picked California Rolls! My favorite! 💖")
elif meal == 7:
	print("You picked Tuna Nigiri! I need to try that someday! 🥰")
elif meal == 8:
	print("You picked Shrimp Onigiri! I'm OBSESSED with shrimp! 😍")
elif meal == 9:
	print("You picked Orange Chicken! My dad's favorite! 👌")
elif meal == 10:
	print("You picked Rice! Just plain rice? You do you hehe. 😌")
elif meal == 11:
	print("You picked Black Bean Noodles! They're pretty messy, but its worth the purchase! 🤭")
elif meal == 12:
	print("No meal? That's okay! 👍")
else:
	print("I need a number! 😶")

if meal == 6:
	food_price2 = food_price + 4.15
elif meal == 7:
	food_price2 = food_price + 4.10
elif meal == 8:
	food_price2 = food_price + 4.30
elif meal == 9:
	food_price2 = food_price + 3.45
elif meal == 10:
	food_price2 = food_price + 3.40
elif meal == 11:
	food_price2 = food_price + 4.10
elif meal == 12:
	food_price2 = food_price + 0

dessert = int(input("What dessert would you like to order? Hope you have room for it! (Pick 13-17! If you don't want anything from here, type 18)"))
if dessert == 13:
	print("You picked Rainbow Crepe Cake slice! I've been wanting to try one! 😚")
elif dessert == 14:
	print ("You picked Chocolate Filled Churro! Churros outsold all these desserts ngl 🤩")
elif dessert == 15:
	print("You picked Strawberry Shortcake slice! Yumm 😍")
elif dessert == 16:
	print("You picked Macarons! Oui oui 😎")
elif dessert == 17:
	print("You picked Ice cream! A classic~ 😙")
elif dessert == 18:
	print("You don't want dessert? That's fine! 👍")
else:
	print("I need a number 😶")

if dessert == 13:
	food_price3 = food_price + 5.99
elif dessert == 14:
	food_price3 = food_price + 4.25
elif dessert == 15:
	food_price3 = food_price + 5.99
elif dessert == 16:
	food_price3 = food_price + 4.25
elif dessert == 17:
	food_price3 = food_price + 3.05
elif dessert == 18:
	food_price3 = food_price + 0
	
food_price4 = food_price4 + drink_price + food_price2 + food_price3






# -------------------------------------------- 

# Part 4:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of the order, including:
# - Cost of all  ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 
food_price4 = (round(food_price4 * 0.087) + food_price4) 
print(f"Your total price is {food_price4}")
tip = input("Would you like to add a tip? 😚")
if tip == "yes":
	tip = input("Okay! Would you like to tip 15%, 20%, or 35%? 🤗")
	if tip == "15%" or "15":
		food_price4 = (round(food_price4 * 0.15) + food_price4)
	elif tip == "20%" or "20":
		food_price4 = (round(food_price4 * 0.20) + food_price4)
	elif tip == "35%" or "35":
		food_price4 = (round(food_price4 * 0.35) + food_price4)
	else:
		print("Just pick these prices! 😊")

elif tip == "no":
	print("Alright! Here's your reciept 😘")













# -------------------------------------------- 

# Part 5:
# Let's print out a receipt.

# Write a function that will take the values of the order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item
# - Tax for the order
# - Tip for the order
# - Total cost for the order


# -------------------------------------------- 

print("RECEIPT")

print (f"♡ Drink: {drink_price}")

print (f"♡ Meal: {food_price2}")

print (f"♡ Dessert: {food_price3}")

print("♡~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~♡")

print (f"♡ Tip added: {tip}")

print("♡~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~♡")

print (f"♡ Full Price: {food_price4}")

print("♡~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~♡")


print("Thank you! Have a lovely day!")
# -------------------------------------------- 

# Part 6: Food Order Bot

# Call all of your functions to get your food order bot up and running!

# --------------------------------------------







# -------------------------------------------- 

# Part 7: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering valid values. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------
