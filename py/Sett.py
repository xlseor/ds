#This is an array implementation of a set object.
#It is optimized for efficient memory allocation as opposed to speed.

#Definition

class Set:
  def __init__(self, elements):
    if type(elements) != list
      raise TypeError("Initialized Set with non-list elements array")
    self.__size = len(elements)
    self.__array_length = self.__size*2
    self.__contents = [None for k in range(0, self.__array_length)] #contents is
    #double the length of the number of elements in it, to begin
    #and doubles with earch overrun.
    k=0
    while k < self.length:
      self.__contents[k]=elements[k]   

#enlarge
  def __enlarge(self):
    new_arr_l = self.__array_length*2
    new_con = [None for k in range(0,new_arr_l)]
    i = 0
    for item in self.__contents:
      new_con[i] = item
      i+=1
    self.__contents = new_con
    
#remove_element -- this is needed, we can't just use remove, because it ruins
#the memory-optimized order
  def __remove(self, elem):
    for e in self.__contents:
      if e == elem:
        remove
#insert_element -- insertion function

  
    
#shrink
  def __shrink(self):
    if self.__size >= self.__array_length // 8:
      raise IndexError("called Set __shrink on set with overfull array")
    a = self.__array_length // 4
    new_con = [None for k in range(0,a)]
    k=0
    for elem in self.__contents:
      new_con[k] = self.__contents[k]
      k+=1
    self.__contents = new_con
    self.__array_length = a
#get_elements
  def get_elements(self):
    return self.__contents
#get_length
  def get_size(self):
    return self.__size

#get_array_length
  def __get_array_length(self):
    return self.__array_length

#insert

  def insert_element(self, element): #takes in element, which is any python object
    if element in self.__contents:
      return
    if self.__size == self.__array_length:
      self.__enlarge()
    self.__contents[self.__size]=element
    self.__size+=1
    return
    
#delete

  def delete_element(self, element): #takes in element, which is any python object
    if element not in self.__contents:
      return
    self.__contents.__remove(element)
    #shrink self.__contents if it is less that 1/8 full
    if self.__size < self.array_length // 8
      self.__shrink()
      
#union:
#takes two sets as parameters and returns the union of these sets
  def union(set1, set2):
    union = Set(set_1.get_elements())
    for elem in set2.get_elements()
      union.insert(element)
    return union    
  
#intersect
  def intersect(set1, set2) #take in two sets as parameters and return
    #their intersection
    intersect = set1.get_elements()
    compare = set2.get_elements()
    for elem in intersect:
      if elem not in compare:
        intersect.remove(elem)
    intersect = Set(intersect)
    return intersect

#setminus -- subtract second set from the first and return result

  def setminus(set1, set2):
    arr1 = set1.get_elements()
    arr2 = set2.get_elements()
    for elem in arr1:
      if elem in arr2:
        arr1.remove(elem)
    minus = Set(arr1)
    return minus
    

#delta (return elements of both sets not in intersect)

  def delta(set1, set2):
    intersect = Set.intersect(set1, set2)
    union = Set.union(set1, set2)
    return Set.setminus(union, intersect)

#get_cardinality
  def get_cardinality(self):
    return self.__size

#delete set
  def __del__(self):
    return None
#string method
  def __str__(self): #return string representation of the set. elements are
    #separated by a comma and a space.
    str_rep = "{ "
    for elem in self.__contents:
      str_rep = str_rep + str(elem) + ", "
    str_rep = str_rep[:len(str_rep)-2]
    str_rep = str_rep + " }"
    return str_rep
    


