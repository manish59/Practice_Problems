def merge(left,right):
	left_index=0
	right_index=0
	sorted_array=[]
	while left_index<len(left) and right_index<len(right):
		if left[left_index]<=right[right_index]:
				sorted_array.append(left[left_index])
				left_index=left_index+1
		else:
			sorted_array.append(right[right_index])
			right_index=right_index+1
	print("Sorted Array")
	print(sorted_array)
	print("Left Exteding Array",left)
	sorted_array.extend(left[left_index:])
	print("Right Exteding Array",right)
	sorted_array.extend(right[right_index:])
	print("Extended Arrary:",sorted_array)
	return sorted_array
				
def mergesort(array):
	if len(array)<=1:
		return array
	mid=(len(array)/2)
	print("left:",array[:mid])
	print("Right:",array[mid:])
	left,right=mergesort(array[:mid]),mergesort(array[mid:])
	#print(left,right)
	return merge(left,right)
print(mergesort([1,2,-1,32,12,43,423,23523,2342,4345,345,534,53,3,45345,3453]))