#Question URL: https://www.interviewbit.com/problems/interview-questions/
#Difficulty: Easy

class Solution:
	# @param A : list of integers
	# @return an integer
	def bulbs(self, A):
        value = 0
        
        for bit in A:
            
            if value % 2 == 0:
                bit = bit
            else:
                bit = not bit
                
            if bit % 2 == 1:
                continue
            else:
                value += 1
                
        return value                
                    
