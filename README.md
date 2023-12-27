# User Documentation for Italian Test Application

## Introduction
The Italian Test application is designed to help users practice and test their knowledge of Italian vocabulary. The application presents users with Italian words and requires them to input the corresponding English translation. Users receive feedback on their responses and can track their progress throughout the test.

## Getting Started
To run the Italian Test application, follow these steps:

1. Ensure you have Python installed on your system:
   ```bash
   python --version
   ```
2. Create virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate virtual environment (Windows):
   ```bash
   .venv\Scrippts\activate
   ```
4. Install the required libraries by running the following command in your terminal or command prompt:
   ```bash
   pip install -r requuirements.txt
   ```
5. Run the script using a Python interpreter.
   ```bash
   python test-calendario.py
   ```
## Application Interface
Upon launching the application, you will be presented with the main window, which includes the following components:

![Italian Test Application main interface](/screens/screen1.png "Italian Test Application Screen 1")

- **English Word Display:** The Italian word to be translated is displayed at the top of the window.
- **Translation Input:** Enter your English translation in the text box provided.
- **Navigation Buttons:** Use the "<<," "Check," "Translate," and ">>" buttons to navigate through the test and check your answers.
- **Feedback Area:** Receive feedback on the correctness of your translations in the status area.
- **Score and Progress:** Track your current score, percentage studied of each word, and progress through the test.


## Test Flow

![Italian Test Application main interface](/screens/screen2.png "Italian Test Application Screen 2")

1. Start with the first English word displayed.
2. Enter the Italian translation in the provided text box.
3. Click the "Check" button to verify your answer.
4. If correct, your score will increase, and you can continue to the next word.
5. If incorrect, your score may decrease, and you can continue to the next word.
6. Use the "<<," "Check," "Translate," and ">>" buttons to navigate through the test.

## Additional Features

![Italian Test Application main interface](/screens/screen3.png "Italian Test Application Screen 3")

- **Translation Button:** Click the "Translate" button to reveal the correct English translation of the current Italian word.
- **Navigation Buttons:** Use the "<<," "Check," "Translate," and ">>" buttons to move backward, check answers, reveal translations, and move forward, respectively.

## Tips and Notes
- Ensure that the application window is in focus to capture button clicks and input.
- Take advantage of the "Translate" button if you are unsure of a translation.
- Monitor your score and studied percentage to gauge your progress.

## Support and Feedback
If you encounter any issues or have feedback regarding the Italian Test application, please reach out to the developer for assistance.

Thank you for using the Italian Test application! Happy learning!
