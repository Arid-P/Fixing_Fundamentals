# 04 — Phase 3: C++, Electronics, Digital Logic, Embedded (Simulated), Systems

**Purpose:** build the software-plus-hardware-thinking foundation that helps in an Electrical Engineering degree.
**Constraints:** zero budget (simulators only), ~2.5 h/week (Apr–Sep 2027) rising to ~4 h/week (Oct 2027+); a light 1 h/week start in Oct–Dec 2026; **paused Jan–Mar 2027** for CBSE Class 12.
**Language decision:** **C++** chosen (not C, not Rust). C is still *read* later (vendor SDKs, datasheets, many embedded courses use it); Arduino-style code is C++. Rust is an optional second systems language after the degree starts.
**Legend:** `[ ]` not started · `[~]` partial · `[x]` verified (can do without notes, no AI writing the answer).

Free tools (verify current free-tier limits at time of use): learncpp.com, g++/gdb on Ubuntu, Compiler Explorer, Falstad circuit simulator, Tinkercad Circuits, Wokwi (Arduino/ESP32/Pico), CircuitVerse, Logisim-evolution, EDA Playground (Verilog), ngspice, Python + NumPy/SciPy/Matplotlib via uv, nand2tetris (free).

Each block = ~45 hours. Each block mixes: C++ · concept/math · simulator · system-design habit · one real build.
Follow **topics**, not chapter numbers (learncpp restructures its chapters).

---

## BLOCK 1 — Bits & Basics (~45 h)  · Oct–Dec 2026 (light, ~13 h) + Apr–Jun 2027 (~32 h)

### C++ atoms
- [ ] CPP-01 Toolchain: install `g++`, compile a file, run it; what compiling, linking, and executables are.
- [ ] CPP-02 Program structure: `main`, statements, `#include <iostream>`, `std::cout`/`std::cin`.
- [ ] CPP-03 Variables, initialization forms (`{}` brace init preferred), naming.
- [ ] CPP-04 Fundamental types: `int`, `unsigned`, `double`, `char`, `bool`; sizes; overflow behavior; fixed-width types from `<cstdint>` (`uint8_t`, `int32_t`).
- [ ] CPP-05 Constants: `const`, `constexpr`.
- [ ] CPP-06 Operators: arithmetic, integer division/modulo, comparison, logical, increment; precedence.
- [ ] CPP-07 Control flow: `if`, `switch`, `for`, `while`, `do-while`, `break`, `continue`.
- [ ] CPP-08 Functions: declaration vs definition, parameters, return values, pass by value; header (`.h`) and source (`.cpp`) split; multiple-file compile with a Makefile.
- [ ] CPP-09 Scope and lifetime: local/global, `static` locals.
- [ ] CPP-10 Arrays (C-style) and `std::array`; `std::vector` basics (push_back, indexing, size).
- [ ] CPP-11 Strings: `std::string`, common operations; C-string difference.
- [ ] CPP-12 File I/O with `<fstream>`.
- [ ] CPP-13 Debug basics: compiler warnings (`-Wall -Wextra`), print debugging, first `gdb` session (break, run, next, print).

### Digital and number-system atoms (shared with CBSE Class 11 Unit 1)
- [ ] DG-01 Binary, hex, octal; conversions.
- [ ] DG-02 Unsigned vs signed integers; **two's complement**; range of n-bit numbers.
- [ ] DG-03 Bitwise operators in C++: `& | ^ ~ << >>`; masks; set/clear/toggle/test bit.
- [ ] DG-04 Boolean algebra: laws, De Morgan, truth tables, simplification.
- [ ] DG-05 Gates: AND, OR, NOT, NAND, NOR, XOR; NAND/NOR universality.
- [ ] DG-06 Half adder, full adder, ripple-carry adder from gates.

### Simulator atoms
- [ ] EM-01 Wokwi/Tinkercad: place an Arduino, wire an LED with a resistor, run "blink" in C++ (`setup`/`loop`, `pinMode`, `digitalWrite`, `delay`).
- [ ] SIM-01 CircuitVerse: build gates, then a full adder, then a 4-bit adder.

### System-design habit (see `06` §2)
- [ ] SD-01 Write a one-page design before each build: inputs, outputs, states, block diagram.

### Build 1 — Binary adder, two ways
C++ program that reads two binary strings and adds them (no built-in conversion), and a CircuitVerse 4-bit ripple-carry adder. Acceptance: 20 test cases agree between both; design page and truth table in README; overflow case explained.

---

## BLOCK 2 — Memory & Circuits (~45 h)  · Jul–Oct 2027

