import time 

class GameSession: 

    def __init__(self, player, timer, challenge):

        self.player = player 
        self.timer = timer 
        self.challenge = challenge 

    def display_challenge(self):

        print()

        print(f"📖 Challenge #{self.challenge.leetcode_number}")
        print(f"Title: {self.challenge.title}")
        print(f"Type: {self.challenge.challenge_type}")
        print(f"Topic: {self.challenge.topic}")
        print(f"Difficulty: {self.challenge.difficulty}")
        print(f"⏰ Time Limit: {self.challenge.time_limit} seconds")
        print(f"{self.get_type_icon()} Type: {self.challenge.challenge_type}")

        print()
        print(self.challenge.description)
        print()

        for number, option in enumerate(self.challenge.options, start=1):
            print(f"{number}. {option}")

    def get_answer(self):

        while True:

            try:

                answer = int(input("\nEnter the number of your choice.: "))

                if 1 <= answer <= len(self.challenge.options):

                    return answer
                
                print()

                print("❌ Choose one of the listed options.")

            except ValueError:

                print()

                print("❌ Please enter a number.")
    
    def check_answer(self, answer, elasped_time):

        if answer == self.challenge.answer:

            points = self.challenge.points

            if elasped_time <= self.challenge.time_limit / 2:

                print("\n⚡ Speed Bonus! +50 points")

                points += 50 

            self.player.add_score(points)

            print("\n✅ Correct!")

            self.player.add_score(self.challenge.points)

        else:

            print("\n❌ Incorrect")

            print(f"💡 Hint: {self.challenge.hint}")

    def play(self):

        self.display_challenge()

        start_time = time.time()

        answer = self.get_answer()

        end_time = time.time()

        elasped_time = end_time - start_time

        if elasped_time > self.challenge.time_limit:

            print(f"\n⏰ Time's up!")

            return

        self.check_answer(answer, elasped_time)

        print(f"\n You answered in {elasped_time:.2f} seconds.")

    def get_type_icon(self): 

        icons = { 
            "multiple_choice": "🧠",
            "debug": "🐛",
            "predict": "📝",
            "fill_blank": "✍️", 
            "coding": "⌨️"
        }

        return icons.get(self.challenge.challenge_type, "?")


    
    