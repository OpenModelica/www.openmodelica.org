---
title: "December 1, 2016: OpenModelica 1.11 Beta1 released"
---
<p>&nbsp;The OpenModelica 1.11 Beta1 has been released. You can find the Windows builds&nbsp;<a href="https://build.openmodelica.org/omc/builds/windows/releases/1.11/beta1-15-g8fb863/" target="_blank">here</a>. The Linux and MacOS builds are available via the Download menu above.</p>
<p><strong style="color: #222222; line-height: 1.2;"><span style="font-size: 14pt;">OpenModelica 1.11 Beta1 release, December 1, 2016</span></strong></p>
<p>Summary of most important improvements:</p>
<ul>
<li style="line-height: 17.6px;">Dramatically improved compilation speed and performance, in particular for large models.</li>
<li style="line-height: 17.6px;">3D animation visualization of regular MSL MultiBody simulations and for real-time FMUs.</li>
<li style="line-height: 17.6px;">Better support for synchronous and state machine language elements, now supports 90% of the clocked synchronous library.</li>
<li style="line-height: 17.6px;">Several OMEdit improvements including folding of large annotations.</li>
<li style="line-height: 17.6px;">64-bit OM on Windows further stabilized</li>
<li style="line-height: 17.6px;">An updated OMDev (OpenModelica Development Environment), involving msys2. This was needed for the shift to 64-bit on Windows.</li>
<li style="line-height: 17.6px;">Integration of Sundials/IDA DAE solver with potentially large increase of simulation performance for large models with sparse structure.</li>
<li style="line-height: 17.6px;">Improved library coverage.</li>
<li style="line-height: 17.6px;">Parameter sensitivity analysis added to OMC.</li>
</ul>
<p class="Appendix3"><span style="font-size: 12pt;"><strong>OpenModelica Compiler (OMC)</strong></span></p>
<ul>
<li style="line-height: 17.6px;">Dramatically improved compilation speed and dramatically reduced memory requirements for very large models. In Nov 2015, the largest power generation and transmission system model that OMC could handle had 60000 equations and it took 700 seconds to generate the simulation executable code; it now takes only 45 seconds to do so with OMC 1.11.0, which can also handle a model 10 times bigger (600 000 equations) in less than 15 minutes and with less than 32 GB of RAM. Simulation times are comparable to domain-specific simulation tools.</li>
<li style="line-height: 17.6px;">Improved library coverage</li>
<li style="line-height: 17.6px;">Better support for synchronous and state machine language elements, now simulates 90% of the clocked synchronous library.</li>
<li style="line-height: 17.6px;">Enhanced Cpp runtime to support the PowerSystems library.</li>
<li style="line-height: 17.6px;">Integration of Sundials/IDA solver as an alternative to DASSL.</li>
<li style="line-height: 17.6px;">A DAEMode solver mode was added, which allows to use the sparse IDA solver to handle the DAEs directly. This can lead to substantially faster simulation on large systems with sparse structure, compared to the traditional approach.</li>
<li style="line-height: 17.6px;">The direct sparse solvers KLU and SuperLU have been added, with benefits for models with large algebraic loops.</li>
<li style="line-height: 17.6px;">Multi-parameter sensitivity analysis added to OMC.</li>
<li style="line-height: 17.6px;">Progress on more efficient inline function mechanism.</li>
<li style="line-height: 17.6px;">Stabilized 64-bit Windows support.</li>
<li style="line-height: 17.6px;">Performance improvement of parameter evaluation.</li>
<li style="line-height: 17.6px;">Enhanced tearing support, with prefer iteration variables and user-defined tearing.</li>
<li style="line-height: 17.6px;">Support for external object aliases in connectors and equations (a non-standard Modelica extension).</li>
</ul>
<p class="Appendix3"><strong style="font-size: 12pt;">Graphic Editor OMEdit</strong></p>
<ul>
<li style="line-height: 17.6px;">Significantly faster browsing of most libraries.</li>
<li style="line-height: 17.6px;">Several GUI improvements including folding of multi-line annotations.</li>
<li style="line-height: 17.6px;">Further improved code formatting preservation during edits.</li>
<li style="line-height: 17.6px;">Support for all simulation logging flags.</li>
<li style="line-height: 17.6px;">Select and export variables after simulation.</li>
<li style="line-height: 17.6px;">Support for Byte Order Mark <a href="https://en.wikipedia.org/wiki/Byte_order_mark">https://en.wikipedia.org/wiki/Byte_order_mark</a>.&nbsp;Added support enables other tools to correctly read the files written by OMEdit.</li>
<li style="line-height: 17.6px;">Save files with line endings according to OS (Windows (CRLF), Unix (LF)).</li>
<li style="line-height: 17.6px;">Added OMEdit support for FMU cross compilation. This makes it possible to launch OMEdit on a remote or virtual Linux machine using a Windows X server and export an FMU with Windows binaries.</li>
<li style="line-height: 17.6px;">Support of DisplayUnit and unit conversion.</li>
<li style="line-height: 17.6px;">Fixed automatic save.</li>
<li style="line-height: 17.6px;">Initial support for DynamicSelect in model diagrams (texts and visible attribute after simulation, no expressions yet).</li>
<li style="line-height: 17.6px;">An HTML documentation editor.</li>
<li style="line-height: 17.6px;">Improved logging in OMEdit of structured messages and standard output streams for simulations.</li>
</ul>
<p><strong style="font-size: 12pt;">FMI Support</strong></p>
<ul>
<li>Cross compilation of C++ FMU export. Compared to the C runtime, the C++ cross compilation covers the whole runtime for model exchange.</li>
<li>Improved Newton solver for C++ FMUs (scaling and step size control).</li>
</ul>
<p><strong style="font-size: 12pt;">Other things</strong></p>
<ul>
<li style="line-height: 17.6px;">3D animation visualization of regular MSL MultiBody simulations and for real-time FMUs.</li>
<li style="line-height: 17.6px;">An updated OMDev (OpenModelica Development Environment), involving msys2. This was needed for the shift to 64-bit on Windows.</li>
<li style="line-height: 17.6px;">OMWebbook – a web version of OMNotebook online, <a href="https://omwebbook.openmodelica.org/">https://omwebbook.openmodelica.org/</a> &nbsp;Also, a script is available to convert an OMNotebook to an OMWebbook.</li>
<li style="line-height: 17.6px;">A Jupyter notebook Modelica mode, available in OpenModelica.</li>
</ul>
