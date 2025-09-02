# 🧹 The "Remove Duplicates from Sorted Array" Problem: A Deep Dive

Welcome to the repository! This project explores the classic **"Remove Duplicates from Sorted Array"** problem, a fundamental question in array manipulation and in-place algorithm design. Multiple solutions are presented in C++ with a focus on clarity and optimization.

---

## 🎯 Problem Statement

Given a sorted array `nums`, remove the duplicates **in-place** such that each element appears only once and **returns the new length**. Do not allocate extra space for another array — you must do this by modifying the input array in-place with O(1) extra memory.

### Constraints:
- The input array is sorted in non-decreasing order.
- You must not use extra space for another array.
- Modify the array in-place and return the new length.

### Example:
- **Input:** `nums = [0,0,1,1,1,2,2,3,3,4]`  
- **Output:** `5`, with `nums` modified to `[0,1,2,3,4,...]`

---

## 🛠️ Approaches & Solutions

### 1. Two-Pointer Approach

Uses two pointers to overwrite duplicates while maintaining the relative order of elements.

**Algorithm:**
- Initialize a `slow` pointer at index `0`.
- Iterate `fast` pointer from index `1` to end of array.
- If `nums[fast] != nums[slow]`, increment `slow` and set `nums[slow] = nums[fast]`.
- After the loop, return `slow + 1` as the new length.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

🔗 Code: [`With_Two_Pointer.cpp`](./With_Two_Pointer.cpp)

---

### 2. Brute Force Approach (For Educational Purposes)

This approach uses a set to eliminate duplicates, violating the space constraint but helpful for understanding.

**Algorithm:**
- Insert elements into a `set` to remove duplicates.
- Copy the set elements back into the original array.

> ⚠️ **Note:** This solution does not meet the O(1) space constraint.

**Time Complexity:** O(n log n)  
**Space Complexity:** O(n)

🔗 Code: [`With_Brute_Force.cpp`](./With_Brute_Force.cpp)

---

## 📦 Output Format Clarification

Even though you return the new length, the elements beyond that length in the array may remain unchanged or contain any value. Only the first `k` elements (where `k` is the returned length) should be considered.

---

## 📖 Additional Resources

- [LeetCode: Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [GeeksforGeeks: Remove duplicates from a sorted array](https://www.geeksforgeeks.org/remove-duplicates-sorted-array/)

---
