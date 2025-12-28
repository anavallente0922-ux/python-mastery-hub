"""
Python Mastery Hub - Interactive Learning Platform
Built with Streamlit and PyGWalker-inspired theme
SINGLE FILE VERSION - No external imports needed
"""

import streamlit as st
import random
from datetime import datetime

# Practice Questions Data - 200 Multiple Choice Questions

PRACTICE_QUESTIONS = [
    # Core Syntax (1-25)
    {"id": 1, "category": "Core Syntax", "difficulty": "Easy", "question": "Correct way to create a variable?", "options": ["var x = 5", "int x = 5", "x = 5", "declare x = 5"], "answer": 2, "explanation": "Python uses dynamic typing - just assign with = sign."},
    {"id": 2, "category": "Core Syntax", "difficulty": "Easy", "question": "Single-line comment symbol?", "options": ["//", "/* */", "#", "<!-- -->"], "answer": 2, "explanation": "# starts a comment to end of line."},
    {"id": 3, "category": "Core Syntax", "difficulty": "Easy", "question": "type(5.0) output?", "options": ["<class 'int'>", "<class 'float'>", "<class 'number'>", "<class 'double'>"], "answer": 1, "explanation": "5.0 has decimal, making it float."},
    {"id": 4, "category": "Core Syntax", "difficulty": "Easy", "question": "Multi-line string creation?", "options": ["Using \\\\", "Triple quotes '''", "Semicolons", "Parentheses"], "answer": 1, "explanation": "Triple quotes preserve line breaks."},
    {"id": 5, "category": "Core Syntax", "difficulty": "Easy", "question": "print(2 ** 3)?", "options": ["6", "8", "5", "23"], "answer": 1, "explanation": "** is exponentiation: 2³ = 8"},
    {"id": 6, "category": "Core Syntax", "difficulty": "Easy", "question": "Floor division operator?", "options": ["/", "//", "%", "**"], "answer": 1, "explanation": "// divides and rounds down."},
    {"id": 7, "category": "Core Syntax", "difficulty": "Easy", "question": "Python file extension?", "options": [".pt", ".py", ".python", ".pyt"], "answer": 1, "explanation": ".py is standard Python extension."},
    {"id": 8, "category": "Core Syntax", "difficulty": "Medium", "question": "'is' operator checks?", "options": ["Value equality", "Type equality", "Identity", "String match"], "answer": 2, "explanation": "'is' checks same object in memory."},
    {"id": 9, "category": "Core Syntax", "difficulty": "Easy", "question": "print('A' + ' ' + 'B')?", "options": ["A B", "AB", "A + B", "Error"], "answer": 0, "explanation": "+ concatenates strings."},
    {"id": 10, "category": "Core Syntax", "difficulty": "Easy", "question": "10 % 3 result?", "options": ["3", "1", "3.33", "0"], "answer": 1, "explanation": "% returns remainder: 1"},
    {"id": 11, "category": "Core Syntax", "difficulty": "Medium", "question": ":= operator does?", "options": ["Comparison", "Assignment in expression", "Division", "Bitwise OR"], "answer": 1, "explanation": "Walrus operator assigns in expressions."},
    {"id": 12, "category": "Core Syntax", "difficulty": "Easy", "question": "bool('') result?", "options": ["True", "False", "None", "Error"], "answer": 1, "explanation": "Empty strings are falsy."},
    {"id": 13, "category": "Core Syntax", "difficulty": "Easy", "question": "Correct f-string?", "options": ["f'Hi {x}'", "'Hi {x}'.f()", "format('Hi {x}')", "'Hi'+f{x}"], "answer": 0, "explanation": "f prefix before quotes."},
    {"id": 14, "category": "Core Syntax", "difficulty": "Medium", "question": "0.1 + 0.2 == 0.3?", "options": ["True", "False", "0.3", "Error"], "answer": 1, "explanation": "Float precision issue."},
    {"id": 15, "category": "Core Syntax", "difficulty": "Medium", "question": "__name__ == '__main__' checks?", "options": ["Variable exists", "Script runs directly", "Function defined", "Module imported"], "answer": 1, "explanation": "True when running directly."},
    {"id": 16, "category": "Core Syntax", "difficulty": "Medium", "question": "a, *b, c = [1,2,3,4,5] - b is?", "options": ["2", "[2,3,4]", "[1,2,3,4]", "Error"], "answer": 1, "explanation": "*b collects middle: [2,3,4]"},
    {"id": 17, "category": "Core Syntax", "difficulty": "Easy", "question": "Get user input?", "options": ["scanf()", "input()", "read()", "get()"], "answer": 1, "explanation": "input() reads as string."},
    {"id": 18, "category": "Core Syntax", "difficulty": "Easy", "question": "len('Python')?", "options": ["5", "6", "7", "Error"], "answer": 1, "explanation": "6 characters: P-y-t-h-o-n"},
    {"id": 19, "category": "Core Syntax", "difficulty": "Medium", "question": "Variable inside function scope?", "options": ["Global", "Local", "Universal", "Static"], "answer": 1, "explanation": "Local by default."},
    {"id": 20, "category": "Core Syntax", "difficulty": "Easy", "question": "'pass' does?", "options": ["Exits loop", "Nothing", "Returns None", "Skips iteration"], "answer": 1, "explanation": "Null operation placeholder."},
    {"id": 21, "category": "Core Syntax", "difficulty": "Easy", "question": "Import only sqrt?", "options": ["import sqrt from math", "from math import sqrt", "import math.sqrt", "include math.sqrt"], "answer": 1, "explanation": "from module import item."},
    {"id": 22, "category": "Core Syntax", "difficulty": "Medium", "question": "type(lambda x:x)?", "options": ["lambda", "function", "method", "Error"], "answer": 1, "explanation": "Lambdas are function objects."},
    {"id": 23, "category": "Core Syntax", "difficulty": "Medium", "question": "'nonlocal' does?", "options": ["Creates global", "References enclosing scope", "Deletes variable", "Creates constant"], "answer": 1, "explanation": "Modifies enclosing scope variable."},
    {"id": 24, "category": "Core Syntax", "difficulty": "Easy", "question": "Valid variable name?", "options": ["2name", "my-var", "_count", "class"], "answer": 2, "explanation": "Can start with underscore."},
    {"id": 25, "category": "Core Syntax", "difficulty": "Easy", "question": "3 * 'ab'?", "options": ["Error", "ababab", "3ab", "ab3"], "answer": 1, "explanation": "String repetition."},
    
    # Data Types (26-55)
    {"id": 26, "category": "Data Types", "difficulty": "Easy", "question": "Which is immutable?", "options": ["list", "dict", "tuple", "set"], "answer": 2, "explanation": "Tuples can't be modified."},
    {"id": 27, "category": "Data Types", "difficulty": "Easy", "question": "Create empty dict?", "options": ["[]", "{}", "()", "dict[]"], "answer": 1, "explanation": "{} creates empty dict."},
    {"id": 28, "category": "Data Types", "difficulty": "Easy", "question": "list('abc')?", "options": ["['abc']", "['a','b','c']", "'abc'", "Error"], "answer": 1, "explanation": "Splits into characters."},
    {"id": 29, "category": "Data Types", "difficulty": "Easy", "question": "Add to end of list?", "options": ["add()", "append()", "insert()", "extend()"], "answer": 1, "explanation": "append() adds one item to end."},
    {"id": 30, "category": "Data Types", "difficulty": "Easy", "question": "set([1,2,2,3,3,3])?", "options": ["{1,2,2,3,3,3}", "{1,2,3}", "[1,2,3]", "Error"], "answer": 1, "explanation": "Sets remove duplicates."},
    {"id": 31, "category": "Data Types", "difficulty": "Medium", "question": "append vs extend?", "options": ["Same", "append=one, extend=many", "Opposite", "Speed difference"], "answer": 1, "explanation": "append adds item, extend adds each element."},
    {"id": 32, "category": "Data Types", "difficulty": "Easy", "question": "Access d['name']?", "options": ["d.name", "d[name]", "d['name']", "d->name"], "answer": 2, "explanation": "String key in brackets."},
    {"id": 33, "category": "Data Types", "difficulty": "Easy", "question": "(1,2,3) + (4,5)?", "options": ["(1,2,3,4,5)", "(5,7,3)", "Error", "[(1,2,3),(4,5)]"], "answer": 0, "explanation": "Tuple concatenation."},
    {"id": 34, "category": "Data Types", "difficulty": "Easy", "question": "Get dict keys?", "options": ["d.keys()", "d.get_keys()", "keys(d)", "d.all_keys()"], "answer": 0, "explanation": "keys() method returns view."},
    {"id": 35, "category": "Data Types", "difficulty": "Medium", "question": "frozenset is?", "options": ["Frozen list", "Immutable set", "Frozen dict", "Tuple alias"], "answer": 1, "explanation": "Immutable version of set."},
    {"id": 36, "category": "Data Types", "difficulty": "Medium", "question": "'hello'[1:4]?", "options": ["'hel'", "'ell'", "'ello'", "'hello'"], "answer": 1, "explanation": "Indices 1,2,3 = 'ell'"},
    {"id": 37, "category": "Data Types", "difficulty": "Medium", "question": "List as dict key?", "options": ["Works", "TypeError", "Converts", "Creates nested"], "answer": 1, "explanation": "Lists are unhashable."},
    {"id": 38, "category": "Data Types", "difficulty": "Easy", "question": "[1,2,3][-1]?", "options": ["Error", "1", "3", "2"], "answer": 2, "explanation": "Negative index = last element."},
    {"id": 39, "category": "Data Types", "difficulty": "Medium", "question": "bytes(5) creates?", "options": ["b'5'", "5 null bytes", "Error", "Random bytes"], "answer": 1, "explanation": "Creates 5 zero bytes."},
    {"id": 40, "category": "Data Types", "difficulty": "Easy", "question": "bool([]) result?", "options": ["True", "False", "None", "Error"], "answer": 1, "explanation": "Empty sequences are falsy."},
    {"id": 41, "category": "Data Types", "difficulty": "Medium", "question": "dict.get('x', 0) if 'x' missing?", "options": ["None", "0", "Error", "False"], "answer": 1, "explanation": "Returns default value."},
    {"id": 42, "category": "Data Types", "difficulty": "Medium", "question": "[x**2 for x in range(1,4)]?", "options": ["[1,2,3]", "[1,4,9]", "[2,4,6]", "Error"], "answer": 1, "explanation": "Squares: 1,4,9"},
    {"id": 43, "category": "Data Types", "difficulty": "Medium", "question": "{1,2,3} & {2,3,4}?", "options": ["{1,2,3,4}", "{2,3}", "{1,4}", "Error"], "answer": 1, "explanation": "& is intersection."},
    {"id": 44, "category": "Data Types", "difficulty": "Hard", "question": "defaultdict(list) does?", "options": ["Creates list", "Dict with default []", "Converts", "Error"], "answer": 1, "explanation": "Auto-creates empty list for missing keys."},
    {"id": 45, "category": "Data Types", "difficulty": "Easy", "question": "sorted([3,1,2], reverse=True)?", "options": ["[1,2,3]", "[3,2,1]", "(3,2,1)", "Error"], "answer": 1, "explanation": "Descending order."},
    {"id": 46, "category": "Data Types", "difficulty": "Medium", "question": "namedtuple for?", "options": ["Naming dicts", "Tuple with named fields", "Renaming", "None"], "answer": 1, "explanation": "Creates tuple subclass with names."},
    {"id": 47, "category": "Data Types", "difficulty": "Medium", "question": "deque advantage?", "options": ["Sorting", "O(1) both ends", "Type checking", "Persistence"], "answer": 1, "explanation": "Fast append/pop from both ends."},
    {"id": 48, "category": "Data Types", "difficulty": "Easy", "question": "type([1,2,3])?", "options": ["tuple", "list", "array", "set"], "answer": 1, "explanation": "Square brackets = list."},
    {"id": 49, "category": "Data Types", "difficulty": "Easy", "question": "'Python'.replace('P','J')?", "options": ["'Python'", "'Jython'", "'Jjthon'", "Error"], "answer": 1, "explanation": "Replaces P with J."},
    {"id": 50, "category": "Data Types", "difficulty": "Hard", "question": "'in' complexity: list vs set?", "options": ["Both O(1)", "Both O(n)", "List O(n), Set O(1)", "Opposite"], "answer": 2, "explanation": "Sets use hashing for O(1)."},
    {"id": 51, "category": "Data Types", "difficulty": "Medium", "question": "enumerate() returns?", "options": ["Indices only", "Index-value pairs", "Values only", "Dictionary"], "answer": 1, "explanation": "Yields (index, value) tuples."},
    {"id": 52, "category": "Data Types", "difficulty": "Medium", "question": "Copy a list?", "options": ["b = a", "b = a.copy()", "b = copy(a)", "B and list(a)"], "answer": 3, "explanation": "Use .copy(), list(), or [:]"},
    {"id": 53, "category": "Data Types", "difficulty": "Easy", "question": "'hello'.find('l')?", "options": ["2", "3", "[2,3]", "Error"], "answer": 0, "explanation": "First occurrence at index 2."},
    {"id": 54, "category": "Data Types", "difficulty": "Medium", "question": "zip() does?", "options": ["Compresses", "Pairs elements", "Adds", "Removes dups"], "answer": 1, "explanation": "Pairs corresponding elements."},
    {"id": 55, "category": "Data Types", "difficulty": "Easy", "question": "str.split() default?", "options": ["Comma", "Whitespace", "Newline", "Tab"], "answer": 1, "explanation": "Splits on any whitespace."},
    
    # Control Flow (56-80)
    {"id": 56, "category": "Control Flow", "difficulty": "Easy", "question": "Correct if syntax?", "options": ["if x==5 then:", "if (x==5):", "if x==5:", "if x==5 {"], "answer": 2, "explanation": "if condition: with colon."},
    {"id": 57, "category": "Control Flow", "difficulty": "Easy", "question": "Best for known iterations?", "options": ["while", "for", "do-while", "foreach"], "answer": 1, "explanation": "for with range() when count known."},
    {"id": 58, "category": "Control Flow", "difficulty": "Easy", "question": "break does?", "options": ["Skip iteration", "Exit loop", "Restart", "Pause"], "answer": 1, "explanation": "Exits loop entirely."},
    {"id": 59, "category": "Control Flow", "difficulty": "Easy", "question": "continue does?", "options": ["Exit loop", "Skip to next iteration", "Repeat current", "Nothing"], "answer": 1, "explanation": "Skips rest of current iteration."},
    {"id": 60, "category": "Control Flow", "difficulty": "Easy", "question": "for i in range(3): print(i)?", "options": ["1 2 3", "0 1 2", "0 1 2 3", "1 2"], "answer": 1, "explanation": "range(3) is 0,1,2"},
    {"id": 61, "category": "Control Flow", "difficulty": "Medium", "question": "for/else purpose?", "options": ["Error handling", "Runs if no break", "If false", "Invalid"], "answer": 1, "explanation": "else runs if loop completes normally."},
    {"id": 62, "category": "Control Flow", "difficulty": "Medium", "question": "Python ternary?", "options": ["a?b:c", "a if cond else b", "cond&&a||b", "if cond then a else b"], "answer": 1, "explanation": "value_if_true if condition else value_if_false"},
    {"id": 63, "category": "Control Flow", "difficulty": "Medium", "question": "[x for x in range(5) if x%2==0]?", "options": ["[0,2,4]", "[1,3]", "[0,1,2,3,4]", "[2,4]"], "answer": 0, "explanation": "Filters even: 0,2,4"},
    {"id": 64, "category": "Control Flow", "difficulty": "Medium", "question": "'with' statement does?", "options": ["Creates loop", "Manages resources", "Defines function", "Imports"], "answer": 1, "explanation": "Context manager for cleanup."},
    {"id": 65, "category": "Control Flow", "difficulty": "Easy", "question": "any([False, True, False])?", "options": ["False", "True", "None", "Error"], "answer": 1, "explanation": "True if ANY element truthy."},
    {"id": 66, "category": "Control Flow", "difficulty": "Easy", "question": "all([True, True, False])?", "options": ["True", "False", "None", "[True,True]"], "answer": 1, "explanation": "ALL must be True."},
    {"id": 67, "category": "Control Flow", "difficulty": "Easy", "question": "enumerate() provides?", "options": ["Count", "Index and value", "List", "Sort"], "answer": 1, "explanation": "(index, value) pairs."},
    {"id": 68, "category": "Control Flow", "difficulty": "Medium", "question": "reversed() returns?", "options": ["Reverses in place", "Iterator", "Sorted desc", "New list"], "answer": 1, "explanation": "Returns reversed iterator."},
    {"id": 69, "category": "Control Flow", "difficulty": "Medium", "question": "next(iter([1,2,3]))?", "options": ["[1,2,3]", "1", "(1,2,3)", "Error"], "answer": 1, "explanation": "Gets first item: 1"},
    {"id": 70, "category": "Control Flow", "difficulty": "Medium", "question": "Iterate dict key-values?", "options": ["for k,v in d:", "for k,v in d.items():", "for k,v in d.pairs():", "for (k,v) in d:"], "answer": 1, "explanation": "d.items() returns key-value pairs."},
    {"id": 71, "category": "Control Flow", "difficulty": "Medium", "question": "yield creates?", "options": ["Returns value", "Generator", "Error", "Import"], "answer": 1, "explanation": "Makes function a generator."},
    {"id": 72, "category": "Control Flow", "difficulty": "Easy", "question": "while True: break result?", "options": ["Infinite", "Runs once", "Error", "Never runs"], "answer": 1, "explanation": "Runs once then breaks."},
    {"id": 73, "category": "Control Flow", "difficulty": "Medium", "question": "range(2,10,2)?", "options": ["2,3..10", "2,4,6,8", "2,4,6,8,10", "Error"], "answer": 1, "explanation": "Start 2, stop 10, step 2."},
    {"id": 74, "category": "Control Flow", "difficulty": "Medium", "question": "match statement (3.10+)?", "options": ["Regex", "Pattern matching", "String only", "Not Python"], "answer": 1, "explanation": "Structural pattern matching."},
    {"id": 75, "category": "Control Flow", "difficulty": "Medium", "question": "try/except/else: else runs?", "options": ["On exception", "No exception", "Always", "Syntax error"], "answer": 1, "explanation": "else runs if NO exception."},
    {"id": 76, "category": "Control Flow", "difficulty": "Easy", "question": "Nested loops allowed?", "options": ["No", "Yes", "Max 2", "For only"], "answer": 1, "explanation": "Any depth allowed."},
    {"id": 77, "category": "Control Flow", "difficulty": "Medium", "question": "list(zip([1,2],[3,4]))?", "options": ["[[1,3],[2,4]]", "[(1,3),(2,4)]", "[1,2,3,4]", "Error"], "answer": 1, "explanation": "Pairs into tuples."},
    {"id": 78, "category": "Control Flow", "difficulty": "Easy", "question": "pass in if block?", "options": ["Error", "Does nothing", "Exits", "Skips"], "answer": 1, "explanation": "Placeholder that does nothing."},
    {"id": 79, "category": "Control Flow", "difficulty": "Medium", "question": "assert False result?", "options": ["Nothing", "AssertionError", "False", "None"], "answer": 1, "explanation": "Raises AssertionError."},
    {"id": 80, "category": "Control Flow", "difficulty": "Easy", "question": "How to check 'and'?", "options": ["if x>0 && x<10:", "if x>0 and x<10:", "if x>0 & x<10:", "if (x>0)+(x<10):"], "answer": 1, "explanation": "Python uses 'and' keyword."},
    
    # Functions (81-110)
    {"id": 81, "category": "Functions", "difficulty": "Easy", "question": "Define a function?", "options": ["function f():", "def f():", "func f():", "define f():"], "answer": 1, "explanation": "'def' keyword defines functions."},
    {"id": 82, "category": "Functions", "difficulty": "Easy", "question": "No return statement returns?", "options": ["0", "''", "None", "Error"], "answer": 2, "explanation": "Returns None by default."},
    {"id": 83, "category": "Functions", "difficulty": "Medium", "question": "*args is?", "options": ["Keyword args", "Variable positional args", "Required args", "Defaults"], "answer": 1, "explanation": "Collects extra positional args as tuple."},
    {"id": 84, "category": "Functions", "difficulty": "Medium", "question": "**kwargs is?", "options": ["Variable keywords", "Variable positional", "Two arguments", "Named tuples"], "answer": 0, "explanation": "Collects keyword args as dict."},
    {"id": 85, "category": "Functions", "difficulty": "Easy", "question": "Lambda is?", "options": ["Named function", "Anonymous function", "Recursive function", "Class method"], "answer": 1, "explanation": "Small anonymous one-line function."},
    {"id": 86, "category": "Functions", "difficulty": "Medium", "question": "(lambda x,y: x+y)(3,4)?", "options": ["Error", "7", "34", "lambda"], "answer": 1, "explanation": "Immediately called: 3+4 = 7"},
    {"id": 87, "category": "Functions", "difficulty": "Medium", "question": "Decorator is?", "options": ["Comment type", "Function modifier", "Class attribute", "Variable type"], "answer": 1, "explanation": "Wraps functions to modify behavior."},
    {"id": 88, "category": "Functions", "difficulty": "Medium", "question": "Apply decorator?", "options": ["decorator(f)", "@decorator", "f.decorator()", "Both A and B"], "answer": 3, "explanation": "@decorator = f = decorator(f). Both work."},
    {"id": 89, "category": "Functions", "difficulty": "Hard", "question": "Closure is?", "options": ["Error", "Function with enclosing scope", "File op", "Constructor"], "answer": 1, "explanation": "Function remembering enclosing scope."},
    {"id": 90, "category": "Functions", "difficulty": "Medium", "question": "lru_cache does?", "options": ["Sorts", "Caches results", "Limits calls", "Lazy eval"], "answer": 1, "explanation": "Memoizes function results."},
    {"id": 91, "category": "Functions", "difficulty": "Easy", "question": "return statement purpose?", "options": ["End program", "Print", "Send value to caller", "Create loop"], "answer": 2, "explanation": "Sends value back to caller."},
    {"id": 92, "category": "Functions", "difficulty": "Medium", "question": "Recursion is?", "options": ["Loop type", "Function calling itself", "Variable type", "Error handling"], "answer": 1, "explanation": "Function calls itself."},
    {"id": 93, "category": "Functions", "difficulty": "Medium", "question": "map() does?", "options": ["Creates dict", "Applies function to items", "Maps memory", "Coordinates"], "answer": 1, "explanation": "Applies func to every item."},
    {"id": 94, "category": "Functions", "difficulty": "Medium", "question": "filter() returns?", "options": ["List", "Filter object", "Boolean", "Dict"], "answer": 1, "explanation": "Iterator of items passing test."},
    {"id": 95, "category": "Functions", "difficulty": "Hard", "question": "@staticmethod vs @classmethod?", "options": ["Same", "static=no self, class=cls", "static faster", "class=no access"], "answer": 1, "explanation": "staticmethod: no auto arg, classmethod: gets cls."},
    {"id": 96, "category": "Functions", "difficulty": "Medium", "question": "sorted(items, key=lambda x:-x)?", "options": ["Ascending", "Descending", "Error", "No change"], "answer": 1, "explanation": "Negative key = descending order."},
    {"id": 97, "category": "Functions", "difficulty": "Easy", "question": "help() does?", "options": ["Exit", "Show docs", "Fix errors", "Import"], "answer": 1, "explanation": "Shows documentation."},
    {"id": 98, "category": "Functions", "difficulty": "Easy", "question": "Docstring is?", "options": ["Comment", "Documentation string", "Variable", "Error message"], "answer": 1, "explanation": "Documents code, accessible via __doc__."},
    {"id": 99, "category": "Functions", "difficulty": "Medium", "question": "@property does?", "options": ["Creates variable", "Method as attribute", "Protects data", "Creates class"], "answer": 1, "explanation": "Access method like attribute."},
    {"id": 100, "category": "Functions", "difficulty": "Easy", "question": "Return multiple values?", "options": ["No", "Yes, as tuple", "Separate returns", "Special syntax"], "answer": 1, "explanation": "return a, b returns tuple (a, b)."},
    {"id": 101, "category": "Functions", "difficulty": "Hard", "question": "functools.partial does?", "options": ["Splits function", "Pre-fills arguments", "Partial exec", "Error handling"], "answer": 1, "explanation": "Creates new function with some args pre-filled."},
    {"id": 102, "category": "Functions", "difficulty": "Medium", "question": "Default recursion limit?", "options": ["100", "1000", "No limit", "~1000 system dependent"], "answer": 3, "explanation": "Default around 1000, configurable via sys."},
    {"id": 103, "category": "Functions", "difficulty": "Medium", "question": "Generator uses?", "options": ["Creates classes", "yield", "Random numbers", "No params"], "answer": 1, "explanation": "Generators use 'yield'."},
    {"id": 104, "category": "Functions", "difficulty": "Hard", "question": "functools.wraps purpose?", "options": ["Wraps exceptions", "Preserves metadata", "Creates wrappers", "Wraps strings"], "answer": 1, "explanation": "@wraps preserves original function's name and docstring."},
    {"id": 105, "category": "Functions", "difficulty": "Medium", "question": "Higher-order function?", "options": ["Fast function", "Takes/returns functions", "OOP method", "Built-in only"], "answer": 1, "explanation": "Functions accepting/returning functions."},
    {"id": 106, "category": "Functions", "difficulty": "Hard", "question": "zip(*matrix) does?", "options": ["Compress", "Transpose", "Flatten", "Error"], "answer": 1, "explanation": "Transposes a matrix."},
    {"id": 107, "category": "Functions", "difficulty": "Medium", "question": "Lambda limitation?", "options": ["No limits", "Single expression only", "No arguments", "Can't return"], "answer": 1, "explanation": "Lambdas can only contain single expression."},
    {"id": 108, "category": "Functions", "difficulty": "Medium", "question": "global keyword does?", "options": ["Creates new global", "References global variable", "Deletes", "Makes constant"], "answer": 1, "explanation": "Allows modifying global inside function."},
    {"id": 109, "category": "Functions", "difficulty": "Hard", "question": "reduce() for?", "options": ["Reduces size", "Cumulative operation", "Removes items", "Compression"], "answer": 1, "explanation": "Applies function cumulatively."},
    {"id": 110, "category": "Functions", "difficulty": "Easy", "question": "Can functions be assigned?", "options": ["No", "Yes", "Only lambdas", "Only builtins"], "answer": 1, "explanation": "Functions are first-class objects."},
    
    # OOP (111-140)
    {"id": 111, "category": "OOP", "difficulty": "Easy", "question": "Define a class?", "options": ["class C {}", "class C():", "Class C:", "define class C:"], "answer": 1, "explanation": "class Name(): or class Name:"},
    {"id": 112, "category": "OOP", "difficulty": "Easy", "question": "'self' is?", "options": ["Keyword", "Current instance", "Static var", "Class var"], "answer": 1, "explanation": "Reference to current instance."},
    {"id": 113, "category": "OOP", "difficulty": "Easy", "question": "__init__ is?", "options": ["Destructor", "Constructor", "Static method", "Class method"], "answer": 1, "explanation": "Constructor that initializes instances."},
    {"id": 114, "category": "OOP", "difficulty": "Medium", "question": "Inheritance is?", "options": ["Copying code", "Class inherits from another", "Variable sharing", "Overloading"], "answer": 1, "explanation": "Child inherits from parent."},
    {"id": 115, "category": "OOP", "difficulty": "Medium", "question": "Polymorphism is?", "options": ["Multiple constructors", "Same interface, different impl", "Variable types", "Error handling"], "answer": 1, "explanation": "Same method name, different behavior."},
    {"id": 116, "category": "OOP", "difficulty": "Medium", "question": "super() does?", "options": ["Creates superior", "Calls parent methods", "Makes static", "Deletes"], "answer": 1, "explanation": "Access to parent class."},
    {"id": 117, "category": "OOP", "difficulty": "Medium", "question": "Encapsulation is?", "options": ["Compression", "Bundling data and methods", "Inheritance", "Multiple classes"], "answer": 1, "explanation": "Hiding internals, bundling data+methods."},
    {"id": 118, "category": "OOP", "difficulty": "Medium", "question": "__str__ purpose?", "options": ["Validation", "Human-readable string", "Parsing", "Comparison"], "answer": 1, "explanation": "Readable string for print()."},
    {"id": 119, "category": "OOP", "difficulty": "Medium", "question": "@staticmethod is?", "options": ["Static variable", "Method without self", "Class method", "Constructor"], "answer": 1, "explanation": "Method without self or cls."},
    {"id": 120, "category": "OOP", "difficulty": "Medium", "question": "@classmethod is?", "options": ["Creates class", "Method receiving class", "Static method", "Instance method"], "answer": 1, "explanation": "Receives class as first arg (cls)."},
    {"id": 121, "category": "OOP", "difficulty": "Medium", "question": "Class vs instance attribute?", "options": ["Same", "Class=shared, instance=unique", "Instance=shared", "Class=methods only"], "answer": 1, "explanation": "Class shared, instance unique."},
    {"id": 122, "category": "OOP", "difficulty": "Medium", "question": "Make attribute private?", "options": ["private keyword", "_prefix", "__prefix", "Both B and C"], "answer": 3, "explanation": "_ internal, __ name mangling."},
    {"id": 123, "category": "OOP", "difficulty": "Medium", "question": "isinstance() checks?", "options": ["Variable name", "Object is instance of class", "Class name", "Method existence"], "answer": 1, "explanation": "Checks if object is instance."},
    {"id": 124, "category": "OOP", "difficulty": "Hard", "question": "MRO stands for?", "options": ["Method Return Order", "Method Resolution Order", "Multiple Reference Object", "Module Read Op"], "answer": 1, "explanation": "Method search order in inheritance."},
    {"id": 125, "category": "OOP", "difficulty": "Hard", "question": "__slots__ does?", "options": ["Time slots", "Limits attributes, saves memory", "Method slots", "Hierarchy"], "answer": 1, "explanation": "Fixed attributes, no __dict__."},
    {"id": 126, "category": "OOP", "difficulty": "Medium", "question": "Multiple inheritance?", "options": ["class C(A,B):", "class C extends A,B:", "class C(A)(B):", "class C[A,B]:"], "answer": 0, "explanation": "Comma-separated: class C(A, B):"},
    {"id": 127, "category": "OOP", "difficulty": "Hard", "question": "__new__ vs __init__?", "options": ["Same", "__new__ creates, __init__ initializes", "__init__ creates", "Deprecated"], "answer": 1, "explanation": "__new__ creates, __init__ sets up."},
    {"id": 128, "category": "OOP", "difficulty": "Easy", "question": "Create object from class?", "options": ["new MyClass()", "MyClass.create()", "MyClass()", "create MyClass()"], "answer": 2, "explanation": "Call class like function: MyClass()"},
    {"id": 129, "category": "OOP", "difficulty": "Medium", "question": "__getitem__ enables?", "options": ["Getting items", "obj[key] access", "Getting attrs", "Function calls"], "answer": 1, "explanation": "Enables bracket notation: obj[key]"},
    {"id": 130, "category": "OOP", "difficulty": "Medium", "question": "__eq__ enables?", "options": ["Assignment", "== comparison", "= operator", "Both"], "answer": 1, "explanation": "Defines == equality comparison."},
    {"id": 131, "category": "OOP", "difficulty": "Hard", "question": "Abstract class via?", "options": ["abstract keyword", "ABC and @abstractmethod", "Virtual keyword", "Interface keyword"], "answer": 1, "explanation": "Use ABC module and @abstractmethod."},
    {"id": 132, "category": "OOP", "difficulty": "Medium", "question": "__repr__ vs __str__?", "options": ["Same", "__repr__ for developers", "__str__ for developers", "Deprecated"], "answer": 1, "explanation": "__repr__ for debugging, __str__ for users."},
    {"id": 133, "category": "OOP", "difficulty": "Hard", "question": "Descriptor is?", "options": ["Docstring", "Object with __get__/__set__", "Type annotation", "Decorator"], "answer": 1, "explanation": "Customizes attribute access."},
    {"id": 134, "category": "OOP", "difficulty": "Hard", "question": "Metaclass is?", "options": ["Large class", "Class of classes", "Deprecated", "Method type"], "answer": 1, "explanation": "Defines how classes behave."},
    {"id": 135, "category": "OOP", "difficulty": "Medium", "question": "__call__ makes object?", "options": ["Printable", "Callable", "Iterable", "Comparable"], "answer": 1, "explanation": "Makes instance callable like function."},
    {"id": 136, "category": "OOP", "difficulty": "Medium", "question": "Composition vs Inheritance?", "options": ["Same", "has-a vs is-a", "Opposite", "Composition deprecated"], "answer": 1, "explanation": "Composition: has-a, Inheritance: is-a."},
    {"id": 137, "category": "OOP", "difficulty": "Medium", "question": "__iter__ enables?", "options": ["Iteration", "for loops", "Both", "Neither"], "answer": 2, "explanation": "Makes objects iterable."},
    {"id": 138, "category": "OOP", "difficulty": "Medium", "question": "__len__ enables?", "options": ["Length property", "len() function", "Both", "Neither"], "answer": 2, "explanation": "Lets len() work on object."},
    {"id": 139, "category": "OOP", "difficulty": "Medium", "question": "Property getter syntax?", "options": ["@get", "@property", "@getter", "@attr"], "answer": 1, "explanation": "@property decorator."},
    {"id": 140, "category": "OOP", "difficulty": "Medium", "question": "Property setter syntax?", "options": ["@set", "@setter", "@propname.setter", "Both B and C"], "answer": 2, "explanation": "@propname.setter decorator."},
    
    # Exceptions (141-160)
    {"id": 141, "category": "Exceptions", "difficulty": "Easy", "question": "Handle exceptions?", "options": ["try/catch", "try/except", "handle/error", "error/catch"], "answer": 1, "explanation": "Python uses try/except."},
    {"id": 142, "category": "Exceptions", "difficulty": "Easy", "question": "Raise exception?", "options": ["throw", "raise", "error", "exception"], "answer": 1, "explanation": "'raise' throws exceptions."},
    {"id": 143, "category": "Exceptions", "difficulty": "Easy", "question": "Division by zero raises?", "options": ["MathError", "ZeroDivisionError", "DivideError", "ArithmeticError"], "answer": 1, "explanation": "ZeroDivisionError for x/0."},
    {"id": 144, "category": "Exceptions", "difficulty": "Medium", "question": "finally block?", "options": ["Handles errors", "Always runs", "Only on error", "Ends program"], "answer": 1, "explanation": "Always runs for cleanup."},
    {"id": 145, "category": "Exceptions", "difficulty": "Medium", "question": "Multiple except blocks?", "options": ["No", "Yes", "Max two", "With finally only"], "answer": 1, "explanation": "Different handlers for different types."},
    {"id": 146, "category": "Exceptions", "difficulty": "Medium", "question": "Catch any exception?", "options": ["except:", "except Exception:", "except All:", "Both A and B"], "answer": 3, "explanation": "Both work for most exceptions."},
    {"id": 147, "category": "Exceptions", "difficulty": "Medium", "question": "Access exception object?", "options": ["except E:", "except E as e:", "except (e) E:", "catch E e:"], "answer": 1, "explanation": "'as e' binds to variable."},
    {"id": 148, "category": "Exceptions", "difficulty": "Medium", "question": "Custom exception?", "options": ["class E(Error):", "class E(Exception):", "exception E:", "def E():"], "answer": 1, "explanation": "Inherit from Exception."},
    {"id": 149, "category": "Exceptions", "difficulty": "Easy", "question": "ValueError for?", "options": ["Invalid name", "Wrong value for operation", "Missing value", "Too large"], "answer": 1, "explanation": "Right type, wrong value."},
    {"id": 150, "category": "Exceptions", "difficulty": "Easy", "question": "TypeError for?", "options": ["Wrong type", "Operation on wrong type", "Type not found", "Conversion failed"], "answer": 1, "explanation": "Operation on inappropriate type."},
    {"id": 151, "category": "Exceptions", "difficulty": "Easy", "question": "Invalid list index raises?", "options": ["KeyError", "IndexError", "ValueError", "ListError"], "answer": 1, "explanation": "IndexError for out of range."},
    {"id": 152, "category": "Exceptions", "difficulty": "Easy", "question": "Missing dict key raises?", "options": ["IndexError", "KeyError", "ValueError", "DictError"], "answer": 1, "explanation": "KeyError for missing key."},
    {"id": 153, "category": "Exceptions", "difficulty": "Medium", "question": "Re-raise exception?", "options": ["raise", "throw", "reraise", "raise Exception"], "answer": 0, "explanation": "Bare 'raise' re-raises current."},
    {"id": 154, "category": "Exceptions", "difficulty": "Medium", "question": "assert False?", "options": ["Nothing", "AssertionError", "False", "None"], "answer": 1, "explanation": "Raises AssertionError."},
    {"id": 155, "category": "Exceptions", "difficulty": "Easy", "question": "Undefined variable raises?", "options": ["ValueError", "NameError", "TypeError", "ReferenceError"], "answer": 1, "explanation": "NameError for undefined names."},
    {"id": 156, "category": "Exceptions", "difficulty": "Easy", "question": "Import error raises?", "options": ["ImportError", "ModuleError", "LoadError", "RequireError"], "answer": 0, "explanation": "ImportError when import fails."},
    {"id": 157, "category": "Exceptions", "difficulty": "Hard", "question": "Exception hierarchy root?", "options": ["Exception", "BaseException", "Error", "Throwable"], "answer": 1, "explanation": "BaseException is the root."},
    {"id": 158, "category": "Exceptions", "difficulty": "Medium", "question": "StopIteration is?", "options": ["Loop error", "Iterator exhausted signal", "Stop command", "Syntax error"], "answer": 1, "explanation": "Signals iterator has no more items."},
    {"id": 159, "category": "Exceptions", "difficulty": "Medium", "question": "try/except/else: else runs?", "options": ["On exception", "No exception", "Always", "Error"], "answer": 1, "explanation": "Runs if NO exception."},
    {"id": 160, "category": "Exceptions", "difficulty": "Medium", "question": "Handle multiple types?", "options": ["except E1, E2:", "except (E1, E2):", "except E1 and E2:", "except E1 | E2:"], "answer": 1, "explanation": "Use tuple: except (E1, E2):"},
    
    # Standard Library (161-180)
    {"id": 161, "category": "Std Library", "difficulty": "Easy", "question": "Math functions module?", "options": ["calc", "math", "numbers", "arithmetic"], "answer": 1, "explanation": "'math' has sqrt, sin, cos, pi."},
    {"id": 162, "category": "Std Library", "difficulty": "Easy", "question": "Date/time module?", "options": ["time", "datetime", "date", "Both A and B"], "answer": 3, "explanation": "Both 'time' and 'datetime' work."},
    {"id": 163, "category": "Std Library", "difficulty": "Easy", "question": "JSON module?", "options": ["json", "jason", "jsonlib", "data"], "answer": 0, "explanation": "'json' for encoding/decoding."},
    {"id": 164, "category": "Std Library", "difficulty": "Medium", "question": "os.path.join() does?", "options": ["Combines strings", "Creates cross-platform paths", "Joins lists", "Network connect"], "answer": 1, "explanation": "Creates OS-appropriate paths."},
    {"id": 165, "category": "Std Library", "difficulty": "Easy", "question": "Regex module?", "options": ["regex", "re", "regexp", "pattern"], "answer": 1, "explanation": "'re' for regular expressions."},
    {"id": 166, "category": "Std Library", "difficulty": "Easy", "question": "random.choice() does?", "options": ["Random number", "Pick random element", "Random list", "Shuffle"], "answer": 1, "explanation": "Picks one random element."},
    {"id": 167, "category": "Std Library", "difficulty": "Medium", "question": "CLI parsing module?", "options": ["cli", "args", "argparse", "cmdline"], "answer": 2, "explanation": "'argparse' for command-line args."},
    {"id": 168, "category": "Std Library", "difficulty": "Medium", "question": "collections.Counter does?", "options": ["Counts to n", "Counts occurrences", "Loop counter", "Function calls"], "answer": 1, "explanation": "Counts element occurrences."},
    {"id": 169, "category": "Std Library", "difficulty": "Medium", "question": "itertools for?", "options": ["Error iteration", "Iterator utilities", "List ops", "Loop optimization"], "answer": 1, "explanation": "Iterator building blocks."},
    {"id": 170, "category": "Std Library", "difficulty": "Medium", "question": "Modern path module?", "options": ["os.path", "pathlib", "filepath", "Both A and B"], "answer": 3, "explanation": "pathlib is modern, os.path functional."},
    {"id": 171, "category": "Std Library", "difficulty": "Medium", "question": "subprocess does?", "options": ["Parallel", "Runs external commands", "Threads", "Async"], "answer": 1, "explanation": "Runs external programs."},
    {"id": 172, "category": "Std Library", "difficulty": "Medium", "question": "pickle does?", "options": ["Vegetables", "Serializes objects", "Compresses", "Encrypts"], "answer": 1, "explanation": "Serializes Python objects."},
    {"id": 173, "category": "Std Library", "difficulty": "Medium", "question": "System parameters module?", "options": ["os", "sys", "system", "platform"], "answer": 1, "explanation": "'sys' for interpreter info."},
    {"id": 174, "category": "Std Library", "difficulty": "Medium", "question": "logging provides?", "options": ["Math logs", "Event logging", "User login", "Compression"], "answer": 1, "explanation": "Flexible event logging."},
    {"id": 175, "category": "Std Library", "difficulty": "Hard", "question": "threading vs multiprocessing?", "options": ["Same", "threading=shared memory", "multiprocessing=shared", "Both I/O"], "answer": 1, "explanation": "Threads share memory."},
    {"id": 176, "category": "Std Library", "difficulty": "Medium", "question": "hashlib provides?", "options": ["Hash tables", "Cryptographic hashes", "Password storage", "Dict ops"], "answer": 1, "explanation": "MD5, SHA and other hashes."},
    {"id": 177, "category": "Std Library", "difficulty": "Easy", "question": "unittest for?", "options": ["Unit conversion", "Testing framework", "Type checking", "Performance"], "answer": 1, "explanation": "Built-in testing framework."},
    {"id": 178, "category": "Std Library", "difficulty": "Medium", "question": "copy module provides?", "options": ["File copy", "Object copying", "String copy", "List only"], "answer": 1, "explanation": "copy() and deepcopy()."},
    {"id": 179, "category": "Std Library", "difficulty": "Hard", "question": "GIL is?", "options": ["Global Import Lock", "Global Interpreter Lock", "General Input Lock", "Instance Lock"], "answer": 1, "explanation": "Prevents parallel bytecode execution."},
    {"id": 180, "category": "Std Library", "difficulty": "Easy", "question": "csv module does?", "options": ["Compresses", "Reads/writes CSV", "Validates", "Converts to JSON"], "answer": 1, "explanation": "Handles CSV files."},
    
    # Third-Party & Advanced (181-200)
    {"id": 181, "category": "Third-Party", "difficulty": "Easy", "question": "NumPy for?", "options": ["Web dev", "Numerical arrays", "Databases", "GUIs"], "answer": 1, "explanation": "Fast n-dimensional arrays."},
    {"id": 182, "category": "Third-Party", "difficulty": "Easy", "question": "Pandas for?", "options": ["Animals", "Data analysis", "Games", "ML only"], "answer": 1, "explanation": "DataFrames for data analysis."},
    {"id": 183, "category": "Third-Party", "difficulty": "Easy", "question": "pip does?", "options": ["Interpreter", "Package installer", "Formatter", "Debugger"], "answer": 1, "explanation": "Installs packages from PyPI."},
    {"id": 184, "category": "Third-Party", "difficulty": "Easy", "question": "Flask is?", "options": ["Container", "Web microframework", "Testing", "Data format"], "answer": 1, "explanation": "Lightweight web framework."},
    {"id": 185, "category": "Third-Party", "difficulty": "Easy", "question": "Django is?", "options": ["Music player", "Full web framework", "Game engine", "Data science"], "answer": 1, "explanation": "Full-featured web framework."},
    {"id": 186, "category": "Third-Party", "difficulty": "Easy", "question": "requests for?", "options": ["Feature requests", "HTTP requests", "User requests", "File requests"], "answer": 1, "explanation": "Simple HTTP requests."},
    {"id": 187, "category": "Third-Party", "difficulty": "Easy", "question": "matplotlib for?", "options": ["Math calc", "Data visualization", "Matrix ops", "Maps"], "answer": 1, "explanation": "Charts and visualizations."},
    {"id": 188, "category": "Third-Party", "difficulty": "Medium", "question": "SQLAlchemy is?", "options": ["Chemistry", "SQL ORM", "Validation", "Async only"], "answer": 1, "explanation": "SQL toolkit and ORM."},
    {"id": 189, "category": "Third-Party", "difficulty": "Easy", "question": "pytest is?", "options": ["Testing framework", "Performance", "Type checker", "Linter"], "answer": 0, "explanation": "Powerful testing framework."},
    {"id": 190, "category": "Third-Party", "difficulty": "Medium", "question": "TensorFlow/PyTorch for?", "options": ["Web scraping", "Deep learning", "Database", "Sysadmin"], "answer": 1, "explanation": "Deep learning frameworks."},
    {"id": 191, "category": "Third-Party", "difficulty": "Medium", "question": "BeautifulSoup for?", "options": ["Cooking", "HTML parsing", "CSS framework", "ORM"], "answer": 1, "explanation": "HTML/XML parsing for scraping."},
    {"id": 192, "category": "Third-Party", "difficulty": "Medium", "question": "FastAPI is?", "options": ["Fast food", "Async web framework", "Speed test", "Docs only"], "answer": 1, "explanation": "Modern async API framework."},
    {"id": 193, "category": "Third-Party", "difficulty": "Easy", "question": "black does?", "options": ["Colors", "Code formatting", "Encryption", "Testing"], "answer": 1, "explanation": "Automatic code formatter."},
    {"id": 194, "category": "Third-Party", "difficulty": "Medium", "question": "mypy does?", "options": ["Personal Python", "Static type checking", "Testing", "Package mgmt"], "answer": 1, "explanation": "Static type checker."},
    {"id": 195, "category": "Third-Party", "difficulty": "Easy", "question": "Jupyter for?", "options": ["Planet", "Interactive notebooks", "Web server", "Database"], "answer": 1, "explanation": "Interactive code notebooks."},
    {"id": 196, "category": "Advanced", "difficulty": "Hard", "question": "async def creates?", "options": ["Thread", "Coroutine", "Process", "Generator"], "answer": 1, "explanation": "Creates a coroutine function."},
    {"id": 197, "category": "Advanced", "difficulty": "Hard", "question": "await does?", "options": ["Waits for input", "Pauses coroutine", "Creates thread", "Blocks forever"], "answer": 1, "explanation": "Pauses coroutine until result ready."},
    {"id": 198, "category": "Advanced", "difficulty": "Hard", "question": "Type union syntax 3.10+?", "options": ["int | str", "int or str", "Union[int, str]", "int, str"], "answer": 0, "explanation": "int | str for union types."},
    {"id": 199, "category": "Advanced", "difficulty": "Medium", "question": "dataclass decorator?", "options": ["Creates database", "Auto generates methods", "Creates class", "Validates data"], "answer": 1, "explanation": "Auto-generates __init__, __repr__, etc."},
    {"id": 200, "category": "Advanced", "difficulty": "Easy", "question": "Zen of Python command?", "options": ["python zen", "import this", "zen()", "python --zen"], "answer": 1, "explanation": "import this shows the Zen."},
]

