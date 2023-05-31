class GraduationCeremony:
    def __init__(self, n):
        # n: number of academic days
        if n < 4:
            raise Exception("Invalid Inputs")

        self.n = n


    def solution(self):
        """
        Time Complexity: O(n)
        Space Complexity: O(n)
        Dynamic Programing Tabulation
        """

        n = self.n
        dp = [[0] * (4 + 1) for _ in range(n + 1)]

        for i in range(4):
            dp[0][i] = 1

        for i in range(1, n + 1):
            for j in range(4 - 1, -1, -1):
                dp[i][j] = dp[i - 1][0] + dp[i - 1][j + 1]

        no_of_ways_attend_class = dp[n][0]  # total number of valid way to attend classes
        no_of_ways_miss_class = dp[n - 1][1]  # total number of way to miss last day

        return "{}/{}".format(no_of_ways_miss_class, no_of_ways_attend_class)


if __name__ == "__main__":
    inputs = [5, 10]
    for n in inputs:
        obj = GraduationCeremony(n)
        print(obj.solution())