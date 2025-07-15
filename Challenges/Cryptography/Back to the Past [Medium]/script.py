import random
from datetime import datetime, timezone

FLAG = b'actf{example_flag}'
SEED = int(datetime.now(timezone.utc).timestamp())
random.seed(SEED)

key = bytes([random.randint(0, 255) for _ in range(len(FLAG))])
encrypted_flag = bytes([a ^ b for a, b in zip(FLAG, key)])

with open('flag.enc', 'wb') as f:
    f.write(encrypted_flag)
