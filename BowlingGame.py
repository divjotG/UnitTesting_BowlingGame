class BowlingGame:
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                if rollIndex + 2 < len(self.rolls):  # Check if there are enough rolls left
                    result += self.strikeScore(rollIndex)
                    rollIndex += 1
                else:
                    break
            elif self.isSpare(rollIndex):
                if rollIndex + 2 < len(self.rolls):  # Check if there are enough rolls left
                    result += self.spareScore(rollIndex)
                    rollIndex += 2
                else:
                    break
            else:
                if rollIndex + 1 < len(self.rolls):  # Check if there are enough rolls left
                    result += self.frameScore(rollIndex)
                    rollIndex += 2
                else:
                    break
        return result

    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    def strikeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 2]

    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
