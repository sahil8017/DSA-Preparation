# 🧱 The "Container With Most Water" Problem: A Deep Dive

Welcome to the repository! This project tackles the classic **"Container With Most Water"** problem — a fundamental exercise in two-pointer techniques and greedy optimization. Multiple solutions are implemented in C++ with an emphasis on performance, simplicity, and space efficiency.

---

## 🎯 Problem Statement

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are at `(i, 0)` and `(i, height[i])`.

Find **two lines** that together with the x-axis form a container, such that the container contains the **most water**.

Return the **maximum amount of water** a container can store.

> You **may not** slant the container.

### Constraints:
- `n >= 2`
- `1 <= height[i] <= 10⁵`

### Example:
- **Input:**  
  `height = [1,8,6,2,5,4,8,3,7]`
- **Output:**  
  `49`  
- **Explanation:**  
  The lines at index 1 and 8 (heights 8 and 7) form the container with the most water, storing `min(8,7) * (8-1) = 49` units.

---

## 🛠️ Approaches & Solutions

### 1. Two-Pointer Approach – Optimal & Elegant

This solution leverages a greedy two-pointer strategy by initializing pointers at both ends of the array and moving them inward.

**Algorithm:**
- Initialize two pointers:  
  `left = 0`, `right = n - 1`
- While `left < right`:  
  - Compute `area = min(height[left], height[right]) * (right - left)`
  - Update `max_area` if this area is larger
  - Move the pointer pointing to the **shorter line** inward, as this may increase the height for a larger container

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

🔗 Code: [`TwoPointer_Optimal.cpp`](./TwoPointer_Optimal.cpp)

---

### 2. Brute Force Approach (Educational Only)

A straightforward approach that checks all possible pairs of lines.

**Algorithm:**
- Use two nested loops to check every pair `(i, j)` such that `i < j`
- Compute area for each pair and track the maximum

> ⚠️ **Note:** Highly inefficient for large inputs. Good for understanding the problem but **not suitable** for production use.

**Time Complexity:** O(n²)  
**Space Complexity:** O(1)

🔗 Code: [`BruteForce.cpp`](./BruteForce.cpp)

---

## 🧪 Edge Cases to Consider

- All heights are the same.
- Heights strictly increasing or decreasing.
- Very large array (e.g., size ≥ 10⁵) — performance matters.
- Minimum input size (`n = 2`).

---

## 📚 Additional Resources

- [LeetCode: Container With Most Water](https://leetcode.com/problems/container-with-most-water/)
- [GeeksforGeeks: Maximum water between two lines](https://www.geeksforgeeks.org/container-with-most-water/)
- [Visualization and Intuition (Stack Overflow)](https://stackoverflow.com/questions/42011187/container-with-most-water-leetcode)

---
