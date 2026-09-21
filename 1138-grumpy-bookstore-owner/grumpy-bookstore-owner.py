# Brute Force Code & Optimal code
class Solution: 
    def maxSatisfied(self, customers, grumpy, minutes): 
        # length of the array
        n = len(customers) 
        # dtore unsatisfied customers in current window
        unsatisfied = 0 
        # Calculate unsatisfied customers
        # in the first minutes window
        for i in range(minutes): 
            unsatisfied += customers[i] * grumpy[i] 
        # assume first window gives maximum unsatisfied customers that can be saved
        maxunsatisfied = unsatisfied 
        # sliding window of size minutes
        i = 0 
        j = minutes 
        while j < n: 
            # add customers from the new position if the owner is grumpy
            unsatisfied += customers[j] * grumpy[j]      
            # remove customers from the old position
            unsatisfied -= customers[i] * grumpy[i]     
            # Store maximum customers that can be saved
            maxunsatisfied = max(maxUnsat, unsat)       
            # move window forward
            i += 1 
            j += 1 
        # start with maximum customers that can be made satisfied using the secret technique
        totalcustomers = maxunsatisfied 
        # add customers who are already satisfied because grumpy[i] == 0
        for i in range(n): 
            totalCustomers += customers[i] * (1 - grumpy[i]) 
        # return maximum satisfied customers
        return totalCustomersclass 
    def maxSatisfied(self, customers, grumpy, minutes): 
        # length of the array
        n = len(customers) 
        # store unsatisfied customers in current window
        unsatisfied = 0 
        # calculate unsatisfied customers in the first 'minutes' window
        for i in range(minutes): 
            unsatisfied += customers[i] * grumpy[i] 
        # assume first window gives maximum unsatisfied customers that can be saved
        maxunsatisfied = unsatisfied 
        # sliding window of size minutes
        i = 0 
        j = minutes 
        while j < n: 
            # add customers from the new position if the owner is grumpy
            unsatisfied += customers[j] * grumpy[j]      
            # remove customers from the old position
            unsatisfied -= customers[i] * grumpy[i]      
            # store maximum customers that can be saved
            maxunsatisfied = max(maxunsatisfied, unsatisfied)        
            # move window forward
            i += 1 
            j += 1 
        # start with maximum customers that can be made satisfied using the secret technique
        totalcustomers = maxunsatisfied 
        # add customers who are already satisfied because grumpy[i] == 0
        for i in range(n): 
            totalcustomers += customers[i] * (1 - grumpy[i]) 
        # return maximum satisfied customers
        return totalcustomers