# Category colors for UI
CATEGORY_COLORS = {
    "Core Syntax": "#3B82F6",      # Blue
    "Data Types": "#10B981",        # Green
    "Control Flow": "#F59E0B",      # Amber
    "Functions": "#8B5CF6",         # Purple
    "OOP": "#EC4899",               # Pink
    "Exceptions": "#EF4444",        # Red
    "Std Library": "#06B6D4",       # Cyan
    "Third-Party": "#6366F1",       # Indigo
    "Advanced": "#F97316",          # Orange
}

# Get all categories
def get_categories():
    return list(set(q["category"] for q in PRACTICE_QUESTIONS))

# Filter questions
def filter_questions(category=None, difficulty=None):
    questions = PRACTICE_QUESTIONS
    if category and category != "All":
        questions = [q for q in questions if q["category"] == category]
    if difficulty and difficulty != "All":
        questions = [q for q in questions if q["difficulty"] == difficulty]
    return questions

# Coding Exercises Data

CODING_EXERCISES = [
    {"id": 1, "title": "Hello World", "difficulty": "Easy", "category": "Basics",
     "description": "Print 'Hello, World!' to the console.",
     "starter_code": "# Print Hello, World!\n",
     "solution": "print('Hello, World!')",
     "hints": ["Use the print() function", "Strings need quotes"]},
    
    {"id": 2, "title": "Variable Swap", "difficulty": "Easy", "category": "Basics",
     "description": "Swap the values of two variables a and b without using a third variable.",
     "starter_code": "a = 5\nb = 10\n# Swap a and b\n\nprint(f'a = {a}, b = {b}')",
     "solution": "a = 5\nb = 10\na, b = b, a\nprint(f'a = {a}, b = {b}')",
     "hints": ["Python allows tuple unpacking", "a, b = b, a works!"]},
    
    {"id": 3, "title": "FizzBuzz", "difficulty": "Easy", "category": "Control Flow",
     "description": "Print numbers 1-20. For multiples of 3 print 'Fizz', for 5 print 'Buzz', for both print 'FizzBuzz'.",
     "starter_code": "# FizzBuzz from 1 to 20\nfor i in range(1, 21):\n    # Your code here\n    pass",
     "solution": "for i in range(1, 21):\n    if i % 3 == 0 and i % 5 == 0:\n        print('FizzBuzz')\n    elif i % 3 == 0:\n        print('Fizz')\n    elif i % 5 == 0:\n        print('Buzz')\n    else:\n        print(i)",
     "hints": ["Check divisible by both first", "Use modulo operator %"]},
    
    {"id": 4, "title": "List Sum", "difficulty": "Easy", "category": "Data Structures",
     "description": "Calculate the sum of all numbers in a list without using the built-in sum() function.",
     "starter_code": "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\n# Calculate total without sum()\ntotal = 0\n\nprint(f'Sum: {total}')",
     "solution": "numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\ntotal = 0\nfor num in numbers:\n    total += num\nprint(f'Sum: {total}')",
     "hints": ["Use a for loop", "Accumulate with +="]},
    
    {"id": 5, "title": "Palindrome Check", "difficulty": "Easy", "category": "Strings",
     "description": "Check if a given string is a palindrome (reads same forwards and backwards).",
     "starter_code": "def is_palindrome(text):\n    # Your code here\n    pass\n\n# Test\nprint(is_palindrome('radar'))  # True\nprint(is_palindrome('hello'))  # False",
     "solution": "def is_palindrome(text):\n    text = text.lower()\n    return text == text[::-1]\n\nprint(is_palindrome('radar'))\nprint(is_palindrome('hello'))",
     "hints": ["Reverse string with [::-1]", "Consider case sensitivity"]},
    
    {"id": 6, "title": "Factorial", "difficulty": "Easy", "category": "Functions",
     "description": "Write a function to calculate factorial of a number.",
     "starter_code": "def factorial(n):\n    # Your code here\n    pass\n\nprint(factorial(5))  # Should be 120",
     "solution": "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\n\nprint(factorial(5))",
     "hints": ["Use recursion or a loop", "Base case: 0! = 1! = 1"]},
    
    {"id": 7, "title": "Find Maximum", "difficulty": "Easy", "category": "Data Structures",
     "description": "Find the maximum value in a list without using max().",
     "starter_code": "def find_max(numbers):\n    # Your code here\n    pass\n\nprint(find_max([3, 1, 4, 1, 5, 9, 2, 6]))",
     "solution": "def find_max(numbers):\n    if not numbers:\n        return None\n    maximum = numbers[0]\n    for num in numbers:\n        if num > maximum:\n            maximum = num\n    return maximum\n\nprint(find_max([3, 1, 4, 1, 5, 9, 2, 6]))",
     "hints": ["Start with first element", "Compare each element"]},
    
    {"id": 8, "title": "Count Vowels", "difficulty": "Easy", "category": "Strings",
     "description": "Count the number of vowels in a string.",
     "starter_code": "def count_vowels(text):\n    # Your code here\n    pass\n\nprint(count_vowels('Hello World'))",
     "solution": "def count_vowels(text):\n    vowels = 'aeiouAEIOU'\n    return sum(1 for char in text if char in vowels)\n\nprint(count_vowels('Hello World'))",
     "hints": ["Define vowels string", "Loop through characters"]},
    
    {"id": 9, "title": "Fibonacci Sequence", "difficulty": "Medium", "category": "Functions",
     "description": "Generate first n Fibonacci numbers.",
     "starter_code": "def fibonacci(n):\n    # Return list of first n Fibonacci numbers\n    pass\n\nprint(fibonacci(10))",
     "solution": "def fibonacci(n):\n    if n <= 0:\n        return []\n    if n == 1:\n        return [0]\n    fib = [0, 1]\n    for i in range(2, n):\n        fib.append(fib[-1] + fib[-2])\n    return fib\n\nprint(fibonacci(10))",
     "hints": ["Start with [0, 1]", "Each number = sum of previous two"]},
    
    {"id": 10, "title": "Prime Check", "difficulty": "Medium", "category": "Functions",
     "description": "Check if a number is prime.",
     "starter_code": "def is_prime(n):\n    # Your code here\n    pass\n\nprint(is_prime(17))  # True\nprint(is_prime(4))   # False",
     "solution": "def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n\nprint(is_prime(17))\nprint(is_prime(4))",
     "hints": ["Check divisibility up to sqrt(n)", "2 is the smallest prime"]},
    
    {"id": 11, "title": "Reverse Words", "difficulty": "Medium", "category": "Strings",
     "description": "Reverse the order of words in a sentence.",
     "starter_code": "def reverse_words(sentence):\n    # Your code here\n    pass\n\nprint(reverse_words('Hello World Python'))",
     "solution": "def reverse_words(sentence):\n    words = sentence.split()\n    return ' '.join(words[::-1])\n\nprint(reverse_words('Hello World Python'))",
     "hints": ["Split into words", "Reverse the list, then join"]},
    
    {"id": 12, "title": "Remove Duplicates", "difficulty": "Medium", "category": "Data Structures",
     "description": "Remove duplicates from a list while preserving order.",
     "starter_code": "def remove_duplicates(lst):\n    # Your code here\n    pass\n\nprint(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))",
     "solution": "def remove_duplicates(lst):\n    seen = set()\n    result = []\n    for item in lst:\n        if item not in seen:\n            seen.add(item)\n            result.append(item)\n    return result\n\nprint(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))",
     "hints": ["Use a set to track seen items", "Preserve insertion order"]},
    
    {"id": 13, "title": "Two Sum", "difficulty": "Medium", "category": "Algorithms",
     "description": "Find two numbers in a list that add up to a target sum.",
     "starter_code": "def two_sum(nums, target):\n    # Return indices of two numbers that add to target\n    pass\n\nprint(two_sum([2, 7, 11, 15], 9))",
     "solution": "def two_sum(nums, target):\n    seen = {}\n    for i, num in enumerate(nums):\n        complement = target - num\n        if complement in seen:\n            return [seen[complement], i]\n        seen[num] = i\n    return None\n\nprint(two_sum([2, 7, 11, 15], 9))",
     "hints": ["Use a dictionary for O(n) solution", "Store complement as key"]},
    
    {"id": 14, "title": "Anagram Check", "difficulty": "Medium", "category": "Strings",
     "description": "Check if two strings are anagrams of each other.",
     "starter_code": "def is_anagram(s1, s2):\n    # Your code here\n    pass\n\nprint(is_anagram('listen', 'silent'))  # True\nprint(is_anagram('hello', 'world'))    # False",
     "solution": "def is_anagram(s1, s2):\n    return sorted(s1.lower()) == sorted(s2.lower())\n\nprint(is_anagram('listen', 'silent'))\nprint(is_anagram('hello', 'world'))",
     "hints": ["Anagrams have same characters", "Sort and compare"]},
    
    {"id": 15, "title": "Flatten List", "difficulty": "Medium", "category": "Data Structures",
     "description": "Flatten a nested list into a single list.",
     "starter_code": "def flatten(nested):\n    # Your code here\n    pass\n\nprint(flatten([[1, 2], [3, 4], [5, 6]]))",
     "solution": "def flatten(nested):\n    result = []\n    for item in nested:\n        if isinstance(item, list):\n            result.extend(flatten(item))\n        else:\n            result.append(item)\n    return result\n\nprint(flatten([[1, 2], [3, 4], [5, 6]]))",
     "hints": ["Use recursion for deep nesting", "Check if item is a list"]},
    
    {"id": 16, "title": "Binary Search", "difficulty": "Medium", "category": "Algorithms",
     "description": "Implement binary search on a sorted list.",
     "starter_code": "def binary_search(arr, target):\n    # Return index of target, or -1 if not found\n    pass\n\nprint(binary_search([1, 3, 5, 7, 9, 11], 7))",
     "solution": "def binary_search(arr, target):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if arr[mid] == target:\n            return mid\n        elif arr[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1\n\nprint(binary_search([1, 3, 5, 7, 9, 11], 7))",
     "hints": ["Divide and conquer", "Adjust left or right based on comparison"]},
    
    {"id": 17, "title": "Word Frequency", "difficulty": "Medium", "category": "Data Structures",
     "description": "Count the frequency of each word in a sentence.",
     "starter_code": "def word_frequency(text):\n    # Return dict of word counts\n    pass\n\nprint(word_frequency('the quick brown fox jumps over the lazy dog'))",
     "solution": "def word_frequency(text):\n    words = text.lower().split()\n    freq = {}\n    for word in words:\n        freq[word] = freq.get(word, 0) + 1\n    return freq\n\nprint(word_frequency('the quick brown fox jumps over the lazy dog'))",
     "hints": ["Use a dictionary", "dict.get() with default value"]},
    
    {"id": 18, "title": "Matrix Transpose", "difficulty": "Medium", "category": "Data Structures",
     "description": "Transpose a matrix (swap rows and columns).",
     "starter_code": "def transpose(matrix):\n    # Your code here\n    pass\n\nmatrix = [[1, 2, 3], [4, 5, 6]]\nprint(transpose(matrix))",
     "solution": "def transpose(matrix):\n    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]\n\nmatrix = [[1, 2, 3], [4, 5, 6]]\nprint(transpose(matrix))",
     "hints": ["Use nested list comprehension", "zip(*matrix) also works"]},
    
    {"id": 19, "title": "Merge Sorted Lists", "difficulty": "Medium", "category": "Algorithms",
     "description": "Merge two sorted lists into one sorted list.",
     "starter_code": "def merge_sorted(list1, list2):\n    # Your code here\n    pass\n\nprint(merge_sorted([1, 3, 5], [2, 4, 6]))",
     "solution": "def merge_sorted(list1, list2):\n    result = []\n    i = j = 0\n    while i < len(list1) and j < len(list2):\n        if list1[i] <= list2[j]:\n            result.append(list1[i])\n            i += 1\n        else:\n            result.append(list2[j])\n            j += 1\n    result.extend(list1[i:])\n    result.extend(list2[j:])\n    return result\n\nprint(merge_sorted([1, 3, 5], [2, 4, 6]))",
     "hints": ["Two pointer technique", "Don't forget remaining elements"]},
    
    {"id": 20, "title": "Valid Parentheses", "difficulty": "Medium", "category": "Algorithms",
     "description": "Check if a string of parentheses is valid (balanced).",
     "starter_code": "def is_valid(s):\n    # Your code here\n    pass\n\nprint(is_valid('()[]{}'))  # True\nprint(is_valid('([)]'))    # False",
     "solution": "def is_valid(s):\n    stack = []\n    pairs = {')': '(', ']': '[', '}': '{'}\n    for char in s:\n        if char in '([{':\n            stack.append(char)\n        elif char in ')]}':\n            if not stack or stack[-1] != pairs[char]:\n                return False\n            stack.pop()\n    return len(stack) == 0\n\nprint(is_valid('()[]{}'))\nprint(is_valid('([)]'))",
     "hints": ["Use a stack", "Match closing with last opening"]},
    
    {"id": 21, "title": "Class Creation", "difficulty": "Medium", "category": "OOP",
     "description": "Create a BankAccount class with deposit, withdraw, and balance methods.",
     "starter_code": "class BankAccount:\n    # Your code here\n    pass\n\n# Test\naccount = BankAccount(100)\naccount.deposit(50)\naccount.withdraw(30)\nprint(account.get_balance())",
     "solution": "class BankAccount:\n    def __init__(self, initial_balance=0):\n        self.balance = initial_balance\n    \n    def deposit(self, amount):\n        self.balance += amount\n    \n    def withdraw(self, amount):\n        if amount <= self.balance:\n            self.balance -= amount\n            return True\n        return False\n    \n    def get_balance(self):\n        return self.balance\n\naccount = BankAccount(100)\naccount.deposit(50)\naccount.withdraw(30)\nprint(account.get_balance())",
     "hints": ["Use __init__ for constructor", "Store balance as instance variable"]},
    
    {"id": 22, "title": "Decorator Creation", "difficulty": "Hard", "category": "Functions",
     "description": "Create a decorator that measures function execution time.",
     "starter_code": "import time\n\ndef timer(func):\n    # Your code here\n    pass\n\n@timer\ndef slow_function():\n    time.sleep(1)\n    return 'Done'\n\nslow_function()",
     "solution": "import time\n\ndef timer(func):\n    def wrapper(*args, **kwargs):\n        start = time.time()\n        result = func(*args, **kwargs)\n        end = time.time()\n        print(f'{func.__name__} took {end - start:.2f} seconds')\n        return result\n    return wrapper\n\n@timer\ndef slow_function():\n    time.sleep(1)\n    return 'Done'\n\nslow_function()",
     "hints": ["Return a wrapper function", "Use *args and **kwargs"]},
    
    {"id": 23, "title": "Generator Function", "difficulty": "Hard", "category": "Functions",
     "description": "Create a generator that yields prime numbers indefinitely.",
     "starter_code": "def prime_generator():\n    # Your code here\n    pass\n\n# Get first 10 primes\ngen = prime_generator()\nfor _ in range(10):\n    print(next(gen))",
     "solution": "def prime_generator():\n    def is_prime(n):\n        if n < 2:\n            return False\n        for i in range(2, int(n**0.5) + 1):\n            if n % i == 0:\n                return False\n        return True\n    \n    num = 2\n    while True:\n        if is_prime(num):\n            yield num\n        num += 1\n\ngen = prime_generator()\nfor _ in range(10):\n    print(next(gen))",
     "hints": ["Use yield in an infinite loop", "Include is_prime helper"]},
    
    {"id": 24, "title": "Context Manager", "difficulty": "Hard", "category": "OOP",
     "description": "Create a context manager for file handling with automatic cleanup.",
     "starter_code": "class FileManager:\n    # Your code here\n    pass\n\n# Usage:\n# with FileManager('test.txt', 'w') as f:\n#     f.write('Hello')",
     "solution": "class FileManager:\n    def __init__(self, filename, mode):\n        self.filename = filename\n        self.mode = mode\n        self.file = None\n    \n    def __enter__(self):\n        self.file = open(self.filename, self.mode)\n        return self.file\n    \n    def __exit__(self, exc_type, exc_val, exc_tb):\n        if self.file:\n            self.file.close()\n        return False\n\n# with FileManager('test.txt', 'w') as f:\n#     f.write('Hello')",
     "hints": ["Implement __enter__ and __exit__", "__enter__ returns the resource"]},
    
    {"id": 25, "title": "LRU Cache", "difficulty": "Hard", "category": "Data Structures",
     "description": "Implement a Least Recently Used (LRU) cache.",
     "starter_code": "class LRUCache:\n    def __init__(self, capacity):\n        # Your code here\n        pass\n    \n    def get(self, key):\n        pass\n    \n    def put(self, key, value):\n        pass",
     "solution": "from collections import OrderedDict\n\nclass LRUCache:\n    def __init__(self, capacity):\n        self.capacity = capacity\n        self.cache = OrderedDict()\n    \n    def get(self, key):\n        if key not in self.cache:\n            return -1\n        self.cache.move_to_end(key)\n        return self.cache[key]\n    \n    def put(self, key, value):\n        if key in self.cache:\n            self.cache.move_to_end(key)\n        self.cache[key] = value\n        if len(self.cache) > self.capacity:\n            self.cache.popitem(last=False)",
     "hints": ["Use OrderedDict", "move_to_end() for access tracking"]},
]

