from src.pycoq import PythonToCoqTranslator

def main():
    # Example Python code
    python_code = """
def sum_up_to(n):
    total = 0
    for i in range(n):
        total += i
    return total
    """
    
    translator = PythonToCoqTranslator()
    result = translator.translate(python_code)
    
    print("Generated Coq Code:")
    print(result.coq_code)
    print("\nGenerated Theorems:")
    for theorem in result.theorems:
        print(f"\n{theorem.name}:")
        print(theorem.statement)

if __name__ == "__main__":
    main()