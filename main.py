"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
    if right >= left:
        m = left+(right-left)//2
        if mylist[m] == key: 
          return m
        elif mylist[m] > key:
            return _binary_search(mylist, key, left, m-1)
        else:
            return _binary_search(mylist, key, m+1, right)
    else:
        return -1

def test_binary_search():

  assert binary_search([1,2,3,4,5], 5) == 4
  assert binary_search([1,2,3,4,5], 1) == 0
  assert binary_search([1,2,3,4,5], 6) == -1

  assert binary_search([1,400,400,400,500,1000,11000], 1) == 0
  assert binary_search([1,2,33,12,400,3333,11111,10000011], 123) == -1

def time_search(search_fn, mylist, key):
  start_time = time.time()
  search_fn(mylist, key)
  end_time = time.time()

  ms = (end_time - start_time) * 1000
  
  return ms

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
  l = list()

  for n in sizes:
    test_list = range(1, int(round(n)))
    test_key = 0
    liniar_search_time = time_search(linear_search, test_list, test_key)
    binary_search_time = time_search(binary_search, test_list, test_key)
    t = (n, liniar_search_time, binary_search_time)
    l.append(t)
  return l

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1
