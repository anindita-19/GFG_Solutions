class Solution:
    def maxSubarraySum(self, arr, k):
        window_sum = 0

        for i in range(k):
            window_sum += arr[i]

        ans = window_sum

        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            ans = max(ans, window_sum)

        return ans