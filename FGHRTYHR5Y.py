horseshoe=0
print("what is the current year")
something=int(input())
if something==2021:
    print("correct")
    horseshoe=horseshoe+5
else:
    print("incorrect")
    horseshoe=horseshoe-2
print("what is the current month")
something=(input())
if something=="august":
    print("correct")
    horseshoe=horseshoe+5
    variable=variable+5
else:
    print("incorrect")
    horseshoe=horseshoe-2
    variable=variable-2
print("how many days are in a week")
something=(input())
if something=="seven":
    print("correct")
    horseshoe=horseshoe+5
    variable=variable+5
else:
    print("incorrect")
    horseshoe=horseshoe-2
    variable=variable-2
print("what day is it today")
something=(input)()
if something=="tuesday":
    print("correct")
    horseshoe=horseshoe+5
    variable=variable+5
else:
    print("incorrect")
    horseshoe=horseshoe-2
    variable=variable-2
something=something+5
print("you got" ,horseshoe,"correct")
print("you got",horseshoe,"incorrect")