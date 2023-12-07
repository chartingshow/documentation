

[statement]()
```
statement
         : := variable_declaration
           | variable_reassignment
           | function_declaration
           | function_call
           | structure
```

referenced by:

* block
* local_block
* local_block_loop
* return_value


[variable_initialization]()
```
variable_initialization
         : := variable_declaration '=' expression
           | structure
```


[variable_declaration]()
```
variable_declaration
         : := declaration_mode? type? identifier
           | tuple_declaration
```

referenced by:

* statement
* switch_structure
* variable_initialization


[declaration_mode]()
```
declaration_mode
         : := 'var'
           | 'varip'
```

referenced by:

* variable_declaration


[type]()
```
type: := 'int'
           | 'float'
           | 'bool'
           | 'color'
           | 'string'
           | 'label'
           | 'line'
           | 'box'
           | 'table'
           | 'int[]'
           | 'float[]'
           | 'bool[]'
           | 'color[]'
           | 'string[]'
           | 'label[]'
           | 'line[]'
           | 'box[]'
           | 'table[]'
```

referenced by:

* variable_declaration


[variable_reassignment]()
```
variable_reassignment
         : := identifier ':=' expression
           | function_call
           | structure
```

referenced by:

* statement


[function_declaration]()
```
function_declaration
         : := identifier '(' parameter_list ')' '=>' (local_block | return_value)
```

referenced by:

* statement


[parameter_list]()
```
parameter_list
         : := parameter_definition(',' parameter_definition)*
```

referenced by:

* function_declaration


[parameter_definition]()
```
parameter_definition
         : := identifier('=' literal)?
```

referenced by:

* parameter_list


[structure]()
```
structure
         : := if_structure
           | for_structure
           | while_structure
           | switch_structure
```

referenced by:

* statement
* variable_initialization
* variable_reassignment


[if_structure]()
```
if_structure
         : := 'if' expression local_block('else if' expression local_block) * 'else'? local_block?
```

referenced by:

* structure


[for_structure]()
```
for_structure
         : := 'for' ('[' name ',' name ']' 'in' | name('in' | '=' expression 'to' (expression 'by')?)) expression local_block_loop
```

referenced by:

* structure


[while_structure]()
```
while_structure
         : := 'while' expression(local_block_loop | 'local_block_loop')
```

referenced by:

* structure


[local_block_loop]()
```
local_block_loop
         : := (statement | 'break' | 'continue') * return_value
```

referenced by:

* for_structure
* while_structure


[switch_structure]()
```
switch_structure
         : := (variable_declaration assign)? 'switch' expression newline indent(expression '=>' block) * (newline '=>' block dedent)?
```

referenced by:

* structure


[local_block]()
```
local_block
         : := statement + return_value
```

referenced by:

* function_declaration
* if_structure


[return_value]()
```
return_value
         : := statement
           | expression
           | tuple
```

referenced by:

* function_declaration
* local_block
* local_block_loop


[tuple_declaration]()
```
tuple_declaration
         : := '[' identifier(',' identifier) * ']'
```

referenced by:

* variable_declaration


[tuple]()
```
tuple: := '[' expression(',' expression) * ']'
```

referenced by:

* return_value


[expression]()
```
expression
         : := (literal | identifier | function_call)?
```

referenced by:

* assignment
* for_structure
* function
* function_call
* function_call_named
* if_structure
* literal_color
* reassignment
* return_value
* switch_structure
* tuple
* variable_initialization
* variable_reassignment
* while_structure


[function_call]()
```
function_call
         : := identifier '(' (((expression ',') * | expression ',') expression)? ')'
```

referenced by:

* expression
* statement
* variable_reassignment


[identifier]()
```
identifier
         : := (Letter | '_')(Letter | '_' | Digit)*
```

referenced by:

* expression
* function_call
* function_declaration
* param
* parameter_definition
* tuple_declaration
* variable_declaration
* variable_reassignment


[arithmetic_operators]()
```
arithmetic_operators
         : := '+'
           | '-'
           | '*'
           | '/'
           | '%'
```


[comparison_operators]()
```
comparison_operators
         : := '!='
           | '=='
           | '>'
           | '>='
```


[logical_operators]()
```
logical_operators
         : := 'not'
           | 'and'
           | 'or'
```


