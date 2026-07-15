import random

from game.player import Player
from game.timer import Timer
from game.challenge_loader import ChallengeLoader


class GameEngine:

    def __init__(self):

        loader = ChallengeLoader()

        self.challenges = loader.load_challenges("data/arrays.json")

        self.player = None

        self.timer = Timer(1)

    def start(self):

        self.show_welcome()

        self.get_player_name()

        while True:

            choice = self.show_menu()

            if choice == "1":

                self.play_game()

            elif choice == "2":

                self.show_about()

            elif choice == "3":

                self.show_statistics()

            elif choice == "4":

                print()

                print("👋 Thanks for playing Tic-Toc Code!")

                break

            elif choice == "5":

                self.practice_by_topic()

            else:

                print()

                print("❌ Invalid choice.")

    def show_welcome(self):

        print("=" * 45)
        print("          ⏰ TIC-TOC CODE ⏰")
        print("=" * 45)
        print()

    def get_player_name(self):

        name = input("Enter your name: ")

        self.player = Player(name)

        print()

        print(f"Welcome, {self.player.name}!")

        print()

    def load_random_challenge(self):

        return random.choice(self.challenges)

    def display_challenge(self, challenge):

        print(f"📖 Challenge #{challenge.leetcode_number}")

        print(f"Title: {challenge.title}")

        print(f"Topic: {challenge.topic}")

        print(f"Difficulty: {challenge.difficulty}")

        print()

        print(challenge.description)

        print()

        for number, option in enumerate(challenge.options, start=1):

            print(f"{number}. {option}")

    def get_player_answer(self):

        answer = int(input("\nYour answer: "))

        return answer 
    
    def check_answer(self, challenge, answer):

        if answer == challenge.answer:

            print()

            print("✅ Correct!")

            self.player.add_score(challenge.points)

        else:

            print()

            print("❌ Incorrect")

            print(challenge.hint)

    def display_score(self):

        print()

        print("=" * 30)

        print(f"🏆 Score: {self.player.score}")

        print("=" * 30)

        
    def show_menu(self):

        print()

        print("1. ▶ Play")

        print("2. 📖 About")

        print("3. 📊 Statistics")

        print("4. 🚪 Quit")

        print("5. 📚 Practice by Topic")

        print()

        return input("Choose an option: ")
    

    def play_game(self):

        challenge = self.load_random_challenge()

        self.display_challenge(challenge)

        answer = self.get_player_answer()

        self.check_answer(challenge, answer)

        self.display_score()

    def show_about(self):

        print()

        print("=" * 40)

        print("About Tic-Toc Code")

        print("=" * 40)

        print()

        print("Tic-Toc Code helps players")

        print("practice Python and Data")

        print("Structures & Algorithms")

        print("through timed challenges.")

        print()

        input("Press Enter to return...")

    def show_statistics(self):

        print()

        print("=" * 40)

        print("Player Statistics")

        print("=" * 40)

        print()

        print(f"Player: {self.player.name}")

        print(f"Score : {self.player.score}")

        print(f"Level : {self.player.level}")

        print(f"Streak: {self.player.streak}")

        print()

        input("Press Enter to return...")

    def practice_by_topic(self):

        print("Coming Soon!")

        print()

        input("Press Enter to return...")

    
