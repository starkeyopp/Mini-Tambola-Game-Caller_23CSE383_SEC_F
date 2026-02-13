import random
import time

class TumbolaGame:
    def __init__(self):
        self.all_numbers = list(range(1, 41))  
        self.called_numbers = []        

    def start_game(self):
        print(" Welcome to Tumbola Game ")
        print("Numbers will be generated from 1 to 41.")
        print("Press Enter to generate a number.")
        print("Type 'q' and press Enter to quit the game.\n")

        while len(self.called_numbers) < 40:
            user_input = input("Press Enter to generate number (q to quit): ")

            if user_input.lower() == 'q':
                print("Game ended by user.")
                break

            number = self.generate_number()

            if number is not None:
                print(f" Number Called: {number}")
                print(f"Numbers Called So Far: {sorted(self.called_numbers)}")
                print(f"Remaining Numbers: {40 - len(self.called_numbers)}\n")
                time.sleep(1)
            else:
                print("All numbers have been called!")
                break

        print("\n Game Over ")
        print("All Called Numbers:")
        print(sorted(self.called_numbers))

    def generate_number(self):
        if not self.all_numbers:
            return None

        number = random.choice(self.all_numbers)
        self.all_numbers.remove(number)
        self.called_numbers.append(number)
        return number


if __name__ == "__main__":
    game = TumbolaGame()
    game.start_game()

