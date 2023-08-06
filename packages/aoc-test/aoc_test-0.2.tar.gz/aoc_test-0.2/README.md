# Advent of code tester
A simple program that checks your AOC solution written in python against provided test cases.

Testing your AOC solutions is tedious and time-consuming. This program automates this process by comparing your solution to the expected result for every test case in the current directory. There are a few [requirements](#requirements) you have to satisfy first for this to work.

## Example
Here is what the output looks like.
The faded out text is the debug logs from [icecream](https://github.com/gruns/icecream), which you can use to inspect the execution of your program.

![](./img/success.png)

![](./img/failed.png)

## How to
First, install it from [pypi](https://pypi.org/project/pytest-aoc/):
``` shell
pip install pytest-aoc
```

To run the tests, simply execute the command in the directory with your solution and test cases:
``` shell
aoct
```

You can run it for a specific part:
``` shell
aoct 1
aoct 2
```

## Requirements
For this program to work its magic, you must satisfy two requirements:
1. Your solution script takes input from `stdin` and outputs solution to `stdout`.
2. The test files are named according to a specific scheme.

### Solution template

The solution file must be named `main.py`.

You can use this template for your solution script:
``` python
def p1(int):
    return 0

def p2(int):
    return 0

if __name__ == "__main__":
    import sys
    inp = sys.stdin.read().strip()
    
    # optional
    if not 'test' in sys.argv:
        ic.disable()

    if '2' not in sys.argv:
        print(p1(inp))
    if '1' not in sys.argv:
        print(p2(inp))
```

Basically, `aoct` will invoke your solution script with two arguments: 
problem part (`1` or `2`) and the argument `test`.

By providing the `test` argument,
`aoct` allows you to optimize your own program when you want to run it on the big input.
For example, if you're using a logger,
you can disable it if the argument isn't given 
to avoid wasting performance on formatting those logs.

Since `aoct` relies on the solution being returned through `stdin`, you can't do your usual [caveman debugging](https://medium.com/supernova-invention-park/the-caveman-debugging-ab8f7151415f) anymore. What you can do, though, and what `icecream` does, is print to `stderr` instead.
### Test cases
Your files should be named like this:
``` text
Problem_directory
├── main.py
├── test_1.1.out
├── test_1.2.out
└── test_1.in
├── test_2.2.out
└── test_2.in
```

For tests, this is sorta the naming scheme:
- for test input: `test*.in`
- for expected output in part 1: `test*.1.out`
- for expected output in part 2: `test*.2.out`

For example, for [AOC 2022 day 3](https://adventofcode.com/2022/day/3), you would have the following test files:

File `test_1.in`:
``` text
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
```

File `test_1.1.out`:
``` text
157
```

File `test_1.2.out`:
``` text
70
```
