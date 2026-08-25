# Brute Force Code & Optimal Code
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # dictionary to store the frequency of every number in the array
        mp = {}
        # count how many times each number appears
        for x in arr:
            # if x already exists in the dictionary increase its frequncy by 1 otherwise start its frequency from 0 and add 1
            mp[x] = mp.get(x, 0) + 1
        # set to store frequencies that have been seen set is used because it does not allow duplicates
        st = set()
        # check the frequency of every distinct numbers
        for x in mp:
            # get the frequency of the current numbers
            freq = mp[x]
            # if this frequency already exists in the set then two diffrent numbers have the same number of occurences therefore occurence are not unique
            if freq in st:
                return False
            # store the current frequency so that can detect it if another number has the same frequncy
            st.add(freq)
        # no duplicate frequency was found therefore every number has a unique number of occurence
        return True

# Time Complexity : O(N)
# Space Complexity : O(N) 