# Get exercise categories
def get_exercise_categories():
    return list(set(ex["category"] for ex in CODING_EXERCISES))

# Filter exercises
def filter_exercises(category=None, difficulty=None):
    exercises = CODING_EXERCISES
    if category and category != "All":
        exercises = [ex for ex in exercises if ex["category"] == category]
    if difficulty and difficulty != "All":
        exercises = [ex for ex in exercises if ex["difficulty"] == difficulty]
    return exercises

# Library and Resources Data

PYTHON_LIBRARIES = [
    # Data Science & Analysis
    {"name": "NumPy", "category": "Data Science", "description": "Fundamental package for numerical computing with powerful N-dimensional array objects.",
     "install": "pip install numpy", "docs": "https://numpy.org/doc/", "icon": "📊",
     "example": "import numpy as np\narr = np.array([1, 2, 3, 4, 5])\nprint(arr.mean())  # 3.0"},
    
    {"name": "Pandas", "category": "Data Science", "description": "Data manipulation and analysis library with DataFrame structures.",
     "install": "pip install pandas", "docs": "https://pandas.pydata.org/docs/", "icon": "🐼",
     "example": "import pandas as pd\ndf = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})\nprint(df)"},
    
    {"name": "Matplotlib", "category": "Data Science", "description": "Comprehensive library for creating static, animated, and interactive visualizations.",
     "install": "pip install matplotlib", "docs": "https://matplotlib.org/stable/", "icon": "📈",
     "example": "import matplotlib.pyplot as plt\nplt.plot([1, 2, 3, 4])\nplt.show()"},
    
    {"name": "Seaborn", "category": "Data Science", "description": "Statistical data visualization based on matplotlib with beautiful default styles.",
     "install": "pip install seaborn", "docs": "https://seaborn.pydata.org/", "icon": "🎨",
     "example": "import seaborn as sns\nsns.set_theme()\ntips = sns.load_dataset('tips')"},
    
    {"name": "Plotly", "category": "Data Science", "description": "Interactive graphing library for creating publication-quality graphs.",
     "install": "pip install plotly", "docs": "https://plotly.com/python/", "icon": "📉",
     "example": "import plotly.express as px\nfig = px.scatter(x=[1,2,3], y=[1,2,3])"},
    
    {"name": "SciPy", "category": "Data Science", "description": "Scientific computing library with modules for optimization, integration, and statistics.",
     "install": "pip install scipy", "docs": "https://scipy.org/", "icon": "🔬",
     "example": "from scipy import stats\nstats.norm.pdf(0)  # Normal distribution"},
    
    # Machine Learning
    {"name": "Scikit-learn", "category": "Machine Learning", "description": "Simple and efficient tools for predictive data analysis and machine learning.",
     "install": "pip install scikit-learn", "docs": "https://scikit-learn.org/stable/", "icon": "🤖",
     "example": "from sklearn.ensemble import RandomForestClassifier\nclf = RandomForestClassifier()"},
    
    {"name": "TensorFlow", "category": "Machine Learning", "description": "End-to-end open source platform for machine learning and deep learning.",
     "install": "pip install tensorflow", "docs": "https://www.tensorflow.org/", "icon": "🧠",
     "example": "import tensorflow as tf\nmodel = tf.keras.Sequential()"},
    
    {"name": "PyTorch", "category": "Machine Learning", "description": "Deep learning framework with strong GPU acceleration and dynamic computation graphs.",
     "install": "pip install torch", "docs": "https://pytorch.org/docs/", "icon": "🔥",
     "example": "import torch\nx = torch.tensor([1.0, 2.0, 3.0])"},
    
    {"name": "XGBoost", "category": "Machine Learning", "description": "Optimized distributed gradient boosting library for high performance.",
     "install": "pip install xgboost", "docs": "https://xgboost.readthedocs.io/", "icon": "⚡",
     "example": "import xgboost as xgb\nmodel = xgb.XGBClassifier()"},
    
    {"name": "Keras", "category": "Machine Learning", "description": "High-level neural networks API, now integrated with TensorFlow.",
     "install": "pip install keras", "docs": "https://keras.io/", "icon": "🔮",
     "example": "from keras.models import Sequential\nmodel = Sequential()"},
    
    # Web Development
    {"name": "Django", "category": "Web Development", "description": "High-level Python web framework for rapid development with clean, pragmatic design.",
     "install": "pip install django", "docs": "https://docs.djangoproject.com/", "icon": "🎸",
     "example": "django-admin startproject mysite"},
    
    {"name": "Flask", "category": "Web Development", "description": "Lightweight WSGI web application framework, simple and extensible.",
     "install": "pip install flask", "docs": "https://flask.palletsprojects.com/", "icon": "🧪",
     "example": "from flask import Flask\napp = Flask(__name__)"},
    
    {"name": "FastAPI", "category": "Web Development", "description": "Modern, fast web framework for building APIs with automatic OpenAPI documentation.",
     "install": "pip install fastapi", "docs": "https://fastapi.tiangolo.com/", "icon": "⚡",
     "example": "from fastapi import FastAPI\napp = FastAPI()"},
    
    {"name": "Streamlit", "category": "Web Development", "description": "Framework for creating beautiful data apps in pure Python.",
     "install": "pip install streamlit", "docs": "https://docs.streamlit.io/", "icon": "🎈",
     "example": "import streamlit as st\nst.title('Hello World')"},
    
    {"name": "Requests", "category": "Web Development", "description": "Elegant and simple HTTP library for Python.",
     "install": "pip install requests", "docs": "https://requests.readthedocs.io/", "icon": "🌐",
     "example": "import requests\nr = requests.get('https://api.github.com')"},
    
    # Database
    {"name": "SQLAlchemy", "category": "Database", "description": "SQL toolkit and Object-Relational Mapping (ORM) library.",
     "install": "pip install sqlalchemy", "docs": "https://docs.sqlalchemy.org/", "icon": "🗄️",
     "example": "from sqlalchemy import create_engine\nengine = create_engine('sqlite:///:memory:')"},
    
    {"name": "PyMongo", "category": "Database", "description": "Python driver for MongoDB NoSQL database.",
     "install": "pip install pymongo", "docs": "https://pymongo.readthedocs.io/", "icon": "🍃",
     "example": "from pymongo import MongoClient\nclient = MongoClient()"},
    
    {"name": "Redis-py", "category": "Database", "description": "Python client for Redis in-memory data store.",
     "install": "pip install redis", "docs": "https://redis-py.readthedocs.io/", "icon": "🔴",
     "example": "import redis\nr = redis.Redis(host='localhost')"},
    
    # Testing & Quality
    {"name": "Pytest", "category": "Testing", "description": "Full-featured testing framework with simple syntax.",
     "install": "pip install pytest", "docs": "https://docs.pytest.org/", "icon": "✅",
     "example": "def test_example():\n    assert 1 + 1 == 2"},
    
    {"name": "Black", "category": "Testing", "description": "Uncompromising Python code formatter.",
     "install": "pip install black", "docs": "https://black.readthedocs.io/", "icon": "⬛",
     "example": "black myfile.py"},
    
    {"name": "Mypy", "category": "Testing", "description": "Optional static type checker for Python.",
     "install": "pip install mypy", "docs": "https://mypy.readthedocs.io/", "icon": "🔍",
     "example": "mypy myfile.py"},
    
    {"name": "Pylint", "category": "Testing", "description": "Code analysis tool that checks for errors and enforces coding standards.",
     "install": "pip install pylint", "docs": "https://pylint.readthedocs.io/", "icon": "🔧",
     "example": "pylint myfile.py"},
    
    # Automation & Scraping
    {"name": "Selenium", "category": "Automation", "description": "Browser automation tool for web testing and scraping.",
     "install": "pip install selenium", "docs": "https://selenium-python.readthedocs.io/", "icon": "🌍",
     "example": "from selenium import webdriver\ndriver = webdriver.Chrome()"},
    
    {"name": "BeautifulSoup", "category": "Automation", "description": "Library for parsing HTML and XML documents.",
     "install": "pip install beautifulsoup4", "docs": "https://beautiful-soup-4.readthedocs.io/", "icon": "🍜",
     "example": "from bs4 import BeautifulSoup\nsoup = BeautifulSoup(html, 'html.parser')"},
    
    {"name": "Scrapy", "category": "Automation", "description": "Fast high-level web crawling and scraping framework.",
     "install": "pip install scrapy", "docs": "https://docs.scrapy.org/", "icon": "🕷️",
     "example": "scrapy startproject myspider"},
    
    # Utilities
    {"name": "Click", "category": "Utilities", "description": "Package for creating beautiful command line interfaces.",
     "install": "pip install click", "docs": "https://click.palletsprojects.com/", "icon": "👆",
     "example": "@click.command()\ndef hello():\n    click.echo('Hello!')"},
    
    {"name": "Rich", "category": "Utilities", "description": "Library for rich text and beautiful formatting in the terminal.",
     "install": "pip install rich", "docs": "https://rich.readthedocs.io/", "icon": "✨",
     "example": "from rich import print\nprint('[bold red]Hello[/]')"},
    
    {"name": "Pydantic", "category": "Utilities", "description": "Data validation using Python type annotations.",
     "install": "pip install pydantic", "docs": "https://docs.pydantic.dev/", "icon": "📋",
     "example": "from pydantic import BaseModel\nclass User(BaseModel):\n    name: str"},
    
    {"name": "Loguru", "category": "Utilities", "description": "Simplified logging with no boilerplate.",
     "install": "pip install loguru", "docs": "https://loguru.readthedocs.io/", "icon": "📝",
     "example": "from loguru import logger\nlogger.info('Hello!')"},
]

