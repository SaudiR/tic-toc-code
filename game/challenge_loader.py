import json

from game.challenge import Challenge 

class ChallengeLoader: 

    def load_challenges(self, filename):

        with open(filename, "r") as file:

            data = json.load(file)

        challenges = []

        for item in data: 

            challenge = Challenge(
                item["title"],
                item["type"],
                item["topic"],
                item["difficulty"],
                item["description"],
                item["hint"],
                item["points"],
                item["time_limit"],
                item["leetcode_number"],
                item["options"],
                item["answer"]
)

            challenges.append(challenge)

        return challenges 
    
        
    