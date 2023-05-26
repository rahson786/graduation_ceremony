# Question

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
You are not allowed to miss classes for four or more consecutive days. 
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal
Test cases:

for 5 days: 14/29

for 10 days: 372/773

# Prerequisite

Python 3 must be installed in your local machine.

# How to run ?

To run the assignment execute following command:

 python3 solution.py

It ask for input on command prompt, enter the number of days (e.g 5 or 10 or any other value your choice) and hit enter
It will display the expected output for n days passed in argument


# Answer Explanation

The code first checks if `n` is less than 4. If it is, then the function returns Error message. This is because there is no way to miss 4 or more consecutive classes if `n` is less than 4.

If `n` is greater than or equal to 4, then the function calculates the number of ways to attend classes using the following formula, this is to generate the base condition

--------------------------
way1 + way2 + way3 + way4
--------------------------
where:

* `way1` is the number of ways to attend classes for the first day
* `way2` is the number of ways to attend classes for the first two days
* `way3` is the number of ways to attend classes for the first three days
* `way4` is the number of ways to attend classes for the first four days

The formula is derived by considering all possible combinations of attendance and absence. For each day, there are two possible outcomes: attend or miss. There are 4 days that must be attended, and `n - 4` days that can be attended or missed. The total number of possible combinations is therefore `way1 + way2 + way3 + way4`.

The function then calculates the total number of ways to attend attend classes over 'n' days using the following formula:

--------------------------------
(total_class - temp) * 2 + temp
--------------------------------

where:

* `total_class` is the total number of ways to attend classes for `n` days
* `temp` is the number of ways to attend classes for the previous `n - 1` days

The formula is derived by considering the fact that there are two ways to attend classes for the `n`th day: either you attend, or you miss. If you attend, then you can attend classes for the `n - 1`th day in any of the `total_class` ways. If you miss, then you can attend classes for the `n - 1`th day in any of the `temp` ways. The total number of ways to attend classes for the `n`th day is therefore `(total_class - temp) * 2 + temp`.

The function then returns the ratio of the number of ways to attend classes to the count. This is the probability of attending classes for `n` days.
