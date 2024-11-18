Information Theory Wordle
An enhanced command-line implementation of Wordle using information theory principles to provide optimal guessing strategies.
Features

Information theory-based guess suggestions
Entropy calculation for each possible guess
Expanded word dictionary
Colored feedback visualization
Remaining possibilities counter
Game history tracking

Installation
bashCopygit clone https://github.com/yourusername/information-theory-wordle
cd information-theory-wordle
pip install -r requirements.txt
Usage
Run the game:
bashCopypython wordle.py
The game will:

Suggest optimal guesses based on entropy calculations
Show remaining possible words
Provide feedback using colored squares:

🟩 Green: Correct letter, correct position
🟨 Yellow: Correct letter, wrong position
⬜ Grey: Letter not in word



Project Structure
Copyinformation-theory-wordle/
├── README.md
├── requirements.txt
├── LICENSE
├── wordle.py
└── tests/
    └── test_wordle.py
Requirements

Python 3.7+
No external dependencies required

How It Works
The game uses information theory principles to optimize word guessing:

Entropy Calculation: For each possible guess, calculates expected information gain
Probability Distribution: Tracks word probabilities based on feedback
Optimal Guessing: Suggests words that maximize information gain
Pattern Matching: Updates possible words based on feedback patterns

Contributing

Fork the repository
Create your feature branch: git checkout -b feature/new-feature
Commit changes: git commit -m 'Add new feature'
Push to branch: git push origin feature/new-feature
Submit a pull request

License
This project is licensed under the MIT License - see the LICENSE file for details.
