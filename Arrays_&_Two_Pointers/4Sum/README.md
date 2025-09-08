# 🌟 The "4Sum" Problem: A Deep Dive

Welcome to the repository! This project explores the classic **"4Sum"** problem, a popular variation of the **3Sum** problem, where instead of finding triplets that sum to zero, we look for quadruplets that sum to a given target. Multiple solutions are presented in C++ with a focus on clarity and optimization.

---

## 🎯 Problem Statement

Given an integer array `nums` and an integer `target`, return all unique quadruplets `[nums[i], nums[j], nums[k], nums[l]]` such that `i != j != k != l` and `nums[i] + nums[j] + nums[k] + nums[l] == target`.

### Constraints:
- The solution set must not contain duplicate quadruplets.
- The order of the quadruplets does not matter.

### Example:
- **Input:** `nums = [1, 0, -1, 0, -2, 2], target = 0`  
- **Output:** `[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]`, where the unique quadruplets that sum to zero are `[-2, -1, 1, 2]`, `[-2, 0, 0, 2]`, and `[-1, 0, 0, 1]`.

---

## 🛠️ Approaches & Solutions

### 1. Two-Pointer Approach (Optimal Solution)

Sort the array, and then use a combination of two-pointers and nested loops to find all unique quadruplets that sum to the target value. This solution efficiently avoids duplicate quadruplets.

**Algorithm:**
- First, sort the input array.
- For each element `nums[i]`, use a pair of nested loops and two pointers (`left` and `right`) to search for pairs that sum to `target - nums[i]`.
- Skip duplicate elements and indices to avoid counting the same quadruplet multiple times.
- Continue until the entire array is processed.

**Time Complexity:** O(n³)  
**Space Complexity:** O(1) (excluding the output list)

🔗 Code: [`With_Two_Pointer.cpp`](./With_Two_Pointer.cpp)

---

### 2. Brute Force Approach (For Educational Purposes)

This approach uses four nested loops to check every combination of four numbers and see if they sum to the target value.

**Algorithm:**
- Iterate through all possible quadruplets using four loops.
- Check if the sum of the four elements equals the target, and if it does, add the quadruplet to the result.
- This solution will likely involve checking duplicate quadruplets, which can be avoided later by checking and removing duplicates.

> ⚠️ **Note:** This solution is not optimal and is provided for educational purposes only.

**Time Complexity:** O(n⁴)  
**Space Complexity:** O(1) (excluding the output list)

🔗 Code: [`With_Brute_Force.cpp`](./With_Brute_Force.cpp)

---

## 📦 Output Format Clarification

The result should be a list of unique quadruplets where each quadruplet is represented as a list of four integers, and the quadruplets themselves should be sorted in ascending order.

---

## 📖 Additional Resources

- [LeetCode: 4Sum](https://leetcode.com/problems/4sum/)
- [GeeksforGeeks: 4 Sum Problem](https://www.geeksforgeeks.org/4-sum-problem/)

---
