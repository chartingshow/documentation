## Instructions from PyFlowchart Documentation

**Installation:**

1. **Install using pip:**
   ```bash
   $ pip install pyflowchart
   ```

**Basic Usage:**

2. **Flowchart Python code from the command line:**

   ```bash
   $ python -m pyflowchart example.py
   ```

   - Replace `example.py` with the name of your Python file.
   - This outputs the flowchart in flowchart.js DSL.

3. **Output to an HTML file:**

   ```bash
   $ python -m pyflowchart example.py -o example.html
   ```

   - This creates an interactive HTML file (`example.html`) displaying the flowchart.

4. **Flowchart a specific function or method:**
   ```bash
   $ python -m pyflowchart example.py -f function_name
   ```
   - Replace `function_name` with the actual function name.
   - For methods:
     ```bash
     $ python -m pyflowchart example.py -f ClassName.method_name
     ```

**Flowcharting in Python:**

5. **Import necessary classes:**

   ```python
   from pyflowchart import *
   ```

6. **Create nodes:**

   ```python
   st = StartNode('a_pyflow_test')
   op = OperationNode('do something')
   cond = ConditionNode('Yes or No?')
   io = InputOutputNode(InputOutputNode.OUTPUT, 'something...')
   sub = SubroutineNode('A Subroutine')
   e = EndNode('a_pyflow_test')
   ```

7. **Connect the nodes:**

   ```python
   st.connect(op)
   op.connect(cond)
   cond.connect_yes(io)
   cond.connect_no(sub)
   sub.connect(op, "right")
   io.connect(e)
   ```

8. **Create a Flowchart object and generate the flowchart DSL:**

   ```python
   fc = Flowchart(st)
   print(fc.flowchart())
   ```

9. **Output to an HTML file (programmatically):**
   ```python
   output_html('output.html', 'a_pyflow_test', fc.flowchart())
   ```

**Python to Flowchart (from code):**

10. **Generate a flowchart from Python code:**

```python
from pyflowchart import Flowchart
with open('simple.py') as f:
    code = f.read()
fc = Flowchart.from_code(code)
print(fc.flowchart())
```

- Replace `simple.py` with your Python filename.

**Advanced Usage (from code):**

11. **Using `Flowchart.from_code()`:**

```python
Flowchart.from_code(code, field="", inner=True, simplify=True, conds_align=False)
```

- `code`: Python code to convert.
- `field`: Specific function/method to flowchart (e.g., "foo" or "Bar.buzz").
- `inner`: If `True`, parse the body of `field` as nested. If `False`, treat as a single node.
- `simplify`: If `True`, simplify one-line `if` and `while` statements.
- `conds_align`: If `True`, align consecutive `if` statements.

**Command Line Interface (CLI):**

12. **Advanced options with CLI:**

```bash
python -m pyflowchart [-f FIELD] [-i] [--no-simplify] [--conds-align] [-o OUTPUT] code_file
```

- `-f FIELD`: Specify the `field` (function/method).
- `-i`: Equivalent to `inner=True`.
- `--no-simplify`: Disable simplification (`simplify=False`).
- `--conds-align`: Enable alignment of `if` statements.
- `-o OUTPUT`: Output to a file (e.g., `-o output.html`).
