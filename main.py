"""
from game.game_engine import GameEngine

game = GameEngine()

game.start()

"""

from game.challenge_loader import ChallengeLoader

loader = ChallengeLoader()

challenges = loader.load_challenges("data/arrays.json")

challenge = challenges[0]

for challenge in challenges:

    print(challenge.title)



