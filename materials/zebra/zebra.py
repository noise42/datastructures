import itertools
import time
def imright(right,left):
	return 1==(right-left)

def nextto(A,B):
	return 1==(A-B) or 1==(B-A)

def zebra_puzzle():
	houses = first, _ , middle, _, _ = [1,2,3,4,5]
	orderings = list(itertools.permutations(houses))
	#print orderings
	solution=[(WATER, ZEBRA) 
					for (red,green,ivory,yellow,blue) in orderings
					for (Englishman,Spaniard,Ukrainian,Japanese,Norwegian) in orderings
					for (dog,snails, fox, horse, ZEBRA) in orderings
					for (coffee, tea, milk, oj, WATER) in orderings
					for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in orderings
					if Englishman is red
					if Spaniard is dog
					if coffee is green
					if Ukrainian is tea
					if imright(green,ivory)
					if OldGold is snails
					if Kools is yellow
					if milk is middle
					if Norwegian is first
					if nextto(Chesterfields, fox)
					if nextto(Kools, horse)
					if LuckyStrike is oj
					if Japanese is Parliaments
					if nextto(Norwegian,blue)
					]
	return solution

t0=time.time()
print(zebra_puzzle())
t1=time.time()
print(str(t1-t0) + " s")