
# Must See this KMP algorithm video for pattern search:
# https://www.youtube.com/watch?v=GTJr8OvyEVQ
# His equivalent Java code: https://github.com/mission-peace/interview/blob/master/src/com/interview/string/SubstringSearch.java

class Solution(object): # My code based on understanding of Tushar Roy's video and his Java code

        def KMP_Search(self,text, pattern):

            if not text or not pattern:
                return False

            lps = self.computeLPS(pattern)
            i = j = 0
            while i < len(text) and j < len(pattern):
                if text[i] == pattern[j]:
                    i += 1
                    j += 1
                else:
                    if j != 0:
                        j = lps[j-1]
                    else:
                        i += 1
            if j == len(pattern):
                return True
            else:
                return False

        def computeLPS(self,str):  # lps indicates longest proper prefix which is also suffix # # Compute temporary array to maintain size of suffix which is same as prefix
            lps = [0] * len(str)

            i = 1
            j = 0
            while i < len(str):
                if str[i] == str[j]:
                    lps[i] = j + 1
                    i += 1
                    j += 1
                else:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps            # This array lps, will help us in doing substring search. Time Complexity of this O(n) & space complexity is also O(n)
                                  # Next: Lets apply this substring search ( pattern) to real string (text) to find, if that pattern exists in that text. See the KMP function below in java.  Note LC-76 is different, to find min window, where char may not be continous

if __name__ == '__main__':
    s = Solution()
    text = "abcxabcdabcdabcy"
    pattern = "abcdabcy"
    print "\nDoes pattern exists in text? : ",s.KMP_Search(text,pattern)


#########################################################################################################


# /**  JAVA - Tushar Roy

 # * Date 09/22/2014
 # * @author tusroy
 # *
 # * Do pattern matching using KMP algorithm
 # *
 # * Runtime complexity - O(m + n) where m is length of text and n is length of pattern
 # * Space complexity - O(n)
 # */
# public class SubstringSearch {
#
#     /**
#      * Slow method of pattern matching
#      */
#     public boolean hasSubstring(char[] text, char[] pattern){
#         int i=0;
#         int j=0;
#         int k = 0;
#         while(i < text.length && j < pattern.length){
#             if(text[i] == pattern[j]){
#                 i++;
#                 j++;
#             }else{
#                 j=0;
#                 k++;
#                 i = k;
#             }
#         }
#         if(j == pattern.length){
#             return true;
#         }
#         return false;
#     }
#
#     /**
#      * Compute temporary array to maintain size of suffix which is same as prefix
#      * Time/space complexity is O(size of pattern)
#      */
#     private int[] computeTemporaryArray(char pattern[]){
#         int [] lps = new int[pattern.length];
#         int index =0;
#         for(int i=1; i < pattern.length;){
#             if(pattern[i] == pattern[index]){
#                 lps[i] = index + 1;
#                 index++;
#                 i++;
#             }else{
#                 if(index != 0){
#                     index = lps[index-1];
#                 }else{
#                     lps[i] =0;
#                     i++;
#                 }
#             }
#         }
#         return lps;
#     }
#
#     /**
#      * KMP algorithm of pattern matching.
#      */
#     public boolean KMP(char []text, char []pattern){
#
#         int lps[] = computeTemporaryArray(pattern);
#         int i=0;
#         int j=0;
#         while(i < text.length && j < pattern.length){   # Important since we are dealing with two different strings
#             if(text[i] == pattern[j]){
#                 i++;
#                 j++;
#             }else{
#                 if(j!=0){
#                     j = lps[j-1];
#                 }else{
#                     i++;  # Since we never look back in original string (text), so we keep moving forward in this string (text)
#                 }
#             }
#         }
#         if(j == pattern.length){
#             return true;
#         }
#         return false;
#     }
#
#     public static void main(String args[]){
#
#         String text = "abcxabcdabcdabcy";
#         String pattern = "abcdabcy";
#         SubstringSearch ss = new SubstringSearch();
#         boolean result = ss.KMP(text.toCharArray(), pattern.toCharArray());
#         System.out.print(result);
#
#     }
# }
#




