# import time

# class Block:
#     def __init__(self, index, timestamp, data, previous_hash, nonce=0):
#         """Initialize a block with index, timestamp, data, previous hash, and nonce."""
#         self.index = index
#         self.timestamp = timestamp
#         self.data = data
#         self.previous_hash = previous_hash
#         self.nonce = nonce
#         self.current_hash = self.compute_hash()

#     def compute_hash(self):
#         """Custom hash function: combines block attributes and transforms them into a unique hash."""
#         block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        
#         # Custom hash: sum of ASCII values transformed mathematically
#         custom_hash = sum(ord(char) for char in block_string) * 31
#         return str(custom_hash)

#     def mine_block(self, difficulty):
#         """Proof of Work: Adjust nonce until the hash meets the difficulty requirement."""
#         while not self.current_hash.startswith("0" * difficulty):  # Ensure hash starts with '00' (for difficulty=2)
#             self.nonce += 1
#             self.current_hash = self.compute_hash()

#         print(f"Block {self.index} mined! Hash: {self.current_hash}")

# class Blockchain:
#     def __init__(self, difficulty=2):
#         """Initialize the blockchain with the Genesis Block"""
#         self.chain = []
#         self.difficulty = difficulty  # Define mining difficulty
#         self.create_genesis_block()

#     def create_genesis_block(self):
#         """Manually create the first block (Genesis Block)"""
#         timestamp = time.time()
#         genesis_block = Block(0, timestamp, "Genesis Block", "0")
#         genesis_block.mine_block(self.difficulty)  # Mine the first block
#         self.chain.append(genesis_block)

#     def get_latest_block(self):
#         """Return the last block in the chain"""
#         return self.chain[-1]

#     def add_block(self, data):
#         """Mine a new block and add it to the blockchain"""
#         previous_block = self.get_latest_block()
#         new_index = previous_block.index + 1
#         timestamp = time.time()
#         previous_hash = previous_block.current_hash

#         new_block = Block(new_index, timestamp, data, previous_hash)
#         new_block.mine_block(self.difficulty)  # Mine before adding

#         self.chain.append(new_block)

#     def print_blockchain(self):
#         """Print details of all blocks in the blockchain"""
#         print("\n🔗 Blockchain:")
#         for block in self.chain:
#             print(f"Index: {block.index}, Hash: {block.current_hash}, Previous Hash: {block.previous_hash}, Nonce: {block.nonce}")
#         print("\n")

# # Example usage
# blockchain = Blockchain(difficulty=2)  # Create a blockchain with difficulty 2

# # Add some blocks
# blockchain.add_block("Transaction 1: Alice pays Bob 10 coins")
# blockchain.add_block("Transaction 2: Bob pays Charlie 5 coins")

# # Print the blockchain
# blockchain.print_blockchain()



# import time
# import random
# from datetime import date

# class Block:
#     def __init__(self, index, date, timestamp, data, previous_hash, nonce=0):
#         self.index = index
#         self.timestamp = timestamp
#         self.date = date
#         self.data = data
#         self.previous_hash = previous_hash
#         self.nonce = nonce
#         self.current_hash = self.compute_hash()  # Compute hash when block is created

#     def compute_hash(self):
#         """
#         Custom hash function: Generates a hexadecimal-like hash using bitwise operations.
#         """
#         block_string = f"{self.index}/{self.date}/{self.timestamp}/{self.data}/{self.previous_hash}/{self.nonce}"
        
#         # Custom hashing logic
#         hash_value = random.randint(0, 111)
#         for char in block_string:
#             hash_value = hash_value + ord(char)  # Shift & Mix
#             hash_value = hash_value + int(bin(random.randint(100, 200))[2:])

#         return hex(hash_value)[2:]  # Remove '0x' prefix

#     def mine_block(self, difficulty):
#         """
#         Proof of Work: Adjust nonce until the hash starts with '0' * difficulty.
#         """
#         while not self.current_hash.startswith("0" * difficulty):
#             self.nonce += 1
#             self.current_hash = self.compute_hash()

#         print(f"Block {self.index} mined! Hash: {self.current_hash}")



# class Blockchain:
#     def __init__(self, difficulty=2):
#         """Initialize the blockchain with the Genesis Block and set mining difficulty"""
#         self.chain = []  # List to store blocks
#         self.difficulty = difficulty  # Set mining difficulty
#         self.create_genesis_block()

#     def create_genesis_block(self):
#         """Manually create the first block (Genesis Block)"""
#         timestamp = time.time()
#         genesis_block = Block(0, date.today(), timestamp, "Genesis Block", "0")
#         genesis_block.mine_block(self.difficulty)  # Mine the first block
#         self.chain.append(genesis_block)

#     def get_latest_block(self):
#         """Return the last block in the chain"""
#         return self.chain[-1]

