# Brute Force Code & Optimal Code
class Solution:
    def applyMessageEvent(self, event, mentionCount, offlineTime):
        # extract the timestamp of the current message event.
        timestamp = int(event[1])
        # extract the message content and split it into individual ids or keywords separated by whitespace
        ids = event[2].split()
        # process every ID or keyword mentioned in the message a single message can contain multiple mentions.
        for id in ids:
            # case 1: all
            # if the keyword is "ALL", every user receives one additional mention. this applies regardless of whether a user is currently online or offline.
            if id == "ALL":
                # traverse all users the length of mentionCount represents the total number of users.
                for i in range(len(mentionCount)):
                    # increase the mention count of user i by one.
                    mentionCount[i] += 1
            # case 2: HERE
            # if the keyword is "HERE", only users who are currently online receive an additional mention.
            elif id == "HERE":
                # check the online/offline status of every user.
                for i in range(len(mentionCount)):
                    # user is considered online if either:
                    # 1. offlineTime[i] == 0: user has never gone offline.
                    # 2. offlineTime[i] + 60 <= timestamp: at least 60 time units have passed since the user went offline therefore, the user has automatically come back online after 60 time units if either condition is true, the user should receive a HERE mention.
                    if offlineTime[i] == 0 or offlineTime[i] + 60 <= timestamp:
                        # increase the mention count of the currently online user by one.
                        mentionCount[i] += 1
            # case 3: Specific user ID (for example: id0, id1, id2).
            # if the token is neither ALL nor HERE it represents a specific user ID.
            else:
                # extract the numeric part of the user ID.
                # id[2:] removes the first two characters ("id").
                user_id = int(id[2:])
                # increase the mention count of the specified user a specific user mention is counted regardles of whether that user is currently online or offline.
                mentionCount[user_id] += 1
    def countMentions(self, numberOfUsers: int, events: list[list[str]]) -> list[int]:
        # initialize the mention count of every user to zero numberOfUsers represents the total number of users each index represents a user:
        # 1. mentionCount[0] = mentions received by user 0.
        # 2. mentionCount[1] = mentions received by user 1.
        # 3. mentionCount[2] = mentions received by user 2.
        # initially, no user has received any mentions.
        mentionCount = [0] * numberOfUsers
        # store the timestamp when each user most recently went offline initially, all users are online use 0 to indicate that a user has never gone offline.
        offlineTime = [0] * numberOfUsers
        # sort all events in chronological order events may not be provided in timestamp order therefore, sorting is necessary before simulation.
        events.sort(key=lambda event: (int(event[1]), 0 if event[0] == "OFFLINE"
        else 1))
        # process all events in the sorted chronological order.
        for event in events:
            # case 1: The current event is a MESSAGE event.
            if event[0] == "MESSAGE":
                # call the helper function to process the message.
                # Pass:
                # event        = current MESSAGE event.
                # mentionCount = current mention counts of all users.
                # offlineTime  = last offline timestamp of every user.
                # helper function updates mentionCount directly.
                self.applyMessageEvent(event, mentionCount, offlineTime)
            # case 2: The current event is an OFFLINE event.
            elif event[0] == "OFFLINE":
                # extract the timestamp when the user goes offline.
                # event[1] contains the timestamp as a string so convert it into an integer.
                timestamp = int(event[1])
                # extract the user ID from the event.
                # For an OFFLINE event: event[2] contains the numeric user ID as a string.
                user_id = int(event[2])
                # record the timestamp when this user went offline this timestamp is used later to determine whether the user has automatically returned online the user becomes online again when: offlineTime[user_id] + 60 <= current_timestamp
                offlineTime[user_id] = timestamp
        # after processing all events, return the final mention counts each position in the result represents the total number of mentions received by the corresponding user.
        return mentionCount


# Time Complexity : O(N)
# Space Complexity : O(N)