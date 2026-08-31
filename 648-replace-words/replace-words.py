# Brute Force Code & Optimal Code
class Solution:
    def findRoot(self, word, st):
        # try every possible prefix of the current word start from length 1 because want to find the shortest possible root.
        for l in range(1, len(word) + 1):
            # take the first l characters of the word
            root = word[:l]
            # check whether this prefix exists in the dictionary set since check prefixes from shortest to longest, the first match is the shortest root.
            if root in st:
                return root
        # if no prefix of the word exists in the dictionary keep the original word unchanged.
        return word
    def replaceWords(self, dictionary, sentence):
        # convert the dictionary list into a set.
        st = set(dictionary)
        # split the sentence into individual words
        words = sentence.split()
        # store the final words after replacing them with their shortest roots.
        result = []
        # process every word in the sentence.
        for word in words:
            # find the shortest dictionary root for the current word.
            root = self.findRoot(word, st)
            # add the root to the result.
            result.append(root)
        # join all processed words with a single space.
        return " ".join(result)

# Time Complexity : O(N)
# Space Complexity : O(N) 