#     def add_block(self, data):
#         """Mine a new block and add it to the blockchain"""
#         previous_block = self.get_latest_block()
#         new_index = previous_block.index + 1
#         timestamp = time.time()
#         previous_hash = previous_block.current_hash

#         new_block = Block(new_index, date.today(), timestamp, data, previous_hash)
#         new_block.mine_block(self.difficulty)  # Mine before adding

#         self.chain.append(new_block)

#     def print_blockchain(self):
#         """Print details of all blocks in the blockchain"""
#         print("\n🔗 Blockchain:")
#         for block in self.chain:
#             print(f"Index: {block.index}, Hash: {block.current_hash}, Previous Hash: {block.previous_hash}, Nonce: {block.nonce}")
#         print("\n")


# blockchain = Blockchain(difficulty=2)  # Set difficulty level

# # Add some blocks
# blockchain.add_block("Transaction 1: Alice pays Bob 10 coins")
# blockchain.add_block("Transaction 2: Bob pays Charlie 5 coins")

# # Print the blockchain
# blockchain.print_blockchain()

'''
# # Example usage
# blockchain = Blockchain()  # Create a blockchain

# # Add new blocks
# blockchain.add_block("Transaction 1: Alice sends Bob 10 coins")
# blockchain.add_block("Transaction 2: Bob sends Charlie 5 coins")

# # Print the blockchain
# blockchain.print_blockchain()
'''


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

    '''
    def compute_hash(self):
        """
        Custom deterministic hash function: Generates a hexadecimal-like hash using bitwise operations.
        """
        block_string = f"{self.index}/{self.date}/{self.timestamp}/{self.data}/{self.previous_hash}/{self.nonce}"
        
        # Deterministic custom hashing logic
        hash_value = 0
        for char in block_string:
            hash_value = (hash_value * 31 + ord(char)) % (2**32)  # Ensures hash remains within a 32-bit range
        
        return hex(hash_value)[2:]  # Convert to hexadecimal and remove '0x' prefix
    '''

    def compute_hash(self):
        """
        Custom hash function that ensures a more distributed hash output.
        Uses bitwise operations and mixing techniques for randomness.
        """
        block_string = f"{self.index}/{self.date}/{self.timestamp}/{self.data}/{self.previous_hash}/{self.nonce}"
    
        hash_value = 0  
        for char in block_string:
            hash_value = ((hash_value << 5) - hash_value) + ord(char)  # Bitwise left shift & mix
            hash_value = hash_value & 0xFFFFFFFF  # Ensure it's within 32-bit range
    
        # Convert to a hex string with a fixed length
        return f"{hash_value:08x}"  # Ensures a 8-character hex output


    '''# def mine_block(self, difficulty):
    #     """
    #     Proof of Work: Adjust nonce until the hash starts with '0' * difficulty.
    #     """
    #     while not self.current_hash.startswith("0" * difficulty):
    #         self.nonce += 1
    #         self.current_hash = self.compute_hash()

    #     print(f"Block {self.index} mined! Hash: {self.current_hash}")'''
    def mine_block(self, difficulty):
        while not self.current_hash.startswith("0" * difficulty):
            self.nonce += 1
            self.current_hash = self.compute_hash()
            print(f"Trying nonce {self.nonce}: {self.current_hash}")  # Debugging


class Blockchain:
    def __init__(self, difficulty=2):
        """Initialize the blockchain with the Genesis Block and set mining difficulty"""
        self.chain = []  # List to store blocks
        self.difficulty = difficulty  # Set mining difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        """Manually create the first block (Genesis Block)"""
        timestamp = time.time()
        genesis_block = Block(0, date.today(), timestamp, "Genesis Block", "0")
        genesis_block.mine_block(self.difficulty)  # Mine the first block
        self.chain.append(genesis_block)

    def get_latest_block(self):
        """Return the last block in the chain"""
        return self.chain[-1]

    def add_block(self, data):
        """Mine a new block and add it to the blockchain"""
        previous_block = self.get_latest_block()
        new_index = previous_block.index + 1
        timestamp = time.time()
        previous_hash = previous_block.current_hash

        new_block = Block(new_index, date.today(), timestamp, data, previous_hash)
        new_block.mine_block(self.difficulty)  # Mine before adding

        self.chain.append(new_block)

    def print_blockchain(self):
        """Print details of all blocks in the blockchain"""
        print("\n🔗 Blockchain:")
        for block in self.chain:
            print(f"Index: {block.index}, Hash: {block.current_hash}, Previous Hash: {block.previous_hash}, Nonce: {block.nonce}")
        print("\n")

# Create Blockchain with mining difficulty 2
blockchain = Blockchain(difficulty=2)

# Add new blocks
blockchain.add_block("Transaction 1: Alice pays Bob 10 coins")
blockchain.add_block("Transaction 2: Bob pays Charlie 5 coins")

# Print the blockchain
blockchain.print_blockchain()
