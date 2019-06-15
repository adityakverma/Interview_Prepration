

# 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms

# Time complexity is O(n)
# Space complexity is O(n)

class Solution():

    # The stack maintain the indexes of buildings with ascending height. Before adding a new building pop the
    # building who is taller than the new one. The building popped out represent the height of a rectangle with
    # the new building as the right boundary and the current stack top as the left boundary. Calculate its area
    # and update ans of maximum area. Boundary is handled using dummy buildings.
    # https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms

    def largestRectangleArea(self, heights):

        if len(heights) == 1:  # Corner cases
            return heights[0]
        elif len(heights) == 0:
            return 0

        heights.append(0)  # To make sure we append to empty stack when we fail check -- while height[i] < height[stack[-1]]
        stack = [-1]  # Stack of Indexes, as told by tushar Roy
        area = 0

        for i in range(len(heights)):  # Getting index of array of heights
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1  # Note, this stack contains indexes, that's why we are doing i - stack top -1
                area = max(area, h * w)
            stack.append(i)

        heights.pop()  # Since we are appending zero in the begining...
        return area  # Gives Max Area

    # --------------------------------------------------------------------------------------------------

    # https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28912/Python-O(n)-time-and-space-solution-55ms-beat-99

    def _max_histogram_rectangle(self,heights): # This seems like Tushar Roy's method ... See his Java code -Same.
        stack = []
        area = 0

        if len(heights) == 1:  # Corner cases
            return heights[0]
        elif len(heights) == 0:
            return 0

        for i, h in enumerate(heights):
            if not stack or h >= stack[-1][1]:  # some_list[-1] gets the last element, some_list[-2] gets the second to last
                stack.append((i, h))
            else:
                while stack and stack[-1][1] > h:
                    index, height = stack.pop()  # Because stack has values in pair [ index, height]
                    area = max(area, height * (i - index))
                stack.append((i, h))

        while stack:
            index, height = stack.pop()
            area = max(area, (len(heights) - index) * height)

        return area


if __name__ == '__main__':

    height = [2, 1, 5, 6, 2, 3]
    s = Solution()
    print "\nMax Area: ", s.largestRectangleArea(height)
    print "\nMax Area: ", s._max_histogram_rectangle(height)




# The stack maintain the indexes of buildings with ascending height. Before adding a new building pop the building
#  who is taller than the new one. The building popped out represent the height of a rectangle with the new
#  building as the right boundary and the current stack top as the left boundary. Calculate its area and update
#  ans of maximum area. Boundary is handled using dummy buildings.


# Not sure, why do you need to height.pop() in the end. Seems redundant to me.
# @rahul8590 Actually this is the most beautiful line of code I see from that program, that line is to recover the
# original state of the input, since python list is passed by reference instead of shadow copy. It is not gonna
#  give you wrong result for this problem. However in real world development, think about your colleague created
# a list contains some values that he will need in the future, you added a sentinel value to make your life easier,
#  if you don't clean it up afterward, your colleague's code is very likely to crash. This is a good programming
# habit, it added one more "redundant" line, but it also make everybody's life easier. Hope it helps

#----------------------------------------------------------------------------------------------------------
# Note Solution is inspired from video of Tushar Roy on youtube, who has also given similar java solution:
# https://github.com/mission-peace/interview/blob/master/src/com/interview/stackqueue/MaximumHistogram.java

# public class MaximumHistogram {
#
#     public int maxHistogram(int input[]){
#         Deque<Integer> stack = new LinkedList<Integer>();
#         int maxArea = 0;
#         int area = 0;
#         int i;
#         for(i=0; i < input.length;){
#             if(stack.isEmpty() || input[stack.peekFirst()] <= input[i]){
#                 stack.offerFirst(i++);
#             }else{
#                 int top = stack.pollFirst();
#                 //if stack is empty means everything till i has to be
#                 //greater or equal to input[top] so get area by
#                 //input[top] * i;
#                 if(stack.isEmpty()){
#                     area = input[top] * i;
#                 }
#                 //if stack is not empty then everythin from i-1 to input.peek() + 1
#                 //has to be greater or equal to input[top]
#                 //so area = input[top]*(i - stack.peek() - 1);
#                 else{
#                     area = input[top] * (i - stack.peekFirst() - 1);
#                 }
#                 if(area > maxArea){
#                     maxArea = area;
#                 }
#             }
#         }
#         while(!stack.isEmpty()){
#             int top = stack.pollFirst();
#             //if stack is empty means everything till i has to be
#             //greater or equal to input[top] so get area by
#             //input[top] * i;
#             if(stack.isEmpty()){
#                 area = input[top] * i;
#             }
#             //if stack is not empty then everything from i-1 to input.peek() + 1
#             //has to be greater or equal to input[top]
#             //so area = input[top]*(i - stack.peek() - 1);
#             else{
#                 area = input[top] * (i - stack.peekFirst() - 1);
#             }
#         if(area > maxArea){
#                 maxArea = area;
#             }
#         }
#         return maxArea;
#     }
#
#     public static void main(String args[]){
#         MaximumHistogram mh = new MaximumHistogram();
#         int input[] = {2,2,2,6,1,5,4,2,2,2,2};
#         int maxArea = mh.maxHistogram(input);
#         //System.out.println(maxArea);
#         assert maxArea == 12;
#     }
# }