[literal]()
```
literal: := literal_int
           | literal_float
           | literal_bool
           | literal_color
           | literal_string
```

referenced by:

* expression
* param
* parameter_definition
* udt


[literal_int]()
```
literal_int
         : := ('-' | '+')? Digit+
```

referenced by:

* literal


[literal_float]()
```
literal_float
         : := ('-' | '+')? Digit + ('.' Digit +)? ('E' | 'e' Digit + )?
```

referenced by:

* literal


[literal_bool]()
```
literal_bool
         : := 'true'
           | 'false'
           | 'bool(na)'
```

referenced by:

* literal


[literal_color]()
```
literal_color
         : := 'color' (name | ('.rgb' '(' expression ',' expression ',' (expression ',')? | ('r' | 'g' | 'b') '(') expression ')')
           | '#' Hex_digit Hex_digit Hex_digit Hex_digit Hex_digit Hex_digit(Hex_digit Hex_digit)?
```

referenced by:

* literal


[literal_string]()
```
literal_string
         : := '"' (characters | escape_dq) * '"'
           | "'" (characters | escape_sq) * "'"
```

referenced by:

* literal


[characters]()
```
characters
         : := character+
```

referenced by:

* literal_string


[character]()
```
character
         : := non_quote
           | escape_dq
           | escape_sq
```

referenced by:

* characters


[escape_dq]()
```
escape_dq
         : := '\' ( '\"' | '\n' | '\t' | '\r' | '\f' | '\b')?
```

referenced by:

* character
* literal_string



[escape_sq]()
```
escape_sq: := '\' ( "'" | '\n' | '\t' | '\r' | '\f' | '\b')?
```

referenced by:

* character
* literal_string



[name]()
```
name: := Letter(Letter | Digit | '_') *
```

referenced by:

* assignment
* for_structure
* function
* function_call_named
* literal_color
* reassignment
* storage_type
* udt



[non_quote]()
```
non_quote: := '!'
           | '#'
           | '$'
           | '%'
           | '&'
           | '('
           | ')'
           | '*'
           | '+'
           | ','
           | '-'
           | '.'
           | '/'
           | ':'
           | ';'
           | '<'
           | '='
           | '>'
           | '?'
           | '@'
           | '['
           | ']'
           | '^'
           | '`'
           | '~'
```

referenced by:

* character



[udt]()
```
udt: := 'export'? 'type' name(indent storage_type name('=' literal)? newline) +
```



[function]()
```
function: := 'export'? 'method'? name '(' (param (',' param) * )? ')' 'arrow' (block | expression ) 'newline'
```



[assignment]()
```
assignment: := 'varip'? (name assign expression | storage_type name assign(expression | 'na'))
```



[reassignment]()
```
reassignment: := name ':=' expression
```



[function_call_named]()
```
function_call_named: := name '(' (name assign expression (',' name assign expression) *)? ')'
```



[built_in_type]()
```
built_in_type: := 'bool'
           | 'int'
           | 'float'
           | 'color'
           | 'string'
           | 'label'
           | 'line'
           | 'linefill'
           | 'table'
```

referenced by:

* storage_type



[storage_type]()
```
storage_type: := ('array' | 'matrix') '<' (name | built_in_type) '>'
           | name
           | built_in_type
```

referenced by:

* assignment
* udt



[block]()
```
block: := statement +
```

referenced by:

* function
* switch_structure



[param]()
```
param: := identifier('=' literal)?
```

referenced by:

* function



[assign]()
```
assign: := ':='
           | '='
```

referenced by:

* assignment
* function_call_named
* switch_structure



[newline]()
```
newline: :=  # xA
```

referenced by:

* switch_structure
* udt



[indent]()
```
indent: :=  # x9
```

referenced by:

* switch_structure
* udt



[dedent]()
```
dedent: :=  # xA
```

referenced by:

* switch_structure



[_]()
```
_: := Newline
          / * ws: definition * /
```



[Digit]()
```
Digit: := [0-9]
```

referenced by:

* Hex_digit
* identifier
* literal_float
* literal_int
* name



[Hex_digit]()
```
Hex_digit: := Digit
           | [a-fA-F]
```

referenced by:

* literal_color



[Letter]()

```
Letter: := [a-zA-Z]
```

referenced by:

* identifier
* name



[Newline]()

```
Newline: := [\r]?  # xa
```

referenced by:

* _
