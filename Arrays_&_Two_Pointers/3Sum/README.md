# 🌟 The "3Sum" Problem: A Deep Dive

Welcome to the repository! This project explores the classic **"3Sum"** problem, a widely recognized question in array manipulation and algorithm design. Multiple solutions are presented in C++ with a focus on clarity and optimization.

---

## 🎯 Problem Statement

Given an integer array `nums`, return all the unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j != k` and `nums[i] + nums[j] + nums[k] == 0`.

### Constraints:
- The solution set must not contain duplicate triplets.
- The order of the triplets does not matter.

### Example:
- **Input:** `nums = [-1, 0, 1, 2, -1, -4]`  
- **Output:** `[[-1, -1, 2], [-1, 0, 1]]`, where the unique triplets that sum to zero are `[-1, -1, 2]` and `[-1, 0, 1]`.

---

## 🛠️ Approaches & Solutions

### 1. Two-Pointer Approach (Optimal Solution)

Sort the array, and then use a two-pointer technique to find all unique triplets that sum to zero. This solution efficiently avoids duplicate triplets.

**Algorithm:**
- First, sort the input array.
- For each element `nums[i]`, use two pointers (`left` and `right`) to search for pairs that sum to `-nums[i]`.
- Skip duplicate elements to avoid counting the same triplet multiple times.
- Continue until the entire array is processed.

**Time Complexity:** O(n²)  
**Space Complexity:** O(1) (excluding the output list)

🔗 Code: [`With_Two_Pointer.cpp`](./With_Two_Pointer.cpp)

---

### 2. Brute Force Approach (For Educational Purposes)

This approach uses three nested loops to check every combination of three numbers and see if they sum to zero.

**Algorithm:**
- Iterate through all possible triplets using three loops.
- Check if the sum of the three elements equals zero, and if it does, add the triplet to the result.
- This solution will likely involve checking duplicate triplets, which can be avoided later by checking and removing duplicates.

> ⚠️ **Note:** This solution is not optimal and is provided for educational purposes only.

**Time Complexity:** O(n³)  
**Space Complexity:** O(1) (excluding the output list)

🔗 Code: [`With_Brute_Force.cpp`](./With_Brute_Force.cpp)

---

## 📦 Output Format Clarification

The result should be a list of unique triplets where each triplet is represented as a list of three integers, and the triplets themselves should be sorted in ascending order.

---

## 📖 Additional Resources

- [LeetCode: 3Sum](https://leetcode.com/problems/3sum/)
- [GeeksforGeeks: 3 Sum Problem](https://www.geeksforgeeks.org/3-sum-problem/)

---
