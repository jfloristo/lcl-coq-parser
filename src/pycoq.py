import ast
from .classes import TranslationResult
from .patternRecognizer import PatternRecognizer
from .theoremGenerator import TheoremGenerator
from .coqGenerator import CoqGenerator

 # --- Main Translator ---
class PythonToCoqTranslator:
    def __init__(self):
        self.pattern_recognizer = PatternRecognizer()
        self.theorem_generator = TheoremGenerator()
        self.coq_generator = CoqGenerator()

    def translate(self, python_code: str) -> TranslationResult:
        # Parse Python code
        tree = ast.parse(python_code)
        
        # Collect patterns and generate theorems
        theorems = []
        for node in ast.walk(tree):
            patterns = self.pattern_recognizer.recognize(node)
            for pattern in patterns:
                theorem = self.theorem_generator.generate_theorem(pattern)
                theorems.append(theorem)
        
        # Generate Coq code
        coq_code = self.coq_generator.generate(tree)
        
        return TranslationResult(coq_code=coq_code, theorems=theorems)