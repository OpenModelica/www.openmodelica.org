---
title: "January 31, 2016: OpenModelica 1.9.4 beta1 released"
---
<p>The OpenModelica 1.9.4-beta1 is now available <a href="https://build.openmodelica.org/omc/builds/windows/releases/1.9.4/beta1/">here</a>.</p>
<p><strong style="line-height: 1.8;">This OpenModelica 1.9.4 Beta1 release</strong><span style="line-height: 1.8;"> includes a number of improvements compared to the 1.9.3 release.</span></p>
<p>The final 1.9.4 release is planned middle of &nbsp;February. The most important improvements are the following:</p>
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
</ul>
<p>Improvements in the OpenModelica FMI 2.0 support</p>
<ul>
<li>Full FMI 2.0 co-simulation support now available.</li>
</ul>
<p>&nbsp;</p>