import sys
import binascii
import numpy as np

assert len(sys.argv) > 1, "Please give at least 1 argument"
print("{:10s}\t  \t{:10s}".format('    fp16', ' hex'))
for i in range(len(sys.argv)-1):
    arg_fp16 = np.fromstring(str(sys.argv[i+1]), dtype=np.float16, sep=" ")
    arg_hex = binascii.hexlify(arg_fp16.byteswap().tostring()).decode('utf-8')
    print("{:10f}\t->\t0x{:10s}".format(arg_fp16[0], arg_hex))