LEARNING_RESOURCES = [
    # Official Documentation
    {"name": "Python Official Docs", "category": "Documentation", "type": "Docs",
     "url": "https://docs.python.org/3/", "icon": "📖",
     "description": "The official Python documentation - comprehensive and authoritative."},
    
    {"name": "Python Tutorial", "category": "Documentation", "type": "Tutorial",
     "url": "https://docs.python.org/3/tutorial/", "icon": "📚",
     "description": "Official Python tutorial for beginners."},
    
    {"name": "PEP 8 Style Guide", "category": "Documentation", "type": "Guide",
     "url": "https://peps.python.org/pep-0008/", "icon": "📏",
     "description": "The official Python style guide for writing clean code."},
    
    # Online Courses
    {"name": "Codecademy Python", "category": "Courses", "type": "Interactive",
     "url": "https://www.codecademy.com/learn/learn-python-3", "icon": "🎓",
     "description": "Interactive Python course with hands-on exercises."},
    
    {"name": "Real Python", "category": "Courses", "type": "Tutorials",
     "url": "https://realpython.com/", "icon": "🐍",
     "description": "High-quality Python tutorials and articles."},
    
    {"name": "Python.org Beginners", "category": "Courses", "type": "Guide",
     "url": "https://www.python.org/about/gettingstarted/", "icon": "🚀",
     "description": "Official getting started guide for beginners."},
    
    {"name": "Coursera Python", "category": "Courses", "type": "Course",
     "url": "https://www.coursera.org/specializations/python", "icon": "🎯",
     "description": "University-level Python courses on Coursera."},
    
    {"name": "freeCodeCamp Python", "category": "Courses", "type": "Video",
     "url": "https://www.freecodecamp.org/learn/scientific-computing-with-python/", "icon": "📹",
     "description": "Free Python certification course."},
    
    # Practice Platforms
    {"name": "LeetCode", "category": "Practice", "type": "Challenges",
     "url": "https://leetcode.com/", "icon": "💻",
     "description": "Coding challenges for interview preparation."},
    
    {"name": "HackerRank Python", "category": "Practice", "type": "Challenges",
     "url": "https://www.hackerrank.com/domains/python", "icon": "🏆",
     "description": "Python skill certification and practice."},
    
    {"name": "Codewars", "category": "Practice", "type": "Kata",
     "url": "https://www.codewars.com/", "icon": "⚔️",
     "description": "Martial arts-themed coding challenges."},
    
    {"name": "Exercism Python", "category": "Practice", "type": "Exercises",
     "url": "https://exercism.org/tracks/python", "icon": "🏃",
     "description": "Free code practice with mentorship."},
    
    {"name": "Project Euler", "category": "Practice", "type": "Math",
     "url": "https://projecteuler.net/", "icon": "🔢",
     "description": "Mathematical/computational problems."},
    
    # Books
    {"name": "Automate the Boring Stuff", "category": "Books", "type": "Free Book",
     "url": "https://automatetheboringstuff.com/", "icon": "📕",
     "description": "Practical programming for total beginners."},
    
    {"name": "Think Python", "category": "Books", "type": "Free Book",
     "url": "https://greenteapress.com/wp/think-python-2e/", "icon": "📗",
     "description": "How to Think Like a Computer Scientist."},
    
    {"name": "Python Crash Course", "category": "Books", "type": "Book",
     "url": "https://nostarch.com/pythoncrashcourse2e", "icon": "📘",
     "description": "Hands-on, project-based introduction."},
    
    {"name": "Fluent Python", "category": "Books", "type": "Book",
     "url": "https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/", "icon": "📙",
     "description": "Advanced Python programming techniques."},
    
    # Community
    {"name": "r/learnpython", "category": "Community", "type": "Forum",
     "url": "https://www.reddit.com/r/learnpython/", "icon": "👥",
     "description": "Subreddit for Python learners."},
    
    {"name": "Stack Overflow Python", "category": "Community", "type": "Q&A",
     "url": "https://stackoverflow.com/questions/tagged/python", "icon": "💬",
     "description": "Q&A for Python programming."},
    
    {"name": "Python Discord", "category": "Community", "type": "Chat",
     "url": "https://discord.gg/python", "icon": "💭",
     "description": "Active Python community on Discord."},
    
    # Tools
    {"name": "PyPI", "category": "Tools", "type": "Package Index",
     "url": "https://pypi.org/", "icon": "📦",
     "description": "Python Package Index - find and install packages."},
    
    {"name": "Replit", "category": "Tools", "type": "Online IDE",
     "url": "https://replit.com/", "icon": "💻",
     "description": "Online Python development environment."},
    
    {"name": "Google Colab", "category": "Tools", "type": "Notebooks",
     "url": "https://colab.research.google.com/", "icon": "📓",
     "description": "Free Jupyter notebooks with GPU support."},
    
    {"name": "Python Tutor", "category": "Tools", "type": "Visualizer",
     "url": "https://pythontutor.com/", "icon": "👁️",
     "description": "Visualize Python code execution step by step."},
]

