# Python Binary Search Techniques 🧑‍💻

**Author**: Prasanna Kumar

---

## Binary Search Techniques 🔍

Binary search is a highly efficient algorithm for finding an element in a **sorted list**. The key idea is to divide the search space in half at each step, significantly reducing the number of comparisons. Below is a guide to understanding the different scenarios in which binary search can be applied, along with its various use cases and edge cases.

| **Search Type**                       | **Explanation**                                                                                                    | **Best Time Complexity** | **Worst Time Complexity** | **Space Complexity** | **Use Cases**                                                                                                                                                   |
|---------------------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------|---------------------------|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Classic Binary Search**             | Search for a target element in a sorted array by repeatedly dividing the search interval in half.                    | O(log n)                 | O(log n)                  | O(1)                 | Ideal for searching in **sorted arrays**. Efficient for large datasets.                                                                                         |
| **Binary Search on Rotated Array**    | Used when the array is rotated but still sorted. The pivot is found and the array is split for searching.           | O(log n)                 | O(log n)                  | O(1)                 | Suitable for **rotated sorted arrays**. Example: Finding an element in a rotated array like `[6, 7, 9, 15, 19, 2, 4]`.                                            |
| **Binary Search for First Occurrence**| Find the first occurrence of a target element, even if there are duplicates. Modify the search to continue left.     | O(log n)                 | O(log n)                  | O(1)                 | When there are duplicates and you need to find the **first occurrence** of an element. Example: Finding the first occurrence of `7` in `[2, 3, 7, 7, 7, 8, 9]`.      |
| **Binary Search for Last Occurrence** | Similar to the first occurrence, but searching for the **last occurrence** of a target element.                      | O(log n)                 | O(log n)                  | O(1)                 | When you need the **last occurrence** of a target in a sorted array with duplicates. Example: Finding the last occurrence of `7` in `[2, 3, 7, 7, 7, 8, 9]`.       |
| **Binary Search for Insertion Point** | Finding the **insertion point** of a target element, i.e., where it should be placed in a sorted array.             | O(log n)                 | O(log n)                  | O(1)                 | Useful when inserting elements into a sorted list and finding their correct position. Example: Inserting `5` into `[1, 3, 6, 8, 9]`.                          |
| **Binary Search for Closest Value**   | Finding the closest value to a target in a sorted array (whether it is less than, greater than, or equal to the target). | O(log n)                 | O(log n)                  | O(1)                 | Used to find the closest value to the target in scenarios where the exact target may not exist. Example: Finding the closest element to `4` in `[1, 3, 5, 8]`.    |
| **Binary Search on 2D Matrix**        | Applied to a 2D matrix where each row and column is sorted. The algorithm can be adjusted to search either row-wise or column-wise. | O(log(m * n))            | O(log(m * n))             | O(1)                 | Efficient for searching in **2D sorted matrices**. Example: Searching for `5` in a matrix like `[[1, 4], [2, 5], [3, 6]]`.                                       |
| **Binary Search for Peak Element**    | Find a peak element in an array, where an element is greater than or equal to its neighbors. Can be solved using binary search. | O(log n)                 | O(log n)                  | O(1)                 | Used for finding **peak elements** in unsorted arrays. Example: Finding a peak element in `[1, 3, 20, 4, 1]`.                                                   |
| **Binary Search for Square Root**     | Finding the square root of a number using binary search. The search space is between `0` and `n`.                    | O(log n)                 | O(log n)                  | O(1)                 | Used for **computing square roots** or any operation where you need to find the root of a number. Example: Finding the square root of `27`.                    |

---

## Do's for Binary Search 📝

- **Always Work on Sorted Data**: Binary search only works on **sorted data**. Make sure the data is sorted before performing binary search. If the data is unsorted, first sort it or use a different search technique.
- **Check for Edge Cases**: Always consider the edge cases, such as an empty array, an array with a single element, or an array where all elements are the same.
- **Apply Proper Boundary Checks**: When implementing binary search, ensure that you properly handle the boundaries (`low`, `high`, and `mid`) to avoid infinite loops or index errors.
- **Use Iterative Approach**: Binary search can be implemented either recursively or iteratively. Prefer the iterative approach to avoid stack overflow issues with recursion in case of large datasets.
- **Consider Special Variants**: If you're looking for a **first or last occurrence** of an element, you can modify the binary search by adjusting the search to continue left or right even after finding the target.
- **Handle Duplicates**: If your dataset contains duplicates and you need to find the first or last occurrence, adjust your binary search to search for the boundary.
- **Use for Large Datasets**: Binary search is efficient with **large datasets**, especially in comparison to linear search. Use it when your data is large and sorted.
- **Use for Optimized Search in Multi-dimensional Data**: For 2D matrices or multidimensional arrays where rows and columns are sorted, binary search can significantly reduce search time.

---

## Don'ts ⚠️

- **Don’t Use Binary Search for Unsorted Data**: Binary search works only with sorted data. For unsorted datasets, you must either sort the data first or use a different algorithm.
- **Don’t Skip Boundary Checks**: Properly adjust your `low`, `high`, and `mid` values during each step of the search to avoid out-of-bound errors and infinite loops.
- **Don’t Assume No Duplicates**: If the array may contain duplicates and you need to find the first or last occurrence, modify the binary search to handle these cases.
- **Don’t Forget About Integer Overflow**: In some programming languages, calculating `mid = (low + high) // 2` can result in integer overflow for very large datasets. A safer formula is `mid = low + (high - low) // 2`.
- **Don’t Overuse Recursion**: Recursive binary search is elegant but might cause a stack overflow if the dataset is too large. Use the iterative approach to avoid this problem.
- **Don’t Ignore Space Complexity**: While binary search itself uses O(1) space for the iterative approach, recursive implementations can use O(log n) space due to recursion depth. Consider the trade-offs.

---
