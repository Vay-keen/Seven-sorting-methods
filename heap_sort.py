# -*- coding:utf-8 -*-

def min_heap_sort(input_list):
	
	def heap_adjust(input_list, parent, length):
		temp = input_list[parent]
		child=2 * parent + 1

		while child < length:
			if child+1 < length and input_list[child+1] < input_list[child]:
				child += 1
			if temp <= input_list[child]:
				break
			input_list[parent] = input_list[child]
			parent = child
			child = 2 * parent + 1
		input_list[parent] = temp

	sorted_list = input_list
	length = len(sorted_list)

	# 初始化堆
	for i in range(0, length // 2 + 1)[::-1]:
		heap_adjust(sorted_list, i, length)

	# 
	for j in range(1, length)[::-1]:
		sorted_list[j],sorted_list[0]=sorted_list[0],sorted_list[j]

		heap_adjust(sorted_list, 0, j)
		print('第%d趟排序:' % (length - j), end = '')
		print(sorted_list)

	return sorted_list

if __name__ == '__main__':
	input_list = [6, 4, 8, 9, 2, 3, 1]
	print('排序前:', input_list)
	sorted_list = min_heap_sort(input_list)
	print('排序后:', sorted_list)


