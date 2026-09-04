# Brute Force Code & Optimal Code
class Solution: 
    def lengthAfterTransformations(self, s, t): 
        # modulo value to keep numbers within a manageable range
        M = 10**9 + 7 
        # store the length of the original string
        n = len(s) 
        # frequency of each character index 0 = 'a', 1 = 'b', ..., 25 = 'z'
        mp = [0] * 26 
        # count how many times each character appears in s
        for ch in s: 
            mp[ord(ch) - ord('a')] += 1 
        # perform the transformation t times
        for count in range(1, t + 1): 
            # temporary frequency array for the next transformation
            temp = [0] * 26 
            # process all 26 characters
            for i in range(26): 
                # get the frequency of the current character
                freq = mp[i] 
                # For characters 'a' to 'y'
                if i != 25: 
                    # move the current frequency to the next character
                    temp[i + 1] = (temp[i + 1] + freq) % M 
                else: 
                    # add the frequency of z to both a and b
                    temp[0] = (temp[0] + freq) % M 
                    temp[1] = (temp[1] + freq) % M 
            # temporary array becomes the frequency array for the next transformation
            mp = temp 
        # calculate the final length by adding frequencies of all 26 characters
        result = 0 
        for i in range(26): 
            result = (result + mp[i]) % M 
        # Return the final length after t transformations
        return result

# Time Complexity : O(N)
# Space Complexity : O(N)