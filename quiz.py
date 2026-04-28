import json
import os
from typing import List, Dict

# Load quiz questions from JSON
def load_quiz_questions() -> Dict[str, List[Dict]]:
    with open('data/quiz_questions.json', 'r', encoding='utf-8') as f:
        return json.load(f)

# Example structure:
# {
#     "constitution": [
#         {"question": "Вопрос?", "options": ["A", "B", "C", "D"], "answer": "A"}
#     ]
# }