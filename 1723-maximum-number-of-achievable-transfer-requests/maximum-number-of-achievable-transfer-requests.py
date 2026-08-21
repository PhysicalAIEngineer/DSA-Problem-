# Brute Force Code & Optimal Code
class Solution:
    def __init__(self):
        # store the total number of requests.
        self.m = 0
        # store the maximum number of accepted requents from all valid combination found so far intially no valid combination has been found so use negative infinity
        self.result = float("-inf")
    def solve(self, idx, count,n, resultant, requests):
        # base case : if all requests have been considered check whether the current selection of reqests is valid
        if idx == self.m:
            # assume every buliding is balanced when the number of people entering it equal to the number of people leaving it
            allZero = True
            # check the net change of every buliding
            for x in resultant:
                # if any buliding has non zero net change the selected requents are invalid
                if x != 0:
                    allZero = False
                    break
            # if every buliding has net change 0, this is a valid combination of requensts
            if allZero:
                # keep the maximum number of accepted requests found so far.
                self.result = max(self.result, count)
            return
        # get the current request from_buliding -> building where the person currently is and to -> builiding where the person wants to go
        from_building = requests[idx][0]
        to = requests[idx][1]
        # option 1: accept the current request one person leaves the source buliding therefore its number of people decreased by 1
        resultant[from_building] -= 1
        # one person enter the destination building therfore its number of people increases by 1
        resultant[to] += 1
        # recusively process the next request since accepted this request, increase the accpeted request count by 1
        self.solve(idx + 1, count + 1, n, resultant, requests)
        # backtracking undo the changes caused by accpecting the current request restore the source buidling
        resultant[from_building] += 1
        # restore the destination buliding
        resultant[to] -= 1
        # option 2: reject the current request do not modify resultant because the request is not accepted simply move the next request
        self.solve(idx + 1, count, n, resultant, requests)
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        # store the total number of requests.
        self.m = len(requests)
        # # resultant[i] stores the net changes in the number of people at buliding i 
        # 1. positive value --> more people enterted
        # 2. negative value --> more people left
        # 3. zero --> balanced
        resultant = [0] * n
        # start considering requensts from index 0 initially count = 0 no requests have been accepted
        self.solve(0,0,n,resultant,requests)
        # Return the maximum number of requests that can be accepted while keeping every building balanced.
        return self.result

# Time Complexity : O(N)
# Space Complexity : O(N)