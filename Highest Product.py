#Question URL: https://www.interviewbit.com/problems/highest-product/
#Difficulty: Easy

class Solution:
	# @param A : list of integers
	# @return an integer
	def maxp3(self, A):
        
        A = sorted(A)
        
        highest_3 = A[-3] * A[-2] * A[-1]
        
        lowest_2_highest_1 = A[0] * A[1] *A[-1]
        
        return max(highest_3, lowest_2_highest_1)