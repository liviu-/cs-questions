#!/usr/bin/env python3

"""
Write a recursive function for generating all permutations of an input string. Return them as a set. 

Source: interviewcake.com

Usage:
    $ ./recursive_str_perm hi
    {'hi', 'ih'}
"""

import sys, math, random, collections, operator, functools

get_perm = lambda s, strings=set(): (
            strings 
                if len(strings) == (
                        math.factorial(len(s))
                        /
                        functools.reduce(
                            operator.mul,
                            map(
                                math.factorial,
                                collections.Counter(list(s)).values()
                                ),
                            1) 
                    )
                else 
            get_perm(
                ''.join(random.sample(s, len(s))),
                set(list(strings) + [s])
            )
        )

print(get_perm(sys.argv[1]))
