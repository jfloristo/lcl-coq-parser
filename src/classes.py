from dataclasses import dataclass
from typing import List, Any

# --- Data Structures ---
@dataclass
class CoqTheorem:
    name: str
    statement: str
    proof: str

@dataclass
class Pattern:
    pattern_type: str
    python_ast: Any
    theorem_template: str

@dataclass
class TranslationResult:
    coq_code: str
    theorems: List[CoqTheorem]