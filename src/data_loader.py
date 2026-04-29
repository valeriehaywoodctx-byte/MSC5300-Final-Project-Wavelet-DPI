import random
import logging
import os

logger = logging.getLogger(__name__)

class DataLoader:
    """Handles data generation, file I/O, and ingestion."""

    @staticmethod
    def generate_synthetic_traffic(size_kb: int, seed: int = 42) -> list:
        """Generates reproducible byte data."""
        random.seed(seed)
        return [random.randint(0, 255) for _ in range(size_kb * 1024)]

    @staticmethod
    def save_to_disk(data: list, filename: str):
        """Saves byte list to a binary file on disk."""
        os.makedirs("data", exist_ok=True)
        path = os.path.join("data", filename)
        with open(path, "wb") as f:
            f.write(bytearray(data))
        logger.info(f"Dataset saved to {path}")

    @staticmethod
    def load_from_disk(filename: str) -> list:
        """Reads a file from disk and converts it to a byte list."""
        path = os.path.join("data", filename)
        with open(path, "rb") as f:
            data = list(f.read())
        logger.info(f"Loaded {len(data)} bytes from {path}")
        return data