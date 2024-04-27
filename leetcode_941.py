class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        n = len(arr)

        if n < 3:
            return False

        peak = max(arr)
        peak_index = arr.index(peak)

        if peak_index == 0 or peak_index == n - 1:
            return False

        for i in range(1, peak_index):
            if arr[i] <= arr[i - 1]:
                return False

        for i in range(peak_index, n - 1):
            if arr[i] <= arr[i + 1]:
                return False

        else:

            return True