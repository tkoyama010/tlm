#  !/usr/bin/python -t
#   -*- coding: utf-8 -*-
import numpy as np

def system(coefficient, element):
  '''
  システムマトリックスの作成
  '''
  if(np.size(coefficient) == 1):
     return coefficient[0]*element
  else:
     system = np.kron(np.diag(coefficient), element)
     index1 = np.size(element[0])*np.arange(1, np.size(coefficient))
     index2 = index1 + 1
     system[index1-1,:] = system[index1-1,:] + system[index2-1,:]
     system[:,index1-1] = system[:,index1-1] + system[:,index2-1]
     system = np.delete(np.delete(system, index2-1, 0), index2-1, 1)
     return system

class glo:
  '''
  全体マトリックス
  '''
  def __init__(self, thi, element):
    self.gam   = thi.gam
    self.mu    = thi.mu
    self.la    = thi.la
    self.H     = thi.H

    self.A     = element.A
    self.BS    = system(coefficient =                 self.mu  / 2., element = element.BS)
    self.BP    = system(coefficient = (self.la + 2. * self.mu) / 2., element = element.BP)
    self.C     = element.C

    self.AS    = system(coefficient = self.mu * self.H / 6., element = self.A)
    self.AP    = system(coefficient = (self.la + 2. * self.mu) * self.H / 6., element = self.A)
    self.BB    = self.BS + self.BP
    self.CS    = system(coefficient =                 self.mu           / self.H, element = self.C)
    self.CP    = system(coefficient = (self.la + 2. * self.mu)          / self.H, element = self.C)
    self.ZE    = self.CP*0.0

