---
title: "December 6, 2019: OpenModelica 1.14.0 released"
---
<p><strong><span style="font-family: Arial, sans-serif; color: black; border: 1pt none windowtext; padding: 0in;">The OpenModelica 1.14.0 is now released.&nbsp;<br /> <br /> </span></strong><strong></strong></p>
<p><span style="font-size: 9pt; font-family: Arial, sans-serif; color: black;">Download&nbsp;</span><span style="text-decoration: underline;"><span style="font-size: 9pt; font-family: Arial, sans-serif; color: #1b57b1; border: 1pt none windowtext; padding: 0in;"><a href="/download/download-linux"><span style="color: #1b57b1;">Linux</span></a></span></span><span style="font-size: 9pt; font-family: Arial, sans-serif; color: black;">,&nbsp;</span><span style="text-decoration: underline;"><span style="font-size: 9pt; font-family: Arial, sans-serif; color: #1b57b1; border: 1pt none windowtext; padding: 0in;"><a href="/download/download-mac"><span style="color: #1b57b1;">Mac</span></a></span></span><span style="font-size: 9pt; font-family: Arial, sans-serif; color: black;">,&nbsp;</span><span style="text-decoration: underline;"><span style="font-size: 9pt; font-family: Arial, sans-serif; color: #1b57b1; border: 1pt none windowtext; padding: 0in;"><a href="/download/download-windows"><span style="color: #1b57b1;">Windows</span></a></span></span><span style="font-size: 9pt; font-family: Arial, sans-serif; color: black;">. Report bugs in&nbsp;</span><a href="{{< param "bugreporting" >}}"><span style="font-size: 9pt; font-family: Arial, sans-serif; color: #1b57b1; border: 1pt none windowtext; padding: 0in;">Trac</span></a><span style="font-size: 9pt; font-family: Arial, sans-serif; color: black;">.</span></p>
<p>Compared with beta2, several bugs have been fixed.</p>
<hr />
<p>The most dramatic enhancement of the OpenModelica Compiler is the New Frontend, which on the average gives a factor of 10-20 speed improvement in the flattening phase of compilation. The new frontend is default in this release, but a feature is implemented that allows the user to switch to the old frontend if problems appear for a specific model.</p>
<p>The speed of the OMEdit GUI has only slightly increased in this version, since it is still dependent mostly on the old frontend. Further GUI speed increases are available in the coming OpenModelica.1.15.0.</p>
<p>About <a href="https://github.com/OpenModelica/OpenModelica/releases/tag/v1.14.0">200 issues have been fixed</a>, including enhancements, compared to the previous 1.13.2 release. The bug fixes are on trac.</p>
<p class="BulletItem"><i>OpenModelica Compiler New Frontend news:</i></p>
<ul>
<li>Implementation of expandable connectors completed, a rather large piece of work.</li>
<li>A number of smaller enhancements and fixes</li>
<li>The New Frontend (NF)gives slightly better simulation coverage on MSL 3.2.3 than the Old Frontend</li>
<li>The New Frontend is on the average about 20 times faster on flattening.</li>
<li>Remaining work is mainly on further bug fixing and testing the new frontend for all other libraries, as well as more work on modifiers of arrays in conjunction with non-expanded arrays. (The array modifiers have now been implemented in 1.16.0 but not yet it 1.14.0 in order to not delay the 1.14.0 release)</li>
</ul>
<p class="BulletItem"><i>OMEdit news:</i></p>
<ul>
<li>Drag and drop for the text layer.</li>
<li>Auto completion of class names, components and annotations.</li>
<li>GUI for data reconciliation – a method for increasing sensor data precision</li>
<li>Improved duplication functionality for copying classes.</li>
<li>Better handling of Compiler flags.</li>
<li>Partly completed: annotations for dynamic icon update.</li>
<li>Support for connectorSizing annotation</li>
<li>Several bug fixes. You can find the list <a href="https://trac.openmodelica.org/OpenModelica/query?status=closed&amp;owner=adeas31&amp;component=OMEdit&amp;milestone=1.14.0&amp;col=id&amp;col=summary&amp;col=component&amp;col=milestone&amp;col=status&amp;col=type&amp;col=priority&amp;order=priority">here</a><span style="color: #1f497d;">.</span></li>
<li>Docs: <a href="/doc/OpenModelicaUsersGuide/latest/omedit.html">https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/omedit.html</a> .</li>
<li>Autocomplete annotations.</li>
<li>Support for Icon/Diagram map annotation</li>
<li>Copy paste functionality</li>
<li>Reset OMEdit settings/options.</li>
<li>Array plots update on re-simulation</li>
<li>Support for connectorSizing annotation.</li>
<li>Drag and drop class names to text layer in OMEdit</li>
<li>OMPlot: Improved plotting e.g., top and bottom margins for better view, snap to curve etc.</li>
<li>GUI support for replaceable libraries is being tested in a separate branch and will be made available in the coming 1.15.0 release.</li>
</ul>
<p><i> OMC backend and run-time system:</i></p>
<ul>
<li>A new more efficient and correct implementation of arrays and records.</li>
<li>The FMI OMSimulator API calls are now also available in the OMC API functions, e.g. for use from OMNotebook, Jupyter notebooks.</li>
</ul>
<p>&nbsp;&nbsp;&nbsp;&nbsp; Backend new features</p>
<ul>
<li>Added possibility to generate analytic Jacobians for linear strong components
<ul>
<li>-Use flag LSanalyticJacobian to enable analytical Jacobian for linear loops. Default false.</li>
</ul>
</li>
<li>Added output language options for linearization: matlab, python, julia.</li>
<li>Available with --linearizationDumpLanguage=modelica/matlab/python/julia. Default is modelica.</li>
</ul>
<p>&nbsp;&nbsp;&nbsp;&nbsp; Backend enhancements</p>
<ul>
<li>Unified Jacobian evaluation from DASSL and IDA integrators</li>
<li>Added result check for linear solvers Lis, Klu, Total Pivot and Umfpack if a residual function is available.</li>
<li>Improved debug dumping
<ul>
<li>-d=bltdump (Index reduction information)</li>
<li>-d=initialization</li>
<li>-d=dumpLoops</li>
</ul>
</li>
</ul>
<ul>
<li>Improved warning for iteration variables:
<ul>
<li>Only warn about non-linear iteration variables with default start attribute.</li>
<li>Other variables have no influence on simulation at all.</li>
</ul>
</li>
</ul>
<ul>
<li>Build instructions for OpenModelica on Windows Subsystem for Linux</li>
<li>Improved Jacobian evaluation with translation flag -d=symJacConstantSplit (requires --generateSymbolicJacobian) Generate Jacobians with separated constant part to split equations that are independent of the seed vector. These equations only need to be evaluated only once per Jacobian evaluation.</li>
</ul>
<p>&nbsp;&nbsp;&nbsp;&nbsp; Backend bugfixes</p>
<ul>
<li>Homotopy: Use simplified version only during initialization to avoid errors during matching and differentiation.</li>
<li>Logging for Homotopy path fixed so log can be loaded in OMEdit.</li>
<li>Support general function call differentiation for equations in residual form.</li>
<li>Equations in residual form don't fail during index reduction any more.</li>
<li>Use correct index from sparse pattern for linear solver Lis.</li>
<li>Fixed auxiliary variables handling for DAEMode. This leads to a greater library coverage for DAEMode.</li>
<li>Fixed build crashes caused by OMSI on OSX.</li>
</ul>
<p><i>OMSimulator (FMI simulation) News:</i></p>
<ul>
<li>Improvements in error control and numeric stability including numerical adaptive step size control. Achieved by adding adaptive step-size control for hybrid CT simulation without rollback, method developed by Rebeka Farkas (presented at 13th Int. Modelica Conference, <a href="https://2019.international.conference.modelica.org/proceedings/html/papers/Modelica2019paper4D2.pdf">https://2019.international.conference.modelica.org/proceedings/html/papers/Modelica2019paper4D2.pdf</a>). Not all tools exporting FMUs provide the optional FMI features, e.g. fmi2SetFMUstate and fmi2GetFMUstate. These are usually required for algorithms providing error control and adaptive step-sizes. OMSimulator now provides a method that doesn’t require these optional FMI features and uses instead additional knowledge about the simulation units provided by the modeller</li>
<li>Added adaptive step-size control based on roll-back mechanism. (still experimental)</li>
<li>Improved handling of output/input derivatives</li>
<li>Provide first order derivatives for all continuous outputs of lookup tables</li>
<li>Fixed various C-API calls and scripting bindings (lua, python)</li>
<li>Fixed some command line options</li>
<li>Improved various error messages</li>
<li>Fixed signal filter for result files</li>
<li>New functionality to add cpu time to the results for each simulation component</li>
<li>Improved FMI export from OpenModelica (further improvements ongoing now)</li>
</ul>
<p>Other functionality:</p>
<ul>
<li>OMMatlab - A complete implementation is now available</li>
</ul>