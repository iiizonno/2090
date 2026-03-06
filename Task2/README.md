<!-- @format -->

# Heap Sort & Min-Heap Demo

Simple Python project that shows:

- Min-heap implementation
- Heap Sort (ascending)
- Bubble Sort (for comparison)
- Basic benchmark
- Step-by-step heap demonstration

## Files

- `main.py` : main program (bench + demo)
- `heap.py` : Min-Heap class
- `heap_sort.py` : heap sort function
- `bubble_sort.py` : bubble sort function
- `test_input.txt` : numbers to sort

## How to run

### 1. See the heap working step by step

```bash
python main.py demo

# with your own numbers(default: 14, 5, 19, 2, 8, 11, 3, 7 and insert 1, 13, 0)
python main.py demo --numbers 50 12 7 33 1 90 --insert 2
```

### 2. Compare sorting speed

```bash
# sort numbers in test_input.txt(default size: 100000 numbers) to test_output.txt
# time usage will be display
python main.py demo2

# Heap Sort vs Bubble Sort (array size 1000 ~ 30000)
python main.py bench

# with your own array size, seed, and skip bubble sort (because it's too slow)
python main.py bench --sizes 50000 500000 --seed 50 --no-bubble

# change number of measurements (default is 5)
python main.py bench --runs 10
```

