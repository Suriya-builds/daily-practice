# Running Sum of 1d Array

**Difficulty:** Easy | **Tags:** Array, Prefix Sum | [Open on LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/)

## Problem

<p>Given an array <code>nums</code>. We define a running sum of an array as&nbsp;<code>runningSum[i] = sum(nums[0]&hellip;nums[i])</code>.</p>

<p>Return the running sum of <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [1,3,6,10]
<strong>Explanation:</strong> Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,1,1,1,1]
<strong>Output:</strong> [1,2,3,4,5]
<strong>Explanation:</strong> Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,1,2,10,1]
<strong>Output:</strong> [3,4,6,16,17]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>-10^6&nbsp;&lt;= nums[i] &lt;=&nbsp;10^6</code></li>
</ul>


## My approach

Keep a running `total` that starts at 0. Loop through the numbers, add each one to `total`,
and append the current `total` to a `result` list. Return `result` after the loop.
This idea is called a **prefix sum**.

## Complexity

- Time: O(n), one pass through the list
- Space: O(n), for the result list

## What I learned

- `total` must start as a number (`0`), not a list (`[]`), or `total + m` gives a TypeError.
- `result = total` replaces the whole variable; `result.append(total)` adds to the end of the list.
- `return` must be outside the loop (lined up with `for`), or the function stops after the first round.
- Trace the code by hand in a table before running it.
