# MiniPy – Day 1 Notes

## **Project Overview**

**MiniPy** is a lightweight, Python-like interpreted programming language designed for learning compiler and interpreter concepts.
It focuses on simplicity, readability, and type safety, while keeping Python’s clean syntax.

---

## **Goals / Improvements over Python**

1. **Mandatory `let` keyword** for variable declaration → avoids accidental dynamic typing.
2. **Optional type hints** → `let x:int = 5` for better debugging.
3. **Safe arithmetic** → `/` returns float, `//` returns int.
4. **Strict indentation** → enforces consistent block structure.
5. **Simplified print** → works with all types, no `str()` needed.
6. **Scoped variables** → local variables inside functions; global accessible if not shadowed.
7. **No automatic type coercion** → e.g., string + int throws error.

---

## **Keywords**

```
let, print, if, else, while, def, return
```

---

## **Operators**

```
Arithmetic: +, -, *, /, //
Comparison: <, >, <=, >=, ==, !=
Logical: and, or, not
```

---

## **Syntax Rules**

* **Variable declaration:**

```txt
let x = 10
let name = "Alice"
```

* **Print statement:**

```txt
print(x + y)
```

* **Conditional statements:**

```txt
if x < y:
    print(x)
else:
    print(y)
```

* **While loops:**

```txt
let i = 0
while i < 5:
    print(i)
    i = i + 1
```

* **Functions:**

```txt
def add(a, b):
    return a + b
```

* **Comments:** start with `#`

```txt
# this is a comment
```

---

## **Sample Programs**

**1️⃣ Arithmetic + Print**

```txt
let x = 5
let y = 10
print(x + y)
```

**2️⃣ Conditional**

```txt
let a = 5
let b = 10
if a > b:
    print(a)
else:
    print(b)
```

**3️⃣ Loop**

```txt
let i = 0
while i < 3:
    print(i)
    i = i + 1
```

**4️⃣ Function**

```txt
def multiply(a, b):
    return a * b

print(multiply(2, 3))
```

---

## **Next Steps**

* **Day 2:** Build the lexer to convert MiniPy code into tokens.
* **Day 3:** Parse tokens into an Abstract Syntax Tree (AST).
