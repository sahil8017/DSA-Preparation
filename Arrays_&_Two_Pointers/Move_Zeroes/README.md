# 🧹 The "Move Zeroes" Problem: A Deep Dive

Welcome to the repository! This project explores the classic **"Move Zeroes"** problem, an important question in array manipulation and in-place algorithm design. Multiple solutions are presented in C++ with a focus on clarity and optimization.

---

## 🎯 Problem Statement

Given an array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements. You must do this **in-place** without making a copy of the array.

### Constraints:
- Do not use extra space for another array.
- Maintain the relative order of the non-zero elements.

### Example:
- **Input:** `nums = [0,1,0,3,12]`  
- **Output:** `[1,3,12,0,0]`, with the first three elements being the non-zero elements in the original order.

---

## 🛠️ Approaches & Solutions

### 1. Two-Pointer Approach (Optimal Solution)

Uses two pointers to swap non-zero elements to the left side while pushing zeroes to the right.

**Algorithm:**
- Initialize a `lastNonZeroFoundAt` pointer at index `0`.
- Iterate through the array with a `current` pointer.
- If `nums[current] != 0`, swap `nums[lastNonZeroFoundAt]` with `nums[current]`, and increment `lastNonZeroFoundAt`.
- After the loop, the zeroes will be automatically moved to the end of the array.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

🔗 Code: [`With_Two_Pointer.cpp`](./With_Two_Pointer.cpp)

---

### 2. Brute Force Approach (For Educational Purposes)

This approach iterates through the array and builds a new array, placing non-zero elements first and zeroes at the end.

**Algorithm:**
- Create a new array for the non-zero elements.
- Iterate through the input array and add all non-zero elements to the new array.
- Append the necessary number of zeroes to the new array and copy it back to the original array.

> ⚠️ **Note:** This solution does not meet the O(1) space constraint.

**Time Complexity:** O(n)  
**Space Complexity:** O(n)

🔗 Code: [`With_Brute_Force.cpp`](./With_Brute_Force.cpp)

---

## 📦 Output Format Clarification

After the array is modified, any element beyond the new "non-zero length" can be considered a zero, but it’s not required to be explicitly set to zero in the array.

---

## 📖 Additional Resources

- [LeetCode: Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- [GeeksforGeeks: Move all zeroes to end of array](https://www.geeksforgeeks.org/move-all-zeroes-to-end-of-array/)

---
