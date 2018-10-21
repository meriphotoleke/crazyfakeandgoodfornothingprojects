#Python program to display my mood based on current factors
#Author: Shashank Shekhar (meriphotoleke)
#Date: 21 October, 2018

def moodcalculator(a,b,c,d,e,f):
	#a is body health
	#b is mental condition
	#c is work pressure
	#d is peer pressure
	#e is motivation level
	#f is previous history of mood
	#Weightage of a is: 1
	#Weightage of b is: 2
	#Weightage of c is: 2
	#Weightage of d is: 1.5
	#Weightage of e is: 1.5
	#Weightage of f is: 3
	return (((a)*(b**2)*(e**(1.5))*(f**3))/((d**(1.5))*(c**(2))))

def healthpressuremotivationandmoodhistory(s):
	if((s>0) and (s<4)):
		a=10
	elif((s>3) and (s<8)):
		a=5
	else:
		a=1
	return a
	
def mentalcondition(t):
	if(t==1):
		b=10
	else:
		b=1
	return b

a=int(input("Enter your body health from a scale of 1-10:\n"))
a=healthpressuremotivationandmoodhistory(a)
b=int(input("Did you suffer from mental illness? Enter 1 for yes and 0 for no!\n"))
b=mentalcondition(b)
c=int(input("Enter your work pressure level from 1-10:\n"))
c=healthpressuremotivationandmoodhistory(c)
d=int(input("Enter your peer pressure level from 1-10:\n"))
d=healthpressuremotivationandmoodhistory(d)
e=int(input("Enter your motivation level from 1-10:\n"))
e=healthpressuremotivationandmoodhistory(e)
f=int(input("Enter your previous mood history from 1-10:\n"))
f=healthpressuremotivationandmoodhistory(f)
score=moodcalculator(a,b,c,d,e,f)
pscore=(0.00031622776601683794/score)*100
print("You score:")
print(pscore)
print("Yes, mood is exponential. Apologies.")