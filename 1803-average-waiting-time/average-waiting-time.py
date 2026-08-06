# Brute Force Code & Optimal Code
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # total number of customers
        n = len(customers)
        # store the total waiting time of all customers
        total_wait_time = 0
        # time when the chef becomes avaliables
        current_time = 0
        # process every customer in the given arrival order
        for customer in customers:
            # arrival time of the current customers
            arrival_time = customer[0]
            # time required to prepare the order
            cook_time = customer[1]
            # if the chef is free before the customers arrives move the current time to the customers arrival time because the chef waits idle
            if current_time < arrival_time:
                current_time = arrival_time
            # finish time of the current oder : current_time + cook_time  and waiting time : finish_time - arrival_time
            wait_time = (current_time + cook_time - arrival_time)
            # add this customer waiting time to the total
            total_wait_time += wait_time
            # update the time when the chef becomes free after preparing the current order
            current_time += cook_time
        # return the average waiting time
        return total_wait_time / n

# Time Complexity : O(N)
# Space Complexity : O(1)