### C++ atoms
- [ ] CPP-14 References vs values; `const` references.
- [ ] CPP-15 Pointers: address-of, dereference, null, pointer arithmetic, arrays decaying to pointers.
- [ ] CPP-16 Stack vs heap; `new`/`delete`; why leaks and dangling pointers happen.
- [ ] CPP-17 Structs and enums (`enum class`).
- [ ] CPP-18 Classes: members, constructors, destructors, access control, `this`.
- [ ] CPP-19 RAII; smart pointers (`std::unique_ptr` first; `shared_ptr` concept).
- [ ] CPP-20 `std::vector` internals: size vs capacity, reallocation; iterators basics.
- [ ] CPP-21 Overloading, default args; simple operator overloading; templates (function templates intro).
- [ ] CPP-22 `gdb` proper: breakpoints, watch, backtrace, inspect pointers; AddressSanitizer (`-fsanitize=address`) to catch memory bugs.
- [ ] CPP-23 Build tooling: Makefile fluency; CMake intro (optional).

### Electronics atoms
- [ ] EL-01 Charge, current, voltage, resistance; units and prefixes.
- [ ] EL-02 Ohm's law; power (`P = VI`).
- [ ] EL-03 Series and parallel resistors; equivalent resistance.
- [ ] EL-04 Kirchhoff's current and voltage laws.
- [ ] EL-05 Voltage divider and current divider.
- [ ] EL-06 Node-voltage analysis for small networks (needs linear systems; see `05`).
- [ ] EL-07 Multimeter concepts (measure V, I, R in simulation); breadboard reading.
- [ ] EL-08 LED current-limiting resistor calculation; pull-up/pull-down resistors and why buttons need them.

### Simulator atoms
- [ ] SIM-02 Falstad: build divider, series-parallel; observe current flow animation.
- [ ] EM-02 Tinkercad/Wokwi: read a button, read a potentiometer (analog), drive an LED with PWM.

### System-design atoms
- [ ] SD-02 State machines: states, events, transitions; draw as a diagram *before* coding; implement with `enum class` + `switch`.

### Build 2 — Traffic-light controller + resistor-network solver
(a) Traffic light with pedestrian button as an explicit state machine on a simulated Arduino (state diagram in README; debounce discussed). (b) A C++ program that computes node voltages of a given resistor network by solving a linear system (Gaussian elimination), checked against Falstad. Acceptance: state diagram matches code; solver matches simulator within 1%; no memory errors under AddressSanitizer.

---

## BLOCK 3 — Data & Sensors (~45 h)  · Nov 2027–Jan 2028

### C++ atoms
- [ ] CPP-24 STL containers: `vector`, `array`, `deque`, `list`, `map`/`unordered_map`, `set`, `stack`, `queue`, `priority_queue`.
- [ ] CPP-25 Algorithms/iterators: `sort`, `find`, `accumulate`, lambdas.
- [ ] CPP-26 Exceptions (concept) and error-handling strategies; why embedded code often avoids exceptions.
- [ ] CPP-27 Implement from scratch: dynamic array, singly linked list, stack, queue, hash table (chaining), binary search tree.
- [ ] CPP-28 Complexity analysis of the above; compare with STL versions by measurement.

### DSA atoms (C++ versions; see `06` §4)
- [ ] DS-01 Sorting: insertion, merge, quick (and stability); when to use `std::sort`.
- [ ] DS-02 Binary search and its off-by-one traps.
- [ ] DS-03 Recursion in depth; call stack; base cases; memoization idea.
- [ ] DS-04 Trees: traversal (pre/in/post/level order), BST ops.
- [ ] DS-05 Graphs: adjacency list/matrix, BFS, DFS.
- [ ] DS-06 Dynamic programming: overlapping subproblems, top-down vs bottom-up, 5 classic problems.
- [ ] DS-07 Ring buffer (circular queue) and why embedded systems love it.

### Concept/math atoms (see `05`)
- [ ] MA-INT Integrals as area/accumulation; sampling and quantization; ADC resolution (LSB size = Vref / 2^n).
- [ ] MA-PROB Mean, variance, standard deviation, normal distribution intuition; averaging reduces noise.

### Simulator and system atoms
- [ ] EM-03 ADC read, map ADC counts to volts, serial print, PWM output.
- [ ] SD-03 Producer/consumer through a ring buffer; interfaces between modules; data-flow diagram.

