# Brute Force Code & Optimal Code
class Solution: 
    def balanced(self, num): 
        # create a frequency array for digits 0 to 9 freq[d] = how many times digit d appears
        freq = [0] * 10 
        # extract every digit from the number
        while num > 0: 
            # get the last digit
            digit = num % 10 
            # increase the frequency of this digit
            freq[digit] += 1 
            # Remove the last digit
            num //= 10  
        # check the frequency of every digit
        for d in range(10): 
            # if digit d appears in the number its frequency must be exactly d if the digit does not appear, freq[d] = 0 which is allowed.
            if freq[d] != 0 and freq[d] != d: 
                return False 
        # all digits satisfy the condition so the number is balanced
        return True 
    def nextBeautifulNumber(self, n): 
        # check every number starting from n + 1 because we need the next beautiful number
        for num in range(n + 1, 1224445): 
            # check whether the current number is balanced
            if self.balanced(num): 
                # return the first balanced number found since we check numbers in increasing order this is the smallest possible answer
                return num 
        # if no balanced number is found
        return -1

# Time Complexity : O(N)
# Space Complexity : O(N)