from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

class Question:
    def __init__(self, text, options, correct_answer, difficulty):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        self.difficulty = difficulty

class QuizAlgorithm:
    def __init__(self):
        self.questions = []
        self.user_score = 0
        self.user_level = 'beginner'
        self.difficulty_levels = ['beginner', 'intermediate', 'advanced']

    def add_question(self, question):
        self.questions.append(question)

    def calculate_user_level(self):
        if self.user_score < 50:
            self.user_level = 'beginner'
        elif 50 <= self.user_score < 80:
            self.user_level = 'intermediate'
        else:
            self.user_level = 'advanced'

    def get_questions_for_level(self, num_questions):
        level_index = self.difficulty_levels.index(self.user_level)
        available_levels = self.difficulty_levels[max(0, level_index - 1):min(len(self.difficulty_levels), level_index + 2)]
        
        suitable_questions = [q for q in self.questions if q.difficulty in available_levels]
        return random.sample(suitable_questions, min(num_questions, len(suitable_questions)))

quiz = QuizAlgorithm()

# Add 50 sample questions
quiz.add_question(Question("What is a stack?", 
    ["A linear data structure that follows FIFO", "A hierarchical structure", 
     "A linear data structure that follows LIFO", "A tree structure"], 2, "beginner"))
quiz.add_question(Question("Which operation is not applicable to a stack?", 
    ["Push", "Pop", "Peek", "Random Access"], 3, "beginner"))
quiz.add_question(Question("What is an application of stacks?", 
    ["Recursion", "Breadth-First Search", "Dijkstra's Algorithm", "Merge Sort"], 0, "intermediate"))
quiz.add_question(Question("What's the result of: Push(1), Push(2), Pop(), Push(3), Pop(), Pop()?", 
    ["3", "2", "1", "Stack is empty"], 3, "intermediate"))
quiz.add_question(Question("Time complexity of insertion in a full array-based stack?", 
    ["O(1)", "O(n)", "O(log n)", "O(n^2)"], 1, "advanced"))
quiz.add_question(Question("Main difference between stack and queue?", 
    ["LIFO vs FIFO", "Same order", "Queue efficiency", "Stack type restriction"], 0, "beginner"))
quiz.add_question(Question("Operation to add an element to a stack?", 
    ["Enqueue", "Push", "Insert", "Append"], 1, "beginner"))
quiz.add_question(Question("Operation to remove the most recent element from a stack?", 
    ["Peek", "Pop", "Push", "Add"], 1, "beginner"))
quiz.add_question(Question("Best data structure for undo functionality?", 
    ["Queue", "Stack", "Array", "Linked List"], 1, "intermediate"))
quiz.add_question(Question("Space complexity of a dynamic array-based stack?", 
    ["O(1)", "O(n)", "O(log n)", "O(n^2)"], 1, "advanced"))
quiz.add_question(Question("What is the primary purpose of a stack?", 
    ["Sorting", "Temporary storage", "Permanent storage", "Data transmission"], 1, "beginner"))
quiz.add_question(Question("In which order are elements processed in a stack?", 
    ["Alphabetical", "Numerical", "Last In First Out", "First In First Out"], 2, "beginner"))
quiz.add_question(Question("What happens when you try to pop from an empty stack?", 
    ["Nothing", "Returns null", "Stack underflow error", "Crashes the program"], 2, "intermediate"))
quiz.add_question(Question("Which data structure is typically used to implement a stack?", 
    ["Linked List", "Array", "Both A and B", "Neither A nor B"], 2, "intermediate"))
quiz.add_question(Question("What is the time complexity of push operation in a stack?", 
    ["O(1)", "O(n)", "O(log n)", "O(n^2)"], 0, "advanced"))
quiz.add_question(Question("Which of these is not a basic operation of a stack?", 
    ["Push", "Pop", "Peek", "Sort"], 3, "beginner"))
quiz.add_question(Question("What does the peek operation do in a stack?", 
    ["Removes top element", "Adds new element", "Views top element without removing", "Empties the stack"], 2, "beginner"))
quiz.add_question(Question("In which scenario is a stack most useful?", 
    ["Breadth-first search", "Depth-first search", "Sorting", "Shortest path finding"], 1, "intermediate"))
quiz.add_question(Question("What is the space complexity of a stack implemented using a linked list?", 
    ["O(1)", "O(n)", "O(log n)", "O(n^2)"], 1, "advanced"))
quiz.add_question(Question("Which of these is a real-world analogy for a stack?", 
    ["Queue at a ticket counter", "Pile of plates", "Water in a glass", "Book on a shelf"], 1, "beginner"))
quiz.add_question(Question("What is the primary disadvantage of using an array to implement a stack?", 
    ["Slow access time", "Fixed size", "High memory usage", "Complexity in implementation"], 1, "intermediate"))
quiz.add_question(Question("In a stack, where does the 'top' pointer point?", 
    ["First element", "Last element", "Middle element", "Random element"], 1, "beginner"))
quiz.add_question(Question("Which of these sorting algorithms uses a stack?", 
    ["Bubble Sort", "Insertion Sort", "Quick Sort", "Selection Sort"], 2, "advanced"))
quiz.add_question(Question("What is the time complexity of accessing the middle element in a stack?", 
    ["O(1)", "O(n)", "O(log n)", "Not possible directly"], 3, "intermediate"))
quiz.add_question(Question("Which of these is not an application of stack?", 
    ["Function call management", "Expression evaluation", "Backtracking", "Queue implementation"], 3, "intermediate"))
