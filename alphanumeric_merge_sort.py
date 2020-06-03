def mergeSort(numericList):
	n = len(numericList)
	middle = int(n / 2)

	if n == 1:
		return numericList
	
	left = numericList[:middle]
	right = numericList[middle:]

	left = mergeSort(left)
	right = mergeSort(right)

	return merge(left, right)


def merge(left, right):
	sort = []
	
	while len(left) > 0 and len(right) > 0:
		if(compareAlphanumeric(left[0], right[0]) == 1):
			sort.append(right[0])
			right.remove(right[0])
		else:
			sort.append(left[0])
			left.remove(left[0])

	while len(left) > 0:
		sort.append(left[0])
		left.remove(left[0])

	while len(right) > 0:
		sort.append(right[0])
		right.remove(right[0])

	return sort

def compareAlphanumeric(first, second):
	#  1 : The firstPhase is greather that secondPhase
	# -1 : The firstPhase is less that secondPhase
	#  0 : The firstPhase is equals to secondPhase

	firstPhase = str(first)
	secondPhase = str(second)

	if (len(firstPhase) < len(secondPhase)):
		length = len(firstPhase)
	else:
		length = len(secondPhase)

	for index in range(length):
		charOfFirstPhase = ord(firstPhase[index])
		charOfSecondPhase = ord(secondPhase[index])

		if (charOfFirstPhase > charOfSecondPhase):
			return 1
		elif (charOfFirstPhase < charOfSecondPhase):
			return -1
		else:
			continue


	if (len(firstPhase) > len(secondPhase)):
		return 1
	elif (len(firstPhase) < len(secondPhase)):
		return -1
	else:
		return 0

# Examples
print("" + str(mergeSort(["ABC1", "ABC001", "01", "0", "Zzz", "zzz"])))
print("" + str(mergeSort(["4","3","2","1","0"])))
print("" + str(mergeSort([4,3,2,1,0])))