---
title: "February 1, 2013: OpenModelica 1.9.0 Beta4 released"
---
<p>The OpenModelica 1.9.0 Beta4 has been released. You can find the Windows builds&nbsp;<a href="https://build.openmodelica.org/omc/builds/windows/releases/1.9.0/beta4" target="_blank">here</a>. The Linux and MacOS builds are available via the Download menu above.</p>
<p>Many thanks to everybody who contributed!</p>
<h1><span style="mso-list: Ignore;">A.1<span style="font: 7.0pt 'Times New Roman';"> </span></span>OpenModelica 1.9.0 Beta4, February 2013</h1>
<p class="MsoBodyText">The OpenModelica 1.9.0 beta4 release has a more complete OMC model compiler. It simulates many more models than the previous 1.8.1 version and 1.9.0 beta1 and beta2 releases. This is the first release that simulates many (58%) of the MSL 3.2.1 Fluid models. Regarding the whole MSL 3.2.1, 233 out of 253 example models now simulate (92%) compared to 118 in the beta2 release Oct 20, and 30% in the 1.9.0 beta1 release. There is also partial support for some other libraries like ThermoSysPro. It also contains a further improved ModelicaML version for the latest Eclipse and Papyrus releases.<span lang="EN-US"> </span></p>
<h2 class="Appendix3" style="mso-list: l0 level3 lfo1;"><span style="mso-list: Ignore;">A.1.1<span style="font: 7.0pt 'Times New Roman';"> </span></span>OpenModelica Compiler (OMC)</h2>
<ul>
<li>This release mainly includes bug fixes and improvements of the OpenModelica Compiler (OMC), including, but not restricted to the following:</li>
<li>A more stable and complete OMC model compiler. The 1.9.0 beta3 version simulates many more models than the previous 1.8.1 version and OpenModelica 1.9.0 beta1 and beta2 versions.</li>
<li>Much better simulation support for MSL 3.2.1, now 233 out of 253 example models simulate (92%) compared to 118 in the beta2 release Oct 20, and 30% in the 1.9.0 beta1 release.</li>
<li>Good support for the MSL 3.2.1 MultiBody library. All example models except one simulate using dynamic state selection, the remaining one simulates with a special flag.</li>
<li>Fairly good support for the MSL 3.2.1 Fluid library, now 24 example models simulate (58%), and all flatten.</li>
<li>Better simulation support for several other libraries, e.g. more than twenty examples simulate from ThermoSysPro, and all but one model from PlanarMechanics simulate.</li>
<li>Improved tearing algorithm for the compiler backend. Tearing is by default used.</li>
<li>Much faster matching and dynamic state selection algorithms for the compiler backend.</li>
<li>New index reduction algorithm implementation.</li>
<li>New default initialization method that symbolically solves the initialization problem much faster and more accurately. This is the first version that in general initialize hybrid models correctly.</li>
<li>Better class loading from files. The package.order file is now respected and the file structure is more thoroughly examined.</li>
<li>It is now possible to translate the error messages in the omc kernel.</li>
<li>Enhanced ModelicaML version with support for value bindings in requirements-driven modeling available for the latest Eclipse and Papyrus versions. GUI specific adaptations. Automated model composition workflows (used for model-based design verification against requirements) are modularized and have improved in terms of performance.</li>
<li>FMI for co-simulation with OMC as master, and improved FMI import.</li>
<li>Checking (when possible) that variables have been assigned to before they are used in algorithmic code.</li>
<li>Full version of Python scripting.</li>
<li>3D graphics visualization using the Modelica3D library.</li>
<li>Prototype support for uncertainty computations, special feature enabled by special flag.</li>
<li>Parallel algorithmic Modelica support (ParModelica) for efficient portable parallel algorithmic programming based on the OpenCL standard, for CPUs and GPUs.</li>
<li>Support for optimisation of semiLinear according to MSL 3.3 chapter 3.7.2.5 semiLinear.</li>
<li>NOTE: interactive simulation is not operational in this beta release. It will be put back again in the near future, first available as a nightly build. It is also available in the previous 1.8.0 release.</li>
</ul>
<p>&nbsp;</p>
<h2 class="Appendix3" style="mso-list: l0 level3 lfo1;"><span style="mso-list: Ignore;">A.1.2<span style="font: 7.0pt 'Times New Roman';"> </span></span></h2>
<h2 class="Appendix3" style="mso-list: l0 level3 lfo1;">Other OpenModelica Subsystems</h2>
<p class="MsoBodyText"><strong><em><span lang="EN-US">OpenModelica Notebook (OMNotebook)</span></em></strong><span lang="EN-US">. A </span><span class="CODE"><span style="font-size: 9.5pt;" lang="EN-US">shortOutput</span></span><span lang="EN-US"> option has been introduced in the simulate command for less verbose output. The DrModelica interactive document has been updated and the models tested. Almost all models now simulate with OpenModelica.</span></p>
<p class="MsoBodyText"><strong><em><span lang="EN-US">OpenModelica Eclipse Plug-in (MDT)</span></em></strong><em><span lang="EN-US">. </span></em><span lang="EN-US">Enhanced debugger for algorithmic Modelica code, supporting both standard Modelica algorithmic code called from simulation models, and MetaModelica code.</span></p>
<p class="MsoBodyText"><strong><em><span lang="EN-US">OpenModelica Development Environment (OMDev.)</span></em></strong><span lang="EN-US"> Migration of version handling and configuration management from CodeBeamer to Trac.</span></p>
<p class="MsoBodyText"><strong><em><span lang="EN-US">Graphic Editor OMEdit</span></em></strong><span lang="EN-US">:</span></p>
<p class="BulletItemFirst" style="mso-list: l1 level1 lfo2;"><span style="font-family: Symbol;" lang="EN-US"><span style="mso-list: Ignore;">·<span style="font: 7.0pt 'Times New Roman';"> </span></span></span><span lang="EN-US">Options to set matching algorithm and index reduction method for simulation.</span></p>
<p class="BulletItem" style="mso-list: l1 level1 lfo2;"><span style="font-family: Symbol;" lang="EN-US"><span style="mso-list: Ignore;">·<span style="font: 7.0pt 'Times New Roman';"> </span></span></span><span lang="EN-US">Backward and Forward navigation support in Documentation view.</span></p>
<p><span style="font-family: Symbol;" lang="EN-US"><span style="mso-list: Ignore;">·<span style="font: 7.0pt 'Times New Roman';"> </span></span></span><span lang="EN-US">Output window for simulations.</span></p>
<p class="BulletItem" style="mso-list: l1 level1 lfo2;"><span style="font-family: Symbol;" lang="EN-US"><span style="mso-list: Ignore;">·<span style="font: 7.0pt 'Times New Roman';"> </span></span></span><span lang="EN-US">Preserving user customizations.</span></p>
<p class="BulletItem" style="mso-list: l1 level1 lfo2;"><span style="font-family: Symbol;" lang="EN-US"><span style="mso-list: Ignore;">·<span style="font: 7.0pt 'Times New Roman';"> </span></span></span><span lang="EN-US">Show dummy red box for models with no graphical annotations.</span></p>
<p class="MsoBodyText"><strong><em><span lang="EN-US">FMI Support</span></em></strong><span lang="EN-US">. FMI co-simulation with OpenModelica as master. Improved FMI Import.</span></p>
<p class="MsoNormal">&nbsp;</p>