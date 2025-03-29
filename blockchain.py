import time
import random

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.current_hash = self.compute_hash()  # Compute hash when block is created

    def compute_hash(self):
        """
        Custom hash function: combines index, timestamp, data, previous_hash, and nonce.
        """
        block_string = f"{self.index}-{self.timestamp}-{self.data}-{self.previous_hash}-{self.nonce}"
        
        # Print the raw block string
        print("Block String:", block_string)

        # Generate a simple custom hash
        custom_hash = sum(ord(char) for char in block_string) * 31
        return str(custom_hash)

# Example usage
timestamp = time.time()  # Get the current time
block1 = Block(0, timestamp, "First block", "0")  # Genesis block

print("Computed Hash:", block1.current_hash)  # Print the computed hash
