import math
import copy as cp


	
def shell_sort(array):
	n=len(array)
	gap=n//2
	while gap>0:
		i=gap
		while i<n:
			if array[i]<array[i-gap]:
				j=i-gap
				while j>=0:
					if array[j]>array[j+gap]:
						# swap operation
						array[j],array[j+gap]=array[j+gap],array[j]
						j=j-gap
					else:
						break
			i=i+1
		gap=gap//2

	
if __name__=='__main__':

	testlist=[2,5,7,1,9,4,6,0,12,35,7,3,30]
	shell_sort(testlist)  
	print(testlist)

	




