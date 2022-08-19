# https://www.codewars.com/kata/51fda2d95d6efda45e00004e

class User:
    ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, problem_rank):
        current_rank = self.ranks.index(self.rank)
        difference = self.ranks.index(problem_rank) - current_rank
        current_progress = self.progress

        if difference < -1:
            pass

        elif difference == -1:
            self.progress += 1

        elif difference == 0:
            self.progress += 3

        elif difference > 0:
            self.progress += 10 * difference * difference

        if self.progress >= 100:
            rank_up = int(self.progress / 100)
            try:
                if self.rank != 8:
                    self.progress = self.progress % 100
                    self.rank = self.ranks[current_rank + rank_up]
            except:
                self.progress = 0
                self.rank = 8

        if self.rank == 8:
            self.progress = 0

user = User()
print(user.rank)
print(user.progress)
user.inc_progress(8)
print(user.ranks)
print(user.rank)
print(user.progress)

