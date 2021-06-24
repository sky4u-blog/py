# pip install tqdm
from tqdm import tqdm, trange
import time

# manual: assign to a variable
# don't forget to call close() at the end

pbar = tqdm(total=100)
for i in range(10):
    time.sleep(.4)
    pbar.update(10)
pbar.close()

print('done')