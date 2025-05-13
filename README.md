# Sequence Alignment: Dynamic Programming and Memory-Efficient Comparison

---

## 📊 Datapoints

| M+N  | Time (ms) Basic | Time (ms) Efficient | Memory (KB) Basic | Memory (KB) Efficient |
|------|------------------|----------------------|--------------------|------------------------|
| 16   | 0.00             | 0.00                 | 27460.00           | 27724.00               |
| 64   | 1.01             | 1.00                 | 27504.00           | 27668.00               |
| 128  | 3.01             | 4.01                 | 27684.00           | 27680.00               |
| 256  | 14.02            | 21.53                | 27868.00           | 27752.00               |
| 384  | 30.58            | 48.58                | 27900.00           | 27792.00               |
| 512  | 53.03            | 88.58                | 28504.00           | 27728.00               |
| 768  | 135.63           | 208.55               | 28856.00           | 27820.00               |
| 1024 | 238.64           | 364.71               | 30224.00           | 27748.00               |
| 1280 | 409.29           | 572.41               | 31444.00           | 27776.00               |
| 1536 | 613.06           | 863.88               | 32856.00           | 27484.00               |
| 2048 | 1007.57          | 1575.59              | 36372.00           | 27624.00               |
| 2560 | 1909.66          | 2827.13              | 41292.00           | 27076.00               |
| 3072 | 2335.13          | 5034.32              | 47412.00           | 27428.00               |
| 3584 | 3188.72          | 4962.75              | 55056.00           | 27624.00               |
| 3968 | 3849.86          | 6148.57              | 61948.00           | 27576.00               |

---

## 📈 Graph 1 – Memory vs Problem Size (M + N)

![Insert Graph1 here](#)

### Nature of the Graph
- **Basic:** Polynomial (roughly quadratic)  
- **Efficient:** Linear (almost)

### Explanation:
- The basic version uses a 2D DP table of size `m × n`, causing memory to grow quadratically with input size.
- The efficient version (Hirschberg’s algorithm) uses only two columns, leading to linear memory complexity.

---

## ⏱ Graph 2 – Time vs Problem Size (M + N)

![Insert Graph2 here](#)

### Nature of the Graph
- **Basic:** Polynomial (roughly quadratic)  
- **Efficient:** Polynomial (still O(mn), slightly higher due to recursion overhead)

### Explanation:
- Both algorithms have O(mn) time complexity.
  - **Basic:** Fills an `m × n` table directly.
  - **Efficient:** Uses divide-and-conquer and forward/backward DP passes. Total cost still under `2mn`.

---

## 🧪 Threshold Benchmarking

### Benchmarking Threshold for Efficient Algorithm

To select the best threshold at which the efficient algorithm switches to classic DP:

- **Threshold = 40** was selected based on:
  - Low average runtime
  - Local minimum in memory usage
  - Balanced time-space tradeoff

> Hirschberg's algorithm remains memory-efficient throughout. Threshold = 40 minimizes time without sacrificing space benefits.

---

## 🔗 GitHub Repository

📎 [https://github.com/yashgawankar/Sequence-Alignment](https://github.com/yashgawankar/Sequence-Alignment)

This contains:
- All code
- Benchmark scripts
- Input/output samples
- Graph generation utilities
