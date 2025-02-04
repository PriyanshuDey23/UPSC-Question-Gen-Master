# Import required libraries
import streamlit as st
import pandas as pd
from Helper.helper import QuestionGenerator
import os

# Main class to handle quiz functionality
class QuizManager:
    def __init__(self):
        # Initialize empty lists to store questions, user answers and results
        self.questions = []
        self.user_answers = []
        self.results = []

    def generate_questions(self, generator, topic, question_type, difficulty, num_questions): # UI argument
        # Reset all lists before generating new questions(For second time )
        self.questions = []
        self.user_answers = []
        self.results = []

        try:
            # Generate specified number of questions
            for _ in range(num_questions):
                # Handle Multiple Choice Questions
                if question_type == "Multiple Choice":
                    question = generator.generate_mcq(topic, difficulty.lower()) # generate mcq question
                    self.questions.append({
                        'type': 'MCQ',
                        'question': question.question,
                        'options': question.options,
                        'correct_answer': question.correct_answer
                    })

                # Handle Fill in the Blank Questions
                elif question_type == "Fill in the Blank":
                    question = generator.generate_fill_blank(topic, difficulty.lower()) # generate fill in the blanks question
                    self.questions.append({
                        'type': 'Fill in the Blank',
                        'question': question.question,
                        'correct_answer': question.answer
                    })
                
                # Handle True/False
                elif question_type == "True/False":
                    question = generator.generate_true_false(topic, difficulty.lower())
                    self.questions.append({
                        'type': 'True/False',
                        'question': question.question,
                        'options': ["True", "False"],
                        'correct_answer': question.correct_answer
                    })

        except Exception as e:
            # Display error if question generation fails
            st.error(f"Error generating questions: {e}")
            return False
        return True

    # Attempt a quiz
    def attempt_quiz(self):
        # Display questions and collect user answers
        for i, q in enumerate(self.questions): # self.questions likely holds a list of questions for the quiz.
            # i - input query and the actual question (q). 

            # Display question with bold formatting
            st.markdown(f"**Question {i+1}: {q['question']}**")
            
            # MCQ
            if q['type'] == 'MCQ':
                user_answer = st.radio(f"Select an answer for Question {i+1}", q['options'], key=f"mcq_{i}")
            # Fill in the Blanks
            elif q['type'] == 'Fill in the Blank':
                user_answer = st.text_input(f"Fill in the blank for Question {i+1}", key=f"fill_blank_{i}")
            # True /False
            elif q['type'] == 'True/False':
                user_answer = st.radio(f"Select True or False for Question {i+1}", ["True", "False"], key=f"tf_{i}")
            self.user_answers.append(user_answer) # Append

    # Evaluation for score generation
    def evaluate_quiz(self):
        # Reset results before evaluation
        self.results = []
        # Evaluate each question and user answer pair
        for i, (q, user_ans) in enumerate(zip(self.questions, self.user_answers)):
            # Create base result dictionary
            result_dict = {
                'question_number': i + 1,
                'question': q['question'],
                'question_type': q['type'],
                'user_answer': user_ans,
                'correct_answer': q['correct_answer'],
                'is_correct': user_ans.strip().lower() == q['correct_answer'].strip().lower()
            }
            self.results.append(result_dict)
            
    # Convert to data frame 
    def generate_result_dataframe(self):
        # Convert results to pandas DataFrame
        if not self.results:
            return pd.DataFrame()
        return pd.DataFrame(self.results)

    # Save to csv
    def save_to_csv(self, filename='quiz_results.csv'):
        try:
            # Check if results exist
            if not self.results:
                st.warning("No results to save. Please complete the quiz first.")
                return None
            
            # Generate DataFrame from results
            df = self.generate_result_dataframe()
            
            # Create unique filename with timestamp
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            unique_filename = f"quiz_results_{timestamp}.csv"
            
            # Ensure results directory exists
            os.makedirs('results', exist_ok=True)
            full_path = os.path.join('results', unique_filename)
            
            # Save results to CSV
            df.to_csv(full_path, index=False)
            
            # Display success message
            st.success(f"Results saved to {full_path}")
            return full_path
        except Exception as e:
            # Handle any errors during saving
            st.error(f"Failed to save results: {e}")
            return None

