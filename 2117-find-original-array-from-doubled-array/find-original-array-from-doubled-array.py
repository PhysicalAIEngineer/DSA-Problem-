# Optimal Code
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        # total number of elements
        n = len(changed)
        # valid doubled array must have an even number of elements
        if n % 2 != 0:
            return []
        # sort the array so that smaller number are processed first
        changed.sort()
        # dictionary to map : number -> frequency
        mp = {}
        # count the frequency of evey number
        for num in changed:
            mp[num] = mp.get(num, 0)  + 1
        # store the reconstruted original array
        result = []
        # process the number in sorted orders
        for num in changed:
            # double of the current number
            twice = 2 * num
            # skip number that have already been paired
            if mp[num] == 0:
                continue
            # if the double does not exist or has already been used the array is invalid
            if twice not in mp or mp[twice] == 0:
                return []
            # add the current number to the original array
            result.append(num)
            # use one occurence of the number and its double
            mp[num] -= 1
            mp[twice] -= 1
        # return the recoverd original array
        return result 

# Time Complexity : O(Nlog)
# Space Complexity : O(N)
        