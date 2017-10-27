import itertools
import time

def after(right,left):
	return 1==(right-left)

def nextto(A,B):
	return 1==(A-B) or 1==(B-A)

def zebra_puzzle():
	houses = first, _ , middle, _, _ = [1,2,3,4,5]
	orderings = list(itertools.permutations(houses))
	#print orderings
	solution=[
					print((Metal, Classical, Rock, Country, Pop))
 
					for (red,green,ivory,yellow,blue) in orderings

					for (Englishman,Spanish,Ukrainian,Japanese,Norwegian) in orderings


					for (dog,snails, fox, horse, ZEBRA) in orderings

					for (coffee, tea, milk, rum, WATER) in orderings
					

					for (Metal, Classical, Rock, Country, Pop) in orderings
					]
	return solution
t0=time.time()
print(zebra_puzzle())
t1=time.time()
print(str(t1-t0) + "s")
