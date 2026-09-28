# 05 — Math Track (just-in-time)

**Learner's decision:** learn math either directly in college, or *as concepts demand it* while building.
No standalone math phase before the degree. Math appears when a build needs it.

## 1. Protocol ("math debt")

1. While working, a build hits a missing concept (e.g. solving a resistor network needs linear systems).
2. **Stop the build.** Log the concept in the *Math Debt List* (bottom of this file) with the atom ID.
3. Learn *only that atom*, in a session capped at **~1 hour** (Slot B in the weekly template).
4. Verify with **5 problems solved from memory, without notes**, of which at least one is applied (from the build).
5. If it does not click in 1–2 sessions, log "partial", use the simulator/NumPy to proceed, and leave the rest for college. Do not let math stall a build for weeks.
6. Mark the atom `[x]` only after step 4.

**Free resources (verify availability):** Khan Academy, 3Blue1Brown (Essence of Calculus, Essence of Linear Algebra, differential equations series), MIT OpenCourseWare (18.01 single-variable calculus, 18.02 multivariable, 18.03 differential equations, 18.06 linear algebra, Strang's lectures), Paul's Online Math Notes, Professor Leonard (calculus). Use NumPy/SymPy to *check* answers, never to replace understanding.

## 2. Calibration warning
An earlier AI audit called his math "elite," based on olympiad-style work. That level is **unverified** for the topics below. Before the first math-heavy block (Block 2, ~Jul 2027), run a 20–30 statement diagnostic on algebra, functions, trig, exponentials/logs, and complex numbers. Record results in `07`.

## 3. Atom map (with the build that triggers it)

### A. Algebra and functions repair (Blocks 1–2)
- [ ] MA-01 Algebraic manipulation, factoring, solving linear and quadratic equations. *(Block 1)*
- [ ] MA-02 Functions and graphs: domain/range, composition, inverse, reading graphs. *(Block 1–2)*
- [ ] MA-03 Exponentials and logarithms (base e, log properties, log scales). *(Block 2–3)*
- [ ] MA-04 Trigonometry: unit circle, identities, radians, sine waves (amplitude, frequency, phase). *(Block 4–5)*
- [ ] MA-05 Systems of linear equations by elimination. *(Block 2: node-voltage solver)*
- [ ] MA-06 Inequalities and absolute value (tolerances, error bounds). *(Block 3)*

### B. Discrete/logic (mostly covered by CBSE Class 11)
- [ ] MA-07 Boolean algebra, truth tables, De Morgan. *(Block 1; shared with C11-U1)*
- [ ] MA-08 Number bases and two's complement. *(Block 1; shared with DG-01/02)*
- [ ] MA-09 Combinatorics/counting basics (likely already strong from olympiad practice; verify). *(Block 3: complexity, DP)*

### C. Calculus (Blocks 2–4)
- [ ] MA-10 Limits (intuition) and continuity.
- [ ] MA-11 Derivative as rate of change; rules (power, product, quotient, chain); derivative of `e^x`, `sin`, `cos`. *(Block 2: circuit rates; Block 4: capacitor `i = C dv/dt`)*
- [ ] MA-INT Integrals as accumulation/area; basic antiderivatives; definite integrals; numerical integration (trapezoid). *(Block 3: sampling/averaging)*
- [ ] MA-12 Sequences, series, Taylor series intuition (`e^x`, `sin x`). *(Block 4–5)*

### D. Complex numbers and ODEs (Block 4)
- [ ] MA-CX Complex numbers: rectangular/polar, Euler's formula `e^{jθ} = cos θ + j sin θ`, magnitude and phase.
- [ ] MA-ODE1 First-order linear ODEs (separable, integrating factor idea); RC charging/discharging solution.
- [ ] MA-ODE2 Second-order linear ODEs with constant coefficients (concept; RLC and oscillators). *(Block 4–5, exposure only)*

### E. Linear algebra (Blocks 2 and 5)
- [ ] MA-LA1 Vectors: dot product, magnitude, projection.
- [ ] MA-LA2 Matrices: multiplication, identity, inverse, determinant, transpose.
- [ ] MA-LA3 Solving `Ax = b` (elimination, LU idea) and checking with NumPy (`numpy.linalg.solve`).
- [ ] MA-LA4 Eigenvalues and eigenvectors (intuition, NumPy use). *(Block 5)*

### F. Signals-related (Block 5, exposure)
- [ ] MA-FS Fourier series: periodic signals as sums of sines; intuition for harmonics.
- [ ] MA-FT Fourier transform and FFT: what the frequency spectrum tells you.
- [ ] MA-LT Laplace transform: why it turns ODEs into algebra (intuition only).

### G. Probability and statistics (Block 3)
- [ ] MA-PROB Mean, variance, standard deviation; normal distribution; noise averaging (variance reduces as 1/N).
- [ ] MA-13 Basic probability rules; independence; expected value.

### H. Numerical methods (Blocks 3–5)
- [ ] MA-NUM1 Root finding: bisection, Newton's method.
- [ ] MA-NUM2 Numerical integration (rectangle, trapezoid, Simpson).
- [ ] MA-NUM3 Euler and RK4 for ODEs; compare with analytic RC solution.
- [ ] MA-NUM4 Floating-point error, rounding, conditioning (why `0.1 + 0.2 != 0.3`).

## 4. Verification style
- 5 problems, no notes, timed (≈ 20 min); one must be an applied circuit/code problem.
- Explain aloud the geometric/physical meaning (e.g., "derivative is slope of the voltage curve at that instant").
- Where possible, cross-check with a program: NumPy for algebra, SciPy/SymPy for calculus, Matplotlib for visual sanity checks.

## 5. Math Debt List (append as you go)

| Date | Atom | Triggered by (build/step) | Status (open / partial / cleared) | Notes |
|---|---|---|---|---|
| — | — | — | — | (empty at start) |
