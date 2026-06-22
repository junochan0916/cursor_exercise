# cursor_exercise

A Cursor exercise for physicists: practice reviewing physics code with AI, separating scientific reasoning from debugging.

## Repository structure

```
cursor_exercise/
├── debug_exercise/
│   └── free_fall_calculator.py   # Sample script with physics + programming bugs
└── .cursor/skills/physics-review/
    └── skill.md                  # Cursor skill for physics-first code review
```

## Debug exercise

`debug_exercise/free_fall_calculator.py` models **one-dimensional free fall** from rest under constant gravity (`g = 9.81 m/s²`).

It is meant to be read and discussed, not treated as production code. The script:

1. Asks for an initial height (meters)
2. Computes fall time using \(t = \sqrt{2h/g}\)
3. Plots height vs. time using \(y(t) = h - \tfrac{1}{2}gt^2\)
4. Prints the final height at impact

The physics model is correct for ideal free fall (no air resistance, constant \(g\)). The exercise is to find where the **implementation** breaks down.

### Run it

Requires Python 3 with [NumPy](https://numpy.org/) and [Matplotlib](https://matplotlib.org/):

```bash
pip install numpy matplotlib
python debug_exercise/free_fall_calculator.py
```

## Physics-review skill

The project includes a Cursor Agent Skill at `.cursor/skills/physics-review/skill.md`. It guides the agent through a **physics-first** review workflow:

1. Identify the physical system and goal
2. Extract and check the mathematical model
3. Perform unit / dimensional analysis
4. Explain numerical methods (if any)
5. Explain each function in scientific terms
6. Look for physics errors before programming errors
7. Verify results with order-of-magnitude reasoning
8. Suggest physics, numerical, and software improvements separately

### Using the skill in Cursor

Ask the agent explicitly, for example:

> Apply the physics-review skill and explain the code in the debug exercise.

The skill is not applied automatically to every question unless you request it or add a project rule that requires it.

## Suggested workflow

1. Open `debug_exercise/free_fall_calculator.py` and run it (or predict what will happen).
2. Ask Cursor to review the file with the physics-review skill.
3. Compare the agent’s physics analysis with your own before fixing any bugs.
