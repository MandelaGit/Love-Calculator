# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lower = name1.lower()
name2_lower = name2.lower()

#Could have been less bulky had I combined the string earlier
#combined_name = name1 + name2

t_occurs = name1_lower.count("t") + name2_lower.count("t")
print(f"T occurs {t_occurs} times")
r_occurs = name1_lower.count("r") + name2_lower.count("r")
print(f"R occurs {r_occurs} times")
u_occurs = name1_lower.count("u") + name2_lower.count("u")
print(f"U occurs {u_occurs} times")
e_occurs = name1_lower.count("e") + name2_lower.count("e")
print(f"E occurs {e_occurs} times")
True_total = t_occurs + r_occurs + u_occurs + e_occurs
print(f"Total = {True_total}")

l_occurs = name1_lower.count("l") + name2_lower.count("l")
print(f"L occurs {l_occurs} times")
o_occurs = name1_lower.count("o") + name2_lower.count("o")
print(f"O occurs {o_occurs} times")
v_occurs = name1_lower.count("v") + name2_lower.count("v")
print(f"V occurs {v_occurs} times")
ee_occurs = name1_lower.count("e") + name2_lower.count("e")
print(f"E occurs {ee_occurs} times")
Love_total = l_occurs + o_occurs + v_occurs + ee_occurs
print(f"Total = {Love_total}")

true_conversion = str(True_total)
love_conversion = str(Love_total)

love_score = true_conversion + love_conversion

print("Love Score = " + love_score)
print("Your score is " + love_score)

if int(love_score) < 10 or int(love_score) > 90:
    print("Your score is " +love_score+ ", you go together like coke and mentos.")

elif int(love_score) <=50 and int(love_score) >=40:
    print("Your score is " +love_score+ ", you are alright together.")

else:
    print("Your score is " + love_score+ ".")



