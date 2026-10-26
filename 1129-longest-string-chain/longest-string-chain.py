# Brute Force Code & Optimal Code
class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        # store the total number of words in the input list
        n = len(words)
        # short words by their lengths in ascending orders
        words.sort(key=len)
        # create 2D memorization table with n rows and n column t[prev_index][curr_index] stores the maximum length of a chain can bulid by considering pairs starting at curr_index given that the previously slected pair is at prev_index and -1 mean that state has not been calculated yet, prev_index can also be -1 meaning no pairs has been selected
        t = [[-1] * n for _ in range(n)]
        # define helper function to check whether one word is predecessor of anther word if can insert exactly one characters anywhere in prev to obtain curr 
        def predecessor(prev, curr):
            m = len(prev)
            length_curr = len(curr)
            # predecessor must be exactly one characters shorters than its succesors if the length diffrence is not exactly 1 cannot obtain curr by inserting exactly one characters into prev
            if length_curr - m != 1:
                return False
            # use two pointer to check whether every characters in prev appears in curr in the same orders
            # i -> points to the current characters in the shorters words
            # j -> points to the current characters in the longers words
            i = 0
            j = 0
            # continue while both pointers are within their words
            while i < m and j < length_curr:
                # if the characters match have found the next chracters of prev in curr advance i to check the next characters in prev
                if prev[i] == curr[j]:
                    i += 1
                # always advance j to examine the next characters in curr if the characters did not match effectively treat curr[j] as the one extra characters inserted into prev
                j += 1
            # if i reaches m every charaters of prev has matched characters in curr in the correct order because already checked that curr in exactly one characters longers prev is valid predecessor otherwise at least one characters of prev could not be matched so return false
            return i == m
        # define recursive helper function 
        # prev_index = index of the previously selected word -1 means no word has been selected yet
        # curr_index = index of the word currently being considered 
        # lis(prev_index, curr_index) return the maximum length of valid string chian can form by considering words from curr_index onward given the previosly selected word
        def lis(prev_index, curr_index):
            # base case : if curr_index reaches n all words been considered no more words can be added so return 0
            if curr_index == n:
                return 0
            # memoization check : if prev_index is valid and have already calculated this state return its cached result this avoid recalculting the same subproblem
            if (prev_index != -1 and t[prev_index][curr_index] != -1):
                return t[prev_index][curr_index]
            # ption 1: take the current word
            # assume do not select the current word if the word can be added to the chain calculate the chain length obtained by selecting it 
            take_current_word = 0
            # select the current word if either:
            # 1. prev_index == -1 : no word has been selected yet so the current word can start new chain
            # 2. predecessor(word[prev_index], words[curr_index]) : previosly selected word is valid predecessor of the current word
            # word are sorted by length valid sucessor are considered after their shorters predessors
            if (prev_index == -1 or predecessor(words[prev_index], words[curr_index])):
                take_current_word = (1 + lis(curr_index, curr_index + 1))
            # option 2 : skip the current word
            # do not include words[curr_index] in the chain keep prev_index unchanged because the previously selected words has not chagned move to the next word and search for longers chain
            skip_current_word = lis(prev_index, curr_index + 1)
            # Find the maximum chain length
            result = max(take_current_word, skip_current_word)
            # store the result : if prev_index is valid store the better of two choices : 1. select_current_word = chain length when selecting the current word. and 2. skip_current_word = chain length when skipping the current word 
            # saving this answer avoids repeating the same computation
            if prev_index != -1:
                t[prev_index][curr_index] = result
            return result
        # start at index 0 with no previously selected word 
        # - prev_index = -1 means the first words of the chain can be any words in the list
        return lis(-1, 0)

# Time Complexity : O(N^2)
# Space Complexity : O(N)