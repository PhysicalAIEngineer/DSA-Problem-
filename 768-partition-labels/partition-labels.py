# Brute Force Code & Optimal Code
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # total number of characters in the strings
        n = len(s)
        # list to store the size of each parition
        result = []
        # array to store the last occurence of every lowercase character
        last_occurence = [-1] * 26
        # record the last index of each characters
        for i in range(n):
            index = ord(s[i]) - ord('a')
            last_occurence[index] = i
        # intialize pointer
        # current_index -> current position in the strings
        current_index = 0
        # parition_start -> starting index of the current parition
        parition_start = 0
        # parition_end -> farthest index of the current parition must extend 
        parition_end = 0
        # traverse the string
        while current_index < n:
            # extend the current parition to include the last occurence of the current characters
            parition_end = max(parition_end, last_occurence[ord(s[current_index]) - ord("a")])
            # if the current index reaches the end of the parition record its size and start a new parition
            if current_index == parition_end:
                result.append(parition_end - parition_start + 1)
                # next parition starts immediately after the current parition
                parition_start = parition_end + 1
            # move to the next characters
            current_index += 1
        # return the sizes of all parition
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)