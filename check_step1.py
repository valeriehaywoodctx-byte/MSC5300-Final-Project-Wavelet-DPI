from src.indexer import WaveletNode
from src.data_loader import DataLoader
import time

# 1. Generate 100KB of "Fake" Network Traffic
print("Generating 100KB of traffic...")
large_data = DataLoader.generate_synthetic_traffic(100)

# 2. Build the Index (Benchmark the time)
print("Building Wavelet Tree (This is the stress test)...")
start_build = time.time()
root = WaveletNode(large_data)
end_build = time.time()

# 3. Perform a Rank Query for byte 108
target = 108
result = root.rank(target, len(large_data))

print(f"\n--- 100KB Stress Test Results ---")
print(f"Build Time: {end_build - start_build:.4f} seconds")
print(f"Occurrences of byte {target}: {result}")
print(f"Total Bytes Processed: {len(large_data)}")
print(f"STATUS: SUCCESS - System handled large dataset.")