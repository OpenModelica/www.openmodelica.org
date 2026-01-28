---
title: "Modelica Development Tooling (MDT)"
---
<h1>MDT - Modelica Development Tooling</h1>
<p><a href="https://www.ida.liu.se/%7Eadrpo/mdt/"> <img src="https://www.ida.liu.se/labs/pelab/modelica/OpenModelica/MDT/screenshot.png" alt="MDT screenshot" align="right" border="0" /></a></p>
<p>The Modelica Development Tooling (MDT) Eclipse Plug-In integrates the <a href="https://www.openmodelica.org">OpenModelica</a> compiler with <a href="https://www.eclipse.org/">Eclipse</a>. MDT, together with the OpenModelica compiler, provides an environment for working with <a href="https://www.modelica.org/">Modelica</a> projects.</p>
<p>The following features are available: [<a href="https://www.ida.liu.se/%7Eadrpo/mdt/">Cool Screen Dumps</a>]</p>
<ul>
<li>Browsing support for Modelica projects, packages, and classes</li>
<li>Wizards for creating Modelica projects, packages, and classes</li>
<li>Syntax color highlighting</li>
<li>Syntax checking</li>
<li>Browsing of the Modelica Standard Library</li>
<li>Simple code completion</li>
<li>Code indentation correction</li>
<li>Paranthesis matching</li>
<li>MetaModelica browsing and assistance</li>
<li>OpenModelica command console</li>
</ul>
<p>&nbsp;</p>
<p>MDT was developed by two loony undergraduate students in their eternal quest for a degree. They have finished with their master thesis in April 2006 and, since then, the responsible with maintaining and enhancing MDT is <a href="https://www.ida.liu.se/%7Eadrpo">Adrian Pop</a>. The work on the plugin is a part of the larger project by <a href="https://www.ida.liu.se/labs/pelab/">PELAB</a> which aims to create a complete Modelica and MetaModelica modeling, compilation and simulation environment.</p>
<p>MDT is used at <a href="https://www.ida.liu.se/labs/pelab">PELAB</a> for the development of the <a href="https://www.openmodelica.org">OpenModelica</a> compiler.</p>
<h2>Using</h2>
<p>To use MDT you need the OpenModelica Compiler and <a href="https://www.eclipse.org./downloads/">Eclipse</a> installed on your system.</p>
<p>You can find MDT documentation <a href="https://openmodelica.org/svn/MDT/trunk/docs">HERE</a>.</p>
<p><span style="text-decoration: underline;"><strong>You will also need Java 5.0 (aka 1.5) to use the plugin.</strong></span></p>
<p><span style="text-decoration: underline;"><strong>&nbsp;</strong></span></p>
<h2 id="Installing"><a></a>Installing</h2>
<p><a href="https://trac.openmodelica.org/documents/MDT/install/">Here</a> you can find an MDT installation howto.</p>
<p>The most convenient way to install MDT is by instructing Eclipse to fetch the plugin from the<br /> update site which is located at <a href="https://www.ida.liu.se/labs/pelab/modelica/OpenModelica/MDT/">https://www.ida.liu.se/labs/pelab/modelica/OpenModelica/MDT/</a>.<br /> If you are not sure how to accomplish this, just follow the instructions below.</p>
<ul>
<li>Start Eclipse</li>
<li>Select <em>Help -&gt; Software Updates -&gt; Find and Install...</em> from the menu</li>
<li>Select <em>Search for new features to install</em> and click <em>Next</em></li>
<li>Select <em>New Remote Site...</em></li>
<li>Enter <em>MDT</em> as name and <em>https://www.ida.liu.se/labs/pelab/modelica/OpenModelica/MDT/</em> as URL and click <em>OK</em></li>
<li>Make sure <em>MDT</em> is selected and click <em>Finish</em></li>
<li>In the updates dialog select the <em>MDT</em> feature and click <em>Next</em></li>
<li>Read through the license agreement, select <em>I accept...</em> and click <em>Next</em></li>
<li>Click <em>Finish</em> to install MDT</li>
</ul>
<p>Another way to install MDT is by downloading a zip file, unzip it locally and point the Eclipse to the unpacked directory.</p>
<ul>
<li>Download the latest zip file from <a href="https://www.ida.liu.se/labs/pelab/modelica/OpenModelica/MDT/releases">here</a></li>
<li>The zip file will unpack to a local directory called "mdt"</li>
<li>Start Eclipse, then go Help-&gt;Software Updates...</li>
<li>Add the "mdt" directory as a local site (this is different from version to version) and then install the latest version of MDT from this local site.</li>
</ul>
<h2>Contributing</h2>
<p>A <a href="https://trac.openmodelica.org/MDT">trac system </a>is available for MDT, please contribute by reporting bugs.</p>
<p>Modelica Development Tooling (MDT) is part of <a href="https://openmodelica.org">OpenModelica</a> and is free software distributed under the <a href="/useresresources/license">OSMC-PL License</a>.<br /> This basically means you can do whatever you want with it non-commercially.<br /> To use it comercially you need to be a member of the <a href="/home/consortium">Open Source Modelica Consortium</a>.<br /> Please, help us improve! Download the tool and <a href="https://trac.openmodelica.org/OpenModelica">report bugs</a>, or, even better, take the<br /> source and implement something you always wanted, and contribute it to the MDT!</p>
<h2>Source code</h2>
<p>You can access the source code from the project's repository at <a href="https://openmodelica.org/svn/MDT/trunk">https://openmodelica.org/svn/MDT/trunk</a>.<br /> Anonymous read access is not enabled. You must use user: <strong>anonymous</strong> password: <strong>none</strong>.</p>
<h2>Documentation</h2>
<p>The primary source of information for the aspiring MDT developer is the <a href="https://openmodelica.org/svn/MDT/trunk/docs">MDT documentation</a>. <br /> The manual has information on code repository structure, how to build the package<br /> and other important information. To checkout the manual and other documentation type:</p>
<pre>svn co https://openmodelica.org/svn/MDT/trunk/docs user: anonymous pass: none </pre>
<h2>News</h2>
<p><em>Thursday, 12 July 2012</em></p>
<p>A Trac project management system for reporting bugs and follow development is now <a href="https://trac.openmodelica.org/MDT">available</a>.</p>
<p><em>Monday, 30 January 2012</em><br />Version 0.7.22 has been released.<br />For this release, you can use the&nbsp;<a href="https://www.openmodelica.org" style="color: #1b57b1; text-decoration: none; font-weight: normal;">OpenModelica</a> compiler.</p>
<p><em>Tuesday, 12 April 2011</em><br />Version 0.7.7 has been released.<br />For this release, you can use the&nbsp;<a href="https://www.openmodelica.org" style="color: #1b57b1; text-decoration: none; font-weight: normal;">OpenModelica</a> compiler.</p>
<p><span style="color: red;"><em>Saturday, 01 November 2009</em></span><br /> A short document on <a href="https://trac.openmodelica.org/documents/MDT/install/">MDT installation HowTo</a>.</p>
<p><span style="color: red;"><em>Saturday, 04 October 2009</em></span><br /> We have a new website for ModelicaML - A UML Profile for Modelica.</p>
<p><em>Saturday, 01 March 2008</em><br /> Subversion repository moved to: <a href="https://openmodelica.org/svn/MDT/">https://openmodelica.org/svn/MDT/</a></p>
<p><em>Tuesday, 21 August 2007</em></p>
<p>Version 0.7.2 has been released.</p>
<p>For this release, you can use the <a href="https://openmodelica.org">OpenModelica</a> compiler.</p>
<p>this MDT does not work with OpenModelica less than 1.4.3</p>
<p>Matching parentheses are highlighted.</p>
<h2>Contact</h2>
<p>If you want to contact the current author and maintainer of MDT send an email to <a href="https://www.ida.liu.se/%7Eadrpo">Adrian Pop</a> [<a href="mailto:Adrian.Pop@liu.se">Adrian.Pop@liu.se</a>].
<!--
<br /> The MDT authors can be contacted via: <a href="mailto:x05elmja%20at%20ida%20dot%20liu%20dot%20se"><img src="https://www.ida.liu.se/labs/pelab/modelica/OpenModelica/MDT/boris.png" alt="" border="0" /></a> or <a href="mailto:x05andre%20at%20ida%20dot%20liu%20dot%20se"><img src="https://www.ida.liu.se/labs/pelab/modelica/OpenModelica/MDT/remar.png" alt="" border="0" /></a>. -->
<br /> Bug reports, patches, general feed back or anything else is welcome.</p>
<h3>Updates</h3>
<p>Latest update: <span style="color: red;">2015-05-05 12:58</span>&nbsp;by <a href="https://www.ida.liu.se/%7Eadrpo">Adrian Pop</a></p>
