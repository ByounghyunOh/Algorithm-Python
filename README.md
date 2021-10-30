# Python Basic

## Data type (basic only)
Built-in by default, dynamically type(likes JavaScript)

 Type | Name |Note
---   | ---  | ---
Text Type |	str |
Numeric Types |	int, float|
Sequence Types|	list, tuple, range |
Mapping Type |	dict |
Set Types |	set |
Boolean Type |	bool | True, False (Capital letter on Fist)|
Binary Types |	bytes |

<br><br>

## Data Type (Collection )
 Name | Use | Note
---   | ---  | ---
List  |  []  | ['e', 3, 4, 'test']
Dictionary | {key:value} |  {'1':'orange', '2','red'} 
Set | {} | {'orange', 'red'} 
Tuple | () | ('orange', 'red'), **Immutable** 

<br><br>


## Built in Functions
Name | Description | Note 
---  | --- | ---
range() | returns a sequence of items | range([start,]stop[,step]) 
type() | Returns the type of an object |
sorted() | **Returns a sorted list** of the specified iterable object| x = sorted(a[, reverse=True\|False], [key=myFunc])
enumerate() | Takes a collection (e.g. a tuple) and returns it as an enumerate object |for i,x in enumerate(a):
map() |  function for each item in an iterable | map(function, iterables)

