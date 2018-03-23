'''

README

This module aims to introduce the popular sorting method--bubble sort
and three different kind of schemes are conducted by python 3 language.


'''

# -*- coding:utf-8 -*-

import math

class BubbleSortMethod(object):
	# construction method
	def __init__(self,array):
		self.array=array

	# the most common method, the maximum number in the array is swapped to the last position during an iteration.
	def bubble_sort1(self):
		array=self.array
		n=len(array)
		for i in range(n):
			for j in range(n-i-1):
				if array[j] > array[j+1]:
					tmp=array[j]
					array[j]=array[j+1]
					array[j+1]=tmp

		return array

	# set a tag when each swapping operation occurs
	def bubble_sort2(self):
		array=self.array
		n=len(array)
		swap_tag=True
		for i in range(n):
			if swap_tag:
				swap_tag=False
				for j in range(n-i-1):
					if array[j] > array[j+1]:
						tmp=array[j]
						array[j]=array[j+1]
						array[j+1]=tmp
						swap_tag=True  # it means that the array has't been soted completely yet
			else:
				break
		return array

	# record the position where the last swapping operation occurs during the iterations
	def bubble_sort3(self):
		array=self.array
		n=len(array)
		swap_index=n
		while swap_index>0:
			k=swap_index
			swap_index=0 # if no swapping operation occus, the loop will break
			for j in range(k-1):
				if array[j] > array[j+1]:
					tmp=array[j]
					array[j]=array[j+1]
					array[j+1]=tmp
					swap_index=j
			
		return array



if __name__=='__main__':

	testlist=[2,5,7,1,9,4,6,0,12,35,7]
	bubble=BubbleSortMethod(testlist)  # new object of BubbleSortMethod class
	sortlist=bubble.bubble_sort1()
	print(sortlist)
	sortlist=bubble.bubble_sort2()
	print(sortlist)
	sortlist=bubble.bubble_sort3()
	print(sortlist)







