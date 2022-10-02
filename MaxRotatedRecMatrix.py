class MaxRotatedRecMatrix:
    ''' 
    Max sum of rotated 45 degree rectanglular matrix - primary or secondary diagonally rotated 
    '''
    def __init__(self,a,b,matrix):
      self.a=a
      self.b=b
      self.matrix=matrix

    def getMaxRotatedRectSum(self):
      # https://leetcode.com/discuss/interview-question/1482150/rotatedrectsum-codesignal-quora-two-sigma-oa
      # https://leetcode.com/problems/rotate-image/
      
      