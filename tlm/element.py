#  !/usr/bin/python -t
#   -*- coding: utf-8 -*-
import numpy as np

class dimension1:
  '''
  要素マトリックス
  '''
  def __init__(self):

    self.A  = np.array([[ 2.,  1.], \
                        [ 1.,  2.]])

    self.BS = np.array([[-3., -1.], \
                        [ 1.,  3.]])

    self.BP = np.array([[ 1.,  1.], \
                        [-1., -1.]])

    self.C  = np.array([[ 1., -1.], \
                        [-1.,  1.]])

    self.MR = np.array([[2, 1], [1, 2]])

    self.MC = np.array([[3, 0], [0, 3]])

class dimension2:
  '''
  ２次の要素マトリックス
  '''
  def __init__(self):

    self.A  = np.array([[ 4.,  2., -1.], \
                        [ 2., 16.,  2.], \
                        [-1.,  2.,  4.]])

    self.BS = np.array([[-9., -4.,  1.], \
                        [ 4.,  0., -4.], \
                        [-1.,  4.,  9.]])

    self.BP = np.array([[ 3.,  4., -1.], \
                        [-4.,  0.,  4.], \
                        [ 1., -4., -3.]])

    self.C  = np.array([[ 7., -8.,  1.], \
                        [-8., 16., -8.], \
                        [ 1., -8.,  7.]])
