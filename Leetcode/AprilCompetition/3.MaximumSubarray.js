/**
Given an integer array nums, find the contiguous subarray(containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
*/

/**
 * @param {number[]} nums
 * @return {number}
 */
const maxSubArray = (nums) => {
  let a1 = 0;
  let a2 = nums[0];
  nums.forEach((i, a) => {
    a1 = Math.max(i, a1 + i);
    a2 = Math.max(a2, a1);
  });
  return a2;
};
