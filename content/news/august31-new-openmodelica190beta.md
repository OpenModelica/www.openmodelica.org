---
title: "August 31, 2012: OpenModelica 1.9.0 Beta released"
---
<p>The OpenModelica 1.9.0 Beta has been <a href="https://build.openmodelica.org/omc/builds/windows/releases/1.9.0/beta" target="_blank">released</a>. You can find the Windows builds&nbsp;<a href="https://build.openmodelica.org/omc/builds/windows/releases/1.9.0/beta" target="_blank">here</a>. The Linux and MacOS builds are available via the Download menu above.</p>
<p>Many thanks to everybody who contributed!</p>
<h1><span lang="SV">A.1<span style="font: 7pt;"> </span></span><span lang="SV">OpenModelica 1.9.0 Beta, August 2012</span></h1>
<p>The OpenModelica 1.9.0 beta release has a more complete OMC model compiler. It simulates more models than the previous 1.8.1 version, for example 74 MSL 3.1 example models compared to 36 example models for the previous release, and partial support for some other libraries like ThermoSysPro. It also contains a further improved ModelicaML version for the latest Eclipse and Papyrus releases. However it does not yet contain support for the Fluid library, which is the target for the final 1.9.0 release planned for the October/November time frame.</p>
<h2><span lang="SV">A.1.1<span style="font: 7pt;"> </span></span><span lang="SV">OpenModelica Compiler (OMC)</span></h2>
<p>This release mainly includes bug fixes and improvements of the OpenModelica Compiler (OMC), including, but not restricted to:</p>
<ul>
<li>A more stable and complete OMC model compiler. The 1.9.0 beta version simulates more models than the previous 1.8.1 version.</li>
<li>Better simulation support for MSL, e.g. 74 MSL 3.1 example models now simulate compared to 36 models for the 1.8.1 version. Almost all MultiBody example models (except 2) now simulate.</li>
<li>Better simulation support for several other libraries, e.g. more than twenty examples simulate from ThermoSysPro, and all but one model from PlanarMechanics simulate.</li>
<li>NOTE: this beta version does not support simulation of the Fluid library. That is the target for the final 1.9.0 release, planned for the October/November time frame.</li>
<li>Improved tearing algorithm for the compiler backend. Tearing is by default used.</li>
<li>Matching and dynamic state selection algorithms for the compiler backend.</li>
<li>New index reduction algorithm implementation.</li>
<li>Better initialization, including symbolic matrices for initialization.</li>
<li>Better class loading from files. The package.order file is now respected and the file structure is more thoroughly examined.</li>
<li>It is now possible to translate the error messages in the omc kernel.</li>
<li>Enhanced ModelicaML version with support for value bindings in requirements-driven modeling available for the latest Eclipse and Papyrus versions. GUI specific adaptations. Automated model composition workflows (used for model-based design verification against requirements) are modularized and have improved in terms of performance.</li>
<li>Improved FMI import to prepare for FMI for co-simulation.</li>
<li>Checking (when possible) that variables have been assigned to before they are used in algorithmic code.</li>
<li>Full version of Python scripting.</li>
<li>Prototype support for uncertainty computations, special feature enabled by special flag.</li>
<li>Parallel algorithmc Modelica support (ParModelica) for efficient portable parallel algorithmic programming based on the OpenCL standard, for CPUs and GPUs.</li>
<li>Support for optimisation of semiLinear according to MSL 3.3 chapter 3.7.2.5 semiLinear.</li>
<li>Various bugfixes.</li>
<li>NOTE: interactive simulation is not operational in this beta release. It will be put back again in the near future, first available as a nightly build. It is also available in the previous 1.8.0 release.</li>
</ul>
<h2><span lang="SV">A.1.2<span style="font: 7pt;"> </span></span><span lang="SV">OpenModelica Notebook (OMNotebook)</span></h2>
<ul>
<li>No changes.</li>
</ul>
<h2><span lang="SV">A.1.3<span style="font: 7pt;"> </span></span><span lang="SV">OpenModelica Shell (OMShell)</span></h2>
<ul>
<li>No changes.</li>
</ul>
<h2>A.1.4<span style="font: 7pt;"> </span>OpenModelica Eclipse Plug-in (MDT)</h2>
<ul>
<li>Enhanced debugger for algorithmic Modelica code, supporting both standard Modelica algorithmic code called from simulation models, and MetaModelica code.</li>
</ul>
<h2><span lang="SV">A.1.5<span style="font: 7pt;"> </span></span><span lang="SV">OpenModelica Development Environment (OMDev)</span></h2>
<ul>
<li>Migration of version handling and configuration management from CodeBeamer to Trac.</li>
</ul>
<h2><span lang="SV">A.1.6<span style="font: 7pt;"> </span></span><span lang="SV">Graphic Editor OMEdit</span></h2>
<ul>
<li>Preserving user customizations.</li>
<li>Show dummy red box for models with no graphical annotations.</li>
<li>Bug fixes.</li>
</ul>
<h2><span lang="SV">A.1.7<span style="font: 7pt;"> </span></span><span lang="SV">OMOptim Optimization Subsystem</span></h2>
<ul>
<li>Bug fixes.</li>
</ul>
<h2><span lang="SV">A.1.8<span style="font: 7pt;"> </span></span><span lang="SV">FMI Support</span></h2>
<ul>
<li>Bug fixes.</li>
</ul>
