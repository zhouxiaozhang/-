from __future__ import division
import os
import sys
import linecache
if __name__ == "__main__":
	if len(sys.argv) != 3:
		print "Usage: python evaluate.py inputfile goldfile"
		
	infile = "answer.txt"
	goldfile = "gold"
	count = 1
	count_right = 0
	count_split = 0
	count_gold = 0
	f = file(infile)
	for line in f:
		inlist = line.strip().decode('utf-8').split(' ')
  
		goldlist = linecache.getline(goldfile, count).strip().decode('utf-8').split(' ')
		count += 1
		count_split += len(inlist)
		count_gold += len(goldlist)
		tmp_in = inlist
		tmp_gold = goldlist 
		for key in tmp_in:
			if key in tmp_gold:
				count_right += 1
				tmp_gold.remove(key)
	f.close()
	print "count_right", count_right
	print "count_gold", count_gold
	print "count_split", count_split

	p = count_right / count_split
	r = count_right / count_gold
	F = 2 * p * r /(p + r) 
	print "p:", p
	print "r:", r
	print "F:", F

		

