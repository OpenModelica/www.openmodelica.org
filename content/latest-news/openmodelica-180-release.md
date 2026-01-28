---
title: "Nov 25: OpenModelica 1.8.0 released"
---
<p>The OpenModelica 1.8.0 was&nbsp;<a href="https://build.openmodelica.org/omc/builds/windows/releases/1.8.0/">released</a>. You can find the Windows builds&nbsp;<a href="https://build.openmodelica.org/omc/builds/windows/releases/1.8.0/">here</a>. The Linux and MacOS builds are available via the Download menu above.<br />Many thanks to everybody that contributed!</p>
<p>&nbsp;</p>
<h1><span lang="SV">A.1<span style="font: 7.0pt 'Times New Roman';"> </span></span><span lang="SV">OpenModelica 1.8, November 2011</span></h1>
<p>&nbsp;</p>
<p class="MsoBodyText">The OpenModelica 1.8 release contains OMC flattening improvements for the Media library – it now flattens the whole library and simulates about 20% of its example models. Moreover, about half of the Fluid library models also flatten. This release also includes two new tool functionalities – the FMI for model exchange import and export, and a new efficient Eclipse-based debugger for Modelica/MetaModelica algorithmic code.</p>
<h2><span lang="SV">A.1.1<span style="font: 7.0pt 'Times New Roman';"> </span></span><span lang="SV">OpenModelica Compiler (OMC)</span></h2>
<p class="MsoBodyText">This release includes bug fixes and improvements of the flattening frontend part of the OpenModelica Compiler (OMC) and several improvements of the backend, including, but not restricted to:</p>
<p class="BulletItem" style="margin-top: 6.0pt;"><span style="font-family: Symbol;">·<span style="font: 7.0pt 'Times New Roman';"> </span></span>A faster and more stable OMC model compiler. The 1.8.0 version flattens and simulates more models than the previous 1.7.0 version.</p>
<p class="BulletItem" style="margin-top: 2.0pt;"><span style="font-family: Symbol;">·<span style="font: 7.0pt 'Times New Roman';"> </span></span> Flattening of the whole Media library, and about half of the Fluid library. Simulation of approximately 20% of the Media library example models.</p>
<p class="BulletItem" style="margin-top: 2.0pt;"><span style="font-family: Symbol;">·<span style="font: 7.0pt 'Times New Roman';"> </span></span>Functional Mockup Interface FMI 1.0 for model exchange, export and import, for the Windows platform.</p>
<p class="BulletItem" style="margin-top: 2.0pt;"><span style="font-family: Symbol;">·<span style="font: 7.0pt 'Times New Roman';"> </span></span>Bug fixes in the OpenModelica graphical model connection editor OMEdit, supporting easy-to-use graphical drag-and-drop modeling and MSL 3.1.</p>
<p class="BulletItem" style="margin-top: 2.0pt;"><span style="font-family: Symbol;">·<span style="font: 7.0pt 'Times New Roman';"> </span></span>Bug fixes in the OMOptim optimization subsystem.</p>
<p class="BulletItem" style="margin-top: 2.0pt;"><span style="font-family: Symbol;">·<span style="font: 7.0pt 'Times New Roman';"> </span></span>Beta version of compiler support for a new Eclipse-based very efficient algorithmic code debugger for functions in MetaModelica/Modelica, available in the development environment when using the bootstrapped OpenModelica compiler.</p>
<p class="BulletItem" style="margin-top: 2.0pt;"><span style="font-family: Symbol;">·<span style="font: 7.0pt 'Times New Roman';"> </span></span>Improvements in initialization of simulations.</p>
<p class="BulletItem" style="margin-top: 2.0pt;"><span style="font-family: Symbol;">·<span style="font: 7.0pt 'Times New Roman';"> </span></span>Improved index reduction with dynamic state selection, which improves simulation.</p>
<p class="BulletItem" style="margin-top: 2.0pt;"><span style="font-family: Symbol;">·<span style="font: 7.0pt 'Times New Roman';"> </span></span>Better error messages from several parts of the compiler, including a new API call for giving better error messages.</p>
<p class="BulletItem" style="margin-top: 2.0pt;"><span style="font-family: Symbol;">·<span style="font: 7.0pt 'Times New Roman';"> </span></span>Automatic partitioning of equation systems and multi-core parallel simulation of independent parts based on the shared-memory OpenMP model. This version is a preliminary experimental version without load balancing.</p>
<h2><span lang="SV">A.1.2<span style="font: 7.0pt 'Times New Roman';"> </span></span><span lang="SV">OpenModelica Notebook (OMNotebook)</span></h2>
<p class="MsoBodyText">No changes.</p>
<h2><span lang="SV">A.1.3<span style="font: 7.0pt 'Times New Roman';"> </span></span><span lang="SV">OpenModelica Shell (OMShell)</span></h2>
<p class="MsoBodyText">Small performance improvements.</p>
<h2>A.1.4<span style="font: 7.0pt 'Times New Roman';"> </span>OpenModelica Eclipse Plug-in (MDT)</h2>
<p class="Appendix3">&nbsp;</p>
<p class="MsoBodyText">Small fixes and improvements. MDT now also includes a beta version of a new Eclipse-based very efficient algorithmic code debugger for functions in MetaModelica/Modelica.</p>
<h2><span lang="SV">A.1.5<span style="font: 7.0pt 'Times New Roman';"> </span></span><span lang="SV">OpenModelica Development Environment (OMDev)</span></h2>
<p class="MsoBodyText">Third party binaries, including Qt libraries and executable Qt clients, are now part of the OMDev package. Also, now uses GCC 4.4.0 instead of the earlier GCC 3.4.5.</p>
<h2><span lang="SV">A.1.6<span style="font: 7.0pt 'Times New Roman';"> </span></span><span lang="SV">Graphic Editor OMEdit</span></h2>
<p class="MsoBodyText">Bug fixes. Access to FMI Import/Export through a pull-down menu. Improved configuration of library loading. A function to go to a specific line number. A button to cancel an on-going simulation. Support for some updated OMC API calls.</p>
<h2><span lang="SV">A.1.7<span style="font: 7.0pt 'Times New Roman';"> </span></span><span lang="SV">New OMOptim Optimization Subsystem</span></h2>
<p class="MsoBodyText">Bug fixes, especially in the Linux version.</p>
<h2><span lang="SV">A.1.8<span style="font: 7.0pt 'Times New Roman';"> </span></span><span lang="SV">FMI Support</span></h2>
<p class="MsoBodyText">The Functional Mockup Interface FMI 1.0 for model exchange import and export is supported by this release. The functionality is accessible via API calls as well as via pull-down menu commands in OMEdit.</p>
<p>&nbsp;</p>
<p class="MsoBodyText">&nbsp;</p>
<p class="MsoBodyText">&nbsp;</p>
