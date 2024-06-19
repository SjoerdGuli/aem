import random

def generate_unique_random_sequence():
    return random.sample(range(1, 6), 5)

random_sequence = generate_unique_random_sequence()
print(random_sequence)
import random

def generate_unique_random_sequence():
    return random.sample(range(1, 6), 5)

# Generate 20 random sequences
for _ in range(20):
    random_sequence = generate_unique_random_sequence()
    print(random_sequence)
