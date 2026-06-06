---
title: "February 18, 2016: OpenModelica 1.9.4 beta2 released"
---
<p>The OpenModelica 1.9.4-beta2 is now available <a href="https://build.openmodelica.org/omc/builds/windows/releases/1.9.4/beta2/">here</a>.</p>
<p><strong style="line-height: 1.8;">This OpenModelica 1.9.4 Beta2 release</strong><span style="line-height: 1.8;"> includes a number of improvements compared to the 1.9.3 release.</span></p>
<p>The final 1.9.4 release is planned mid March. <span style="color: #ff0000;">The current blocker tickets we are still investigating for the final release can be found at:</span> <a href="https://trac.openmodelica.org/OpenModelica/query?status=accepted&amp;status=assigned&amp;status=new&amp;status=reopened&amp;milestone=1.9.4&amp;group=priority&amp;col=id&amp;col=summary&amp;col=owner&amp;col=type&amp;col=priority&amp;col=component&amp;col=version&amp;order=priority">OpenModelica Trac</a>. From the list #3477 and #3630 should be fixed, the others are investigated now.</p>
<p>A number of improvements in the OpenModelica graphic model editor OMEdit (also described <a href="https://www.openmodelica.org/doc/OpenModelicaUsersGuide/latest/omedit.html">here</a>):</p>
<ul>
<li>Undo/Redo support.</li>
<li>Preserving text formatting, including indentation and whitespace. This is especially important for diff/merge with several collaborating developers possibly using several different Modelica tools.</li>
<li>Better support for inherited classes.</li>
<li>Allow simulating models using visual studio compiler.</li>
<li>Support for saving Modelica package in a folder structure.</li>
<li>Allow reordering of classed inside a package.</li>
<li>Highlight matching parentheses in text view.</li>
<li>When copying the text retain the text highlighting and formatting.</li>
</ul>
<p>Several improvements in the OpenModelica model compiler and simulator:</p>
<ul>
<li>Improved simulation speed for many models. simulation speed went up for 80% of the models.&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The compiler frontend became faster for almost all models, average about 30% faster.</li>
<li>Initial support for synchronous models with clocked equations as defined in the Modelica 3.3 standard</li>
</ul>
<p>Improvements in the OpenModelica FMI 2.0 support</p>
<ul>
<li>Full FMI 2.0 co-simulation support now available</li>
<li>Upgrade Cpp runtime from C++03 to C++11 standard, minimizing external link dependencies. Exported FMUs don't depend on additional libraries such as boost anymore</li>
</ul>
<p>&nbsp;</p>