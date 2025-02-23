import ast
from typing import List, Optional
from .classes import Pattern

# --- Pattern Recognition ---
class PatternRecognizer:
    def __init__(self):
        self.patterns = {
            'loop_invariant': self._match_loop_invariant,
            'function_postcondition': self._match_function_postcondition,
            'list_operation': self._match_list_operation
        }
    
    def _match_loop_invariant(self, node: ast.AST) -> Optional[Pattern]:
        if isinstance(node, ast.For):
            # Detect simple numerical loops
            if (isinstance(node.target, ast.Name) and 
                isinstance(node.iter, ast.Call) and 
                isinstance(node.iter.func, ast.Name) and 
                node.iter.func.id == 'range'):
                
                return Pattern(
                    pattern_type='loop_invariant',
                    python_ast=node,
                    theorem_template="""
                    Theorem {name}: forall n,
                      0 <= n -> 
                      {loop_var} < n ->
                      {invariant}.
                    """
                )
        return None

    def _match_function_postcondition(self, node: ast.AST) -> Optional[Pattern]:
        if isinstance(node, ast.FunctionDef):
            return Pattern(
                pattern_type='function_postcondition',
                python_ast=node,
                theorem_template="""
                Theorem {name}_postcondition:
                  forall {args},
                  {preconditions} ->
                  {postcondition}.
                """
            )
        return None

    def _match_list_operation(self, node: ast.AST) -> Optional[Pattern]:
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute) and node.func.attr in ['append', 'extend', 'pop']:
                return Pattern(
                    pattern_type='list_operation',
                    python_ast=node,
                    theorem_template="""
                    Theorem {name}_list_operation:
                      forall l1 l2,
                      {operation_property}.
                    """
                )
        return None

    def recognize(self, node: ast.AST) -> List[Pattern]:
        patterns = []
        for matcher in self.patterns.values():
            pattern = matcher(node)
            if pattern:
                patterns.append(pattern)
        return patterns