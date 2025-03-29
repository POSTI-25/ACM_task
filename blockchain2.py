import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        """Initialize a block with index, timestamp, data, previous hash, and nonce."""
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.current_hash = self.compute_hash()

    def compute_hash(self):
        """Custom hash function: combines block attributes and transforms them into a unique hash."""
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        
        # Custom hash: sum of ASCII values transformed mathematically
        custom_hash = sum(ord(char) for char in block_string) * 31
        return str(custom_hash)

    def mine_block(self, difficulty):
        """Proof of Work: Adjust nonce until the hash meets the difficulty requirement."""
        while not self.current_hash.startswith("0" * difficulty):  # Ensure hash starts with '00' (for difficulty=2)
            self.nonce += 1
            self.current_hash = self.compute_hash()

        print(f"Block {self.index} mined! Hash: {self.current_hash}")

class Blockchain:
    def __init__(self, difficulty=2):
        """Initialize the blockchain with the Genesis Block"""
        self.chain = []
        self.difficulty = difficulty  # Define mining difficulty
        self.create_genesis_block()

    def create_genesis_block(self):
        """Manually create the first block (Genesis Block)"""
        timestamp = time.time()
        genesis_block = Block(0, timestamp, "Genesis Block", "0")
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

        new_block = Block(new_index, timestamp, data, previous_hash)
        new_block.mine_block(self.difficulty)  # Mine before adding

        self.chain.append(new_block)

    def print_blockchain(self):
        """Print details of all blocks in the blockchain"""
        print("\n🔗 Blockchain:")
        for block in self.chain:
            print(f"Index: {block.index}, Hash: {block.current_hash}, Previous Hash: {block.previous_hash}, Nonce: {block.nonce}")
        print("\n")

# Example usage
blockchain = Blockchain(difficulty=2)  # Create a blockchain with difficulty 2

# Add some blocks
blockchain.add_block("Transaction 1: Alice pays Bob 10 coins")
blockchain.add_block("Transaction 2: Bob pays Charlie 5 coins")

# Print the blockchain
blockchain.print_blockchain()
