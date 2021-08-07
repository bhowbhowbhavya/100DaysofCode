from IPython import get_ipython
get_ipython().magic('clear')

data = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name?")
    bid = int(input("What's your bid?"))
    data[name] = bid
    get_ipython().magic('clear')
    should_continue = input("Do you wish to continue with another user, if yes type 'yes' or type 'no'!").lower()
    if should_continue == "no":
        bidding_finished = True
    else:
        get_ipython().magic('clear')

print(data)
for i in data:
    max = 0
    value = ""
    if data[i]>max:
        max = data[i]
        value = i
        
print(f"The highest bid is by {value} with the bid as {max} dollars")         