CHEAT_SHEETS = [
    {"title": "Python Basics", "category": "Syntax", "content": """
# Variables
x = 5                   # Integer
y = 3.14                # Float
name = "Python"         # String
is_valid = True         # Boolean

# Type conversion
int("5")                # String to int
str(5)                  # Int to string
float("3.14")           # String to float

# String operations
len("hello")            # Length: 5
"hello".upper()         # "HELLO"
"hello".split("l")      # ["he", "", "o"]
f"Hello {name}"         # f-string formatting
"""},
    
    {"title": "Data Structures", "category": "Collections", "content": """
# Lists
lst = [1, 2, 3]
lst.append(4)           # Add to end
lst.insert(0, 0)        # Insert at index
lst.pop()               # Remove last
lst[1:3]                # Slice [2, 3]

# Dictionaries
d = {"key": "value"}
d["new"] = "item"       # Add/update
d.get("key", default)   # Safe access
d.keys(), d.values()    # Views

# Sets
s = {1, 2, 3}
s.add(4)                # Add item
s1 & s2                 # Intersection
s1 | s2                 # Union

# Tuples
t = (1, 2, 3)           # Immutable
a, b, c = t             # Unpacking
"""},
    
    {"title": "Control Flow", "category": "Logic", "content": """
# If statements
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")

# Loops
for i in range(5):      # 0 to 4
    print(i)

for item in lst:        # Iterate list
    print(item)

while x > 0:            # While loop
    x -= 1

# Comprehensions
[x**2 for x in range(5)]           # List
{x: x**2 for x in range(5)}        # Dict
{x for x in range(5)}              # Set
"""},
    
    {"title": "Functions", "category": "Functions", "content": """
# Basic function
def greet(name):
    return f"Hello, {name}"

# Default arguments
def greet(name="World"):
    return f"Hello, {name}"

# *args and **kwargs
def func(*args, **kwargs):
    print(args)         # Tuple
    print(kwargs)       # Dict

# Lambda
square = lambda x: x**2

# Decorators
def decorator(func):
    def wrapper(*args):
        return func(*args)
    return wrapper

@decorator
def my_func():
    pass
"""},
    
    {"title": "Classes", "category": "OOP", "content": """
class Dog:
    species = "Canine"      # Class attribute
    
    def __init__(self, name):
        self.name = name    # Instance attribute
    
    def bark(self):
        return "Woof!"
    
    @classmethod
    def get_species(cls):
        return cls.species
    
    @staticmethod
    def info():
        return "Dogs are pets"

# Inheritance
class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
"""},
    
    {"title": "File Operations", "category": "I/O", "content": """
# Reading files
with open("file.txt", "r") as f:
    content = f.read()          # Entire file
    lines = f.readlines()       # List of lines

# Writing files
with open("file.txt", "w") as f:
    f.write("Hello World")

# Appending
with open("file.txt", "a") as f:
    f.write("New line")

# JSON
import json
data = json.loads(json_string)  # Parse
json.dumps(data)                # Stringify

# CSV
import csv
with open("data.csv") as f:
    reader = csv.reader(f)
"""},
    
    {"title": "Error Handling", "category": "Exceptions", "content": """
# Try/Except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print(f"Error: {e}")
else:
    print("Success")
finally:
    print("Always runs")

# Raise exceptions
raise ValueError("Invalid value")

# Custom exceptions
class MyError(Exception):
    pass

# Assert
assert x > 0, "x must be positive"
"""},
    
    {"title": "Common Imports", "category": "Modules", "content": """
# Standard library
import os                   # OS operations
import sys                  # System
import json                 # JSON handling
import datetime             # Date/time
import random               # Random numbers
import math                 # Math functions
import re                   # Regex
import collections          # Data structures
import itertools            # Iterators
from pathlib import Path    # Modern paths

# Specific imports
from typing import List, Dict, Optional
from dataclasses import dataclass
from functools import lru_cache
from contextlib import contextmanager
"""},
]