### Build 3 — Simulated sensor logger
Wokwi project reading a simulated temperature/light sensor, storing samples in a ring buffer, computing moving average, raising alarms at thresholds, and printing a report over serial. Acceptance: buffer wrap-around tested; unit tests for the ring buffer in desktop C++; data-flow diagram and design doc in README.

---

## BLOCK 4 — Time & Interrupts (~45 h)  · Feb–Apr 2028

### C++/embedded atoms
- [ ] CPP-29 Bit manipulation mastery: registers as bit fields; masks and shifts; `constexpr` bit helpers.
- [ ] CPP-30 `volatile`; why compilers optimize away hardware reads; atomicity of shared variables between ISR and main.
- [ ] CPP-31 Embedded patterns: no dynamic allocation, fixed-size buffers, fixed-width integer types, avoiding blocking `delay`.
- [ ] EM-04 Timers and timer interrupts; ISR rules (short, no blocking, flag-and-handle).
- [ ] EM-05 `millis()`-style non-blocking timing; scheduling multiple periodic tasks by hand.
- [ ] EM-06 UART basics; (concept) I2C and SPI: buses, addresses, clocks.
- [ ] EM-07 Debouncing: software approach; interrupt-driven button.
- [ ] EM-08 Fixed-point arithmetic vs floating point (why and when).

### Electronics and math atoms
- [ ] EL-09 Capacitor: charge/discharge; RC time constant `τ = RC`.
- [ ] EL-10 Inductor basics; RL time constant.
- [ ] EL-11 Diode, LED as diode; transistor (BJT/MOSFET) as a switch; driving loads from a microcontroller pin.
- [ ] EL-12 Ideal op-amp concept: buffer, inverting/non-inverting amplifier.
- [ ] MA-CX Complex numbers and Euler's formula.
- [ ] MA-ODE1 First-order ODE for RC charging: solve and verify against simulation.

### Simulator atoms
- [ ] SIM-03 Falstad and ngspice: transient analysis of RC/RL circuits; compare with `V(t) = V0(1 − e^(−t/RC))`.

### System-design atoms
- [ ] SD-04 Timing/latency budget: worst-case execution time, period vs deadline; interface contracts between modules.

### Build 4 — Simulated controller (on/off, then PID)
Wokwi (or desktop C++ plant simulation) controlling a simulated heater/motor: on/off with hysteresis first, then PID. Log data, plot response in Python (`uv` project, Matplotlib). Acceptance: step response plotted; overshoot and settling time measured for two PID settings; ISR/timer usage documented; design doc with timing budget.

---

## BLOCK 5 — Signals & Systems Thinking (~45 h; as far as time allows)  · May–Jun 2028

### Atoms
- [ ] CPP-32 Numeric C++ (`<cmath>`, `<numbers>`, precision/rounding errors) and cross-checking against Python/NumPy.
- [ ] SIG-01 Signals: sampling, Nyquist idea, aliasing, quantization noise.
- [ ] SIG-02 Filters: RC low-pass/high-pass (analog); moving-average and first-order IIR (digital).
- [ ] SIG-03 FFT in Python (record or synthesize a signal, spot frequencies).
- [ ] MA-LA Vectors, matrices, solving linear systems, eigenvalues (intuition).
- [ ] MA-FS Fourier series and transform intuition; Laplace transform intuition (RLC as motivation).
- [ ] SD-05 Classic software system design: client/server, APIs, database schema, failure handling (reuses M03/M04).
- [ ] SD-06 Design doc with tradeoffs and failure modes.

### Build 5 — Filter comparison
Digital low-pass filter in C++, compared against an analog RC low-pass simulation and an FFT plot in Python of the same noisy signal. Acceptance: three results plotted on one figure; cutoff frequency derived by hand and matched; README explains discrepancies.

---

## OPTIONAL BUFFER (only if time remains before mid-2028)

- Verilog basics on EDA Playground (combinational and sequential circuits, a small counter, a UART transmitter).
- nand2tetris part 1 (logic gates → ALU → CPU) as a guided hardware-thinking capstone.
- FreeRTOS concepts (tasks, scheduling), purely conceptual.
- Preview the first-semester syllabus of the chosen EE program; log gaps in `07`.

## What is intentionally *not* done before the degree
Rigorous multivariable calculus, complete differential equations, full signals & systems theory, analog circuit design, electromagnetics, real hardware bring-up. The degree teaches these; the goal here is exposure and habits.

## Time-shift note
Originally six 13-week blocks starting Oct 2026 were planned. Adding CBSE Class 11/12, the frozen milestones, and a 3-month C++ pause forced this compressed 5-block plan. **Re-plan in March 2027 using measured pace** (real hours per atom from the READMEs).
