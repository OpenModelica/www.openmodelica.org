---
title: "March 08, 2014: OpenModelica 1.9.1 Beta2 released"
---
<p>The OpenModelica 1.9.1 Beta2 has been released. You can find the Windows builds&nbsp;<a href="https://build.openmodelica.org/omc/builds/windows/releases/1.9.1/beta2" target="_blank">here</a>. The Linux and MacOS builds are available via the Download menu above.</p>
<p>Many thanks to everybody who contributed!</p>
<h1><span lang="SV">A.1<span style="font: 7pt;"> </span></span><span lang="SV">OpenModelica 1.9.1 Beta2, March 2014</span></h1>
<p>The most important enhancements in the OpenModelica 1.9.1 Beta2 release:</p>
<ul>
<li>Improved library support.</li>
<li>Further enhanced OCM compiler front-end scalability, speed and memory, will be part of 1.9.1 final release.</li>
<li>Significant improved simulation support for libraries using Fluid and Media will come with final 1.9.1 release.</li>
<li>Dynamic debugger for equation-based models with the bootstrapped OM compiler.</li>
</ul>
<div>New features: Dynamic debugger for equation-based models with the bootstrapped OM compiler; Dynamic Optimization with collocation built into OpenModelica.</div>
<h2><span lang="SV">A.1.1<span style="font: 7pt;"> </span></span><span lang="SV">OpenModelica Compiler (OMC)</span></h2>
<p>This release mainly includes improvements of the OpenModelica Compiler (OMC), including, but not restricted to the following:</p>
<ul>
<li>Further improved OMC model compiler support for a number of libraries including MSL 3.2.1, ModelicaTest 3.2.1, PetriNet, Buildings, PowerSystems, OpenHydraulics, ThermoPower, and ThermoSysPro.</li>
<li>Automatic differentiation of algorithms and functions.</li>
<li>Improved testing facilities and library coverage reporting.</li>
<li>Improved model compilation speed by compiling model parts in parallel (bootstrapped compiler).</li>
<li>Support for running model simulations in a web browser.</li>
<li>Compiler back-end partly redesigned for improved scalability and better modularity.</li>
<li>The first run-time Modelica equation-based model debugger, not available in any other Modelica tool, integrated with OMEdit and the bootstrapped OpenModelica compiler.</li>
<li>Further enhanced OCM compiler front-end scalability, speed and memory, will be part of 1.9.1 final release.</li>
<li>Better coverage of Modelica libraries using Fluid and Media, will be part of 1.9.1 final release.</li>
</ul>
<h2><span lang="SV">A.1.2<span style="font: 7pt;"> </span></span><span lang="SV">OpenModelica Notebook (OMNotebook)</span></h2>
<ul>
<li>No changes apart from bug fixing.</li>
</ul>
<h2><span lang="SV">A.1.3<span style="font: 7pt;"> </span></span><span lang="SV">OpenModelica Shell (OMShell)</span></h2>
<ul>
<li>No changes.</li>
</ul>
<h2>A.1.4<span style="font: 7pt;"> </span>OpenModelica Eclipse Plug-in (MDT)</h2>
<ul>
<li>No changes apart from bug fixing.</li>
</ul>
<h2><span lang="SV">A.1.5<span style="font: 7pt;"> </span></span><span lang="SV">OpenModelica Development Environment (OMDev)</span></h2>
<ul>
<li>No changes apart from bug fixing.</li>
</ul>
<h2><span lang="SV">A.1.6<span style="font: 7pt;"> </span></span><span lang="SV">Graphic Editor OMEdit</span></h2>
<ul>
<li>Convenient editing of model parameter values and re-simulation without recompilation after parameter changes.</li>
<li>Run-time Modelica equation-based model debugger.</li>
</ul>
<h2><span lang="SV">A.1.7<span style="font: 7pt;"> </span></span><span lang="SV">Optimization</span></h2>
<ul>
<li>A native integrated Dynamic Optimization prototype using Ipopt is now in the OpenModelica release.</li>
</ul>
<h2><span lang="SV">A.1.8<span style="font: 7pt;"> </span></span><span lang="SV">FMI Support</span></h2>
<ul>
<li>No changes apart from bug fixing.</li>
</ul>