quiz.add_question(Question("What is a double-ended stack?", 
    ["A stack with two tops", "A stack with no bottom", "A stack that can grow in both directions", "There's no such thing"], 2, "advanced"))
quiz.add_question(Question("In which memory segment are stack variables stored?", 
    ["Heap", "Stack", "Data", "Code"], 1, "intermediate"))
quiz.add_question(Question("What is the primary advantage of using a linked list to implement a stack?", 
    ["Faster operations", "Dynamic size", "Less memory usage", "Simpler implementation"], 1, "intermediate"))
quiz.add_question(Question("Which of these is true about stack overflow?", 
    ["It occurs when stack is empty", "It occurs when stack is full", "It's impossible in dynamic stacks", "It's a type of sorting algorithm"], 1, "beginner"))
quiz.add_question(Question("What is the time complexity of reversing a stack?", 
    ["O(1)", "O(n)", "O(log n)", "O(n^2)"], 1, "advanced"))
quiz.add_question(Question("Which data structure is used to check for balanced parentheses?", 
    ["Queue", "Stack", "Linked List", "Array"], 1, "intermediate"))
quiz.add_question(Question("What is a stack frame?", 
    ["A GUI element", "Memory allocated for function call", "A type of stack", "A stack overflow error"], 1, "advanced"))
quiz.add_question(Question("In which order are function parameters pushed onto the stack?", 
    ["Left to right", "Right to left", "Random order", "Depends on the compiler"], 1, "advanced"))
quiz.add_question(Question("What is the primary use of stack in memory management?", 
    ["Storing global variables", "Managing function calls and local variables", "Allocating heap memory", "Storing program instructions"], 1, "intermediate"))
quiz.add_question(Question("Which of these is not stored in a stack frame?", 
    ["Return address", "Local variables", "Parameters", "Global variables"], 3, "advanced"))
quiz.add_question(Question("What is the difference between push and pop operations in terms of stack pointer movement?", 
    ["Push decreases, pop increases", "Push increases, pop decreases", "Both increase", "Both decrease"], 1, "intermediate"))
quiz.add_question(Question("Which of these is true about stack in terms of memory allocation?", 
    ["It uses dynamic memory allocation", "It uses static memory allocation", "It doesn't use memory", "It uses both static and dynamic allocation"], 1, "intermediate"))
quiz.add_question(Question("What is the primary advantage of using stack for function call management?", 
    ["Faster execution", "Memory efficiency", "Simplicity in handling nested calls", "Better security"], 2, "advanced"))
quiz.add_question(Question("In which scenario would you prefer a queue over a stack?", 
    ["Undo mechanism", "Function call management", "Breadth-first search", "Expression evaluation"], 2, "intermediate"))
quiz.add_question(Question("What is a stack pointer?", 
    ["A pointer to the base of the stack", "A pointer to the top of the stack", "A pointer to the middle of the stack", "A pointer to the next available memory location"], 1, "intermediate"))
quiz.add_question(Question("Which of these is not a valid state for a stack?", 
    ["Empty", "Full", "Half-full", "Sorted"], 3, "beginner"))
quiz.add_question(Question("What is the time complexity of finding the minimum element in a stack?", 
    ["O(1)", "O(n)", "O(log n)", "O(n^2)"], 1, "advanced"))
quiz.add_question(Question("Which of these is true about multi-stack?", 
    ["It's a single stack with multiple elements", "It's multiple stacks in the same memory space", "It's a stack of stacks", "There's no such concept"], 1, "advanced"))
quiz.add_question(Question("What is the primary use of stack in parsing?", 
    ["Storing variables", "Handling nested structures", "Sorting elements", "Creating parse tree"], 1, "advanced"))
quiz.add_question(Question("In which memory model is stack size fixed?", 
    ["32-bit Windows", "64-bit Windows", "Linux", "All of the above"], 0, "advanced"))
quiz.add_question(Question("What is the relationship between stack and heap in memory management?", 
    ["Stack is a part of heap", "Heap is a part of stack", "They are separate memory areas", "They are the same thing"], 2, "intermediate"))
quiz.add_question(Question("Which of these is true about stack memory allocation?", 
    ["It's slower than heap allocation", "It's faster than heap allocation", "It's the same speed as heap allocation", "Speed depends on the size of allocation"], 1, "intermediate"))
quiz.add_question(Question("What happens to local variables when a function returns?", 
    ["They are moved to the heap", "They remain in the stack", "They are popped off the stack", "They become global variables"], 2, "intermediate"))
quiz.add_question(Question("Which of these is not a characteristic of stack memory?", 
    ["Last In First Out", "Fixed size", "Fast allocation", "Dynamic size"], 3, "intermediate"))

# Route to serve the Quiz HTML file
@app.route('/')
def quiz_page():
    return render_template('Quiz.html')

# API endpoint to send the questions to the front-end
@app.route('/questions', methods=['GET'])
def get_questions():
    num_questions = 10  # Set to 10 questions per quiz
    questions_for_quiz = quiz.get_questions_for_level(num_questions)
    questions_json = [
        {
            "question": q.text,
            "answers": [{"Text": option, "correct": i == q.correct_answer} for i, option in enumerate(q.options)]
        }
        for q in questions_for_quiz
    ]
    return jsonify(questions_json)

# API endpoint to update user score and level
@app.route('/update_score', methods=['POST'])
def update_score():
    data = request.json
    quiz.user_score = data['score']
    quiz.calculate_user_level()
    return jsonify({"level": quiz.user_level})

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