def get_library_categories():
    return list(set(lib["category"] for lib in PYTHON_LIBRARIES))

def get_resource_categories():
    return list(set(res["category"] for res in LEARNING_RESOURCES))

def filter_libraries(category=None):
    if category and category != "All":
        return [lib for lib in PYTHON_LIBRARIES if lib["category"] == category]
    return PYTHON_LIBRARIES

def filter_resources(category=None):
    if category and category != "All":
        return [res for res in LEARNING_RESOURCES if res["category"] == category]
    return LEARNING_RESOURCES

# Page config
st.set_page_config(
    page_title="Python Mastery Hub",
    page_icon="🐍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS - PyGWalker-inspired dark theme
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #0F172A 100%);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1E293B 0%, #0F172A 100%);
        border-right: 1px solid #334155;
    }
    
    /* Cards */
    .css-1r6slb0, .css-12oz5g7 {
        background-color: #1E293B;
        border: 1px solid #334155;
        border-radius: 12px;
    }
    
    /* Custom card styling */
    .custom-card {
        background: linear-gradient(145deg, #1E293B, #0F172A);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 0.5rem 0;
        transition: all 0.3s ease;
    }
    
    .custom-card:hover {
        border-color: #8B5CF6;
        box-shadow: 0 0 20px rgba(139, 92, 246, 0.2);
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #E2E8F0 !important;
    }
    
    .gradient-text {
        background: linear-gradient(90deg, #8B5CF6, #EC4899);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #8B5CF6, #7C3AED);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #7C3AED, #6D28D9);
        box-shadow: 0 0 15px rgba(139, 92, 246, 0.4);
    }
    
    /* Answer buttons */
    .answer-btn {
        background: #1E293B;
        border: 1px solid #475569;
        border-radius: 8px;
        padding: 1rem;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.2s ease;
        width: 100%;
        text-align: left;
    }
    
    .answer-btn:hover {
        border-color: #8B5CF6;
        background: #334155;
    }
    
    .answer-correct {
        background: rgba(34, 197, 94, 0.2) !important;
        border-color: #22C55E !important;
    }
    
    .answer-wrong {
        background: rgba(239, 68, 68, 0.2) !important;
        border-color: #EF4444 !important;
    }
    
    /* Code blocks */
    .stCodeBlock {
        background-color: #0F172A !important;
        border: 1px solid #334155;
        border-radius: 8px;
    }
    
    /* Progress bar */
    .stProgress > div > div {
        background: linear-gradient(90deg, #8B5CF6, #EC4899);
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        color: #8B5CF6 !important;
    }
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #1E293B;
        border-radius: 12px;
        padding: 0.5rem;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        border-radius: 8px;
        color: #94A3B8;
        padding: 0.5rem 1rem;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #8B5CF6, #7C3AED) !important;
        color: white !important;
    }
    
    /* Expander */
    .streamlit-expanderHeader {
        background-color: #1E293B;
        border-radius: 8px;
    }
    
    /* Select boxes */
    .stSelectbox > div > div {
        background-color: #1E293B;
        border-color: #475569;
    }
    
    /* Text input */
    .stTextInput > div > div > input {
        background-color: #1E293B;
        border-color: #475569;
        color: #E2E8F0;
    }
    
    /* Text area */
    .stTextArea > div > div > textarea {
        background-color: #0F172A;
        border-color: #475569;
        color: #22C55E;
        font-family: 'Fira Code', monospace;
    }
    
    /* Category badges */
    .category-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 0.5rem;
    }
    
    /* Difficulty badges */
    .diff-easy { background: rgba(34, 197, 94, 0.2); color: #22C55E; }
    .diff-medium { background: rgba(234, 179, 8, 0.2); color: #EAB308; }
    .diff-hard { background: rgba(239, 68, 68, 0.2); color: #EF4444; }
    
    /* Library cards */
    .lib-card {
        background: linear-gradient(145deg, #1E293B, #0F172A);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1rem;
        height: 100%;
        transition: all 0.3s ease;
    }
    
    .lib-card:hover {
        border-color: #8B5CF6;
        transform: translateY(-2px);
    }
    
    /* Score display */
    .score-display {
        background: linear-gradient(145deg, #1E293B, #0F172A);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
    }
    
    /* Chat messages */
    .user-message {
        background: rgba(59, 130, 246, 0.2);
        border-left: 3px solid #3B82F6;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 0.5rem 0;
    }
    
    .ai-message {
        background: rgba(139, 92, 246, 0.2);
        border-left: 3px solid #8B5CF6;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 0.5rem 0;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Animations */
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.5; }
    }
    
    .loading {
        animation: pulse 1.5s infinite;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = {'correct': 0, 'wrong': 0}
if 'answered' not in st.session_state:
    st.session_state.answered = False
if 'selected_answer' not in st.session_state:
    st.session_state.selected_answer = None
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""
if 'current_exercise' not in st.session_state:
    st.session_state.current_exercise = 0
if 'show_solution' not in st.session_state:
    st.session_state.show_solution = False
if 'generated_content' not in st.session_state:
    st.session_state.generated_content = None

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 1rem;">
        <h1 style="font-size: 2rem;">🐍</h1>
        <h2 class="gradient-text" style="font-size: 1.5rem; margin: 0;">Python Mastery Hub</h2>
        <p style="color: #64748B; font-size: 0.875rem;">Interactive Learning Platform</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Navigation
    page = st.radio(
        "Navigate",
        ["📝 Practice Quiz", "💻 Coding Exercises", "🤖 AI Assistant", "✨ AI Create", 
         "📚 Library", "🔗 Resources", "📋 Cheat Sheets"],
        label_visibility="collapsed"
    )
    
    st.divider()
    
    # Score display
    st.markdown("""
    <div class="score-display">
        <h4 style="margin: 0; color: #94A3B8;">Your Score</h4>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("✓ Correct", st.session_state.score['correct'])
    with col2:
        st.metric("✗ Wrong", st.session_state.score['wrong'])
    
    st.divider()
    
    # API Key input
    with st.expander("🔑 API Settings"):
        api_key = st.text_input("Anthropic API Key", type="password", value=st.session_state.api_key)
        if api_key:
            st.session_state.api_key = api_key
            st.success("API Key saved!")

# Main content
def render_practice_quiz():
    """Render the practice quiz section"""
    st.markdown('<h1 class="gradient-text">📝 Practice Quiz</h1>', unsafe_allow_html=True)
    st.markdown("Test your Python knowledge with 200 questions!")
    
    # Filters
    col1, col2, col3 = st.columns([2, 2, 2])
    with col1:
        category = st.selectbox("Category", ["All"] + get_categories())
    with col2:
        difficulty = st.selectbox("Difficulty", ["All", "Easy", "Medium", "Hard"])
    with col3:
        if st.button("🔀 Random Question"):
            questions = filter_questions(category, difficulty)
            if questions:
                st.session_state.current_question = random.randint(0, len(questions) - 1)
                st.session_state.answered = False
                st.session_state.selected_answer = None
                st.rerun()
    
    # Get filtered questions
    questions = filter_questions(category, difficulty)
    if not questions:
        st.warning("No questions match your filters.")
        return
    
    # Progress bar
    progress = (st.session_state.current_question + 1) / len(questions)
    st.progress(progress)
    st.caption(f"Question {st.session_state.current_question + 1} of {len(questions)}")
    
    # Current question
    q = questions[st.session_state.current_question % len(questions)]
    
    # Question card
    st.markdown(f"""
    <div class="custom-card">
        <div style="margin-bottom: 1rem;">
            <span class="category-badge" style="background: {CATEGORY_COLORS.get(q['category'], '#8B5CF6')}20; color: {CATEGORY_COLORS.get(q['category'], '#8B5CF6')};">
                {q['category']}
            </span>
            <span class="category-badge diff-{q['difficulty'].lower()}">{q['difficulty']}</span>
        </div>
        <h3 style="color: #E2E8F0; margin: 0;">Q{q['id']}: {q['question']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Answer options
    for i, option in enumerate(q['options']):
        # Determine button state
        if st.session_state.answered:
            if i == q['answer']:
                btn_type = "primary"  # Correct answer
            elif i == st.session_state.selected_answer:
                btn_type = "secondary"  # Wrong selection
            else:
                btn_type = "secondary"
        else:
            btn_type = "secondary"
        
        # Create button with label
        label = f"{'ABCD'[i]}. {option}"
        if st.session_state.answered:
            if i == q['answer']:
                label = f"✓ {label}"
            elif i == st.session_state.selected_answer and i != q['answer']:
                label = f"✗ {label}"
        
        if st.button(label, key=f"opt_{i}", use_container_width=True, disabled=st.session_state.answered):
            st.session_state.selected_answer = i
            st.session_state.answered = True
            if i == q['answer']:
                st.session_state.score['correct'] += 1
            else:
                st.session_state.score['wrong'] += 1
            st.rerun()
    
    # Show explanation after answering
    if st.session_state.answered:
        if st.session_state.selected_answer == q['answer']:
            st.success(f"✓ Correct! {q['explanation']}")
        else:
            st.error(f"✗ Incorrect. The correct answer is: {q['options'][q['answer']]}")
            st.info(f"💡 {q['explanation']}")
    
    # Navigation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.button("← Previous", use_container_width=True):
            st.session_state.current_question = max(0, st.session_state.current_question - 1)
            st.session_state.answered = False
            st.session_state.selected_answer = None
            st.rerun()
    with col3:
        if st.button("Next →", use_container_width=True):
            st.session_state.current_question = min(len(questions) - 1, st.session_state.current_question + 1)
            st.session_state.answered = False
            st.session_state.selected_answer = None
            st.rerun()

def render_coding_exercises():
    """Render the coding exercises section"""
    st.markdown('<h1 class="gradient-text">💻 Coding Exercises</h1>', unsafe_allow_html=True)
    st.markdown("Practice Python with hands-on coding challenges!")
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        category = st.selectbox("Category", ["All"] + get_exercise_categories(), key="ex_cat")
    with col2:
        difficulty = st.selectbox("Difficulty", ["All", "Easy", "Medium", "Hard"], key="ex_diff")
    
    exercises = filter_exercises(category, difficulty)
    if not exercises:
        st.warning("No exercises match your filters.")
        return
    
    # Exercise selector
    exercise_titles = [f"{ex['id']}. {ex['title']} ({ex['difficulty']})" for ex in exercises]
    selected = st.selectbox("Select Exercise", exercise_titles)
    selected_idx = exercise_titles.index(selected)
    ex = exercises[selected_idx]
    
    # Exercise card
    st.markdown(f"""
    <div class="custom-card">
        <div style="margin-bottom: 1rem;">
            <span class="category-badge" style="background: rgba(139, 92, 246, 0.2); color: #8B5CF6;">{ex['category']}</span>
            <span class="category-badge diff-{ex['difficulty'].lower()}">{ex['difficulty']}</span>
        </div>
        <h3 style="color: #E2E8F0;">{ex['title']}</h3>
        <p style="color: #94A3B8;">{ex['description']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Code editor
    st.markdown("### Your Code")
    code = st.text_area("", value=ex['starter_code'], height=300, key=f"code_{ex['id']}")
    
    # Buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("💡 Show Hints"):
            for hint in ex['hints']:
                st.info(f"💡 {hint}")
    with col2:
        if st.button("✓ Show Solution"):
            st.session_state.show_solution = not st.session_state.show_solution
    with col3:
        if st.button("🔄 Reset Code"):
            st.rerun()
    
    if st.session_state.show_solution:
        st.markdown("### Solution")
        st.code(ex['solution'], language='python')

def render_ai_assistant():
    """Render the AI assistant chat"""
    st.markdown('<h1 class="gradient-text">🤖 AI Assistant</h1>', unsafe_allow_html=True)
    st.markdown("Ask me anything - I can help with Python and more!")
    
    if not st.session_state.api_key:
        st.warning("⚠️ Please enter your Anthropic API key in the sidebar to use the AI Assistant.")
        return
    
    # Chat display
    chat_container = st.container()
    with chat_container:
        if not st.session_state.messages:
            st.markdown("""
            <div style="text-align: center; padding: 2rem; color: #64748B;">
                <h3>👋 Hello!</h3>
                <p>I'm your AI assistant. Ask me anything about Python, coding, or any other topic!</p>
            </div>
            """, unsafe_allow_html=True)
        
        for msg in st.session_state.messages:
            if msg['role'] == 'user':
                st.markdown(f'<div class="user-message"><strong>You:</strong> {msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="ai-message"><strong>AI:</strong> {msg["content"]}</div>', unsafe_allow_html=True)
    
    # Quick prompts
    st.markdown("### Quick Prompts")
    cols = st.columns(5)
    prompts = ["💡 Explain a concept", "🔧 Debug my code", "📝 Give an example", "🎯 Best practices", "⚡ Quick tip"]
    for i, prompt in enumerate(prompts):
        with cols[i]:
            if st.button(prompt, use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": prompt})
                # Here you would call the API
                st.session_state.messages.append({"role": "assistant", "content": f"You asked: {prompt}. Please enter your Anthropic API key and ask a specific question for a real response!"})
                st.rerun()
    
    # Chat input
    user_input = st.text_input("Type your message...", key="chat_input")
    col1, col2 = st.columns([4, 1])
    with col2:
        if st.button("Send 📤", use_container_width=True) and user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            # Simulate AI response (replace with actual API call)
            st.session_state.messages.append({"role": "assistant", "content": "This is a placeholder response. Connect to the Anthropic API for real AI responses!"})
            st.rerun()
    
    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

def render_ai_create():
    """Render the AI content generator"""
    st.markdown('<h1 class="gradient-text">✨ AI Create</h1>', unsafe_allow_html=True)
    st.markdown("Generate custom quizzes, exercises, and study materials!")
    
    if not st.session_state.api_key:
        st.warning("⚠️ Please enter your Anthropic API key in the sidebar to use AI Create.")
        return
    
    # Generator controls
    col1, col2, col3 = st.columns(3)
    with col1:
        gen_type = st.selectbox("Content Type", ["📝 Quiz", "💻 Coding Exercise", "🎴 Flashcards", "🏆 Challenge"])
    with col2:
        difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
    with col3:
        count = st.selectbox("Count", [3, 5, 10])
    
    topic = st.text_input("Topic", placeholder="e.g., Python decorators, Machine Learning, Spanish verbs...")
    
    # Quick topics
    st.markdown("**Quick Topics:**")
    quick_topics = ["Python basics", "Data structures", "OOP concepts", "Web scraping", "API development", "Testing", "Async/await", "Type hints"]
    cols = st.columns(4)
    for i, t in enumerate(quick_topics):
        with cols[i % 4]:
            if st.button(t, key=f"topic_{i}"):
                topic = t
    
    if st.button("✨ Generate Content", type="primary", use_container_width=True):
        if topic:
            with st.spinner("Generating content..."):
                # Placeholder - replace with actual API call
                st.session_state.generated_content = {
                    "type": gen_type,
                    "topic": topic,
                    "content": f"Generated {gen_type} about {topic} at {difficulty} difficulty"
                }
        else:
            st.warning("Please enter a topic!")
    
    if st.session_state.generated_content:
        st.markdown("### Generated Content")
        st.markdown(f"""
        <div class="custom-card">
            <h4>{st.session_state.generated_content['type']}: {st.session_state.generated_content['topic']}</h4>
            <p>{st.session_state.generated_content['content']}</p>
        </div>
        """, unsafe_allow_html=True)

def render_library():
    """Render the Python library reference"""
    st.markdown('<h1 class="gradient-text">📚 Python Library</h1>', unsafe_allow_html=True)
    st.markdown("Explore popular Python libraries and their usage!")
    
    # Search and filter
    col1, col2 = st.columns([3, 1])
    with col1:
        search = st.text_input("🔍 Search libraries...", placeholder="NumPy, Pandas, Flask...")
    with col2:
        category = st.selectbox("Category", ["All"] + get_library_categories())
    
    libraries = filter_libraries(category)
    if search:
        libraries = [lib for lib in libraries if search.lower() in lib['name'].lower() or search.lower() in lib['description'].lower()]
    
    # Display libraries in grid
    for i in range(0, len(libraries), 3):
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(libraries):
                lib = libraries[i + j]
                with col:
                    with st.expander(f"{lib['icon']} {lib['name']}", expanded=False):
                        st.markdown(f"**Category:** {lib['category']}")
                        st.markdown(lib['description'])
                        st.code(lib['install'], language='bash')
                        st.markdown("**Example:**")
                        st.code(lib['example'], language='python')
                        st.markdown(f"[📖 Documentation]({lib['docs']})")

def render_resources():
    """Render the learning resources section"""
    st.markdown('<h1 class="gradient-text">🔗 Learning Resources</h1>', unsafe_allow_html=True)
    st.markdown("Curated collection of the best Python learning materials!")
    
    # Filter tabs
    tabs = st.tabs(["All", "📖 Docs", "🎓 Courses", "💻 Practice", "📕 Books", "👥 Community", "🔧 Tools"])
    
    categories = ["All", "Documentation", "Courses", "Practice", "Books", "Community", "Tools"]
    
    for tab, cat in zip(tabs, categories):
        with tab:
            resources = filter_resources(None if cat == "All" else cat)
            
            for i in range(0, len(resources), 2):
                cols = st.columns(2)
                for j, col in enumerate(cols):
                    if i + j < len(resources):
                        res = resources[i + j]
                        with col:
                            st.markdown(f"""
                            <div class="custom-card">
                                <h4>{res['icon']} {res['name']}</h4>
                                <span class="category-badge" style="background: rgba(139, 92, 246, 0.2); color: #8B5CF6;">{res['type']}</span>
                                <p style="color: #94A3B8; margin-top: 0.5rem;">{res['description']}</p>
                                <a href="{res['url']}" target="_blank" style="color: #8B5CF6;">Visit →</a>
                            </div>
                            """, unsafe_allow_html=True)

def render_cheat_sheets():
    """Render the cheat sheets section"""
    st.markdown('<h1 class="gradient-text">📋 Cheat Sheets</h1>', unsafe_allow_html=True)
    st.markdown("Quick reference guides for Python concepts!")
    
    # Cheat sheet tabs
    tabs = st.tabs([cs['title'] for cs in CHEAT_SHEETS])
    
    for tab, cs in zip(tabs, CHEAT_SHEETS):
        with tab:
            st.markdown(f"""
            <div class="custom-card">
                <span class="category-badge" style="background: rgba(139, 92, 246, 0.2); color: #8B5CF6;">{cs['category']}</span>
            </div>
            """, unsafe_allow_html=True)
            st.code(cs['content'], language='python')
            if st.button(f"📋 Copy {cs['title']}", key=f"copy_{cs['title']}"):
                st.toast("Copied to clipboard!", icon="✓")

# Main router
if "📝 Practice Quiz" in page:
    render_practice_quiz()
elif "💻 Coding Exercises" in page:
    render_coding_exercises()
elif "🤖 AI Assistant" in page:
    render_ai_assistant()
elif "✨ AI Create" in page:
    render_ai_create()
elif "📚 Library" in page:
    render_library()
elif "🔗 Resources" in page:
    render_resources()
elif "📋 Cheat Sheets" in page:
    render_cheat_sheets()

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748B; padding: 1rem;">
    <p>🐍 Python Mastery Hub | Built with Streamlit</p>
    <p style="font-size: 0.75rem;">© 2024 | Interactive Python Learning Platform</p>
</div>
""", unsafe_allow_html=True)
