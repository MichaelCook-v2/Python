# Coin Counter

# coins = 0
# want = "yes"
# while want == "yes"
#     print(f"You have {coins} coins")
#     coins += 1
#     print(input(f"Do you want a coin")
#     want= input("Do you want another?").strip()
    
    
# print(ok)

number = 0
print(f"You have {number} coins.")
while (True):
    yesorno = input("Do you want another, yes or no?").lower()
    if yesorno == "yes":
        number += 1
        print(f"You have {number} coins.")
    elif (yesorno == "no"):
        break
    else:
        print("Invalid Input")
print("Bye")