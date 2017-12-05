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
					(WATER, ZEBRA)
 
					for (red,green,ivory,yellow,blue) in orderings

					for (Englishman,Spanish,Ukrainian,Japanese,Norwegian) in orderings


					for (dog,snails, fox, horse, ZEBRA) in orderings

					for (coffee, tea, milk, rum, WATER) in orderings
					

					for (Metal, Classical, Rock, Country, Pop) in orderings
"""					if after(green,ivory)# is green after ivory?
					if Spanish is dog #
					if milk is 3 #
					if coffee is green#
					if Ukrainian is tea #
					if Englishman is red#
					if Norwegian is 1 #
					if nextto(Norwegian,blue) #
					if Metal is snails	#				
					if Classical is yellow					
					if nextto(Rock, fox)#
					if nextto(Classical, horse)#
					if Country is rum #
					if Japanese is Pop # """
					]
	return solution
t0=time.time()
print(zebra_puzzle())
t1=time.time()
print(str(t1-t0) + "s")
