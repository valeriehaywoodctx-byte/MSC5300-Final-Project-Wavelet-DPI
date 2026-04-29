import logging

# Professional Logging for Part 1/6
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class WaveletNode:
    """A succinct Wavelet Tree node for high-throughput packet indexing."""
    
    def __init__(self, data, low=0, high=255):
        """Initializes the node and recursively builds the tree structure."""
        self.low = low
        self.high = high
        self.left = None
        self.right = None
        
        # Base case: empty data or single character range
        if not data or low == high:
            self.bit_vector = []
            return

        mid = (low + high) // 2
        # Succinct partitioning: 0 if in lower half, 1 if in upper half [cite: 46]
        self.bit_vector = [1 if x > mid else 0 for x in data]
        
        # Recursive data splitting
        left_data = [x for x in data if x <= mid]
        right_data = [x for x in data if x > mid]

        if left_data:
            self.left = WaveletNode(left_data, low, mid)
        if right_data:
            self.right = WaveletNode(right_data, mid + 1, high)

    def rank(self, char, index):
        """Standard Rank Query: Counts occurrences of 'char' up to 'index'."""
        if self.low == self.high:
            return index

        mid = (self.low + self.high) // 2
        if char <= mid:
            # Count 0s in the bit vector up to the index for the left branch
            new_index = self.bit_vector[:index].count(0)
            return self.left.rank(char, new_index) if self.left else 0
        else:
            # Count 1s in the bit vector up to the index for the right branch
            new_index = self.bit_vector[:index].count(1)
            return self.right.rank(char, new_index) if self.right else 0