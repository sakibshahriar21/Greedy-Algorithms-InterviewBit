class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        i = 0
        
        maximum = len(A)
        _dict = {x: i for i, x in enumerate(A)}
        
        while B and i < len(A):
            j = _dict[maximum]
            if i == j:
                pass
            else:
                B -= 1
                A[i], A[j] = A[j], A[i]
                _dict[A[i]], _dict[A[j]] = _dict[A[j]], _dict[A[i]]
                
            i += 1
            maximum -= 1
            
        return A  