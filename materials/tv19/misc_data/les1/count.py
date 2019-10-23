#Lezione 1

def count_v1(dna, base):
	#for var in iterable
	#un iterabile è una qualunque variabile da cui è possibile
	#accedere ai suoi elementi in sequenza (iterable.__next__)

	#### es. radio.volume radio.turnOn() radio.modVolume(50)
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

### if (a) and (b or c) or (1,2,3) == (t,h,l)
###tupla a singolo elemento: (var, ) -- trailing comma

def count_v4_fabio(dna, base, ):
	#array -> Lists [], mutable ||  or Tuples (), immutable

	bases = list("ACGT")
	ind = "ACGT".index(base)
	result = []
	count = 0
	count2 = 0
	for base_nt in bases:
		if dna[count2] == base_nt:
			count += 1
		result.append(count)
		count = 0
	return result[ind]

def count_v5(dna, base):
	m = []
	for c in dna:
		m.append( True if c == base else False)
		# if c == base:
		#	m.append(True)
		# else:
		#   m.append(False)
		##guardatevi l'operatore ternario in C

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











