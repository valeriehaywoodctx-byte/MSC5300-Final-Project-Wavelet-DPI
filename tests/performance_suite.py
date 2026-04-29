import time
import csv
import os
from src.indexer import WaveletNode
from src.data_loader import DataLoader

def run_benchmarks():
    # Define the sizes we want to test (in KB)
    # We start small and go up to 5MB (5120 KB)
    test_sizes = [100, 500, 1000, 2500, 5000]
    results_file = "results/performance_data.csv"
    
    # Ensure the results folder exists
    os.makedirs("results", exist_ok=True)

    print(f"{'Size (KB)':<10} | {'Build Time (s)':<15} | {'Search Time (s)':<15}")
    print("-" * 45)

    with open(results_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Size_KB", "Build_Time_Sec", "Search_Time_Sec"])

        for size in test_sizes:
            # 1. Prepare Data
            data = DataLoader.generate_synthetic_traffic(size)
            
            # 2. Benchmark Construction
            start_b = time.time()
            root = WaveletNode(data)
            build_time = time.time() - start_b

            # 3. Benchmark Search (1000 searches to get a good average)
            start_s = time.time()
            for _ in range(1000):
                root.rank(108, len(data))
            search_time = (time.time() - start_s) / 1000 # Average per search

            # 4. Save and Print
            writer.writerow([size, build_time, search_time])
            print(f"{size:<10} | {build_time:<15.4f} | {search_time:<15.6f}")

    print(f"\n[DONE] Results saved to {results_file}")

if __name__ == "__main__":
    run_benchmarks()