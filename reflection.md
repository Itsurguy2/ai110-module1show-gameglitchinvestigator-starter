# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

A. The first time I ran the game, it appeared to be a simple minimum viable product (MVP) application. The interface looked clean and functional, and at first glance it seemed like a normal application that worked as expected. The layout included the guessing input, difficulty settings, and score information, which made it look like a complete game. However, after interacting with it and testing different scenarios, I began to notice several inconsistencies and bugs in the gameplay logic. This showed that even though the interface looked correct, the underlying functionality still required debugging and improvement.

- List at least two concrete bugs you noticed at the start  

B. One of the first bugs I noticed was related to submitting guesses. The input box displayed a message that said “Press Enter to submit,” but pressing the Enter key did not actually submit the guess. Instead, I had to click the Submit Guess button for the program to process the input, which created confusion for the user. Another issue occurred after correctly guessing the secret number. The game displayed a message indicating that I had won, but when I clicked the New Game button, the game did not restart and instead displayed a message saying “You already won.” As a result, the New Game button was effectively non-functional and prevented the player from starting another round.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

A. For this project, I used the embedded Claude.ai agent as my primary AI assistant. The tool helped analyze the code, identify potential bugs, and suggest possible fixes during the debugging process. It also assisted with explaining issues in the program logic and generating ideas for improvements and tests. However, I still reviewed the suggestions carefully and verified that the solutions made sense before applying them. This helped ensure that I remained in control of the development process rather than relying entirely on the AI’s output.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

B. One example of a correct AI suggestion involved removing the line of code that revealed the secret number in the Developer Debug Info section. Originally, the debug panel displayed the secret number using the line st.write("Secret:", st.session_state.secret), which allowed any player to view the correct answer and win the game immediately. The AI suggested removing this line so that the secret number would not be visible to users. This change preserved the integrity of the guessing game while still allowing other useful debug information to remain visible. After applying the change and refreshing the application, I verified that the secret number was no longer displayed, confirming that the fix worked as intended.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

C. During the debugging process, I did not encounter an AI suggestion that was completely incorrect, but there were a few issues that the AI initially overlooked. One example was the continued exposure of the secret number in the Developer Debug Info section of the application. Although the AI helped identify several other bugs, this issue required additional observation and discussion before we decided that the secret value should be hidden from the user interface. Revealing the secret number allowed players to see the correct answer and removed the challenge of the game. After removing the line that displayed the secret number and refreshing the application, I confirmed that the answer was no longer visible and that the game behaved as expected.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

A. I determined whether a bug was fixed by reviewing the relevant section of the code and then testing the application after making the change. After applying a fix, I refreshed and reran the application using the command python -m streamlit run app.py in the VS Code terminal. This allowed me to interact with the game and observe whether the behavior matched the expected outcome. By repeating the steps that originally caused the bug, I could confirm whether the issue had been resolved. If the problem no longer occurred during testing, I considered the bug to be successfully fixed.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.

B. One automated test I used involved verifying the get_range_for_difficulty function with pytest. This test checked that each difficulty level returned the correct range values, such as (1, 20) for Easy, (1, 100) for Normal, and (1, 200) for Hard. It also included a test to ensure that Hard mode actually had a larger range than Normal mode, confirming that the difficulty progression was logical. In addition, the test verified that if an unknown difficulty value was passed to the function, the program would safely default to the Normal range. Running these tests helped confirm that the difficulty logic in the game worked correctly and behaved consistently under different inputs.

- Did AI help you design or understand any tests? How?

C. Yes, the AI agent helped me better understand how to design and interpret tests by providing example test cases. It demonstrated how to structure tests using pytest, including how to check expected outputs for specific functions in the program. By reviewing these examples, I was able to see how different inputs could be used to verify that the functions behaved correctly under various conditions. The examples also helped me understand how automated tests can confirm that logic, such as difficulty ranges and scoring behavior, works as intended. This guidance improved my understanding of how testing can be used to validate code and detect potential errors.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

A. The secret number kept changing because Streamlit reruns the entire script every time the user interacts with the app. In the original version of the program, the secret number was generated with random.randint() during each rerun.

This meant that every time the user entered a guess, clicked a button, or changed a setting, the script executed again and generated a new secret number, making it impossible for the player to guess the correct number consistently.

Because the value was not stored anywhere persistent, the game effectively reset the secret number on every interaction.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

B. Streamlit works differently from traditional web apps. Instead of running continuously, the entire Python script runs from top to bottom every time the user interacts with the interface. This behavior is called a rerun.

For example, if a user:

enters text

presses a button

changes a dropdown

Streamlit immediately reruns the entire script to update the interface.

Because of this behavior, any variables created normally in the script will be reset each time the app reruns.

To preserve values between reruns, Streamlit provides st.session_state, which acts like a small storage area that remembers values for the duration of the user’s session. By saving important variables there, such as the secret number, the app can maintain state even though the script keeps rerunning.

- What change did you make that finally gave the game a stable secret number?

C. The fix was to store the secret number in Streamlit's session state instead of recreating it on every rerun.

The secret number is now only generated once when the session starts, using a conditional check:

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

This ensures that:

the secret number is created only once

it persists across reruns

the player can keep guessing the same number until the game ends or a new game is started

By using st.session_state, the game maintains consistent state even though Streamlit reruns the script after every interaction.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? This could be a testing habit, a prompting strategy, or a way you used Git.

A. One habit I want to continue using is testing edge cases early in development. During this project I saw how easy it is for programs to break when users enter unexpected input, such as empty values, non-numeric input, or numbers outside the expected range. Writing tests and intentionally trying unusual inputs helped reveal several bugs that were not obvious when simply running the program normally. In future projects I want to make edge-case testing a regular part of my workflow instead of waiting until the end to check for errors.

- What is one thing you would do differently next time you work with AI on a coding task?

B. Next time I would review AI-generated code more carefully before assuming it is correct. In this project the AI generated code that looked reasonable at first but contained logical issues, such as reversed hints and inconsistent difficulty settings. In the future I would spend more time reading through the code step by step and verifying the logic before integrating it into the project.  

- In one or two sentences, describe how this project changed the way you think about AI generated code.

C. This project showed me that AI can be very helpful for generating starting points, but the output still needs careful review and testing. AI-generated code may appear correct, but small logic errors or design problems can still occur, so developers must actively verify and refine the results.