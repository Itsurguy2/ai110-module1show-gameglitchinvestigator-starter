# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [X] Describe the game's purpose.
      The game is a number guessing challenge where you try to guess a secret number based on the difficulty you choose. You get a limited number of attempts and hints if your guess is too high or too low. It’s a simple, interactive way to practice logic, prediction, and see how Streamlit handles user input and state.
      
- [x] Detail which bugs you found.
      At first, pressing Enter in the input box didn’t actually submit my guess—I had to click the Submit button, which was confusing. After winning, the New Game button didn’t fully reset the game and still showed “You already won.” I also noticed that the secret number kept changing every time I interacted with the app because it wasn’t being stored persistently.
      
- [x] Explain what fixes you applied.
      I fixed the secret number by storing it in st.session_state so it stays the same across reruns. I also made the New Game button reset all the important values: attempts, score, history, status, and generate a new secret number. Finally, I made sure the guess form worked properly so guesses are processed reliably, making the game behave as expected.

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

      
<img width="1525" height="1167" alt="Glithy Guesser" src="https://github.com/user-attachments/assets/fdecbf45-18eb-406b-b193-4fdd0b9502f2" />

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
