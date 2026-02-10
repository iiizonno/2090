import argparse
import random
import time
from typing import Callable, List

from heap import Heap
from heap_sort import heap_sort
from bubble_sort import bubble_sort

def measure_sort_time(sort_func: Callable, data: List[int], runs: int = 3) -> float:
    total = 0.0
    for _ in range(runs):
        arr = data[:]
        start = time.perf_counter()
        sort_func(arr)
        elapsed = time.perf_counter() - start
        total += elapsed
    return total / runs


def generate_random_data(n: int, seed: int | None = None) -> List[int]:
    rng = random.Random(seed)
    return [rng.randint(1, 1_000_000) for _ in range(n)]


def run_benchmarks(args):
    algorithms = [
        ("Heap Sort", heap_sort),
    ]
    if not args.no_bubble:
        algorithms.append(("Bubble Sort", bubble_sort))

    print(f"\nBenchmark – random data, {args.runs} runs")
    print("─" * 60)

    for size in args.sizes:
        data = generate_random_data(size, args.seed)
        print(f"\n  n = {size:7,d}")

        for name, func in algorithms:
            try:
                t = measure_sort_time(func, data, args.runs)
                print(f"    {name:12}  {t:8.4f} s")
            except Exception as e:
                print(f"    {name:12}  ERROR — {e}")


def run_demo(args):
    numbers = args.numbers or [14, 5, 19, 2, 8, 11, 3, 7]
    print("\n=== Min-Heap Demo ===")
    print(f"Initial: {numbers}")

    h = Heap(numbers)
    print("After build:")
    print(f"  {h.to_list()}")
    print(f"  min = {h.peek()}")

    for val in (args.insert or [1, 13, 0]):
        print(f"\nInsert {val}")
        h.insert(val)
        print(f"  {h.to_list()}")
        print(f"  min = {h.peek()}")

    print("\nExtracting mins")
    extracted = []
    while h:
        extracted.append(h.extract_min())

    print("Result:", extracted)


def main():
    parser = argparse.ArgumentParser(description="Heap + sorting benchmark & demo")
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    b = subparsers.add_parser("bench", help="run performance comparison")
    b.add_argument("--sizes", nargs="+", type=int,
                   default=[1000, 3000, 10000, 30000],
                   help="array sizes to test")
    b.add_argument("--runs", type=int, default=5,
                   help="number of timing runs per algorithm")
    b.add_argument("--seed", type=int, default=42,
                   help="random seed")
    b.add_argument("--no-bubble", action="store_true",
                   help="skip bubble sort")
    
    d1 = subparsers.add_parser("demo", help="min-heap demonstration")
    d1.add_argument("--numbers", nargs="*", type=int,
                   help="starting numbers")
    d1.add_argument("--insert", nargs="*", type=int,
                   help="values to insert")
    
    d2 = subparsers.add_parser("demo2", help="sort demonstration")
    

    args = parser.parse_args()

    if args.cmd == "bench":
        run_benchmarks(args)
    elif args.cmd == "demo":
        run_demo(args)
    elif args.cmd == "demo2":
        with open("test_input.txt", "r") as infile: 
            test_numbers = [int(line.strip()) for line in infile if line.strip()]
        start = time.perf_counter()
        heap_sort(test_numbers)
        elapsed = time.perf_counter() - start
        with open("test_output.txt", "w") as outfile:
            print(f"Sort finished.\nArray size: {len(test_numbers)}\nTime taken to sort: {elapsed:.4f} seconds\n")
            outfile.write(f"Time taken to sort: {elapsed:.4f} seconds\n")
            outfile.write("Sorted numbers:\n")
            for num in test_numbers:
                outfile.write(f"{num}\n")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()