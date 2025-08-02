import numpy as np
# Uniform distribution (0 to 1)
rand_nums = np.random.rand(5)
print("Random numbers [0,1):", rand_nums)

# Integers between 10 and 50
rand_ints = np.random.randint(10, 50, size=5)
print("Random integers between 10 and 50:", rand_ints)

# Normal distribution (mean=0, std=1)
normal_dist = np.random.randn(5)
print("Normal distribution:", normal_dist)
