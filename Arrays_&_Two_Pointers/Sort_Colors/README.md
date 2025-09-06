# 🎨 The "Sort Colors" Problem: A Deep Dive

Welcome to the repository! This project explores the classic **"Sort Colors"** problem — a fundamental exercise in in-place sorting and pointer manipulation, often used to teach the Dutch National Flag algorithm. Multiple C++ solutions are implemented with a focus on efficiency, clarity, and in-place optimization.

---

## 🎯 Problem Statement

Given an array `nums` with `n` objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order **red (0), white (1), and blue (2)**.

We will use the integers `0`, `1`, and `2` to represent the color red, white, and blue, respectively.

**You must solve this problem without using the library's sort function.**

### Constraints:
- `1 <= nums.length <= 300`
- `nums[i]` is either `0`, `1`, or `2`

### Example:
- **Input:**  
  `nums = [2,0,2,1,1,0]`  
- **Output:**  
  `nums = [0,0,1,1,2,2]`

---

## 🛠️ Approaches & Solutions

### 1. Dutch National Flag Algorithm – Optimal In-Place

A clever three-pointer approach that partitions the array into three segments for 0s, 1s, and 2s.

**Algorithm:**
- Initialize three pointers:  
  `low = 0`, `mid = 0`, `high = n - 1`
- Traverse the array while `mid <= high`:
  - If `nums[mid] == 0`, swap with `nums[low]`, increment both `low` and `mid`.
  - If `nums[mid] == 1`, just move `mid` forward.
  - If `nums[mid] == 2`, swap with `nums[high]`, decrement `high`.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

🔗 Code: [`DutchNationalFlag.cpp`](./DutchNationalFlag.cpp)

---

### 2. Counting Sort – Educational Simplicity

A two-pass counting approach, not optimal in practice but very intuitive for beginners.

**Algorithm:**
- Count the number of 0s, 1s, and 2s.
- Overwrite the array with the correct number of each value in order.

> ⚠️ **Note:** Though this approach is O(n) in time, it involves multiple passes and is not as elegant as the Dutch National Flag method.

**Time Complexity:** O(n)  
**Space Complexity:** O(1)

🔗 Code: [`CountingSort.cpp`](./CountingSort.cpp)

---

### 3. Standard Sort (❌ Not Allowed)

Using built-in sort functions (e.g., `std::sort()` in C++) is **not permitted** for this problem per constraints, but might be useful for quick testing.

---

## 🧪 Edge Cases to Consider

- All elements are the same color (e.g., `[0,0,0]` or `[2,2,2]`)
- The array is already sorted
- The array has only one element
- Colors appear in reverse order

---

## 📚 Additional Resources

- [LeetCode: Sort Colors](https://leetcode.com/problems/sort-colors/)
- [Dutch National Flag Problem - Wikipedia](https://en.wikipedia.org/wiki/Dutch_national_flag_problem)
- [GeeksforGeeks: Sort an array of 0s, 1s and 2s](https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/)
- [In-place Sorting Explanation (Stack Overflow)](https://stackoverflow.com/questions/76963341/what-is-the-dutch-national-flag-problem)

