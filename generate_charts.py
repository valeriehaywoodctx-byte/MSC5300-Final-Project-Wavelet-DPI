import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data you just generated
data = pd.read_csv('results/performance_data.csv')

# 2. Create Plot 1: Construction Time (Scalability)
plt.figure(figsize=(10, 5))
plt.plot(data['Size_KB'], data['Build_Time_Sec'], marker='o', color='b', linestyle='-')
plt.title('Wavelet Tree Construction Scalability')
plt.xlabel('Dataset Size (KB)')
plt.ylabel('Time (Seconds)')
plt.grid(True)
plt.savefig('results/build_scalability.png')
print("Saved: results/build_scalability.png")

# 3. Create Plot 2: Search Efficiency
plt.figure(figsize=(10, 5))
plt.plot(data['Size_KB'], data['Search_Time_Sec'], marker='s', color='r', linestyle='--')
plt.title('Search Latency (Average of 1000 Rank Queries)')
plt.xlabel('Dataset Size (KB)')
plt.ylabel('Average Search Time (Seconds)')
plt.grid(True)
plt.savefig('results/search_efficiency.png')
print("Saved: results/search_efficiency.png")