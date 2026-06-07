---
title: "March 9, 2016: OpenModelica 1.9.4 released"
---
<p><strong><span style="color: #ff0000; font-size: 12pt;"><span style="line-height: 19.8px;">NEW!&nbsp;<span style="color: #000000;">OpenModelica 1.9.6 patch release that fixes an FMI export bug is now available</span>&nbsp;</span><span style="color: #000000;"><span style="line-height: 19.8px; color: #000000;"><a href="newss/169-march-16-openmodelica-196" style="line-height: 19.8px;">here</a>.</span></span><span style="line-height: 19.8px;"><br /></span></span></strong></p>
<p>&nbsp;</p>
<hr />
<p>&nbsp;</p>
<p>The OpenModelica 1.9.4 final release is now available <a href="https://build.openmodelica.org/omc/builds/windows/releases/1.9/4/">here</a>.</p>
<p><strong style="line-height: 1.8;">This OpenModelica 1.9.4 release</strong><span style="line-height: 1.8;"> includes a number of improvements compared to the 1.9.3 release.</span></p>
<p><span style="line-height: 1.8;">A number of improvements in the OpenModelica graphic model editor OMEdit (also described </span><a href="https://www.openmodelica.org/doc/OpenModelicaUsersGuide/latest/omedit.html" style="line-height: 1.8;">here</a><span style="line-height: 1.8;">):</span></p>
<ul>
<li>Undo/Redo support.</li>
<li>Preserving text formatting, including indentation and whitespace. This is especially important for diff/merge with several collaborating developers possibly using several different Modelica tools.</li>
<li>Better support for inherited classes.</li>
<li>Allow simulating models using visual studio compiler.</li>
<li>Support for saving Modelica package in a folder structure.</li>
<li>Allow reordering of classes inside a package.</li>
<li>Highlight matching parentheses in text view.</li>
<li>When copying the text retain the text highlighting and formatting.</li>
<li>Support for global head definition in the documentation by using __OpenModelica_infoHeader annotation.</li>
<li>Support for expandable connectors.</li>
<li>Support for uses annotation.</li>
</ul>
<p>Several improvements in the OpenModelica model compiler and simulator:</p>
<ul>
<li>Improved simulation speed for many models. simulation speed went up for 80% of the models. The compiler frontend became faster for almost all models, average about 40% faster.</li>
<li>Initial support for synchronous models with clocked equations as defined in the Modelica 3.3 standard</li>
<li>Support for homotopy operator</li>
<li><a href="https://github.com/OpenModelica/OpenModelica/releases/tag/v1.9.4">Bug fixes</a></li>
</ul>
<p>Improvements in the OpenModelica FMI 2.0 support</p>
<ul>
<li>Full FMI 2.0 co-simulation support now available</li>
<li>Upgrade Cpp runtime from C++03 to C++11 standard, minimizing external link dependencies. Exported FMUs don't depend on additional libraries such as boost anymore</li>
</ul>
<p><span style="line-height: 19.8px;">64 bit Windows</span></p>
<ul>
<li>Support for 64bit Windows will be included in the <a href="https://build.openmodelica.org/omc/builds/windows/nightly-builds/">nightly-builds</a> after the 1.9.4 release</li>
</ul>
<p>&nbsp;</p>