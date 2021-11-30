
#Set Tester for python array set implementation
import unittest
from Set import Set
#Tests By Category

#1: Basic Functionalities
# functions
#init
class SetTesting(unittest.TestCase):
  def setUp(self):
    self.Set = Set()
    
  def test_empty_init(self):
    case = Set()
    self.assertEqual(str(case), '{ }')
    
  def test_full_init(self):
    case = Set([1,2,3,4,5])
    self.assertEqual(str(case), '{ 1, 2, 3, 4, 5 }')
    
  def test_initialization_exceptions(self):
    with self.assertRaises(TypeError):
      case = Set('r')
    with self.assertRaises(TypeError):
      case = Set(3)
    with self.assertRaises(TypeError):
      case = Set({'b', 'p'})
    with self.assertRaises(TypeError):
      case = Set((5,6,7))

#insertion and removal

  def testSingleInsertionSingleRemoval(self):
    self.Set.insel('4')
    self.assertEqual(str(self.Set), '{ 4 }')
    self.Set.remel('4')
    self.assertEqual(str(self.Set), '{ }')

  def testRemovalFromEmpty(self):
    self.Set.remel(5)
    self.assertEqual(str(self.Set), '{ }')

  def testRemoveNoncontainedElement(self):
    self.Set.insel(5)
    self.Set.insel(6)
    self.Set.remel(2)
    self.assertEqual(str(self.Set), '{ 5, 6 }')

  def testIdempotentRemovalCenter(self):
    self.Set.insel(7)
    self.Set.insel(8)
    self.Set.insel(9)
    self.assertEqual(str(self.Set), '{ 7, 8, 9 }')
    self.Set.remel(7)
    self.assertEqual(str(self.Set), '{ 8, 9 }')
    self.Set.remel(7)
    self.assertEqual(str(self.Set), '{ 8, 9 }')

  def testIdempotentRemovalTrailing(self):
    self.Set.insel(5)
    self.Set.insel(6)
    self.Set.insel(7)
    self.Set.insel(8)
    self.Set.remel(8)
    self.assertEqual(str(self.Set), '{ 5, 6, 7 }')
    self.Set.remel(8)
    self.assertEqual(str(self.Set), '{ 5, 6, 7 }')

  def testIdempotentRemovalLeading(self):
    self.Set.insel(5)
    self.Set.insel(6)
    self.Set.insel(8)
    self.Set.insel('k')
    self.Set.insel('q')
    self.Set.remel(5)
    self.assertEqual(str(self.Set), '{ 6, 8, k, q }')
    self.Set.remel(5)
    self.assertEqual(str(self.Set), '{ 6, 8, k, q }')

  def testRemovalToEmpty(self):
    self.Set.remel(6)
    self.Set.remel('q')
    self.Set.remel(8)
    self.Set.remel('k')
    self.assertEqual(str(self.Set), '{ }')