* Reference - [W3School](https://www.w3schools.com/python/python_ref_functions.asp)
<br><br>

### Sorting 
Function name| Description
--- | ---
sorted() | **Any** iterable, **Return** new sorted data (data itself is **NOT** sorting)
sort() | **list only**, no return (data itself sorting)
```Python
# sorted()
nums = [5, 2, 3, 1, 4]
>>> sorted(nums)
[1, 2, 3, 4, 5]
>>> nums
[5, 2, 3, 1, 4] # Data sorting did NOT change

# sort()
>>> nums.sort()
>>> nums
[1, 2, 3, 4, 5] # Data itself sorted

# Sorting by Key
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
 ]
>>> sorted(student_tuples, key=lambda student: student[2])   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```
* Reference - [python.org](https://docs.python.org/3/howto/sorting.html)
<br>


## String Methods
Name | Description | Note 
---  | --- | ---
lower() | Converts a string into lower case |
upper()	| Converts a string into upper case |
join() | Iterate print into one sting, such as list | x = '#'.joint(['a','b','c'])
isalnum() | [a-zA-z0-9]| Return True/False
isalpha() | [a-zA-z] | | Return True/False
isnumeric() |[0-9] | Return True/False
isdigit() | any numbers, including float | Return True/False
islower() | Returns True if all characters in the string are lower case| 
find() | Searches the string for a specified value and returns the position of where it was found, if not find return -1 | string.find(value[,start ,end])
index() | same as find(), but if not find throw exception| 
count() | Returns the number of times a specified value occurs in a string| string.count(value[, start, end])
replace() | Returns a string where a specified value is replaced with a specified value | string.replace('apple', 'orange')
strip()	| Returns a trimmed white space of string |lstrip(), rstrip()
split() | Split a string into a list. By default white space is a sperator | string.split([sperator]), e.g., x = txt.split(',')

* Reference - [W3School](https://www.w3schools.com/python/python_ref_string.asp)
<br><br>

## List Methods
Name | Description | Note 
---  | --- | ---
append() |	Adds an element at the end of the list |
insert() | Adds an element at the specified position |list.insert(index,element)
sort() | Sorts the list | list.sort([reverse=True \| False], [key=myFunc])
reverse() | Reverses the order of the list |list.reverse()|
count()	| Returns the number of elements with the specified value |
pop() | Removes the last element or specified position |list.pop(), list.pop(index)
remove() |Removes the first item with the specified value |list.remove(element)
index()	|Returns the index of the first element with the specified value |
clear()	| Removes all the elements from the list |

* Reference - [W3School](https://www.w3schools.com/python/python_ref_list.asp)
<br>

### List Slicing
```python
# list[start:End(index-1):Step]
a = [10,20,30,40]
>>> a[1:3] # index 1,2 (not include 3, for (i=0: i<3: i++))
[20, 30]
>>> a[::-1] # Reverse (index -1 is from last of List)
[40,30,20,10]
```
[<img src="./img/list_indexing.png" width="350px">](/img/list_indexing.png)
<br>

### List Comprehension

```python
>>> a = []
>>> for n in range(1, 10+1):
        if n % 2 == 1:
            a.append(n * 2)
[2, 6, 10, 14, 18]

# comprehension
>>> [n * 2 for in range(1, 10+1) if n % 2 == 1]
[2, 6, 10, 14, 18]
```

![List Comprehension](img/list_comprehension.png)
<br><br>


## Dictionary Methods
Method | Description | Note 
---  | --- | ---
update() |Updates the dictionary with the specified key-value pairs |dic.update({key:value}) |
get() | Returns the value of the specified key | dict.get(key)
pop() |Removes the element with the specified key | dict.pop(key)
del() | Removes the element |del(dic[key])
items()	| Returns a list containing a tuple for each key value pair | dict.items()
keys() | Returns a list containing the dictionary's keys | dict.keys()
values() | Returns keys and values | dict.values()

* Reference - [W3School](https://www.w3schools.com/python/python_ref_dictionary.asp)
<br><br>


## collections 
Data type | Description 
--- | ---
deque |  list-like container with fast appends and pops on either end, O(1) 

### deque
  - Kinds of double-ended queue that can be queue and stack

Method | Description
--- | ---
pop()  | Remove and return an element from the right side of the deque, pop(index)
popleft() | Remove and return an element from the left side of the deque
append() | Same as list
count(x) | Count the number of deque elements equal to x

* Reference - [python.org](https://docs.python.org/3/library/collections.html#module-collectionsp)
<br><br>


## Operation
* No short form increment/decrement operator exist in Python, such as ++i or --i
* Most of operators are same as other language

Operator | Description | Note 
---  | --- | ---
** | power | same as ^
// | quotient | 5//2 = 2, 5/2 = 2.5

<br><br>


## Loop
``` Python
# Sample 1
text = 'test'
for c in text:
    print(c)

# Sample 2
list = [1,3,5,7,9]
for i in list:
    print(i)


# Sample 3
# range([start,]stop[,step])
for x in range(6): # 0 to 5, 6 is not included

# Sample 4
for x in range(2, 30, 3): # 2 to 29, ++3
    if x <= 10:
        continue  # if x <= 10, continue back to loop
    else
        print(x)

# Sample 5
i = 0
while (i < 6):
    print(x)
    if i == 4:
        break
    i += 1

```
<br><br>

## Print()
Type | Description | Note 
---  | --- | ---
, | basic |print('name is', name)
% | old  | print('%d + %d = %d' % (a,b,a+b))
format() | common | print('{0} * {1} = {2}'.format(a, b, a*b))
f-String | Python3.6~ | print(f'{a} * {b} = {a*b}')

<br><br>


## RegEx
  * import re
  
Function | Description | Note 
---  | --- | ---
sub() | Replaces one or many matches with string | re.sub('regex', 'replace', string)


```Python
import re
s = 'Python the best!!!'

# ^ means Not, a-zA-z0-9 is range of regex, '' is what is will be replace.
# If s is not in [a-zA-Z0-9], replace with '' (same as removed)
s = re.sub('[^a-zA-z0-9]', '', s)  
print(s)
>>> Pythonthebest  # Replaced all space, special chars with nothing(=Removed)
``` 

<br><br>


## Lambda
* Lambda is small anonymous function(or expression) that it can use without define separate function 
* This is useful when you need to another function inside function without define another function
```Python
# Syntax
# lambda arguments: expression

x = lambda a : a * 10
print(x(5))   # output: 50 

x = lambda a, b : a + b
print(x(5, 10))   # output: 15 

# Inside function
def double_Number(nums: list) -> None:
    dbNums = list(map(lambda x: x*2, nums))
    print(dbNums)  # output: [2, 4, 6, 8, 10]

double_Number([1,2,3,4,5])
```

<br><br>

## Linked List
* Linked list is a data structure which contains data objects which are connected by link
```Python
# Class ListNode:
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Making linked List(=ListNode) from list
def make_linked_list(nums: list) -> ListNode:
    # head hold start cursor of list
    head = linked_list = ListNode(nums[0])
    for num in nums[1:]:
        linked_list.next = ListNode(num)  # linking next ListNode with val 
        linked_list = linked_list.next  # Move cursor
    return head # return head cursor

result = make_linked_list([1,2,3,4])

# checking the linked_list created correctly
prn = ''
while result:
    prn += str(result.val) + '->'
    result = result.next
print(prn[:-2]) # remove last two char '->'
>>> 1->2->3->4
```
[<img src="./img/linked_list01.png" width="500px">](/img/linked_list01.png)
<br><br>