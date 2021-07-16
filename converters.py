user_weight=int(input("weight of user?"))
unit=input("(L)bs or (K)gs")
if unit.upper()=="L":
    converted_weight=user_weight*0.45
    print(f"you are {converted_weight} kilos")
else:
    converted_weight=user_weight/0.45
    print(f"you are {converted_weight} pounds")

    