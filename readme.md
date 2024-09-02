
# Festival schedule generator (FSG)

This is a solution for the Decode Demcon challenge #4.
The `Planner` class can be instantiated with a list of shows, or using the `from_file()` method.
The constructor of the class will try to find an optimal schedule, which can be viewed with the `output()` method

## Authors

- [@Matthijsvs]()


## Usage/Examples

```python
    # Create planner object from iterable list
    ex1 = Planner(["show_1 36 39", "show_2 30 33", "show_3 29 36"])
    ex1.output()

    # Create planner object from file:
    ex2 = Planner.from_file("sample.txt")
    ex2.output(width=6)
    
    # Adjust column width for long names
    ex3 = Planner(["long_Show_name 6 9", "long_Show(tribute_band) 5 6", "show_3 0 3"])
    ex3.output(18)
```

