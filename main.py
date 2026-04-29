import yaml
import time
import logging
from src.indexer import WaveletNode
from src.data_loader import DataLoader

# Setup Logging based on Part 1 requirements
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def run_system():
    # 1. Load the Configuration (The 'Dashboard')
    try:
        with open("config/settings.yaml", "r") as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        logger.error("Config file not found! Ensure config/settings.yaml exists.")
        return

    logger.info(f"--- Starting {config['project_name']} v{config['version']} ---")

    # 2. Extract settings from YAML
    size = config['data_settings']['size_kb']
    seed = config['data_settings']['seed']
    target = config['data_settings']['target_byte']

    # 3. Generate Data using the Data Loader
    data = DataLoader.generate_synthetic_traffic(size, seed)

    # 4. Build and Benchmark
    logger.info(f"Building index for {size}KB...")
    start_time = time.time()
    root = WaveletNode(data)
    duration = time.time() - start_time

    # 5. Execute Search (Rank Query)
    count = root.rank(target, len(data))

    # 6. Report Results
    print("\n" + "="*30)
    print(f"FINAL REPORT: {size}KB PAYLOAD")
    print(f"Build Latency: {duration:.4f} seconds")
    print(f"Occurrences of {target}: {count}")
    print("="*30)

if __name__ == "__main__":
    run_system()