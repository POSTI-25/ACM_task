import time
import random
from datetime import date

class Block:
    def __init__(self, index, date, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.date = date
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.current_hash = self.compute_hash()  # Compute hash when block is created

    def compute_hash(self):
        """
        Custom hash function: Generates a hexadecimal-like hash using bitwise operations.
        """
        block_string = f"{self.index}/{self.date}/{self.timestamp}/{self.data}/{self.previous_hash}/{self.nonce}"
        
        # Print the raw block string
        print("Block String:", block_string)

        # Custom hashing logic
        hash_value = random.randint(0, 111)
        for char in block_string:
            hash_value = hash_value + ord(char)  # Shift & Mix
            hash_value = hash_value + int(bin(random.randint(100, 200))[2:])

        # Convert to hexadecimal-like format (letters + numbers)
        return hex(hash_value)[2:]  # Remove '0x' prefix


class Blockchain:
    def __init__(self, difficulty=2):
        """Initialize the blockchain with the Genesis Block and set difficulty level"""
        self.chain = []  # List to store blocks
        self.difficulty = difficulty  # Difficulty level for Proof of Work
        self.create_genesis_block()  # First block

    def create_genesis_block(self):
        """Manually create the first block (Genesis Block)"""
        timestamp = time.time()
        genesis_block = Block(0, date.today(), timestamp, "Genesis Block", "0")
        self.chain.append(genesis_block)

    def get_latest_block(self):
        """Return the last block in the chain"""
        return self.chain[-1]

    def proof_of_work(self, block):
        """Find a nonce that produces a hash with the required number of leading zeros"""
        while True:
            block.current_hash = block.compute_hash()
            if block.current_hash.startswith('0' * self.difficulty):
                print(f"Proof of Work found: Nonce = {block.nonce}, Hash = {block.current_hash}")
                return block.current_hash
            block.nonce += 1  # Increment nonce and try again

    def add_block(self, data):
        """Create a new block, link it to the previous block, and add it to the blockchain"""
        previous_block = self.get_latest_block()
        new_index = previous_block.index + 1
        timestamp = time.time()
        previous_hash = previous_block.current_hash

        new_block = Block(new_index, date.today(), timestamp, data, previous_hash)
        self.proof_of_work(new_block)  # Perform Proof of Work
        self.chain.append(new_block)

    def print_blockchain(self):
        """Print details of all blocks in the blockchain"""
        print("\n🔗 Blockchain:")
        for block in self.chain:
            print(f"Index: {block.index}, Hash: {block.current_hash}, Previous Hash: {block.previous_hash}, Nonce: {block.nonce}")
        print("\n")

# Example usage
blockchain = Blockchain(difficulty=2)  # Create a blockchain with a difficulty level

# Add new blocks
blockchain.add_block("Transaction 1: Alice sends Bob 10 coins")
blockchain.add_block("Transaction 2: Bob sends Charlie 5 coins")

# Print the blockchain
blockchain.print_blockchain()