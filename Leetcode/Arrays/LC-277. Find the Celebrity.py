
# Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity.
# The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.
#
# Now you want to find out who the celebrity is or verify that there is not one.
# The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?"
# to get information of whether A knows B. You need to find out the celebrity
# (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).
#
# You are given a helper function bool knows(a, b) which tells you whether A knows B.
# Implement a function int findCelebrity(n). There will be exactly one celebrity if he/she is in the party.
# Return the celebrity's label if there is a celebrity in the party. If there is no celebrity, return -1.
#
#
#
# Example 1:
#
# Input: graph = [
#   [1,1,0],
#   [0,1,0],
#   [1,1,1]
# ]
# Output: 1
# Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1 means person i knows person j, otherwise graph[i][j] = 0 means person i does not know person j. The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.
#
# Example 2:
#
# Input: graph = [
#   [1,0,1],
#   [1,1,0],
#   [0,1,1]
# ]
# Output: -1
# Explanation: There is no celebrity.

# Note:

#    The directed graph is represented as an adjacency matrix, which is an n x n matrix where a[i][j] = 1 means person i knows person j while a[i][j] = 0 means the contrary.
#    Remember that you won't have direct access to the adjacency matrix.

# #########################################################################


# Explanation

# The first loop is to exclude n - 1 labels that are not possible to be a celebrity.
# After the first loop, x is the only candidate.
# The second and third loop is to verify x is actually a celebrity by definition.
#
# The key part is the first loop. To understand this you can think the knows(a,b) as a a < b comparison,
# if a knows b then a < b, if a does not know b, a > b.
# Then if there is a celebrity, he/she must be the "maximum" of the n people.
#
# However, the "maximum" may not be the celebrity in the case of no celebrity at all.
# Thus we need the second and third loop to check if x is actually celebrity by definition.
#
# The total calls of knows is thus 3n at most. One small improvement is that in the second loop we only
# need to check i in the range [0, x). You can figure that out yourself easily.


def findCelebrity(self, n):

    x = 0
    for i in xrange(n):
        if knows(x, i): # Return true if x know i, means known-count of i > know-count of x.
            x = i

    # Verify if he is really celebrity. TWO Negative tests:
    if any(knows(x, i) for i in xrange(x)): # Means X ( which is celebrerty) knows someone (i), then he is not a celebrity - return -1, because celebrety knows no one
        return -1
    if any(not knows(i, x) for i in xrange(n)): # Means if there is someone, who doesn't know celebreity, then he is not celebreity. Because all common ppl kow celebreity
        return -1

    return x





