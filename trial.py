import time
from datetime import date
import random

class Block:
    def __init__(self, index, date, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.date = date
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.current_hash = self.compute_hash()  # Compute hash when block is created

    # def compute_hash(self):
    #     """
    #     Custom hash function: Generates a simple hash using the block's attributes.
    #     """
    #     block_string = f"{self.index}/{self.date}/{self.timestamp}/{self.data}/{self.previous_hash}/{self.nonce}"
        
    #     # Simple hash logic: sum of ASCII values of characters + nonce
    #     hash_value = sum(ord(char) for char in block_string) + self.nonce
        
    #     # Convert to hexadecimal-like format (letters + numbers)
    #     hash_hex = hex(hash_value)[2:]  # Remove '0x' prefix
        
    #     # Ensure the hash is 5 characters long, padded with leading zeros if necessary
    #     hash_hex = hash_hex.zfill(5)  # Pad with leading zeros to ensure length of 5
        
    #     return hash_hex[-5:]  # Return the last 5 characters
    def compute_hash(self):
        """
        Custom hash function: Generates a more complex hash using the block's attributes.
        """
        block_string = f"{self.index}/{self.date}/{self.timestamp}/{self.data}/{self.previous_hash}/{self.nonce}"
        
        # Create a hash value based on the block string and nonce
        hash_value = sum(ord(char) for char in block_string) 
        hash_value = hash_value + int(bin(hash_value)[2:])
        hash_value = hash_value + int(hex(random.randint(10,100))[2:]) + self.nonce
        
        # Convert to hexadecimal-like format (letters + numbers)
        hash_hex = hex(hash_value)[2:]  # Remove '0x' prefix
        
        # Ensure the hash is at least 5 characters long, padded with leading zeros if necessary
        # hash_hex = hash_hex.zfill(5)  # Pad with leading zeros to ensure length of 5
        
        # return hash_hex[-5:]  # Return the last 5 characters
        return hash_hex

class Blockchain:
    # def __init__(self, difficulty=2):
    #     """Initialize the blockchain with the Genesis Block and set difficulty level"""
    #     self.chain = []  # List to store blocks
    #     self.difficulty = difficulty  # Difficulty level for Proof of Work
    #     self.create_genesis_block()  # First block
    def __init__(self, difficulty=2):  # Set difficulty to 2 or 3
        self.chain = []
        self.difficulty = difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        """Manually create the first block (Genesis Block)"""
        timestamp = time.time()
        genesis_block = Block(0, date.today(), timestamp, "Genesis Block", "0")
        self.chain.append(genesis_block)

    def get_latest_block(self):
        """Return the last block in the chain"""
        return self.chain[-1]

    # def proof_of_work(self, block):
    #     """Find a nonce that produces a hash with the required number of leading zeros"""
    #     while True:
    #         block.current_hash = block.compute_hash()
    #         if block.current_hash.startswith('0' * self.difficulty):
    #             print(f"Proof of Work found: Nonce = {block.nonce}, Hash = {block.current_hash}")
    #             return block.current_hash
    #         block.nonce += 1  # Increment nonce and try again
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
        print("\n Blockchain:")
        for block in self.chain:
            print(f"Index: {block.index}, Hash: {block.current_hash}, Previous Hash: {block.previous_hash}, Nonce: {block.nonce}")
        print("\n")

# Example usage
blockchain = Blockchain(difficulty=2)  # Create a blockchain with a difficulty level

# Add new blocks
blockchain.add_block("Transaction 1: Alice sends Bob 10 coins")
blockchain.add_block("Transaction 2: Bob sends Charlie 5 coins")
blockchain.add_block("i love peanuts")
blockchain.add_block("OK")

# Print the blockchain
blockchain.print_blockchain()