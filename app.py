import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add(a, b):
    logging.info("Addition operation performed")
    return a + b

# Example usage
if __name__ == "__main__":
    result = add(5, 3)
    print("Result:", result)