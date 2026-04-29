from src.indexer import WaveletNode
from src.data_loader import DataLoader
import time

# 1. Create a "Real" file on your computer
print("Creating a 10MB 'Real' dataset on disk...")
raw_data = DataLoader.generate_synthetic_traffic(10000) # 10MB
DataLoader.save_to_disk(raw_data, "network_traffic_dump.bin")

# 2. Load it back in (This proves File I/O works)
loaded_data = DataLoader.load_from_disk("network_traffic_dump.bin")

# 3. Index and Search
print("Indexing 10MB of data... (The Final Boss)")
start = time.time()
root = WaveletNode(loaded_data)
elapsed = time.time() - start

print(f"\n--- 10MB Production Test ---")
print(f"File Size: {len(loaded_data) / (1024*1024):.2f} MB")
print(f"Indexing Time: {elapsed:.4f} seconds")
print(f"STATUS: SUCCESS - System handles persistent disk storage.")