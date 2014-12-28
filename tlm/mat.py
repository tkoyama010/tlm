#  !/usr/bin/python -t
#   -*- coding: utf-8 -*-
import numpy

def link(K, i):
  '''
  剛性マトリックスKにおいてi番目とj番目の節点を結合(link)する
  '''
  j = i + 1
  K[i-1,:] = K[i-1,:] + K[j-1,:]
  K[:,i-1] = K[:,i-1] + K[:,j-1]
  K      = numpy.delete(numpy.delete(K, j-1, 0), j-1, 1)
  return K

def system(coefficient, element):
  '''
  システムマトリックスの作成
  '''
  if(numpy.size(coefficient) == 1):
     return coefficient[0]*element
  else:
     return link(numpy.kron(numpy.diag(numpy.array(coefficient)), element), numpy.size(element[0])*numpy.array(range(1, numpy.size(coefficient))))

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
