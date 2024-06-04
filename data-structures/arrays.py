############## Exercise One ###############
print("")
print("############ Answers to Exercise One ################")
print("")

# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

exp = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print("In Feb " + str(exp[1]-exp[0]) +
      " dollars more was spent, compared to January.")

# 2. Find out your total expense in first quarter (first three months) of the year.
print("In the first quarter " +
      str(sum(exp[:3])) + " dollars was spent.")

# 3. Find out if you spent exactly 2000 dollars in any month.
if 2000 in exp:
    print("yes, exactly 2000 was spent in a month.")
else:
    print("No, exactly 2000 wasn't spent in a month.")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.insert(len(exp), 1980)
print(exp)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3] -= 200
print(exp)



############### Exercise Two ################
print("")
print("############ Answers to Exercise Two ################")
print("")

# You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']

# Using this find out,

# 1. Length of the list
print(f"The length of the list is {str(len(heros))}" )

# 2. Add 'black panther' at the end of this list
heros.append("black panther")
print(heros)

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.remove("black panther")
heros.insert(3, "black panther")
print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]=['doctor strange']
print(heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)


############ Exercise Three ###########
print("")
print("############ Answers to Exercise Three ################")
print("")

# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
odd = []
max_num = input("Enter max number: ")
for num in range(int(max_num)):
    if num % 2 != 0:
        odd.append(num)
print(odd)