This repo contain anwers for 2 different algorhythmic tasks.


neighbours
      For every point in list find its Radius (= distance to nearest other point) and neighbours (by default
      points in Radius * 2, can be changed calling function findNeighbourOnMinRadiusMultiplyN with second optional parametr)
     
      Result:
       Result is list with tuples, tuple linked with points in pointList by same indexes
       First element in tuple is minRadius of point, which means distance to nearest other point
       Second element in tuple is set of point indexes, which lay in MULTRADIUS*minRadius to point
   
    USAGE:
  
    * as module
      import neighbours.py
      list = [(2,3), (3,3.6), (4,7), (5,4), (7,2), (8,1), (9,6)]
      result = findNeighbourOnMinRadiusMultiplyN(listOfPoints(list))
      print(result)
      >>>[(1.1661903789690602, set([1])), (1.1661903789690602, set([0, 3])), (3.1622776601683795, 
      >>>  set([0, 1, 3, 4, 6])), (2.039607805437114, set([0, 1, 2, 4])), (1.4142135623730951, set([3, 5])), 
      >>>  (1.4142135623730951, set([4])), (4.47213595499958, set([0, 1, 2, 3, 4, 5]))]
  
    * command-line
    
    
      - raw result
      
        python neighbours.py input.txt
        >>>[(1.1661903789690602, set([1])), (1.1661903789690602, set([0, 3])), (3.1622776601683795, 
        >>>  set([0, 1, 3, 4, 6])), (2.039607805437114, set([0, 1, 2, 4])), (1.4142135623730951, set([3, 5])), 
        >>>  (1.4142135623730951, set([4])), (4.47213595499958, set([0, 1, 2, 3, 4, 5]))]
    
    
      - tuple of points x,y instead of point indexes
      
        python neighbours.py -l input.txt
        >>>[[(2, 3), 1.1661903789690602, [(3, 3.6)]], [(3, 3.6), 1.1661903789690602, [(2, 3), (5, 4)]], [(4, 7), 
        >>>3.1622776601683795, [(2, 3), (3, 3.6), (5, 4), (7, 2), (9, 6)]], [(5, 4), 2.039607805437114, [(2, 3), 
        >>>(3, 3.6), (4, 7), (7, 2)]], [(7, 2), 1.4142135623730951, [(5, 4), (8, 1)]], [(8, 1), 1.4142135623730951, 
        >>>[(7, 2)]], [(9, 6), 4.47213595499958, [(2, 3), (3, 3.6), (4, 7), (5, 4), (7, 2), (8, 1)]]]
      
      
      - raw result, index of line = index of point  
      
        python neighbours.py -i input.txt
        >>>(1.1661903789690602, set([1]))
        >>>(1.1661903789690602, set([0, 3]))
        >>>(3.1622776601683795, set([0, 1, 3, 4, 6]))
        >>>(2.039607805437114, set([0, 1, 2, 4]))
        >>>(1.4142135623730951, set([3, 5]))
        >>>(1.4142135623730951, set([4]))
        >>>(4.47213595499958, set([0, 1, 2, 3, 4, 5]))

      - tuple of points x,y result, index of line = index of point
      
        python neighbours.py -p input.txt
        >>>((2, 3), 1.1661903789690602, [(3, 3.6)])
        >>>((3, 3.6), 1.1661903789690602, [(2, 3), (5, 4)])
        >>>((4, 7), 3.1622776601683795, [(2, 3), (3, 3.6), (5, 4), (7, 2), (9, 6)])
        >>>((5, 4), 2.039607805437114, [(2, 3), (3, 3.6), (4, 7), (7, 2)])
        >>>((7, 2), 1.4142135623730951, [(5, 4), (8, 1)])
        >>>((8, 1), 1.4142135623730951, [(7, 2)])
        >>>((9, 6), 4.47213595499958, [(2, 3), (3, 3.6), (4, 7), (5, 4), (7, 2), (8, 1)])

inttokpartition
    Calculate how many unic partitons of integers with exactly k elements can be
  
    USAGE:
    First parameter: n = integer to partioning
    Second parameter: k = elements of partition
    
    
    * as module
      import inttokpartition.py
      result = calcIntegerExactlyKPartition(6, 3)
      print(result)
      >>> 3
      
      
    * command-line
      
      - one pair of numbers per run
        
        python inttokpartition.py 150 100
        >>> 158
  
      - read parameters from file (2 per line)
      
        python inttokpartition.py -f input.txt
        >>> 3
        >>> 158
        
