---
title: "Efficient Traceable Model-Based Dynamic Optimization – EDOp"
aliases: ["/research/omoptim/edop"]
---

The main goal of this project is to develop a more effective model-based optimization approach by integrating optimization into the model-based development process.
Models and optimization algorithms are combined into integrated models.

To reduce execution time, we will develop improved methods to compile such integrated models to efficient code for new multi-core architectures.

Profiling and debugging technology will be developed to highlight sources of performance problems.

The project includes development of optimization methods to address:

1. Computationally heavy goal functions
2. Dynamic optimal control of startup and load cycles are common industrial application areas with especially problematic computation times.

Many of the results will be made available in a tool extension in the open source OpenModelica platform including interoperability and communication with other tools using the new FMI interface standard.

## Modelica Mathematical Modeling Language

- Strongly typed object‐oriented language with a general class concept.
- Declarative – Equation based.
- Multi domain.
- Visual Hierarchical Component Programming.
- Acausal modeling.

## Simulation: Symbolic + Numeric Methods

Compilation of a Modelica model will result in a system of sorted equations.
Simulation is the runtime solution of such an equation system using a solver scheme and a run‐time system.

## Modelica Optimization Extension

## Project Research Summary

**Optimization methods**

- Gradient and non‐gradient methods
- Relaxation techniques
- Structure‐exploiting heuristics
- Fast parametric optimization with heavy goal functions
- Parallel optimization algorithms

**Platform, tooling and modeling language**

- Smart methods for compiling models to efficient multi‐core architectures
- Exploiting parallelism from the model equation system and the numeric solver
- Extension of the Modelica language for integrated optimization modeling
- Traceability with profiling and debugging support
- Integrated platform with modular architecture and standardized interfaces

**Applications and modeling**

- Sensitivity analysis
- Hybrid Systems
- Optimal Control

**Integrated Open Source Tool for Modeling and Optimization**

- Equation oriented modeling tool, generation of efficient parallel code.
- Partly based on OpenModelica, cooperation with Open‐Source Modelica Consortium (www\.openmodelica\.org)
- Including performance problem traceability and localization.

## Example of Pipelined Parallel Inlined Solver Approach

- Solver inlining ‐ distribute the solver across all the processes.
- Use a computation pipeline.
- Only communication in one direction inside a time step.
- Try to keep communication as close as possible between processors.

## Industrial Partners and Applications

- **Volvo Construction Equipment** – Wheel loader systems
- **Siemens Industrial Turbines** – Gas turbines, power generation
- **Frontway** – Process industry modeling and optimization
- **Scania** – Truck vehicle systems, e.g. hybrid power, low emission engines
- **SKF** – Complex mechanical systems with bearings, e.g. wind power

## Scania Truck Engine Emissions and Performance Optimization

**Minimize:**

- Particles
- NOx
- Fuel consumption

**Maximize**:

- Output torque/ response

**Tools:**

- Optimizing gas exchange control
- Optimize Fuel injection system

## References

Peter Fritzson. Principles of Object-Oriented Modeling and Simulation with Modelica 2.1. 940 pages, Wiley-IEEE Press, 2004.

Håkan Lundvall and Peter Fritzson. Automatic Parallelization using Pipelining for Equation Based Simulation Languages In proceedings of the 14th Workshop on Compilers for Parallel Computing (CPC'2009), Zurich, Switzerland, Jan 7-9, 2009.

Kaj Holmberg, Martin Joborn, Kennet Melin. Lagrangian Based Heuristics for the Multicommodity Network Flow Problem with Fixed Costs on Paths. Europ.. Jour. of Operational Research 188, pp 101-108, 2008

Lars Eriksson, Johan Wahlström, and Markus Klein, Physical Modeling of Turbocharged Engines and Parameter Identification. pp. 59\-\-79. Springer Verlag. In: Automotive Model Predictive Control: Models, Methods and Applications, Editors: del Re, Allgöwer, Glielmo, Guardiola, and Kolmanovsky, 2009
