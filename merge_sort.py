# -*- coding:utf-8 -*-

import math
import copy as cp


def merge_sort(array, start, end):
	if start<end:
		mid=(start+end)//2
		merge_sort(array, start, mid)
		merge_sort(array, mid+1, end)
		merge_array(array, start, mid, end)

	
def merge_array(array, start, mid, end):
	tmp=[]
	i=start
	j=mid+1
	while (i<=mid and j<=end):
		if array[i]<array[j]:
			tmp.append(array[i])
			i=i+1
		else:
			tmp.append(array[j])
			j=j+1
	while i<=mid:
		tmp.append(array[i])
		i=i+1
	while j<=end:
		tmp.append(array[j])
		j=j+1
	index=start
	for item in tmp:
		array[index]=item
		index=index+1


if __name__=='__main__':

	testlist=[1,4,6,2,3,5,7,9,2,4]
	n=len(testlist)
	merge_sort(testlist,0,n-1)
	print(testlist)
	




