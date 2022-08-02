class Solution:
	# @param A : list of integers
	# @param B : list of integers
	# @return an integer
	def mice(self, A, B):
		A.sort()
		B.sort()
		
		result = 0
		
		for every_single_mice, every_single_hole in zip(A, B):
			result = max(result, abs(every_single_mice - every_single_hole))
		return result