#contains

  def testContainsOnEmpty(self):
    self.assertEqual(self.Set.contains(None), False)

  def testContainsOnEmptyAfterSingleInsertRemove(self):
    self.Set.insel(3)
    self.Set.remel(3)
    self.assertEqual(self.Set.contains(None), False)

  def testContainsOnEmptyAfterDoubleRemove(self):
    self.Set.insel(4)
    self.Set.insel(5)
    self.Set.remel(5)
    self.Set.remel(4)
    self.assertEqual(self.Set.contains(None), False)

  def testContainsSingleElement(self):
    self.Set.insel(7)
    self.assertEqual(self.Set.contains(7), True)

  def testContainsLeadingMiddleTrailing(self):
    self.Set.insel(1)
    self.Set.insel(2)
    self.Set.insel(3)
    self.assertEqual(self.Set.contains(1), True)
    self.assertEqual(self.Set.contains(2), True)
    self.assertEqual(self.Set.contains(3), True)

  def testNotContainedAfterRemovalLargeSet(self):
    self.Set.insel(1)
    self.Set.insel(2)
    self.Set.insel(3)
    self.Set.insel(4)
    self.Set.insel(5)
    self.Set.remel(3)
    self.Set.remel(1)
    self.Set.remel(5)
    self.assertEqual(self.Set.contains(1), False)
    self.assertEqual(self.Set.contains(2), True)
    self.assertEqual(self.Set.contains(3), False)
    self.assertEqual(self.Set.contains(4), True)
    self.assertEqual(self.Set.contains(5), False)

  def testNotContainedAfterRemovalSmallSet(self):
    self.Set.insel(1)
    self.Set.insel(2)
    self.Set.insel(3)
    self.Set.remel(3)
    self.Set.remel(1)
    self.Set.remel(2)
    self.assertEqual(self.Set.contains(3), False)
    self.assertEqual(self.Set.contains(2), False)
    self.assertEqual(self.Set.contains(1), False)

  def testContainedSingleElementInsertRemove(self):
    self.Set.insel(1)
    self.Set.remel(1)
    self.assertEqual(self.Set.contains(1), False)
    self.Set.insel(1)
    self.assertEqual(self.Set.contains(1), True)

  def containsSetOfThree(self):
    self.Set.insel(1)
    self.Set.insel(2)
    self.Set.insel(3)
    self.assertEqual(self.Set.contains(1), True)
    self.assertEqual(self.Set.contains(2), True)
    self.assertEqual(self.Set.contains(3), True)


#get elements

  def testGetElementsFromEmptySet(self):
    self.assertEqual(self.Set.get_contents(), [])

  def testGetElementsFromEmptySetInsertRemove(self):
    self.Set.insel(1)
    self.Set.remel(1)
    self.assertEqual(self.Set.get_contents(), [])

  def testGetContentsNormalcy(self):
    self.Set.insel(1)
    self.Set.insel(2)
    self.Set.insel(3)
    self.Set.insel(4)
    self.Set.insel(5)
    self.assertEqual(self.Set.get_contents(), [1,2,3,4,5])

  def testGetContentsAfterInsertRemoveLargeSet(self):
    self.Set.insel(1)
    self.Set.insel(2)
    self.Set.insel(3)
    self.Set.insel(4)
    self.Set.insel(5)
    self.Set.remel(1)
    self.Set.remel(3)
    self.Set.remel(5)
    self.assertEqual(self.Set.get_contents(), [2,4])
    
#Giant Set

  def testBuildAndBreakDownVeryLargeSet(self):
    grit = [k for k in range(0,150)]
    for k in grit:
      self.Set.insel(k)
    for k in grit:
      self.assertEqual(self.Set.contains(k), True)
    for k in grit:
      self.Set.remel(k)
    self.assertEqual(str(self.Set), '{ }')
    for k in grit:
      self.assertEqual(self.Set.contains(k), False)
