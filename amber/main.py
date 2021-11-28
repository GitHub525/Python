import os
import sys
import time

def log(msg):
    print("[%s] %s" %(time.asctime(),msg))

class CSplitter:
    def __init__(self,filename):
        self.buf = open(filename,"rb").read()
        self.block_size = 256
    def split(self,directory):
        blocks = len(self.buf) // self.block_size
        for i in range(1,blocks):
            buf = self.buf[:i*self.block_size]
            path = os.path.join(directory,"block_%d"%i)

            log("writing file %s for block %d (until offset 0x%x)"% \
                (path, i, self.block_size * i))
            f = open(path,"wb")
            f.write(buf)
            f.close()
def main(in_path,out_path):
    splitter = CSplitter(in_path)
    splitter.split(out_path)
def usage():
    print("Usage:",sys.argv[0],"<in file> <directory>")

if __name__ == '__main__':
    if len(sys.argv)!=3:
        usage()
    else:
        main(sys.argv[1],sys.argv[2])

