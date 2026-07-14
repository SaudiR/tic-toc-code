import time 

class Timer:
    
    def __init__(self, minutes):
        
        self.minutes = minutes 
        self.seconds = minutes * 60 

    def display_time(self):

        minutes = self.seconds // 60 
        seconds = self.seconds % 60 

        print(f"{minutes:02}:{seconds:02}") 

    def countdown(self):

        while self.seconds >= 0:

            self.display_time()
            time.sleep(1)
            self.seconds -= 1 

        print("⏰ TIME'S UP!")