# -*- coding: UTF-8 -*-
import numpy as np
class NHWC2NCHW:

  def __init__(self, N, C, H, W):
    self.N = N
    self.C = C
    self.H = H
    self.W = W
  
  #offset_nhwc(n, c, h, w) = n * HWC + h * WC + w * C + c
  #offset_nchw(n, c, h, w) = n * CHW + c * HW + h * W + w
  def convert(self, nhwc_list = [], nchw_list = [], scale = 1.0):
     for n in range(self.N):
       for h in range(self.H):
	 for w in range(self.W):
	   for c in range(self.C):
             nchw_list[n * self.C * self.H * self.W +
                        c * self.H * self.W + h * self.W
                        + w] = nhwc_list[n * self.H 
			       * self.W * self.C + 
			       h * self.W * self.C + w * self.C
			       + c]
			
