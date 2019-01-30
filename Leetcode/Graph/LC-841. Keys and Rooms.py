
# There are N rooms and you start in room 0.  Each room has a distinct number in
# 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.
#
# Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an
# integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens
# the room with number v.
#
# Initially, all the rooms start locked (except for room 0).
#
# You can walk back and forth between rooms freely.
#
# Return true if and only if you can enter every room.
#
# Example 1:
#
# Input: [[1],[2],[3],[]]
# Output: true
# Explanation:
# We start in room 0, and pick up key 1.
# We then go to room 1, and pick up key 2.
# We then go to room 2, and pick up key 3.
# We then go to room 3.  Since we were able to go to every room, we return true.
#
# Example 2:
#
# Input: [[1,3],[3,0,1],[2],[0]]
# Output: false
# Explanation: We can't enter the room with number 2.
# -----------------------------------------------------------------------------

# When visiting a room for the first time, look at all the keys in that room. For
# any key that hasn't been used yet, add it to the todo list (stack) for it to be used.

# [Aditya]: So idea is run BFS iteratively. Once done then all nodes( rooms) should have
# been marked as TRUE in visited matrix. If some not is still False aka unvisited - it means
# its not possible to traverse all nodes (Rooms) with given keys of next node.
# You can also imagine it like making directed graph - room to key.

class Solution(object):

    def canVisitAllRooms(self, rooms):

        seen = [False] * len(rooms)
        seen[0] = True
        stack = [0]

        #At the beginning, we have a todo list "stack" of keys to use.
        #'seen' represents at some point we have entered this room.

        while stack:  #While we have keys...
            node = stack.pop() # get the next key 'node'
            for nei in rooms[node]: # For every key in room # 'node'...
                if not seen[nei]: # ... that hasn't been used yet
                    seen[nei] = True # mark that we've entered the room
                    stack.append(nei) # add the key to the todo list

        return all(seen) # Return true iff we've visited every room


if __name__ == '__main__':
    s = Solution()
    rooms =  [[1,3],[3,0,1],[2],[0]] # Here we cannot visit room 2

    print "\nPossible to visit all rooms ?",s.canVisitAllRooms(rooms)

# Complexity Analysis
#
#     Time Complexity: O(N+E), where N is the number of rooms, and E is
#     the total number of keys.
#
#     Space Complexity: O(N) in additional space complexity, to store
#     stack and seen.
