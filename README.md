
# **Binary Search and Linear Search Implementation**

## **Project Overview**
This project demonstrates the implementation of two fundamental search algorithms: **Binary Search** and **Linear Search**. The aim is to compare their performance, understand their time complexities, and reinforce concepts of searching algorithms.

## **Purpose**
- To provide a hands-on understanding of searching algorithms.
- To analyze and compare the efficiency of Binary Search and Linear Search.
- To document and share high-quality code with clear explanations.

---

## **How to Run the Program**

### **Prerequisites**
- Ensure you have Python (or the language used) installed on your system.
- Clone this repository:
  ```bash
  git clone https://github.com/safiabbasi402/Searching-Algorithm.git
  ```
- Navigate to the project folder:
  ```bash
  cd Searching-Algorithm
  ```

### **Execution**
1. Run the program:
   ```bash
   python search_algorithms.py
   ```
2. Input the array and the target value when prompted.
3. The program will output:
   - Whether the target was found.
   - The number of steps taken by each algorithm.
   - The time complexities of the algorithms.

### **Files Included**
- `search_algorithms.py`: Contains the implementation of Binary and Linear Search.
- `README.md`: Documentation explaining the project.

---

## **Algorithms Explanation**

### **Binary Search**
- **Description**: A search algorithm that works on sorted arrays by repeatedly dividing the search interval in half.
- **Steps**:
  1. Check the middle element.
  2. If it's the target, return its index.
  3. If the target is smaller, search the left half. If larger, search the right half.
- **Time Complexity**:
  - Best Case: \( O(1) \)
  - Worst Case: \( O(\log n) \)

### **Linear Search**
- **Description**: A simple search algorithm that checks every element in the array until the target is found.
- **Steps**:
  1. Iterate through the array.
  2. Compare each element to the target.
  3. Return the index if found, otherwise return -1.
- **Time Complexity**:
  - Best Case: \( O(1) \)
  - Worst Case: \( O(n) \)

---

## **Time Complexity Comparison**
| Algorithm       | Best Case   | Worst Case     |
|-----------------|-------------|----------------|
| **Binary Search** | \( O(1) \)   | \( O(\log n) \) |
| **Linear Search** | \( O(1) \)   | \( O(n) \)      |

For example, in the worst case:
- Binary Search takes \( \log_2(n) \) steps.
- Linear Search takes \( n \) steps.

---

## **Sample Output**
### Input
```
Array: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Target: 7
```
### Output
```
Binary Search:
- Target found at index 6.
- Time Complexity: O(log n).
- Steps: 3.

Linear Search:
- Target found at index 6.
- Time Complexity: O(n).
- Steps: 7.
```

---

## **Learning Outcomes**
1. Binary Search is significantly faster for large, sorted datasets due to its logarithmic complexity.
2. Linear Search, while simpler, becomes inefficient as the size of the dataset increases.
3. Documenting and testing the code reinforced best practices in software development.

---

## **Contributing**
Feel free to fork this repository, make improvements, and submit pull requests. Feedback is highly appreciated!

---

## LinkdIn Post Link
 [Check Here LinkdIn Post By Me](https://www.linkedin.com/posts/safiullah-abbasi-a5b203336_programming-algorithms-binarysearch-activity-7286092502464348161-E9wv?utm_source=share&utm_medium=member_android)

---

## **Connect**
If you found this project useful, let’s connect!
- **LinkedIn**: [Your LinkedIn Profile](https://www.linkedin.com/in/safiullah-abbasi-a5b203336?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
- **GitHub**: [Your GitHub Profile](https://github.com/safiabbasi402)