def main():
    # Configure Streamlit page with emoji
    st.set_page_config(page_title="UPSC & PCS Question Generator 📝", page_icon="📝")
    
    # Initialize session state variables
    if 'quiz_manager' not in st.session_state:
        st.session_state.quiz_manager = QuizManager()
    if 'quiz_generated' not in st.session_state:
        st.session_state.quiz_generated = False
    if 'quiz_submitted' not in st.session_state:
        st.session_state.quiz_submitted = False

    # Set page title with emoji
    st.title("UPSC & PCS Question Generator 📝")

    # Create sidebar for quiz settings with emojis
    st.sidebar.header("Quiz Settings ⚙️")
    


    # Question type selection with emojis
    question_type = st.sidebar.selectbox(
        "Select Question Type 🧩", 
        ["Multiple Choice", "Fill in the Blank", "True/False"], 
        index=0
    )

    # Topic input field with emoji
    topic = st.sidebar.text_input(
        "Enter Topic 📚", 
        placeholder="Indian History, Geography, etc."
    )

    # Difficulty level selection with emoji
    difficulty = st.sidebar.selectbox(
        "Difficulty Level ⚖️", 
        ["Easy", "Medium", "Hard"], 
        index=1
    )

    # Number of questions input with emoji
    num_questions = st.sidebar.number_input(
        "Number of Questions 🔢", 
        min_value=1, 
        max_value=10, 
        value=5
    )

    # Generate quiz button handler with emoji
    if st.sidebar.button("Generate Quiz Start the Exam 🎯"):
        st.session_state.quiz_submitted = False
        generator = QuestionGenerator()
        st.session_state.quiz_generated = st.session_state.quiz_manager.generate_questions(
            generator, topic, question_type, difficulty, num_questions
        )
        st.rerun()

    # Display quiz if generated
    if st.session_state.quiz_generated and st.session_state.quiz_manager.questions:
        st.header("Quiz 🎓")
        st.session_state.quiz_manager.attempt_quiz() # User attempt
        
        # Submit quiz button handler with emoji
        if st.button("Submit Quiz 📥"):
            st.session_state.quiz_manager.evaluate_quiz() # Evaluate the quiz
            st.session_state.quiz_submitted = True
            st.rerun()
    
    # Display results if quiz is submitted (In Percentage)
    if st.session_state.quiz_submitted:
        st.header("Quiz Results 🏆")
        results_df = st.session_state.quiz_manager.generate_result_dataframe()
        
        # Show results if available
        if not results_df.empty:
            # Calculate and display score
            # Convert to percentage
            correct_count = results_df['is_correct'].sum() # Correct question sum 
            total_questions = len(results_df)
            score_percentage = (correct_count / total_questions) * 100
            
            st.write(f"Score: {correct_count}/{total_questions} ({score_percentage:.1f}%)")
            
            # Display detailed results for each question
            # which question is correct and which question is wrong 
            for _, result in results_df.iterrows():
                question_num = result['question_number']
                if result['is_correct']:
                    st.success(f"✅ Question {question_num}: {result['question']}")
                else:
                    st.error(f"❌ Question {question_num}: {result['question']}") # Question
                    st.write(f"Your Answer: {result['user_answer']}") # User answer
                    st.write(f"Correct Answer: {result['correct_answer']}") # Correct answer
                
                st.markdown("---")
            
            # Save results button handler
            if st.button("Save Results 💾"):
                saved_file = st.session_state.quiz_manager.save_to_csv()
                if saved_file:
                    with open(saved_file, 'rb') as f:
                        st.download_button(
                            label="Download Results 📥",
                            data=f.read(),
                            file_name=os.path.basename(saved_file),
                            mime='text/csv'
                        )
        else:
            st.warning("No results available. Please complete the quiz first.")

# Entry point of the application
if __name__ == "__main__":
    main()