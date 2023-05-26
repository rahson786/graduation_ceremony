def graduation_ceremony(n):

    """
    Calculates the number of ways to attend classes over n days.

    Args:
    n: The number of days.

    Returns:
    probability that you will miss your graduation ceremony / The number of ways to attend classes.
    
    """

    if n < 4:
        return "Input cannot be less then 4"    # as per question condition students are not allowed to miss 4 or more consicutive class.
    
    '''
    We start with n=1 till n=4 and find the series as base data, after that series(similar to fibonacci) takes over 
    since for next set of records result is the sum of seed data and it moves on.
    '''

    # for first 4 days below are the base case scenario

    way1 = 2                                    # the number of ways to attend classes for the first day
    way2 = 1                                    # the number of ways to attend classes for the first two days
    way3 = 1                                    # is the number of ways to attend classes for the first three days
    way4 = 4                                    # is the number of ways to attend classes for the first four days 
    total_no_of_ways_to_attend_class = 8        # total number of ways to attend classes for `n` days when n = 4 

    '''
        Time Complexity: O(n)  ----- where 'n' is the no. of days
        Space Complexity: O(1) ----- as we used 5 variable and there size will remain constant through out the program
    '''
    # for n >= 4 we will use the below logic to generate the series and calculate the total no of ways to attend class
    for i in range(4, n + 1):
        temp = way3
        way3 = way2
        way2 = way1
        way1 = way4
        way4 = total_no_of_ways_to_attend_class

        total_no_of_ways_to_attend_class = (total_no_of_ways_to_attend_class - temp) * 2 + temp

    return "{}/{}".format((way1+way2+way3), total_no_of_ways_to_attend_class)


if __name__ == "__main__":
    n = int(input("Enter the number of days: "))
    result = graduation_ceremony(n)
    print("for {} days: {}".format(n, result))
