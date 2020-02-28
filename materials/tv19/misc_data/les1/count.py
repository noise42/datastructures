#Lezione 1

def count_v1(dna, base):
	#for var in iterable
	#an iterable is any variable whose elements can be accessed sequentially
	#it exists : iterable.__next__

	#### the notation is typical for object oriented programming es. radio.volume radio.turnOn() radio.modVolume(50)
	count = 0
	for nt in dna:
		#nt = dna.__next__
		if nt == base:
			count += 1
		if nt not in "ACTG":
			return -1
	return count

def count_v2(dna, base):
	count = 0
	for i in range(len(dna)): #[0,1,2,3,4,5,..., len(dna)]
		if dna[i] == base:
			count += 1

	return count

def count_v3(dna, base):
	count = 0
	i = 0
	while i < len(dna):
		if dna[i] == base:
			count += 1
		i+=1
	return count

#parentheses can mean (expressions), or (tuples,) - the comma distinguishes between an expression and a 1-element tuple


def count_v4(dna, base, ):
	#array -> Lists [], mutable ||  or Tuples (), immutable

	bases = list("ACGT")
	ind = "ACGT".index(base)
	result = []
	count2 = 0
	for base_nt in bases:
		for count in range(len(dna)):
			if dna[count] == base:
				count2 += 1
		result.append(count2)
		count2 = 0
	return result[ind]

def count_v5(dna, base):
	m = []
	for c in dna:
		m.append( True if c == base else False)
		##this is equivalent to:
		# if c == base:
		#	m.append(True)
		# else:
		#   m.append(False)
		## and it's called ternary operator

	return sum(m)

def count_v6(dna, base):
	return dna.count(base)

def compare_efficiency():
	import random

	def generate_string(n, alphabet='ACGT'):
		s = ""
		for i in range(n):
			s += random.choice(alphabet)
			#"ACTTTGGGA" + "A"
			#['A', 'C'] + ['A']	
		return s

	dna = generate_string(100000)

	functions = [count_v1, count_v2,
				count_v3,
				count_v4_fabio,
				count_v5,
				count_v6,]
	timings = []

	import time
	for function in functions:
		t0 = time.time()
		function(dna, 'A')
		t1 = time.time()
		timing = t1 - t0

		timings.append(timing)
	return timings

if __name__ == '__main__':
	print(compare_efficiency())











