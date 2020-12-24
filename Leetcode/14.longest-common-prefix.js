/*
 * @lc app=leetcode id=14 lang=javascript
 *
 * [14] Longest Common Prefix
 *
 * https://leetcode.com/problems/longest-common-prefix/description/
 *
 * algorithms
 * Easy (34.76%)
 * Likes:    2128
 * Dislikes: 1706
 * Total Accepted:    663.9K
 * Total Submissions: 1.9M
 * Testcase Example:  '["flower","flow","flight"]'
 *
 * Write a function to find the longest common prefix string amongst an array
 * of strings.
 *
 * If there is no common prefix, return an empty string "".
 *
 * Example 1:
 *
 *
 * Input: ["flower","flow","flight"]
 * Output: "fl"
 *
 *
 * Example 2:
 *
 *
 * Input: ["dog","racecar","car"]
 * Output: ""
 * Explanation: There is no common prefix among the input strings.
 *
 *
 * Note:
 *
 * All given inputs are in lowercase letters a-z.
 *
 */

// @lc code=start
/**
 * @param {string[]} strs
 * @return {string}
 */
const longestCommonPrefix = strs => {
  if (!strs.length) return '';

  const sortedStrings = strs.sort();
  let i = 0;
  let firstString = sortedStrings[0];
  let lastString = sortedStrings[strs.length - 1];

  while (
    i < firstString.length &&
    firstString.charAt(i) === lastString.charAt(i)
  ) {
    i++;
  }
  return firstString.slice(0, i);
};
// @lc code=end