#2: Set Operations

  #subset

  def testEmptySetSubsetOfItself(self):
    case = Set()
    self.assertEqual(Set.subset(case, self.Set), True)

  def testEmptySetSubsetOfFullSet(self):
    case = Set([None, '12'])
    self.assertEqual(Set.subset(self.Set, case), True)

  def testSubsetNormalcy(self):
    case = Set([1,2,3,4,5])
    for k in [1,3,5]:
      self.Set.insel(k)
    self.assertEqual(Set.subset(self.Set, case), True)

  def testSubsetFalsityOneElemEmpty(self):
    case = Set([1])
    self.assertEqual(Set.subset(case, self.Set), False)

  def testSubsetFalsityFullEmpty(self):
    case = Set([1,2,3,4,5])
    self.assertEqual(Set.subset(case, self.Set), False)

  def testSubsetFalsityOneElementOff(self):
    set1 = Set([1,2,3])
    set2 = Set([2,3,4])
    self.assertEqual(Set.subset(set1, set2), False)

  def testSubsetFalsityOneElement(self):
    set1 = Set([1])
    set2 = Set([2])
    self.assertEqual(Set.subset(set1, set2), False)

  #equivalence

  def testEquivalenceOfEmptySets(self):
    set1 = Set()
    set2 = Set()
    self.assertEqual(Set.equiv(set1, set2), True)

  def testEquivalenceOfSingleElementSets(self):
    set1 = Set([1])
    set2 = Set([2])
    self.assertEqual(Set.equiv(set1,set2), False)

  def testEquivalenceOfMultipleElementSets(self):
    set1 = Set([1,2,3,4,5, 'blue'])
    set2 = Set([1,2,3,4,5, 'blue'])
    self.assertEqual(Set.equiv(set1, set2), True)

  def testEquivalenceOfEmptySetAndFullSet(self):
    set1 = Set([4,5,6])
    self.assertEqual(Set.equiv(self.Set, set1), False)
    

  def testCommutativityOfEquivalence(self):
    set1 = Set([1,2,3])
    set2 = Set([1,2,3])
    set3 = Set([1,2,3,4])
    self.assertEqual(Set.equiv(set1, set2), Set.equiv(set2, set1))
    self.assertEqual(Set.equiv(set1, set3), Set.equiv(set3, set1))
  
  def testNonEquivalenceLargeSets(self):
    set1 = Set([k for k in range(1,100)])
    set2 = Set([k for k in range(1,100)])
    set2.remel(14)
    set2.insel("bleeble")
    self.assertEqual(Set.equiv(set2, set1), False)
    
  def testEquivalenceOfNonEmptySingletonSetWithItself(self):
    self.Set.insel(2)
    self.assertEqual(Set.equiv(self.Set, self.Set), True)

  def testEquivalenceOfNonEmptyMediumSetWithItself(self):
    for k in range (0,12):
      self.Set.insel(k)
    self.assertEqual(Set.equiv(self.Set, self.Set), True)

  def testEquivalenceOfNonEmptyLargeSetWithItself(self):
    for k in range (0,100):
      self.Set.insel(k)
    self.assertEqual(Set.equiv(self.Set, self.Set), True)
  #union

  def testUnionOfTwoEmptySets(self):
    case = self.Set
    self.Set = Set.union(self.Set, case)
    self.assertEqual(str(self.Set), '{ }')

  def testUnionOfSingletonSetWithEmptySet(self):
    case = Set()
    self.Set.insel(8)
    self.Set = Set.union(self.Set, case)
    self.assertEqual(str(self.Set), '{ 8 }')

  def testCommutativityOfUnionFullSets(self):
    set1 = Set([1,2,3,4,5])
    set2 = Set([3,4,5,6,7])
    self.assertEqual(Set.equiv(Set.union(set1, set2), Set.union(set2, set1)), True) 

  def testCommutativityOfUnionFullEmpty(self):
    set1 = Set([1,2])
    set2 = Set()
    self.assertEqual(Set.equiv(Set.union(set1, set2), Set.union(set2, set1)), True)
                         
  def testUnionOverlappingSets(self):
    set1 = Set([1,2,3,4])
    set2 = Set([3,4,5,6])
    case = Set.union(set1, set2)
    case2 = Set([1,2,3,4,5,6])
    self.assertEqual(Set.equiv(case, case2), True)

  def testUnionOfSetsWithThemselves(self):
    set1 = Set([6,7,4,3,8,9])
    case = Set.union(set1, set1)
    self.assertEqual(Set.equiv(case, set1), True)

  def testIdempotenceOfUnionSmallSet(self):
    set1 = Set()
    set2 = Set([5])
    case1 = Set.union(set1, set2)
    case2 = Set.union(case1, set2)
    self.assertEqual(Set.equiv(case1, case2), True)
    
  def testIdempotenceOfUnionLargeSet(self):
    set1 = Set([k for k in range(0,50)])
    set2 = Set([j for j in range(32,96)])
    case1 = Set.union(set1, set2)
    case2 = Set.union(case1, set2)
    self.assertEqual(Set.equiv(case1, case2), True)
    
  #intersect

  def testIntersectEmptySets(self):
    set1 = Set()
    set2 = Set()
    case = Set.intersect(set1, set2)
    self.assertEqual(str(case), '{ }')
    
  def testIntersectEmptyAndFull(self):
    set1 = Set()
    set2 = Set([2,3,4])
    case = Set.intersect(set1, set2)
    self.assertEqual(str(case), '{ }')

  def testIntersectNonOverlappingSets(self):
    set1 = Set([4,5,6])
    set2 = Set([1,2,3])
    case = Set.intersect(set1, set2)
    mark = Set()
    cond = Set.equiv(case, mark)
    self.assertEqual(cond, True)
    
  def testIntersectPartiallyOverlappingSets(self):
    set1 = Set([4,5,6])
    set2 = Set([8,6,4])
    case = Set.intersect(set1, set2)
    mark = Set([4,6])
    cond = Set.equiv(case, mark)
    self.assertEqual(cond, True)

  def testIntersectFullyOverlappingSets(self):
    set1 = Set([7,8,9])
    set2 = Set([7,8,9])
    case = Set.intersect(set1, set2)
    mark = Set([9,7,8])
    cond = Set.equiv(case, mark)
    self.assertEqual(cond, True)

  def testIntersectSetWithItself(self):
    set1 = Set([1,2,3])
    cond = Set.equiv(set1, set1)
    self.assertEqual(cond, True)
  
  def testCommutativityOfIntersectEmptyFull(self):
    set1 = Set()
    set2 = Set([1,2,3])
    intr1 = Set.intersect(set1, set2)
    intr2 = Set.intersect(set2, set1)
    cond = Set.equiv(intr1, intr2)
    self.assertEqual(cond, True)

  def testCommutativityOfIntersectFull(self):
    set1 = Set([1,2,3,4,5])
    set2 = Set([2,3,5,1,7,12])
    intr1 = Set.intersect(set1, set2)
    intr2 = Set.intersect(set2, set1)
    cond = Set.equiv(intr1, intr2)
    self.assertEqual(cond, True)    

  #setminus

  def testSetminusOfEmptySets(self):
    set1 = Set()
    set2 = Set()
    minus = Set.setminus(set1, set2)
    cond = Set.equiv(set1, minus)
    self.assertEqual(cond, True)

  def testSetminusOfEmptyFromFull(self):
    set1 = Set([1,2,3,4])
    set2 = Set()
    minus = Set.setminus(set1, set2)
    cond = Set.equiv(set1, minus)
    self.assertEqual(cond, True)

  def testSetminusOfFullFromEmpty(self):
    set1 = Set([1,2,3,4])
    set2 = Set()
    minus = Set.setminus(set2, set1)
    cond = Set.equiv(set2, minus)
    self.assertEqual(cond, True)
    

  def testSetminusNormalcy(self):
    set1 = Set([1,2,3,4])
    set2 = Set([4,5,6,7])
    minus = Set.setminus(set1, set2)
    ans = Set([1,2,3])
    cond = Set.equiv(minus, ans)
    self.assertEqual(cond, True)
    
  def testSetminusSingletonFromSingleton(self):
    set1 = Set([1])
    set2 = Set([1])
    minus = Set.setminus(set1, set2)
    self.assertEqual(str(minus), '{ }')

  def testSetminusSingletonFromLead(self):
    set1 = Set([1,2,3])
    set2 = Set([1])
    minus = Set.setminus(set1, set2)
    ans = Set([2,3])
    cond = Set.equiv(minus, ans)
    self.assertEqual(cond, True)

  def testSetminusSingletonFromTail(self):
    set1 = Set([1,2,3])
    set2 = Set([3])
    minus = Set.setminus(set1, set2)
    ans = Set([1,2])
    cond = Set.equiv(minus, ans)
    self.assertEqual(cond, True)

  def testSetminusSingletonFromMiddle(self):
    set1 = Set([1,2,3])
    set2 = Set([2])
    minus = Set.setminus(set1, set2)
    ans = Set([1,3])
    cond = Set.equiv(minus, ans)
    self.assertEqual(cond, True)

  def testSetminusSubsetLeadTrailMiddle(self):
    set1 = Set([1,2,3,4,5,6,7,8,9])
    set2 = Set([1,5,9])
    minus = Set.setminus(set1, set2)
    ans = Set([2,3,4,6,7,8])
    cond = Set.equiv(minus, ans)
    self.assertEqual(cond, True)

  def testSetMinusNonOverlappingSets(self):
    set1 = Set([1,2,3,4])
    set2 = Set([5,6,7,8])
    minus = Set.setminus(set1, set2)
    cond = Set.equiv(set1, minus)

  def testSubtractedSetUnchanged(self):
    set1 = Set([1,2,3])
    set2 = Set([2,3,4])
    mark = Set([2,3,4])
    minus = Set.setminus(set1, set2)
    cond = Set.equiv(set2, mark)
    self.assertEqual(cond, True)

  
  #delta

  def testDeltaOfEmptySets(self):
    set1 = Set()
    set2 = Set()
    delt = Set.delta(set1, set2)
    mark = Set()
    cond = Set.equiv(delt, mark)
    self.assertEqual(cond, True)
    
  def testDeltaOfFullWithEmptySet(self):
    set1 = Set([1,2,3,4,5])
    set2 = Set()
    delt = Set.delta(set1, set2)
    mark = set1
    cond = Set.equiv(delt, mark)
    self.assertEqual(cond, True)

  def testDeltaNormalcy(self):
    set1 = Set([1,2,3,4])
    set2 = Set([1,3,5,6,7])
    delt = Set.delta(set1, set2)
    mark = Set([2,4,5,6,7])
    cond = Set.equiv(delt, mark)
    self.assertEqual(cond, True)
    
  def testDeltaNonOverLapping(self):
    set1 = Set([1,2,3])
    set2 = Set([4,5,6])
    delt = Set.delta(set1, set2)
    mark = Set([1,2,3,4,5,6])
    cond = Set.equiv(delt, mark)
    self.assertEqual(cond, True)
    
  def testDeltaNonidenticalSingletons(self):
    set1 = Set([1])
    set2 = Set([2])
    delt = Set.delta(set1, set2)
    mark = Set([1,2])
    cond = Set.equiv(delt, mark)
    self.assertEqual(cond, True)

  def testDeltaIdenticalSingletons(self):
    set1 = Set(['p'])
    set2 = Set(['p'])
    delt = Set.delta(set1, set2)
    mark = Set()
    cond = Set.equiv(delt, mark)
    self.assertEqual(cond, True)

  def testDeltaIdenticalNormalSets(self):
    set1 = Set([1,2,3,4,5])
    set2 = Set([1,2,3,4,5])
    delt = Set.delta(set1, set2)
    mark = Set()
    cond = Set.equiv(delt, mark)
    self.assertEqual(cond, True)
  
  def testDeltaOfSetWithItself(self):
    set1 = Set([1,2,3])
    mark = Set()
    delt = Set.delta(set1, set1)
    cond = Set.equiv(mark, delt)
    self.assertEqual(cond, True)
    
  def testDeltaSubsets(self):
    set1 = Set([1,2,3,4,5])
    set2 = Set([1,3,5])
    delt = Set.delta(set1, set2)
    mark = Set([2,4])
    cond = Set.equiv(delt, mark)
    self.assertEqual(cond, True)

  def testCommutativityOfDelta(self):
    set1 = Set([1,2,3,4,5])
    set2 = Set([3,7,4,8])
    delt = Set.delta(set1, set2)
    mark = Set([1,2,5,7,8])
    cond = Set.equiv(delt, mark)
    self.assertEqual(cond, True)
  
if __name__ == "__main__":
  unittest.main()
