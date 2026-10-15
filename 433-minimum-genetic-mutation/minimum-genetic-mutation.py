# Brute Force Code & Optimal Code
class Solution:
    def minMutation(self, start: str, end: str, bank: list[str]) -> int:
        # store all valid genetic sequence in set for fast lookup
        valid_genetic_sequence = set(bank)
        # track visited genetic sequence to avoid revisiting them 
        track_visited_genetic_sequence = set()
        # create a queue for BFS
        queue = deque()
        # add the starting genetic sequence to the queue and mark it visited
        queue.append(start)
        track_visited_genetic_sequence.add(start)
        # count the number of mutations performed
        number_mutations_performed = 0
        # perfrom BFS untill the queue becomes empty
        while queue:
            # number of sequence at the current BFS level
            number_sequence = len(queue)
            # continue until number of sequence
            while number_sequence:
                # remove the front genetic sequence from the queue
                remove_front_genetic_sequence = queue.popleft()
                # if the target sequence is reached return the mutations count
                if remove_front_genetic_sequence == end:
                    return number_mutations_performed
                # try changing each characters to A, C, G or T
                for character in "ACGT":
                    # try changing every position in the current sequence
                    for i in range(len(remove_front_genetic_sequence)):
                        # create new genetic sequence by changing one characters
                        new_genetic_sequence = remove_front_genetic_sequence[:i] + character + remove_front_genetic_sequence[i + 1:]
                        # check whehter the new sequence is valid and unvisited
                        if (new_genetic_sequence not in track_visited_genetic_sequence and new_genetic_sequence in valid_genetic_sequence):
                            # mark the new sequence as visited
                            track_visited_genetic_sequence.add(new_genetic_sequence)
                            # add it to the queue for futhers explorations
                            queue.append(new_genetic_sequence)
                # process the next sequence at the current BFS level
                number_sequence -= 1
            # increase the mutations count after processing one BFS level
            number_mutations_performed += 1
        # retun -1 if the target sequence cannot be reached
        return -1   

# Time Complexity : O(N)
# Space Complexity : O(N)