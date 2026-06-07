---
title: "September 8, 2015: OpenModelica 1.9.3 released"
---
<p>The OpenModelica 1.9.3 has been released. You can find the Windows builds&nbsp;<a href="https://build.openmodelica.org/omc/builds/windows/releases/1.9.3/" target="_blank">here</a>. The Linux and MacOS builds are available via the Download menu above.</p>
<p><strong style="color: #222222; line-height: 1.2;"><span style="font-size: 14pt;">OpenModelica 1.9.3 release, September 8, 2015</span></strong></p>
<p><span style="line-height: 1.8;">The OpenModelica 1.9.3 release is available now, September 8, 2015.</span></p>
<p><span style="line-height: 1.8;">The most important enhancements in the OpenModelica 1.9.3 release:</span></p>
<ul>
<li>Enhanced collaborative development and testing of OpenModelica by moving to the GIT-hub framework for versioning and parallel development.</li>
<li>More accessible and up-to-date automatically generated documentation provided in both html <a href="https://www.openmodelica.org/doc/OpenModelicaUsersGuide/latest/">https://www.openmodelica.org/doc/OpenModelicaUsersGuide/latest/</a> and .pdf <a href="/doc/OpenModelicaUsersGuide/OpenModelicaUsersGuide-latest.pdf">https://openmodelica.org/doc/OpenModelicaUsersGuide/OpenModelicaUsersGuide-latest.pdf</a></li>
<li>Further improved simulation speed and coverage of several libraries.</li>
<li>OMEdit graphic connection editor improvements.</li>
<li>OMNotebook improvements.</li>
</ul>
<p class="Appendix3"><span style="font-size: 12pt;"><strong>OpenModelica Compiler (OMC)</strong></span></p>
<p>This release mainly includes improvements of the OpenModelica Compiler (OMC), including, but not restricted to the following:</p>
<ul>
<li>Further improved simulation speed and coverage for several libraries.&nbsp;</li>
<li>Faster generated code for functions involving arrays, factor 2 speedup for many power generation models.</li>
<li>Better initialization.</li>
<li>An implicit inline Euler solver with adaptive step-size control available.</li>
<li>Code generation to enable vectorization of for-loops.</li>
<li>Improved non-linear, linear and mixed system solving.</li>
<li>Cross-compilation for the ARMhf architecture.</li>
<li>A prototype state machine implementation.</li>
<li>Improved performance and stability of the C++ runtime option.</li>
<li>More accessible and up-to-date automatically generated documentation provided in both html and .pdf.</li>
</ul>
<p class="Appendix3"><span style="font-size: 12pt;"><strong>OpenModelica Notebook (OMNotebook)</strong></span></p>
<p>Several improvements:</p>
<ul>
<li>Support for moving cells from one place to another in a notebook.</li>
<li>A button for evaluation of whole notebooks.</li>
<li>A new cell type called Latex cells, supporting Latex formatted input that provides mathematical typesetting of formulae when evaluated.</li>
</ul>
<p class="Appendix3"><span style="font-size: 12pt;"><strong>OpenModelica Shell (OMShell)</strong></span></p>
<p>No changes.</p>
<p class="Appendix3"><span style="font-size: 12pt;"><strong>OpenModelica Eclipse Plug-in (MDT)</strong></span></p>
<p>No changes apart from bug fixing.</p>
<p class="Appendix3"><span style="font-size: 12pt;"><strong>OpenModelica Development Environment (OMDev)</strong></span></p>
<p>A big change: version handling and parallel development has been improved by moving from SVN to GIThub. This makes it easier for each developer to test his/her fixes and enhancements before committing the code. Automatic mirroring of all code is still performed to the OpenModelica SVN site.</p>
<p class="Appendix3"><span style="font-size: 12pt;"><strong>Graphic Editor OMEdit</strong></span></p>
<p>There are several improvements to the OpenModelica graphic connection editor OMEdit:</p>
<ul>
<li>Support for uses annotations.</li>
<li>Support for declaring components as vectors.</li>
<li>Faster messages browser with clickable error messages.</li>
<li>Support for managing the stacking order of graphical shapes.</li>
<li>Several improvements to the plot tool and text editor in OMEdit.</li>
</ul>
<p><span style="font-size: 12pt;"><strong>Optimization</strong></span></p>
<p>Several improvements of the Dynamic Optimization module with collocation, using Ipopt:</p>
<ul>
<li>Better performance due to smart treatment of algebraic loops for optimization.</li>
<li>Improved formulation of optimization problems with an annotation approach which also allows graphical problem formulation.</li>
<li>It is now possible to formulate final constraints</li>
</ul>
<p class="Appendix3"><span style="font-size: 12pt;"><strong>FMI Support</strong></span></p>
<p>Further improved FMI 2.0 co-simulation support.</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><span style="line-height: 1.8;">Thanks to all who are contributing to the OpenModelica work!</span></p>
<p><span style="line-height: 1.8;">Best regards,<br /></span><span style="line-height: 1.8;">Peter Fritzson and Adrian Pop</span></p>