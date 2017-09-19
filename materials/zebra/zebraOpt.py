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
	solution=[(WATER, ZEBRA) 
					for (red,green,ivory,yellow,blue) in orderings
					if after(green,ivory)# is green after ivory?

					for (Englishman,Spanish,Ukrainian,Japanese,Norwegian) in orderings
					if Englishman is red#
					if Norwegian is 1 #
					if nextto(Norwegian,blue) #

					for (dog,snails, fox, horse, ZEBRA) in orderings
					if Spanish is dog #

					for (coffee, tea, milk, rum, WATER) in orderings
					if milk is 3 #
					if coffee is green#
					if Ukrainian is tea #

					for (Metal, Classical, Rock, Country, Pop) in orderings
					if Metal is snails	#				
					if Classical is yellow					
					if nextto(Rock, fox)#
					if nextto(Classical, horse)#
					if Country is rum #
					if Japanese is Pop #
					
					]
	return solution
t0=time.time()
print(zebra_puzzle())
t1=time.time()
print(str(t1-t0) + "s")
