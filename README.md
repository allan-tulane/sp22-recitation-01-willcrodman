# CMPS 2200  Recitation 01

**Name (Team Member 1):**_Will Rodman___  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate asymptotic complexity. Additionally, we will get familiar with the various technologies we'll use for collaborative coding.

To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.


## Setup
- Make sure you have a Github account.
- Login to Github.
- Login to repl.it, using "sign in with github"
- Click on the assignment link sent through canvas and accept the assignment. 
- Click on your personal github repository for the assignment.
- Login in Repls https://replit.com/repls and then create a new replit by importing from github repository.
- You'll work with a partner to complete this recitation. To do so, we'll break you into Zoom rooms. You will be able to code together in the same `repl.it` instance. You can choose whose repl.it instance you will share. This person will click the "Share" button in their repl.it instance and email the lab partner.
- Make sure the dependencies are installed. Please use 'pip install -r requirements.txt'.

## Running and testing your code
- In the command-line window, run `./ipy` to launch an interactive IPython shell. This is an interactive shell to help run and debug your code. Any code you change in `main.py` will be reflected from this shell. So, you can modify a function in `main.py`, then test it here.
  + If it seems things don't refresh, try running `from main import *`
- You can exit the IPython prompt by either typing `exit` or pressing `ctrl-d`
- To run tests, from the command-line shell, you can run
  + `pytest main.py` will run all tests
  + `pytest main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Version Control" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Comparing search algorithms

We'll compare the running times of `linear_search` and `binary_search` empirically.

`Binary Search`: Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise, narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

- [ ] 1. In `main.py`, the implementation of `linear_search` is already complete. Your task is to implement `binary_search`. Implement a recursive solution using the helper function `_binary_search`. 

- [ ] 2. Test that your function is correct by calling from the command-line `pytest main.py::test_binary_search`

- [ ] 3. Write at least two additional test cases in `test_binary_search` and confirm they pass.

- [ ] 4. Describe the worst case input value of `key` for `linear_search`? for `binary_search`? 


 The worst case key for a liniar search is a key whos value is stored as the as the last element in array of lenght N , assuming the search starts by refrencing the pointer of the first element in the array. In this case the algo will have to check O(N) elements.


 Worst case key for binary search of array lenght N is if the value of the key is stored as the last element in the array. In this case, the algo will have to check O(log2 n) elements.

- [ ] 5. Describe the best case input value of `key` for `linear_search`? for `binary_search`? 


 The best case key for a liniar search is a key whos value is stored as the as the first element in array of lenght N , assuming the search starts by refrencing the pointer of the first element in the array. In this case, the algo will have to check Omega(1) elements.

 Best case key for binary search of array lenght N is if the value of the key is stored as the the middle element of the array such that the key index = lenght of N // 2. In this case, the algo will have to check Omega(1) elements.

- [ ] 6. Complete the `time_search` function to compute the running time of a search function. Note that this is an example of a "higher order" function, since one of its parameters is another function.

- [ ] 7. Complete the `compare_search` function to compare the running times of linear search and binary search. Confirm the implementation by running `pytest main.py::test_compare_search`, which contains some simple checks.

- [ ] 8. Call `print_results(compare_search())` and paste the results here:

[(10.0, 0.003337860107421875, 0.0050067901611328125), 
  (100.0, 0.017642974853515625, 0.00858306884765625),
  (1000.0, 0.23651123046875, 0.011444091796875),
  (10000.0, 2.7365684509277344, 0.02384185791015625),
  (100000.0, 56.61439895629883, 0.025987625122070312),
  (1000000.0, 419.22831535339355, 0.03409385681152344),
  (10000000.0, 4206.875562667847, 0.05555152893066406)]

- [ ] 9. The theoretical worst-case running time of linear search is $O(n)$ and binary search is $O(log_2(n))$. Do these theoretical running times match your empirical results? Why or why not?

These running time do match the empirical results. An easy way of proving this is by observing the liniar search perfonance times, whos worst case is O(n), increases exponentially as the value of n increases exponentially. 

- [ ] 10. Binary search assumes the input list is already sorted. Assume it takes $\Theta(n^2)$ time to sort a list of length $n$. Suppose you know ahead of time that you will search the same list $k$ times. 
  + What is worst-case complexity of searching a list of $n$ elements $k$ times using linear search? T(n) = O(k*n)
  + For binary search? T(n) = O(k*log2n)
  + For what values of $k$ is it more efficient to first sort and then use binary search versus just using linear search without sorting? 
  

Consdiering for linear search T(n) = O(k*n) where n = 1 => T(n) = O(1), linear search for one element is the dominate algo. However, quick sort and binary search T(n) = O(k*log2n + k*n*log2n) = O(k*n*log2n). 

Such that: T_Liniar(5) = 5k and T_Binary(5) = 5k
  
Therefore, liniar search is only the dominate algo when 1 <= n <= 5. 