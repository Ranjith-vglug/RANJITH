b=[]
c=[]
def alp_check(user_input):
	for ch in user_input:
		if  ch.isupper():
			b.append(ch)
		else:
			c.append(ch)
		

user_input=input("enter the string ")
alp_check(user_input)
print("upper case from user:",b,len(b))
print(" lower case from user:",c,len(c))