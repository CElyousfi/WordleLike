import random
import math
from collections import defaultdict
import string
import os


class WordleInfoTheory:
    def __init__(self):
        self.word_length = 5
        self.max_attempts = 6
        self.word_list = self.load_word_list()
        self.possible_words = self.word_list.copy()
        self.target_word = random.choice(self.word_list)
        self.attempts = []
        self.feedback_history = []

    def load_word_list(self):
        # You can expand this list by adding more word sources
        base_words = [
            "about", "above", "abuse", "actor", "acute", "admit",
            "adopt", "adult", "after", "again", "agent", "agree",
            "ahead", "alarm", "album", "alert", "alike", "alive",
            "allow", "alone", "along", "alter", "among", "anger",
            "angle", "angry", "apart", "apple", "apply", "arena",
            "argue", "arise", "array", "aside", "asset", "audio",
            "audit", "avoid", "award", "aware", "badly", "baker",
            "bases", "basic", "basis", "beach", "began", "begin",
            "begun", "being", "below", "bench", "billy", "birth",
            "black", "blame", "blind", "block", "blood", "board",
            "boost", "booth", "bound", "brain", "brand", "bread",
            "break", "breed", "brief", "bring", "broad", "broke",
            "brown", "build", "built", "buyer", "cable", "calif",
            "carry", "catch", "cause", "chain", "chair", "chart",
            "chase", "cheap", "check", "chest", "chief", "child",
            "china", "chose", "civil", "claim", "class", "clean",
            "clear", "click", "clock", "close", "coach", "coast",
            "could", "count", "court", "cover", "craft", "crash",
            "cream", "crime", "cross", "crowd", "crown", "curve",
            "cycle", "daily", "dance", "dated", "dealt", "death",
            "debut", "delay", "depth", "doing", "doubt", "dozen",
            "draft", "drama", "drawn", "dream", "dress", "drill",
            "drink", "drive", "drove", "dying", "eager", "early",
            "earth", "eight", "elite", "empty", "enemy", "enjoy",
            "enter", "entry", "equal", "error", "event", "every",
            "exact", "exist", "extra", "faith", "false", "fault",
            "fiber", "field", "fifth", "fifty", "fight", "final",
            "first", "fixed", "flash", "fleet", "floor", "fluid",
            "focus", "force", "forth", "forty", "forum", "found",
            "frame", "frank", "fraud", "fresh", "front", "fruit",
            "fully", "funny", "giant", "given", "glass", "globe",
            "going", "grace", "grade", "grand", "grant", "grass",
            "great", "green", "gross", "group", "grown", "guard",
            "guess", "guest", "guide", "happy", "harry", "heart",
            "heavy", "hence", "henry", "horse", "hotel", "house",
            "human", "ideal", "image", "index", "inner", "input",
            "issue", "japan", "jimmy", "joint", "jones", "judge",
            "known", "label", "large", "laser", "later", "laugh",
            "layer", "learn", "lease", "least", "leave", "legal",
            "level", "lewis", "light", "limit", "links", "lives",
            "local", "logic", "loose", "lower", "lucky", "lunch",
            "lying", "magic", "major", "maker", "march", "maria",
            "match", "maybe", "mayor", "meant", "media", "metal",
            "might", "minor", "minus", "mixed", "model", "money",
            "month", "moral", "motor", "mount", "mouse", "mouth",
            "movie", "music", "needs", "never", "newly", "night",
            "noise", "north", "noted", "novel", "nurse", "occur",
            "ocean", "offer", "often", "order", "other", "ought",
            "paint", "panel", "paper", "party", "peace", "peter",
            "phase", "phone", "photo", "piece", "pilot", "pitch",
            "place", "plain", "plane", "plant", "plate", "point",
            "pound", "power", "press", "price", "pride", "prime",
            "print", "prior", "prize", "proof", "proud", "prove",
            "queen", "quick", "quiet", "quite", "radio", "raise",
            "range", "rapid", "ratio", "reach", "ready", "refer",
            "right", "rival", "river", "robin", "roger", "roman",
            "rough", "round", "route", "royal", "rural", "scale",
            "scene", "scope", "score", "sense", "serve", "seven",
            "shall", "shape", "share", "sharp", "sheet", "shelf",
            "shell", "shift", "shirt", "shock", "shoot", "short",
            "shown", "sight", "since", "sixth", "sixty", "sized",
            "skill", "sleep", "slide", "small", "smart", "smile",
            "smith", "smoke", "solid", "solve", "sorry", "sound",
            "south", "space", "spare", "speak", "speed", "spend",
            "spent", "split", "spoke", "sport", "staff", "stage",
            "stake", "stand", "start", "state", "steam", "steel",
            "stick", "still", "stock", "stone", "stood", "store",
            "storm", "story", "strip", "stuck", "study", "stuff",
            "style", "sugar", "suite", "super", "sweet", "table",
            "taken", "taste", "taxes", "teach", "teeth", "terry",
            "texas", "thank", "theft", "their", "theme", "there",
            "these", "thick", "thing", "think", "third", "those",
            "three", "threw", "throw", "tight", "times", "tired",
            "title", "today", "topic", "total", "touch", "tough",
            "tower", "track", "trade", "train", "treat", "trend",
            "trial", "tried", "tries", "truck", "truly", "trust",
            "truth", "twice", "under", "undue", "union", "unity",
            "until", "upper", "upset", "urban", "usage", "usual",
            "valid", "value", "video", "virus", "visit", "vital",
            "voice", "waste", "watch", "water", "wheel", "where",
            "which", "while", "white", "whole", "whose", "woman",
            "women", "world", "worry", "worse", "worst", "worth",
            "would", "wound", "write", "wrong", "wrote", "yield",
            "young", "youth"
        ]
        return [word.lower() for word in base_words if len(word) == self.word_length]

    def calculate_entropy(self, guess, possible_words):
        """Calculate the expected information gain for a guess."""
        pattern_probabilities = defaultdict(int)
        total_words = len(possible_words)

        for word in possible_words:
            pattern = self.get_feedback(guess, word)
            pattern_probabilities[pattern] += 1

        entropy = 0
        for count in pattern_probabilities.values():
            probability = count / total_words
            entropy -= probability * math.log2(probability)

        return entropy

    def get_best_guess(self):
        """Get the guess that maximizes expected information gain."""
        max_entropy = -1
        best_guess = None

        # Consider all possible words as guesses
        for guess in self.word_list:
            entropy = self.calculate_entropy(guess, self.possible_words)
            if entropy > max_entropy:
                max_entropy = entropy
                best_guess = guess

        return best_guess

    def get_feedback(self, guess, target):
        """Generate feedback pattern for a guess."""
        feedback = ['_'] * self.word_length
        target_chars = list(target)
        guess_chars = list(guess)

        # First pass: mark correct positions (green)
        for i in range(self.word_length):
            if guess_chars[i] == target_chars[i]:
                feedback[i] = '🟩'
                target_chars[i] = '*'
                guess_chars[i] = '*'

        # Second pass: mark correct letters in wrong positions (yellow)
        for i in range(self.word_length):
            if guess_chars[i] != '*':
                if guess_chars[i] in target_chars:
                    feedback[i] = '🟨'
                    target_chars[target_chars.index(guess_chars[i])] = '*'
                else:
                    feedback[i] = '⬜'

        return ''.join(feedback)

    def update_possible_words(self, guess, feedback):
        """Update the list of possible words based on feedback."""
        new_possible_words = []
        for word in self.possible_words:
            if self.get_feedback(guess, word) == feedback:
                new_possible_words.append(word)
        self.possible_words = new_possible_words

    def play(self):
        """Main game loop."""
        print(f"\nWelcome to Information Theory Wordle!")
        print(f"Try to guess the {self.word_length}-letter word. You have {self.max_attempts} attempts.")
        print("🟩 = Correct letter, correct position")
        print("🟨 = Correct letter, wrong position")
        print("⬜ = Letter not in word")

        for attempt in range(self.max_attempts):
            # Suggest the best guess based on information theory
            suggested = self.get_best_guess()
            entropy = self.calculate_entropy(suggested, self.possible_words)
            print(f"\nSuggested word (entropy: {entropy:.2f} bits): {suggested}")
            print(f"Possible words remaining: {len(self.possible_words)}")

            # Get and validate player's guess
            while True:
                guess = input(f"\nEnter guess #{attempt + 1}: ").lower()
                if len(guess) != self.word_length:
                    print(f"Please enter a {self.word_length}-letter word.")
                elif not guess.isalpha():
                    print("Please enter only letters.")
                elif guess not in self.word_list:
                    print("Word not in word list.")
                else:
                    break

            # Generate and display feedback
            feedback = self.get_feedback(guess, self.target_word)
            print(f"Feedback: {feedback}")

            # Store history
            self.attempts.append(guess)
            self.feedback_history.append(feedback)

            # Check for win
            if guess == self.target_word:
                print(f"\nCongratulations! You won in {attempt + 1} attempts!")
                break

            # Update possible words based on feedback
            self.update_possible_words(guess, feedback)

        else:
            print(f"\nGame over! The word was: {self.target_word}")

        # Display game summary
        print("\nGame Summary:")
        for i, (guess, feedback) in enumerate(zip(self.attempts, self.feedback_history)):
            print(f"Attempt {i + 1}: {guess} - {feedback}")


if __name__ == "__main__":
    game = WordleInfoTheory()
    game.play()