# -*- coding:utf-8 -*-


def quick_sort(array, left, right):
	if left<right:
		mid=adjust_array(array, left, right)
		quick_sort(array, left, mid-1)
		quick_sort(array, mid+1, right)

	
def adjust_array(array, left, right):
	i=left
	j=right
	base_value=array[left]
	while i<j:
		while (i<j and array[j]>base_value):
			j=j-1
		if i<j:
			array[i]=array[j]
			i=i+1
		while ( i<j and array[i]<base_value):
			i=i+1
		if i<j:
			array[j]=array[i]
			j=j-1
	array[i]=base_value
	return i


if __name__=='__main__':

	testlist=[1,4,6,2,3,5,7,9,2,4]
	n=len(testlist)
	quick_sort(testlist,0,n-1)
	print(testlist)
	




