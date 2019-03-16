# -*- coding: UTF-8 -*-
import numpy as np
from nhwc2nchw import NHWC2NCHW

srcfile = "data/nhwc.txt"
targetfile = "data/nchw.txt"
N = 2
C = 2
H = 5
W = 4
format_conv = NHWC2NCHW(2, 2, 5, 4)
with open(srcfile) as src:
  with open(targetfile, 'w') as target:
    src_list = []
    target_list = np.zeros(N*C*H*W)
    sep = " "
    for line in src:
      src_list = src_list + line.strip().split(sep)
    format_conv.convert(src_list, target_list)
    target.write(str(target_list))
    #np.savetxt(targetfile,target_list)


