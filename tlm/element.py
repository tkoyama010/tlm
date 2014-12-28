#  !/usr/bin/python -t
#   -*- coding: utf-8 -*-
import numpy

class dimension1:
  '''
  要素マトリックス
  '''
  def __init__(self):

    self.A  = numpy.array([[ 2.,  1.], \
                           [ 1.,  2.]])

    self.BS = numpy.array([[-3., -1.], \
                           [ 1.,  3.]])

    self.BP = numpy.array([[ 1.,  1.], \
                           [-1., -1.]])

    self.C  = numpy.array([[ 1., -1.], \
                           [-1.,  1.]])

    self.MR = numpy.array([[2, 1], [1, 2]])

    self.MC = numpy.array([[3, 0], [0, 3]])

class dimension2:
  '''
  ２次の要素マトリックス
  '''
  def __init__(self):

    self.A  = numpy.array([[ 4.,  2., -1.], \
                           [ 2., 16.,  2.], \
                           [-1.,  2.,  4.]])

    self.BS = numpy.array([[-9., -4.,  1.], \
                           [ 4.,  0., -4.], \
                           [-1.,  4.,  9.]])

    self.BP = numpy.array([[ 3.,  4., -1.], \
                           [-4.,  0.,  4.], \
                           [ 1., -4., -3.]])

    self.C  = numpy.array([[ 7., -8.,  1.], \
                           [-8., 16., -8.], \
                           [ 1., -8.,  7.]])
