from game.player import Player
from game.timer import Timer
from game.challenge import Challenge 

class GameEngine:

    def __init__(self):

        self.name = input("Enter your name: ")
        self.player = Player(self.name)
        self.timer = Timer(1)
        self.challenge = Challenge(
            "Two Sum",
            "Arrays",
            "Easy",
            "Find two numbers whose sum equals the target.",
            "💡 Think about using a dictionary to remember numbers you've already seen.",
            "60 seconds",
            "200",
            "20"
        )

    def start(self):

        print("=" * 40)
        print("⏰ TIC-TOC CODE")
        print("=" * 40)

        print()

        print(f"Welcome {self.player.name}")

        print()

        print("📖 Today's Challenge")
        print("-" * 30)

        print(f"Title: {self.challenge.title}")
        print(f"Topic: {self.challenge.topic}")
        print(f"Difficulty: {self.challenge.difficulty}")
        print(f"Description: {self.challenge.description}")
        print(f"Hint: {self.challenge.hint}")
        print(f"Time Limit: {self.challenge.time_limit}")
        print(f"Points: {self.challenge.points}")
        print(f"LeetCode #: {self.challenge.leetcode_number}")
        
        print()

        print("-" * 30)

        print()

        self.timer.seconds = 5

        self.timer.countdown()



