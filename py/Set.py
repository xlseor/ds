#Array Set Implementation


class Set:
  def __init__(self, elements=[]):
    if type(elements)!=list:
      raise TypeError("Passed non-list object as element list to set init.")
    self.__contents = [None, None]
    self.__size = 0  #the index of the last valid set element is this value minus one, so it is not stored separately. 
    self.__arr_l = 2
    for elem in elements:
      self.insel(elem)
    #set is initialized as the empty set


  #BASIC OPERATIONS:
  
  #grow
  def __grow(self):
     if self.__size == 0:
       self.__arr_l = 2
       self.__contents = [None, None]
       return
     new_len = self.__arr_l*2
     self.__arr_l = new_len
     new_con = [None for k in range(0,new_len)]
     k = 0
     for item in self.__contents:
       new_con[k] = item
       k+=1
     self.__contents = new_con
     return
  #shrink
  def __shrink(self):
    if self.__size == 0:
      self.__arr_l = 2
      self.__contents = [None, None]
    new_len = self.__arr_l // 2
    if self.__size >= self.__arr_l // 4:
      raise IndexError("Called Set.__shrink on overfull array")
    self.__arr_l = new_len
    new_con = [None for k in range(0,new_len)]
    i = 0
    for item in new_con:
      new_con[i] = self.__contents[i]
      i += 1
    self.__contents = new_con
    return

  #contains
  def contains(self, element):
    k = 0
    if self.__size == 0:
      return False
    for elem in self.__contents:
      if k == self.__size:
        break
      if elem == element:
        return True
      k+=1
    return False
  
  #insert element
  def insel(self, element):
    if self.contains(element):
      return
    if self.__size == self.__arr_l:
      self.__grow()
    self.__contents[self.__size]=element
    self.__size+=1
    return
  #remove element
  def remel(self, element):
    n = 0
    if self.__size == 0:
      return
    if self.__size == 1:
      if self.contains(element):
        self.__contents[0] = None
        self.__size = 0
        if self.__arr_l > 8:
          self.__shrink()
      return
    contains = False
    for elem in self.__contents:
      if n  == self.__size:
        break
      if elem == element:
        contains = True
        break
      n+=1
    if contains:
      while n<self.__size-1:
        self.__contents[n] = self.__contents[n+1]
        n+=1
      self.__contents[self.__size-1]=None
      self.__size-=1
      if self.__size<self.__arr_l//8:
        self.__shrink()
    
  #insert list of elements
  def insarr(self, alist):
    if type(alist) != list:
      raise TypeError("Non-list data type passed to list insertion method.")
    for elem in alist:
      self.insel(elem)
    return 

  #get_contents: return array of the contents of a set
  def get_contents(self):
    if self.__size == 0:
      return []
    to_ret = self.__contents[:self.__size]
    return to_ret
  #__del__
  def __del__(self):
    self.__contents = None
    self.__size = None
    self.__arr_l = None

  #__str__
  def __str__(self):
    if self.__size == 0:
      return "{ }"
    arr = self.get_contents()
    stringrep = "{ "
    for elem in arr:
      stringrep = stringrep + str(elem) + ", "
    stringrep = stringrep[:len(stringrep)-2]
    stringrep = stringrep + " }"
    return stringrep

  #SET OPERATIONS

  #union
  #take in two sets, return the union of the two:
  def union(set1, set2):
    if type(set1) != Set or type(set2) != Set:
      raise TypeError("Called set operation on invalid target.")
    union = Set()
    set1 = set1.get_contents()
    set2 = set2.get_contents()
    for elem in set1:
      union.insel(elem)
    for elem in set2:
      union.insel(elem)
    return union

  #intersection
  #take in two sets, returning their intersection:
  def intersect(set1, set2):
    if type(set1) != Set or type(set2) != Set:
      raise TypeError("Called set operation on invalid target.")
    inter = Set()
    set1 = set1.get_contents()
    set2 = set2.get_contents()
    for elem in set1:
      if elem in set2:
        inter.insel(elem)
    return inter
  
  #setminus
  def setminus(set1, set2):
    if type(set1) != Set or type(set2) != Set:
      raise TypeError("Called set operation on invalid target.")
    minussed = Set(set1.get_contents())
    print(minussed)
    for elem in set2.get_contents():
      print(minussed)
      minussed.remel(elem)
      print(minussed)
    return minussed

  #delta
  def delta(set1, set2):
    if type(set1) != Set or type(set2) != Set:
      raise TypeError("Called set operation on invalid target.")
    un = Set.union(set1, set2)
    print(un)
    inter = Set.intersect(set1, set2)
    print(inter)
    delta = Set.setminus(un, inter)
    return delta

  def subset(set1, set2): #return true if set1 is subset of set2, otherwise #false
    if type(set1) != Set or type(set2) != Set:
      raise TypeError("Called set operation on invalid target.")
    g = set1.get_contents()
    cond = True
    for elem in g:
      if not set2.contains(elem):
        cond = False
    return cond
    
  #set equivalence (elements not stored in particular order)
  def equiv(set1, set2):
    if type(set1) != Set or type(set2) != Set:
      raise TypeError("Called set operation on invalid target.")
    if Set.subset(set1, set2) and Set.subset(set2, set1):
      return True
    return False

    
if __name__ == "__main__":
  nub = Set([1,2,3])
  cub = Set([4,2,5,1])
  un = Set.union(nub, cub)
  intr = Set.intersect(nub, cub)
  minus = Set.setminus(nub, cub)
  delt = Set.delta(nub, cub)
  print(str(nub) + " union " + str(cub) + " : " + str(un))
  print(str(nub) + " intersect " + str(cub) + " : " + str(intr))
  print(str(nub) + " - " + str(cub) + " : " + str(minus))
  print(str(nub) + " delta " + str(cub) + " : " + str(delt))

