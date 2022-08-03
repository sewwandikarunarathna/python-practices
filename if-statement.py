
is_student = False

if is_student:
    print("you are a student")
else:
    print("you are not a student")

#considering two variables
is_male = True
is_tall= False

    #with or
if is_male or is_tall:
    print("You are a male or tall or both ")
else:
    print("You are neither male nor tall ")

    #with and
if is_male and is_tall:
    print("You are a tall male ")
else:
    print("You are either not male or not tall or both")

#using if else (elif)
is_male = False
is_tall= False

if is_male and is_tall:
    print("You are a tall male ")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not male and not tall")

#if with comparisons (<=>)
def max_num(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

print(max_num(2, 67, 34))