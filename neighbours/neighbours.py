from math import sqrt, pow
import voronoi
from memoize import memoize_sorted

def listOfPoints(list):
  class Point():
    def __init__(self, x1, y1):
      self.x = x1
      self.y = y1
    def __str__(self):
      return "({0}, {1})".format(self.x, self.y)
    def __repr__(self):
      return "({0}, {1})".format(self.x, self.y)
    def x(self):
      return self.x
    def y(self):
      return self.y

  result = []
  for ele in list:
    result.append(Point(ele[0], ele[1]))
  return result

  #------------------------------------------------------------------------------

def findNeighbourOnMinRadiusMultiplyN(pointList, MULTRADIUS=2):
  '''
  Find neigbour for every point in pointlist (point must have .x and .y properties)
  Result is list with tuples, tuple linked with points in pointList by same indexes
  First element in tuple is minRadius of point, which means distance to nearest other point
  Second element in tuple is set of point indexes, which lay in MULTRADIUS*minRadius to point
  [(1.1661903789690602, set([1])), (1.1661903789690602, set([0, 3])), (3.1622776601683795, set([0, 1, 3, 4, 6])), (2.039607805437114, set([0, 1, 2, 4])), (1.4142135623730951, set([3, 5])), (1.4142135623730951, set([4])), (4.47213595499958, set([0, 1, 2, 3, 4, 5]))]

  '''
  threeTuple = voronoi.computeDelaunayTriangulation(pointList)

  @memoize_sorted
  def findDistance(indexPoint1, indexPoint2):
    return sqrt(pow((pointList[indexPoint2].x - pointList[indexPoint1].x), 2) + pow((pointList[indexPoint2].y - pointList[indexPoint1].y), 2))

  #print(findDistance(2, 4), 'dist between i2 and i4 points')
    #   for points = [(2,3), (3,3.6), (4,7), (5,4), (7,2), (8,1), (9,6)]
    #print(findDistance(3, 6))
    #   print(findDistance(4, 6))
    #   print(pointList[3], pointList[4], pointList[6])
    #   for points = [(2,3), (3,3.6), (4,7), (5,4), (7,2), (8,1), (9,6)]
    #         and MULTIRADIUS = 1

  resultListOfDict = [{} for i in range(0, len(pointList))]
  resultNeighbourList = []
  resultNeighbourListWithSets = []

  #get all connections and calc dist
  for tup in threeTuple:
    for i in range(0, 3):
      for j in range(0, 3):
        if i != j:
          resultListOfDict[tup[i]].update({tup[j]:findDistance(tup[i], tup[j])})
  #print(resultListOfDict)

  for iDict, pointConnectionDict in enumerate(resultListOfDict):

    #print(iDict, pointConnectionDict)
    indexPointToCompute = []
    computedIndexPoints = pointConnectionDict.keys()

    #print(pointConnectionDict, pointConnectionDict.keys(), pointConnectionDict.values())

    neighboursMRIndexses = []
    r = min(pointConnectionDict.values())
    mr = r*MULTRADIUS
    #print(r, mr)
    
    for indexPoint in pointConnectionDict.keys():
      '''
      first check nearest points of iDict point
      '''
      #print(indexPoint)
      computedIndexPoints.append(indexPoint)
      if pointConnectionDict[indexPoint] <= mr:
        '''
        if point is neighbour, append linked other points to indexPointToCompute
        also check for already computed points
        '''
        neighboursMRIndexses.append(indexPoint)
        checkIndexes = resultListOfDict[indexPoint].keys()
        for ele in checkIndexes: 
          if ele not in computedIndexPoints:
            indexPointToCompute.append(ele)

      while len(indexPointToCompute) > 0:
        '''
        go through linked to neighbour points and checking if it is neighbour, then add to cycle linked
        to new neighbour points
        '''
        nextIndexPoint = indexPointToCompute.pop(0)
        dist = findDistance(nextIndexPoint, iDict)
        computedIndexPoints.append(nextIndexPoint)
        if dist <= mr:
          neighboursMRIndexses.append(nextIndexPoint)
          checkIndexes = resultListOfDict[nextIndexPoint].keys()
          for ele in checkIndexes: 
            if ele not in computedIndexPoints:
              indexPointToCompute.append(ele)
    '''
    remove duplicates and point whom we calc from neighboursMRIndexses
    '''
    setToAdd = set(neighboursMRIndexses)
    if iDict in setToAdd:
      setToAdd.remove(iDict)
    resultNeighbourList.append((r, neighboursMRIndexses))
    resultNeighbourListWithSets.append((r, setToAdd))
    #print(iDict, neighboursMRIndexses, setToAdd, 'neighbourd', mr)

  return resultNeighbourListWithSets #resultNeighbourList

# points = [(2,3), (3,3.6), (4,7), (5,4), (7,2), (8,1), (9,6)]
  # '''        0      1        2      3      4      5'''
  # a = listOfPoints(points)
  # result = voronoi.computeDelaunayTriangulation(a)
  # print(result)
  # print(a)
  # print(findNeighbourOnMinRadiusMultiplyN(a))

  # from random import randint
  # points2 = []
  # for i in range(1, 100):
  #   points2.append((randint(1,150), randint(1,150)))
  # print(len(points2))
  # print(findNeighbourOnMinRadiusMultiplyN(listOfPoints(points2)))


