from .classes import CoqTheorem, Pattern

# --- Theorem Generator ---
class TheoremGenerator:
    def generate_theorem(self, pattern: Pattern) -> CoqTheorem:
        if pattern.pattern_type == 'loop_invariant':
            return self._generate_loop_invariant_theorem(pattern)
        elif pattern.pattern_type == 'function_postcondition':
            return self._generate_function_postcondition_theorem(pattern)
        elif pattern.pattern_type == 'list_operation':
            return self._generate_list_operation_theorem(pattern)
        raise ValueError(f"Unknown pattern type: {pattern.pattern_type}")

    def _generate_loop_invariant_theorem(self, pattern: Pattern) -> CoqTheorem:
        loop_node = pattern.python_ast
        loop_var = loop_node.target.id
        
        theorem = CoqTheorem(
            name=f"loop_invariant_{loop_var}",
            statement=pattern.theorem_template.format(
                name=f"loop_invariant_{loop_var}",
                loop_var=loop_var,
                invariant=f"0 <= {loop_var} <= n"
            ),
            proof="""
            Proof.
              intros n H1 H2.
              induction n.
              - auto.
              - apply IHn.
                auto.
            Qed.
            """
        )
        return theorem