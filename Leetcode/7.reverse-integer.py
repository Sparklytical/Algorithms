#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.57%)
# Likes:    2764
# Dislikes: 4309
# Total Accepted:    921.1K
# Total Submissions: 3.6M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 0 when the reversed
# integer overflows.
# 
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        total=0
        absx=abs(x)
        count=len(str(absx))-1
        while absx!=0:
            temp=absx%10
            total=total+temp*(10**(count))
            count-=1
            absx=(absx-temp)/10
        if total >= 2**31-1:
            return 0
        if x<0:
            return int((-1)*total)
        else:
            return int(total)
# @lc code=end

