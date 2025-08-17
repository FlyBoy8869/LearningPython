import random
import string
import time
import timeit

start = time.time()
s = "".join([random.choice(string.ascii_letters) for _ in range(85_000_000)])
s = s + "-"
print(f"search string of length {len(s)} took {time.time() - start} seconds to create")

# "".find method
elapsed_time = timeit.timeit("s.find('-')", globals={"s": s}, number=1)
print(f"''.find search took {elapsed_time}")

# re.search method
elapsed_time = timeit.timeit(
    "re.search(r'[-]', s)", setup="import re", globals={"s": s}, number=1
)
print(f"re.search took {elapsed_time}")
