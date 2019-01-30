
# Given a list accounts, each element accounts[i] is a list of strings, where the first
# element accounts[i][0] is a name, and the rest of the elements are emails representing
# emails of the account.
#
# Now, we would like to merge these accounts. Two accounts definitely belong to the same
# person if there is some email that is common to both accounts. Note that even if two
# accounts have the same name, they may belong to different people as people could have
# the same name. A person can have any number of accounts initially, but all of their
# accounts definitely have the same name.
#
# After merging the accounts, return the accounts in the following format: the first
# element
# of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
#
# Example 1:
#
# Input:
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# Explanation:
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
#
# Note:
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].
# ====================================================================================================

# Intuition
#
# Draw an edge between two emails if they occur in the same account. The problem comes down to
# finding connected components of this graph. Yep Got it.
#
# Algorithm
#
# For each account, draw the edge from the first email to all other emails. Additionally, we'll
# remember a map from emails to names on the side. After finding each connected component using
# a depth-first search, we'll add that to our answer.


# Basically this is problem of connected Components - where we append different components to result.
import collections

class Solution(object):

    def accountsMerge(self, accounts):

        em_to_name = {}
        graph = collections.defaultdict(set)

        # Add edge to graph
        for acc in accounts:    # For each account
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email) # Now form a graph of emails.
                graph[email].add(acc[1]) # Bi-directed Graph, so add both ways.
                em_to_name[email] = name # In Parallel, also make map of names from email.

        seen = set() # Map of unique emails
        ans = []

        # This is standard Connected component lines:
        for email in graph:   # run DFS for all vertex in graph. Check out ConnectedComponent.py
            if email not in seen: # If node not visited in Graph, then do DFS or BFS. Here we are doing Iterative DFS

                # Below is Iterative DFS now
                seen.add(email)
                stack = [email]
                
                component = []

                while stack:
                    node = stack.pop()
                    component.append(node)

                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)

                ans.append([em_to_name[email]] + sorted(component))

        return ans


