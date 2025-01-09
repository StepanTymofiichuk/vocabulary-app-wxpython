![Italian Test Application logo](icon.png "Italian Test Application logo")

# User Documentation for Italian Test Application

## Introduction
The Italian Test application is designed to help users practice and test their knowledge of Italian vocabulary. The application presents users with Italian words and requires them to input the corresponding English translation. Users receive feedback on their responses and can track their progress throughout the test.

![Quick Start Guide](https://github.com/StepanTymofiichuk/vocabulary-app-wxpython/blob/main/il_Testo_Del_%20Vocabulario.gif)

## Inspiration
Two years ago, I started learning Italian with a set of 500 flashcards. After mastering them, I decided to create a desktop app to help reinforce my vocabulary. This app allows users to enter words or phrases and track their progress through three levels of mastery. Each level challenges the user to correctly translate and write the words in Italian, helping them move from basic recognition to full mastery. I update the app weekly with 30 new words or phrases, making it a consistent tool for language practice. 

## Technical Details
The program is developed using the following technologies:
<table>
    <tr>
        <th>FrontEnd</th>
        <th>BackEnd</th>
    <tr>
    <tr>
        <td><code>wxpython</code></td>
        <td><code>sqlite3</code></td>
    <tr>
</table>
<code>wxpython</code> is used for building User Interface. <code>sqlite3</code> is used as a database for storing vocabulary.

## Getting Started
To run the Italian Test application, follow these steps:

1. Open terminal and clone repository to your computer:
   ```bash
   git clone https://github.com/StepanTymofiichuk/vocabulary-app-wxpython.git
   ```
2. Ensure you have Python installed on your system:
   ```bash
   python --version
   ```
3. Ensure you have Pip installed on your system:
   ```bash
   pip --version
   ```
4. Create virtual environment:
   ```bash
   python -m venv .venv
   ```
5. Activate virtual environment (Windows):
   ```bash
   .venv\Scripts\activate
   ```
   For <code>bash</code> terminal use (Linux):
   ```bash
   source .venv/bin/activate
   ```
6. Install the required libraries by running the following command in your terminal:
   ```bash
   pip install -r requirements.txt
   ```
7. Run the script using a Python interpreter.
   ```bash
   python main-italiano-parlato.py
   ```
To make standalone Italian Test application executable, pleaase follow these steps:

1. Activate virtual environment (Windows):
   ```bash
   .venv\Scripts\activate
   ```
   For <code>bash</code> terminal use (Linux):
   ```bash
   source .venv/bin/activate
   ```
2. Check for <code>pyinstaller</code> package:
   ```bash
   pip list
   ``` 
   If there is no <code>pyinstaller</code> package, run the following command:
   ```bash
   pip install pyinstaller
   ```
3. To make <code>.exe</code> run this command:
   ```bash
   pyinstaller main-italiano-parlato.py logo=icon.png
   ```
To launch application main interface:
1. Copy <code>config.json</code> then paste into <code>dist/main-italiano-parlato</code> folder, then do the same with <code>add.py</code> and <code>clear.py</code>, <code>icon.png</code> and <code>.db</code> files
2. Open <code>dist/main-italiano-parlato</code> then launch <code>.exe</code> file

To launch level 1-3 applications from main interface:
1. Copy <code>level1</code> folder then paste into <code>dist/main-italiano-parlato</code> folder, then do the same with <code>level2</code> and <code>level3</code> folders

## Application Interface
Upon launching the application, you will be presented with the main window, which includes the following components:

![Italian Test Application main interface](/screens/screen1.png "Italian Test Application Screen 1")

- **Ukrainian Word Display:** The Italian word to be translated is displayed at the top of the window.
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
## Logic
1. All vocabulary that is less than 100% studied from specified table will be fetched and then placed in random order in a list. 
2. User navigates between vocabulary and enters corresponding translation. If translation is correct than: <code>True</code> text will be displayed; 1 score point will be added; studied percentage will be increased by 20%; word count will be increased by 1; sound effect from <code>/sounds/true.wav</code> will play. 
3. If translation is not correct than: <code>False</code> text will be displayed; 1 score point will be substracted; studied percentage will not be changed; score count will be decreased by 1; sound effect from <code>/sounds/false.wav</code> will play. 
4. When <code>Translate</code> button is clicked then <code>Check</code> button will be disabled. Sound effect from <code>/sounds/translate.wav</code> will play.

## Additional Features

![Italian Test Application main interface](/screens/screen3.png "Italian Test Application Screen 3")

- **Translation Button:** Click the "Translate" button to reveal the correct English translation of the current Italian word.
- **Navigation Buttons:** Use the "<<," "Check," "Translate," and ">>" buttons to move backward, check answers, reveal translations, and move forward, respectively.

## Adding New Vocabulary
To add new vocabulary to Italian Test application, follow these steps:
 by running the following command
1. Ensure you have <code>ItalianStudent.db</code> file in your directory by running the following command in your terminal:
   ```bash
   dir
   ```
2. Activate virtual environment (Windows):
   ```bash
   .venv\Scripts\activate
   ```
   or
   ```bash
   source .venv/Scripts/activate
   ```
3. Run the script using a Python interpreter.
   ```bash
   python add.py
   ```
## User Interface
Upon launching the application, you will be presented with the main window, which includes the following components:

![Italian Test Application adding new vocabulary interface](/screens/screen4.png "Italian Test Application Screen 4")

- **Table Name Input:** Table name in the db to add new vocabulary (specified table will be created unless it exists in the db).
- **Word Input:** Enter your English word.
- **Translation Inputs:** Enter your Italian translation.
- **Add Button:** Click to insert new vocabulary into a table.
## Logic
1. User enters db name to add new vocabulary.
2. User enters an English word.
3. User enters Italian translation.
4. User clicks Add then new vocabulary will be inserted into a table with 0% studied; sound from <code>sounds/true.wac</code> will play; success message will display; button Add will be disabled.
5. If one of the fields is empty then sound from <code>sounds/false.wav</code> will play; error message will display.

## Tips and Notes
- Ensure that the application window is in focus to capture button clicks and input.
- Take advantage of the "Translate" button if you are unsure of a translation.
- Monitor your score and studied percentage to gauge your progress.

## Support and Feedback
If you encounter any issues or have feedback regarding the Italian Test application, please reach out to the developer for assistance.

Thank you for using the Italian Test application! Happy learning!
