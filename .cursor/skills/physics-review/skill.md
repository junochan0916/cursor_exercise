Physics Code Review Skill

Purpose

Help physics students understand the physics implemented in code rather than only fixing programming errors.

When reviewing code, always follow the workflow below.

⸻

Step 1: Identify the Physics Problem

Before discussing the code:

* Explain what physical system is being modeled.
* Explain the scientific goal.
* Describe the expected physical behaviour.

Use plain language first.

⸻

Step 2: Extract the Mathematical Model

Identify all equations implemented in the code.

For each equation:

* Write the mathematical expression.
* Define every variable.
* State the assumptions.

If an equation appears incorrect, explain why.

⸻

Step 3: Check Units

For every important quantity:

* Identify physical units.
* Check dimensional consistency.
* Highlight missing conversions.

Always perform dimensional analysis.

⸻

Step 4: Explain the Numerical Method

If present, identify:

* Numerical integration
* Differentiation
* Interpolation
* Monte Carlo sampling
* Optimization
* FFTs

Explain:

* Why the method is used
* Expected numerical accuracy
* Limitations

⸻

Step 5: Explain the Code

For each function:

* Physical purpose
* Inputs
* Outputs
* Connection to the equations

Focus on scientific meaning before programming details.

⸻

Step 6: Look for Physics Errors

Check for:

* Unit mistakes
* Sign mistakes
* Missing constants
* Wrong normalization
* Missing factors of π
* Missing factors of c
* Missing factors of G
* Incorrect boundary conditions

Explain the scientific impact.

⸻

Step 7: Look for Programming Errors

Only after the physics review:

* Syntax errors
* Runtime errors
* Logic errors
* Performance issues

⸻

Step 8: Verify the Result

Estimate the expected answer using order-of-magnitude reasoning.

Ask:

* Is the answer physically plausible?
* Does the scale make sense?
* Are limiting cases recovered?

⸻

Step 9: Improve the Model

Separate suggestions into:

Physics Improvements

Numerical Improvements

Software Engineering Improvements

Always prioritize physics correctness over code style.

⸻

Output Format

Use the following structure:

1. Physics Problem
2. Mathematical Model
3. Unit Analysis
4. Numerical Method
5. Code Explanation
6. Physics Errors
7. Programming Errors
8. Verification
9. Suggested Improvements