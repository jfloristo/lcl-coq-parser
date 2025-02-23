import ast

# --- Coq Code Generator ---
class CoqGenerator:
    def __init__(self):
        self.indent_level = 0
        self.indent_str = "  "

    def generate(self, node: ast.AST) -> str:
        if isinstance(node, ast.Module):
            return self._generate_module(node)
        elif isinstance(node, ast.FunctionDef):
            return self._generate_function(node)
        elif isinstance(node, ast.For):
            return self._generate_for_loop(node)
        elif isinstance(node, ast.If):
            return self._generate_if(node)
        elif isinstance(node, ast.Return):
            return self._generate_return(node)
        else:
            return f"(* Unsupported node type: {type(node).__name__} *)"

    def _generate_module(self, node: ast.Module) -> str:
        lines = ["Require Import Coq.Init.Nat.", "Require Import Coq.Lists.List.", "", "Module PythonTranslation.", ""]
        
        for body_node in node.body:
            lines.append(self.generate(body_node))
        
        lines.extend(["", "End PythonTranslation."])
        return "\n".join(lines)

    def _generate_function(self, node: ast.FunctionDef) -> str:
        args = [arg.arg for arg in node.args.args]
        arg_types = " -> ".join(["nat" for _ in args] + ["nat"])  # Simple type inference
        
        lines = [
            f"Definition {node.name} : {arg_types} :=",
            f"{self.indent_str}fix f {' '.join(args)} :=",
        ]
        
        self.indent_level += 2
        for body_node in node.body:
            lines.append(f"{self.indent_str * self.indent_level}{self.generate(body_node)}")
        self.indent_level -= 2
        
        return "\n".join(lines) + "."

    def _generate_for_loop(self, node: ast.For) -> str:
        # Convert Python range-based for loop to Coq
        return 

    def _generate_if(self, node: ast.If) -> str:
        return f"""
        match {self.generate(node.test)} with
        | true => {self.generate(node.body[0])}
        | false => {self.generate(node.orelse[0]) if node.orelse else "0"}
        end
        """

    def _generate_return(self, node: ast.Return) -> str:
        return f"return {self.generate(node.value)}"