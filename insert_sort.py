'''

README

This module aims to introduce the popular sorting method--direct insert sort
and three different kinds of implementation schemes are conducted by python 3 language.


'''

# -*- coding:utf-8 -*-

import math
import copy as cp

class InsertSortMethod():
	# construction method
	def __init__(self, array):
		self.array=array

	# the original method that insert the number to the proper position of sorted subset one by one
	def insert_sort1(self):
		array=cp.deepcopy(self.array)
		n=len(array)
		for i in range(n-1):
			# firstly, array[0] is the sorted subset
			if array[i+1]<array[i]:
				temp=array[i+1]
				j=i;
				while j>=0:
					if array[j]>temp:
						array[j+1]=array[j]
						j=j-1
					else:
						break
				array[j+1]=temp
		return array

	# set a tag when each swapping operation occurs
	def insert_sort2(self):
		array=self.array[:]
		n=len(array)
		for i in range(n-1):
			# firstly, array[0] is the sorted subset
			if array[i+1]<array[i]:
				j=i
				while j>=0:
					if array[j]>array[j+1]:
						# swap operation
						temp=array[j]
						array[j]=array[j+1]
						array[j+1]=temp
						j=j-1
					else:
						break
		return array

	
if __name__=='__main__':

	testlist=[2,5,7,1,9,4,6,0,12,35,7,3,30]
	insert=InsertSortMethod(testlist)  # new object of InsertSortMethod class
	sortlist=insert.insert_sort1()
	print(sortlist)
	print(insert.array)
	sortlist=insert.insert_sort2()
	print(sortlist)
	print(insert.array)
	




