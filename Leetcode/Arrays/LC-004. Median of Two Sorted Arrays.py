
# TAGS: Array, Binary Search, Divide & Conquer, Google, MS, Apple, Yahoo


################### USING BINARY SEARCH - ACCEPTED #######################################

class Solution1(object):   # 4/16/19

    def findMedianSortedArrays(self, A, B):
        """
        :type nums1: List[int] - Sorted List
        :type nums2: List[int] - Sorted List
        :rtype: float
        """
        m, n = len(A), len(B)
        if m > n:
            A, B, m, n = B, A, n, m  # We swap because we want to perform BS on smaller array
        if n == 0:
            raise ValueError

        # We need to do Binary search on smaller array.
        start, end = 0, m
        half_len = (m + n + 1) / 2

        while start <= end:

            i = (start + end) / 2
            j = half_len - i

            if i > 0 and A[i - 1] > B[j]:  # Ideally A[i-1] <= B[j], if not reduce the endpoint of A
                # i is too big, must decrease it
                end = i - 1

            elif i < m and B[j - 1] > A[i]:  # Ideally B[j-1] <= A[i], if not increment the start of A
                # i is too small, must increase it
                start = i + 1

            else:  # i is perfect. Both conditions are met. Just find median now. So find left_part and right_part.
                # So if total length is odd then middle element else if even, then average of two middle.

                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                # Case-1: If total length is odd,  then median will be max of left part only as seen in diagram before.
                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                # Case-2: If total length is even then (max of left part i.e max(A[i-1], B[j-1]) + min of right part i.e min(A[i], B[j]) )//2
                return (max_of_left + min_of_right) / 2.0

#============= BRUTE FORCE ======================================================

    def findMedianSortedArrays_(self, nums1, nums2):
        """
        :type nums1: List[int] - Sorted List
        :type nums2: List[int] - Sorted List
        :rtype: float
        """

        i = 0
        j = 0
        final_list = []

        while ((i < len(nums1)) and (j < len(nums2))):
            if nums1[i] < nums2[j]:
                final_list.append(nums1[i])
                i = i + 1
            else:
                final_list.append(nums2[j])
                j = j + 1

        while (i < len(nums1)):
            final_list.append(nums1[i])
            i = i + 1

        while (j < len(nums2)):
            final_list.append(nums2[j])
            j = j + 1

        # print final_list, len(final_list) % 2

        if len(final_list) % 2:  # If total len is odd
            return final_list[len(final_list) / 2]
        else:
            m1 = final_list[len(final_list) / 2] + final_list[
                len(final_list) / 2 - 1]  # Remeber given lists were sorted so this will work.
            m = float(m1)  # Else first fort both input lists
            return m / 2


###################################################################

# https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2511/Intuitive-Python-O(log-(m+n))-solution-by-kth-smallest-in-the-two-sorted-arrays-252ms?page=1&orderBy=newest_to_oldest

def findMedianSortedArrays(self, A, B):
    l = len(A) + len(B)
    if l % 2 == 1:
        return self.kth(A, B, l // 2)
    else:
        return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.


def kth(self, a, b, k):
    if not a:
        return b[k]
    if not b:
        return a[k]
    ia, ib = len(a) // 2, len(b) // 2
    ma, mb = a[ia], b[ib]

    # when k is bigger than the sum of a and b's median indices
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            return self.kth(a, b[ib + 1:], k - ib - 1)
        else:
            return self.kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
    else:
        # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return self.kth(a[:ia], b, k)
        else:
            return self.kth(a, b[:ib], k)

