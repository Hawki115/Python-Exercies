#Exercise Logical Operators
is_magician = True
is_expert = True
#check if magician AND expert: "You are a master magician"

# check if magician but not expert: "at least youre getting there"

#if youre not magician:"You need magic powers."

if is_magician and is_expert:
    print("You are a master magician")

elif is_magician and (not is_expert):
    print("at least youre getting there")
    
else:
    print ("You need magic powers.")
