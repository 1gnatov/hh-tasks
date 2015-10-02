# -*- coding: utf-8 -*-

	# '''
	# написать функцию, которая берет n, k, с, делает равномерный массив из k элементов (вида 3, 3, 3, 3, 4)
	# далее использует функцию, разамазывающую первый ряд по массиву (получается 1, 4, 4, 4, 4), запоминает число размазываний в C = 2
	# и в дальнейшем использует функцию опять с n-1, k-1 и C из предыдущего. Когда n=1 или k=1 все заканчиваем и возвращаем C

	# TODO:
	# создание равномерного массива 
	# функция "размазывания"
	# основная функция
	# '''

def calcIntegerExactlyKPartition(n, k, c=0):

	def creatingFlatArray(n, k):
		# '''
		# делим n на к, заполняем результатом массив из к элементов, остатки обратным -фор добавляем по еденичке к последним элементам массива
		# [3, 3, 4, 4] n=14 k=4
		# '''
		flatnumber = n//k
		remainder = n%k
		a = [flatnumber for i in range(k)] 
		if remainder:
			for i in range(1, remainder+1):
				a[-i] += 1
		return a
	#print(creatingFlatArray(14, 4))

	def spreadingFirstOrder(a):
		# '''
		# [3, 3, 4, 4]
		# ->
		# [1, 4, 4, 5]
		# нужно стартовое положение если не полностью изоморфный массив
		# '''
		counter = 0
		if len(a) >= 2:
			numberToSpread = a[0]-1
			#print(numberToSpread)
			a[0] = 1


			while numberToSpread > 0:
				# '''случай когда не все цифры одинаковые'''
				if min(a[1:]) != max(a[1:]):
					#print(a)
					# '''находим крайне левое положение'''
					maxindex = a.index(max(a))
					for i in range(len(a)-maxindex+1, len(a)):
						# print(i, 'i', maxindex)
						# print(a)
						if numberToSpread >= 1:
							a[-i] += 1
							counter += 1
							numberToSpread -=1

				maxindex = a.index(max(a))
				for i in range(maxindex, len(a)):
					#print(i,'i inside while')
					if min(a[1:]) != max(a[1:]):
					#print(a)
						maxindex = a.index(max(a))
						for i in range(len(a)-maxindex+1, len(a)):
							#print(i, 'i')
							if numberToSpread >= 1:
								a[-i] += 1
								counter += 1
								numberToSpread -=1	
					if numberToSpread >= 1:
						a[-i] += 1
						counter += 1
						numberToSpread -=1
		return (a, counter)
	# print(spreadingFirstOrder([3, 3, 4, 4]))
		# print(spreadingFirstOrder([4, 4, 5]))
		# print(spreadingFirstOrder([6, 6]))
		# print(spreadingFirstOrder([6, 6, 6, 6, 7, 7]))
		# print(spreadingFirstOrder([6, 6, 6, 7, 7, 7]))
		# print(spreadingFirstOrder([6, 6, 7, 7, 7, 7]))
		# print(spreadingFirstOrder([6, 6, 6, 6, 7, 7, 7, 7, 7]))
		# print(spreadingFirstOrder([10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11]))
		# print(spreadingFirstOrder([10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11]))
		# print(spreadingFirstOrder([10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11]))
		# print(spreadingFirstOrder([10, 10, 10, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11]))

	for i in range(k, 1, -1):
		#print(n, k, c)
		a = creatingFlatArray(n-(k-i), i)
		#print(a, k)
		#bprint(a)
		(aSpreadedFirstOrder, miniCounter) = spreadingFirstOrder(a)
		#print((aSpreadedFirstOrder, miniCounter))
		c += miniCounter
		#print(c)
	# ''' последний случай со всеми еденичками кроме последнего разряда '''
	c += 1
	return c


if __name__ == "__main__":
	# print(calcIntegerExactlyKPartition(6, 3))
	# print(calcIntegerExactlyKPartition(150, 100))

	import sys

	#input.txt
	# 6 3
	# 150 100
	if len(sys.argv) == 3:
		#inttokpartition.py 150 100
		if sys.argv[1] != '-f':
			print(calcIntegerExactlyKPartition(int(sys.argv[1]), int(sys.argv[2])))
		else:
			#inttokpartition.py -f input.txt
			from fileinput import fileToListOfIntFl
			data = fileToListOfIntFl(sys.argv[2])
			for ele in data:
				print(calcIntegerExactlyKPartition(ele[0], ele[1]))
				#