if __name__ == "__main__":
    import sys

    #example of input.txt
      # 2 3 
      # 3 3.6
      # 4 7
      # 5 4
      # 7 2 
      # 8 1 
      # 9 6

    #neighbours.py input.txt
      #[(1.1661903789690602, set([1])), (1.1661903789690602, set([0, 3])), (3.1622776601683795, 
      #  set([0, 1, 3, 4, 6])), (2.039607805437114, set([0, 1, 2, 4])), (1.4142135623730951, set([3, 5])), 
      #  (1.4142135623730951, set([4])), (4.47213595499958, set([0, 1, 2, 3, 4, 5]))]
    if len(sys.argv) == 2:
      from fileinput import fileToListOfIntFl
      data = fileToListOfIntFl(sys.argv[1])
      result = findNeighbourOnMinRadiusMultiplyN(listOfPoints(data))
      print(result)

    #neighbours.py -l input.txt
      # [[(2, 3), 1.1661903789690602, [(3, 3.6)]], [(3, 3.6), 1.1661903789690602, [(2, 3), (5, 4)]], [(4, 7), 
      # 3.1622776601683795, [(2, 3), (3, 3.6), (5, 4), (7, 2), (9, 6)]], [(5, 4), 2.039607805437114, [(2, 3), 
      # (3, 3.6), (4, 7), (7, 2)]], [(7, 2), 1.4142135623730951, [(5, 4), (8, 1)]], [(8, 1), 1.4142135623730951, 
      # [(7, 2)]], [(9, 6), 4.47213595499958, [(2, 3), (3, 3.6), (4, 7), (5, 4), (7, 2), (8, 1)]]]

    if len(sys.argv) == 3 and sys.argv[1] == '-l':
      from fileinput import fileToListOfIntFl
      data = fileToListOfIntFl(sys.argv[2])
      result = findNeighbourOnMinRadiusMultiplyN(listOfPoints(data))
      listresult = []
      for (i, ele) in enumerate(result):
        setToListOfPoints = list()
        #print(ele)

        if len(ele[1]) > 1:
          for p in ele[1]:
            #print(listOfPoints(data)[p])
            setToListOfPoints += (listOfPoints(data)[p],)
        else:
          a = list(ele[1])
          b = a[0]
          #print(listOfPoints(data)[0])
          setToListOfPoints += [listOfPoints(data)[b]]
        listresult.append([listOfPoints(data)[i], ele[0], setToListOfPoints])
      print(listresult)



    #neighbours.py -i input.txt
      # (1.1661903789690602, set([1]))
      # (1.1661903789690602, set([0, 3]))
      # (3.1622776601683795, set([0, 1, 3, 4, 6]))
      # (2.039607805437114, set([0, 1, 2, 4]))
      # (1.4142135623730951, set([3, 5]))
      # (1.4142135623730951, set([4]))
      # (4.47213595499958, set([0, 1, 2, 3, 4, 5]))
    if len(sys.argv) == 3 and sys.argv[1] == '-i':
      from fileinput import fileToListOfIntFl
      data = fileToListOfIntFl(sys.argv[2])
      result = findNeighbourOnMinRadiusMultiplyN(listOfPoints(data))
      for ele in result:
        print(ele)
    
    #neighbours.py -p input.txt
      # ((2, 3), 1.1661903789690602, [(3, 3.6)])
      # ((3, 3.6), 1.1661903789690602, [(2, 3), (5, 4)])
      # ((4, 7), 3.1622776601683795, [(2, 3), (3, 3.6), (5, 4), (7, 2), (9, 6)])
      # ((5, 4), 2.039607805437114, [(2, 3), (3, 3.6), (4, 7), (7, 2)])
      # ((7, 2), 1.4142135623730951, [(5, 4), (8, 1)])
      # ((8, 1), 1.4142135623730951, [(7, 2)])
      # ((9, 6), 4.47213595499958, [(2, 3), (3, 3.6), (4, 7), (5, 4), (7, 2), (8, 1)])

    if len(sys.argv) == 3 and sys.argv[1] == '-p':
      from fileinput import fileToListOfIntFl
      data = fileToListOfIntFl(sys.argv[2])
      result = findNeighbourOnMinRadiusMultiplyN(listOfPoints(data))
      for (i, ele) in enumerate(result):
        setToListOfPoints = list()
        #print(ele)

        if len(ele[1]) > 1:
          for p in ele[1]:
            #print(listOfPoints(data)[p])
            setToListOfPoints += (listOfPoints(data)[p],)
        else:
          a = list(ele[1])
          b = a[0]
          #print(listOfPoints(data)[0])
          setToListOfPoints += [listOfPoints(data)[b]]
        print(listOfPoints(data)[i], ele[0], setToListOfPoints)

    # implementation with tuple in answer
      #
      # if len(sys.argv) == 3 and sys.argv[1] == '-t':
      #   from fileinput import fileToListOfIntFl
      #   data = fileToListOfIntFl(sys.argv[2])
      #   result = findNeighbourOnMinRadiusMultiplyN(listOfPoints(data))
      #     for (i, ele) in enumerate(result):
      #       setToTupleOfPoints = tuple()
      #       #print(ele)

      #       if len(ele[1]) > 1:
      #         for p in ele[1]:
      #           #print(listOfPoints(data)[p])
      #           setToTupleOfPoints += (listOfPoints(data)[p],)
      #       else:
      #         a = list(ele[1])
      #         b = a[0]
      #         #print(listOfPoints(data)[0])
      #         setToTupleOfPoints += (listOfPoints(data)[b],)
      #       print(listOfPoints(data)[i], ele[0], setToTupleOfPoints)
