---
title: "October 25, 2014: OpenModelica 1.9.1 released"
---
<p>The OpenModelica 1.9.1 has been released. You can find the Windows builds&nbsp;<a href="https://build.openmodelica.org/omc/builds/windows/releases/1.9.1/" target="_blank">here</a>. The Linux and MacOS builds are available via the Download menu above.</p>
<p><span style="font-size: 14pt; color: #222222; line-height: 1.2;">OpenModelica 1.9.1 release, October 25, &nbsp;2014</span></p>
<p><span style="line-height: 1.8;">The most important enhancements in the final OpenModelica 1.9.1 release:</span></p>
<p>· Improved library support.</p>
<p>· Further enhanced OMC compiler front-end coverage, scalability, speed and memory.</p>
<p>· Significant improved simulation support for libraries using Fluid and Media.</p>
<p>· Dynamic model debugger for equation-based models integrated with OMEdit.</p>
<p>· Dynamic algorithm model debugger with OMEdit; including support for MetaModelica when using the bootstrapped compiler.</p>
<p>New features: Dynamic debugger for equation-based models; Dynamic Optimization with collocation built into OpenModelica, performance analyzer integrated with the equation model debugger.</p>
<p><span style="font-size: 12pt;">OpenModelica Compiler (OMC)</span></p>
<p>This release mainly includes improvements of the OpenModelica Compiler (OMC), including, but not restricted to the following:</p>
<p>· Further improved OMC model compiler support for a number of libraries including MSL 3.2.1, ModelicaTest 3.2.1, PetriNet, Buildings, PowerSystems, OpenHydraulics, ThermoPower, and ThermoSysPro.</p>
<p>· Further enhanced OMC compiler front-end coverage, scalability, speed and memory.</p>
<p>· Better coverage of Modelica libraries using Fluid and Media.</p>
<p>· Automatic differentiation of algorithms and functions.</p>
<p>· Improved testing facilities and library coverage reporting.</p>
<p>· Improved model compilation speed by compiling model parts in parallel (bootstrapped compiler).</p>
<p>· Support for running model simulations in a web browser.</p>
<p>· New faster initialization that handles over-determined systems, under-determined systems, or both.</p>
<p>· Compiler back-end partly redesigned for improved scalability and better modularity.</p>
<p>· Better tearing support.</p>
<p>· The first run-time Modelica equation-based model debugger, not available in any other Modelica tool, integrated with OMEdit.</p>
<p>· Enhanced performance profiler integrated with the debugger.</p>
<p>· Improved parallelization prototype with several parallelization strategies, task merging and duplication, shorter critical paths, several scheduling strategies.</p>
<p>· Some support for general solving of mixed systems of equations.</p>
<p>· Better error messages.</p>
<p>· Improved bootstrapped OpenModelica compiler.</p>
<p>· Better handling of array subscripts and dimensions.</p>
<p>· Improved support for reduction functions and operators.</p>
<p>· Better support for partial functions.</p>
<p>· Better support for function tail recursion, which reduces memory usage.</p>
<p>· Partial function evaluation in the back-end to improve solving singular systems.</p>
<p>· Better handling of events/zero crossings.</p>
<p>· Support for colored Jacobians.</p>
<p>· New differentiation package that can handle a much larger number of expressions.</p>
<p>· Support for sparse solvers.</p>
<p>· Better handling of asserts.</p>
<p>· Improved array and matrix support.</p>
<p>· Improved overloaded operators support.</p>
<p>· Improved handling of overconstrained connection graphs.</p>
<p>· Better support for the cardinality operator.</p>
<p>· Parallel compilation of generated code for speeding up compilation.</p>
<p>· Split of model files into several for better compilation scalability.</p>
<p>· Improved linear tearing implementation such that it is now enabled by default, leading to significant performance gains for some models. It is now also possible to influence the tearing with annotations in models.</p>
<p>· Support for impure functions.</p>
<p>· Better compilation flag documentation.</p>
<p>· Better automatic generation of documentation.</p>
<p>· Better support for calling functions via instance.</p>
<p>· New text template based unparsing for DAE, Absyn, SCode, TaskGraphs, etc.</p>
<p>· Better support for external objects.</p>
<p>· Improved C++ runtime.</p>
<p>· Improved testing facilities.</p>
<p>· New unit checking implementation.</p>
<p>· Support for model rewriting expressions via rewriting rules in an external file.</p>
<p><span style="font-size: 12pt;">Graphic Editor OMEdit</span></p>
<p>· Convenient editing of model parameter values and re-simulation without recompilation after parameter changes.</p>
<p>· Improved plotting.</p>
<p>· Better handling of flags/units/resources/crashes.</p>
<p>· Run-time Modelica equation-based model debugger that provides both dynamic run-time debugging and debugging of symbolic transformations.</p>
<p>· Run-time Modelica algorithmic code debugger; also MetaModelica debugger with the bootstrapped OpenModelica compiler.</p>
<p><span style="font-size: 12pt;">Optimization</span></p>
<p>A builtin integrated Dynamic Optimization module with collocation, using Ipopt, is now available. Recent improvements includes adding support for handling nonlinear constraints, hessian-matrix approximation, and different order approximation of state. Also added support for using an external input file for the initial guess as well as new flags for output and optimization options.</p>
<p><span style="font-size: 12pt;">FMI Support</span></p>
<p>Support for FMI 2.0 model exchange import and export has been added. FMI 1.0 support has been further improved.</p>
<p>Thanks to all who are contributing to the OpenModelica work!</p>
<hr />
<p>Best regards,<br />Peter Fritzson</p>