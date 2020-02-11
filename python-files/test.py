import time
import sys
from tqdm import tqdm
from contextlib import redirect_stdout


# Class to redirect standard output, replacing #p{percentage} with progress bar
# to use : sys.stdout=OutHandler(sys.stdout)
class OutHandler:
    def __init__(self, out):
        self.out = out
        self.buffer = ""
        self.suspend = False
        # tqdm progress bar
        self.tqdm = None
        self.value = 0

    # writes string. Strings containing #p are transformed into a progress bar
    def write(self, string):
        if string.startswith("#p"):
            self.suspend = True
        if self.suspend:
            self.buffer += string
        else:
            self.out.write(string)
        if self.suspend and "\n" in string:
            try:
                start = self.buffer.index("#p")
                end = self.buffer.index("\n", start)
                part = self.buffer[start + 2:end]
                x = float(part)
                v = int(x * 1000)
                if v != self.value:
                    sys.stdout = self.out
                    if self.tqdm is None:
                        self.tqdm = tqdm(total=1000)
                    self.tqdm.update(n=v - self.value)
                    sys.stdout = self
                    self.value = v
            except:
                pass
            self.suspend = False
            self.buffer = ""

    def flush(self):
        self.out.flush()


# sums integers from 0 to 999 and sleeps a lot
def compute():
    print("computing")
    sum = 0
    for i in range(1000):
        if i ==500 :
            return 1/0
        print('#p', i / 1000)
        time.sleep(0.01)
        sum += i
        if i % 100 == 0:
            print(f"for the moment the sum is {sum}")
    print("finished computing")
    print("final sum", sum)


# MAIN SCRIPT
out = OutHandler(sys.stdout)
with redirect_stdout(out):
    compute()
    # exec(open("facts.py").read())
