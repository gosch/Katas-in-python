def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    s = sorted(nums1 + nums2)
    return s[len(s) // 2 + 1] if len(s) % 2 == 1 else (s[len(s) // 2] + s[len(s) // 2 + 1]) / 2

print()