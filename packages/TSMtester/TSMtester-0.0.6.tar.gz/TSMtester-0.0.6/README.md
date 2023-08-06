# Traveling-salesman

A class for testing discrete optimization algorithms using the "traveling salesman" problem.

**discrete optimization:** arranging an array of several member in the optimal order according to a cost (score)
function.

## Class structure

On creation the class generates n random two-dimensional coordinates in a map of 1000x1000. The locations can be
generated either randomly or in the shape of a circle

The route is represented in a list with all the location names, and the order is the route.

The class contains several attributes and methods for ease of use during testing.

### Attributes and properties

* **`locations` -** dictionary, containing all the coordinates. e.g:
  ```instace.locations = {1: (153, 636), 2: (23, 523), 3: (864, 41)}```
* **`circle` -** boolean(getter), `True` if generated locations in a circle.
* **`initial_route` -** list(getter), the names of locations in the ordered they were generated in.

### Methods

* **instance initiation -** there are two optional arguments:
  * `locations = int` which accepts an integer and determines the number of generated locations(default is 10)
  * `circle = bool` which accepts a boolean and determines if the locations are to be generated in a circle(default
    is `False`)
* **`distance` -** evaluates the route inputted through the argument `route`. the route must be a list containing the
  names of locations in the order to be traveled. the function returns the sum of all distances between locations in the
  order of the route list. this distance will be used as the cost of a solution by the optimizer.
* **`plot` -** show a plot of a given route. has two optional arguments:
  * `route` - a list containing the names of locations if the order to be traveled. if this argument is empty,
    the `initial_route` will be used.
  * `labels` - boolean, if `True` adds labels to all locations.
* **`random_route` -** returns a random route. it should be noted that when `circle = False` the initial_route can also
  serve as a random route since the locations are random. has one optional argument:
  * **`seed` -** accepts any, uses the input as the random seed.
* **`add_location` -** adds a single location to the `locations` dictionary, and the `initial_route` list. has two
  mandatory arguments and one optional argument:
  * `x` - the x coordinate, must be in range of 1, 1000. required argument
  * `y` - the y coordinate, must be in range of 1, 1000. required argument
  * `name` - the name, or key of the location. if `None`, will use an integer that is not already present
    in `locations.keys()`. if the passed through key already exists in the `locations` dictionary, the old location will
    be overwritten.

## Usage

to create an instance of the `TSM` class:

```python
from TSM import TSM

tsm = TSM(locations=10, circle=False)
```

to get the initial route, and a random route

```python
init_route = tsm.initial_route   # return: [0,1,2,3,4,5,6,7,8,9]
rand_route = tsm.random_route()  # return: [5,3,4,7,9,1,0,6,2,8]
```

to get the distance of a route.

```python
distance = tsm.distance(route=rand_route)  # return: 58317
```

to add a location

```python
print(len(tsm.initial_route))  # out: 10

tsm.add_location(x=500, y=250)

print(len(tsm.initial_route))  # out: 11
```

to plot a route

```python
opt_route = [5,3,4,7,9,1,0,6,2,8]  # the optimal route found with an optimization algorithm

tsm.plot(route=opt_route)
```

the printed plot:

![Figure_1](https://user-images.githubusercontent.com/76598250/114361374-59cd3900-9b76-11eb-98ae-f5a87cca2261.png)

## Using circle

Sometimes it is useful to know the true global optima to check how far off the result from the optimization algorithm
is. In order to do that, I've added the `circle` argument when creating the instance. When using this option, the
locations will be generated in the shape of a circle, this means that the `initial_route`
is also the global minima for this set of locations. It is important to note that the optimal route can start and end
anywhere, therefore, the optimal route found by an algorithm might not be 100% identical to the `initial_route` from
the `TSM` class but would still be a global optima. to make sure you have achieved a true optimal route you should make
sure its cost (total distance) is identical to the initial route and not that the route itself is identical.

here is a plot of the initial cost of 50 locations (optimal cost= 6153.5)

![Figure_1](https://user-images.githubusercontent.com/76598250/114386249-42e81000-9b91-11eb-867a-be24bab5c67a.png)
