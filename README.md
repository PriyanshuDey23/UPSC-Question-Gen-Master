# UPSC & PCS Question Generator 📝

## Overview
The **UPSC & PCS Question Generator** is a **Streamlit-based web application** that dynamically generates **Multiple Choice Questions (MCQ), Fill in the Blanks, and True/False** questions based on a given topic and difficulty level. Users can attempt the quiz, submit answers, and view detailed results, including correctness and percentage scores. The app also provides an option to save and download quiz results as a CSV file.

## Features 🚀
- **Supports Three Question Types**: Multiple Choice, Fill in the Blank, and True/False.
- **Dynamic Question Generation**: Generates quiz questions based on user-defined topic and difficulty level.
- **User-Friendly Interface**: Simple and interactive UI with sidebar settings for customization.
- **Real-time Answer Evaluation**: Immediate feedback on correct/incorrect answers.
- **Percentage Score Calculation**: Displays the user's performance as a percentage.
- **Downloadable Results**: Allows users to save quiz results as a CSV file.
- **Error Handling**: Provides error messages if question generation fails.

## Installation & Setup 🛠️

### Prerequisites
Ensure you have **Python 3.9+** installed.

### Step 1: Clone the Repository
```bash
git clone https://github.com/PriyanshuDey23/UPSC-Question-Gen-Master.git
cd upsc-quiz-generator
```

### Step 2: Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```
### Step 4: Set The GROQ Environment Key in .env file 
```bash
GROQ_API_KEY= " " 
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

## Usage 📖
1. **Set Quiz Parameters**: Select question type, enter a topic, set difficulty level, and specify the number of questions.
2. **Generate Quiz**: Click on "Generate Quiz Start the Exam 🎯" to create the quiz.
3. **Attempt Questions**: Answer each question using the provided UI.
4. **Submit Answers**: Click "Submit Quiz 📥" to evaluate your performance.
5. **View Results**: Check your correct/incorrect answers and overall score.
6. **Save & Download Results**: Option to save quiz results as a CSV file.

## File Structure 📂
```
UPSC-Quiz-Generator/
│── Helper/
│   ├── helper.py   # Contains the QuestionGenerator class for generating quiz questions
│── results/        # Directory where quiz results are stored as CSV files
│── app.py         # Main Streamlit application
│── requirements.txt # Dependencies for the project
│── README.md       # Project documentation (this file)
```

## Dependencies 📦
The application uses the following Python libraries:
- **Streamlit** (for UI rendering)
- **Pandas** (for data handling and result storage)
- **os & datetime** (for file management and timestamping results)

## Contributing 🤝
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`feature/your-feature`).
3. Commit your changes.
4. Push to the branch and create a PR.

## License 📜
This project is licensed under the **MIT License**.

## Contact 📧
For queries or feedback, feel free to reach out at **your-email@example.com**.

