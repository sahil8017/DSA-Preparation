# 🔀 The "Merge Sorted Array" Problem: A Deep Dive

Welcome to the repository! This project explores the classic **"Merge Sorted Array"** problem — a staple in array manipulation and in-place merging techniques. Multiple solutions are implemented in C++ with a focus on efficiency, clarity, and adherence to space constraints.

---

## 🎯 Problem Statement

You are given two integer arrays `nums1` and `nums2`, sorted in **non-decreasing order**, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2`, respectively.

**Merge `nums2` into `nums1` as one sorted array.**

You must **do this in-place** without returning anything. Instead, modify `nums1` directly to contain the final sorted array.

### Constraints:
- `nums1.length == m + n`
- `nums2.length == n`
- Elements in both arrays are sorted in non-decreasing order.
- The first `m` elements of `nums1` are the valid elements; the last `n` are placeholders (usually `0`).

### Example:
- **Input:**  
  `nums1 = [1,2,3,0,0,0], m = 3`  
  `nums2 = [2,5,6], n = 3`  
- **Output:**  
  `nums1 = [1,2,2,3,5,6]`

---

## 🛠️ Approaches & Solutions

### 1. Two-Pointer (from the End) – In-Place Optimal

This elegant solution starts merging from the end of `nums1` to avoid overwriting values.

**Algorithm:**
- Initialize three pointers:  
  `i = m - 1` (end of valid elements in `nums1`)  
  `j = n - 1` (end of `nums2`)  
  `k = m + n - 1` (end of `nums1`)
- While `i >= 0` and `j >= 0`:  
  - If `nums1[i] > nums2[j]`, set `nums1[k] = nums1[i]` and decrement `i`.  
  - Else, set `nums1[k] = nums2[j]` and decrement `j`.  
  - Decrement `k`.
- Copy remaining elements from `nums2` if any.

**Time Complexity:** O(m + n)  
**Space Complexity:** O(1)

🔗 Code: [`InPlace_TwoPointer.cpp`](./InPlace_TwoPointer.cpp)

---

### 2. Brute Force with Extra Space (Educational Only)

A simpler but non-optimal solution using an auxiliary array.

**Algorithm:**
- Copy all valid elements from `nums1` and all elements from `nums2` into a temporary array.
- Sort the array and copy it back to `nums1`.

> ⚠️ **Note:** This violates the O(1) space requirement but is helpful for understanding the core idea.

**Time Complexity:** O((m + n) log (m + n))  
**Space Complexity:** O(m + n)

🔗 Code: [`BruteForce_Sort.cpp`](./BruteForce_Sort.cpp)

---

## 🧪 Edge Cases to Consider

- One or both arrays are empty.
- All elements in `nums2` are smaller or larger than those in `nums1`.
- Duplicates between `nums1` and `nums2`.

---

## 📚 Additional Resources

- [LeetCode: Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
- [GeeksforGeeks: Merge two sorted arrays](https://www.geeksforgeeks.org/merge-two-sorted-arrays/)
- [In-place Merge Explanation (Stack Overflow)](https://stackoverflow.com/questions/29527312/merge-sorted-array-in-place)
