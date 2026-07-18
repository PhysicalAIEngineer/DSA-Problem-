# Brute Force & Optimal Code
class Solution:
    def __init__(self):
        # words for numbers from 0 to 9
        self.below_ten = {0: "",1: "One",2: "Two",3: "Three",4: "Four",
                        5: "Five",6: "Six",7: "Seven",8: "Eight",9: "Nine"}

        # words for numbers from 10 to 19
        self.below_twenty = {10: "Ten",11: "Eleven",12: "Twelve",
                            13: "Thirteen",14: "Fourteen",15: "Fifteen",16: "Sixteen",17: "Seventeen",18: "Eighteen",19: "Nineteen"}
        # words for multiples of ten (20, 30, 40, ... 90)
        self.below_hundred = {1: "Ten",2: "Twenty",3: "Thirty",4:   "Forty",5: "Fifty",6: "Sixty",7: "Seventy",8: "Eighty",9: "Ninety"}
    # recursive function to convert a number into words
    def solve(self, num: int) -> str:
        # case 1: numbers from 0 to 9
        if num < 10:
            return self.below_ten[num]
        # case 2: numbers from 10 to 19
        if num < 20:
            return self.below_twenty[num]
        # case 3: numbers from 20 to 99
        if num < 100:
            return (self.below_hundred[num // 10] + (" " + self.below_ten[num % 10] if num % 10 != 0 else ""))
        # case 4: numbers from 100 to 999
        if num < 1000:
            return (self.solve(num // 100) + " Hundred" + (" " + self.solve(num % 100) if num % 100 != 0 else ""))
        # case 5: numbers from 1,000 to 999,999
        if num < 1_000_000:
            return (self.solve(num // 1000) + " Thousand" + (" " + self.solve(num % 1000) if num % 1000 != 0 else ""))
        # case 6: numbers from 1,000,000 to 999,999,999
        if num < 1_000_000_000:
            return (self.solve(num // 1_000_000) + " Million" + (" " + self.solve(num % 1_000_000) if num % 1_000_000 != 0 else ""))
        # case 7: Numbers 1,000,000,000 and above
        return (self.solve(num // 1_000_000_000) + " Billion"
            + (" " + self.solve(num % 1_000_000_000) if num % 1_000_000_000 != 0 else ""))
    # main function to convert a number into English words
    def numberToWords(self, num: int) -> str:
        # special case: 0
        if num == 0:
            return "Zero"
        # convert the number recursively
        return self.solve(num)

# Time Complexity : O(N)
# Space Complexity : O(1)