---
title: "October 31, 2017: OpenModelica 1.12.0 released"
---
<p>The OpenModelica 1.12.0 has been released. You can find the Windows builds&nbsp;<a href="/download/download-windows" target="_blank">here</a>. The Linux and MacOS builds are available via the Download menu above. Release notes in Trac including all the <a href="https://github.com/OpenModelica/OpenModelica/releases/tag/v1.12.0">bug fixes</a>.</p>
<p><strong style="color: #222222; line-height: 1.2;"><span style="font-size: 14pt;">OpenModelica 1.12.0 release, October 31, 2017</span></strong></p>
<ul style="font-family: Verdana, Arial, 'Bitstream Vera Sans', Helvetica, sans-serif; font-size: 13px;">
<li>A new (stand-alone) FMI- and TLM-based simulation tool OMSimulator, first version for connected FMUs, TLM objects, Simulink models (via wrappers), Adams models (via wrappers), BEAST models (via wrappers), Modelica models</li>
<li>Graphic configuration editing of composite models consisting of FMUs</li>
<li>Basic graphical editing support for state machines and transitions</li>
<li>Faster lookup processing, making some libraries faster to browse and compile</li>
<li>Additional advanced visualization features for multibody animation</li>
<li>Increased library coverage including significantly increased verification coverage</li>
<li>Increased tool interoperability by addition of the ZeroMQ communications protocol</li>
<li>Further enhanced OMPython including linearization, now also working with Python 3</li>
<li>Support for RedHat/Fedora binary builds of OpenModelica</li>
</ul>
<h2 id="OpenModelicaCompilerOMC" style="font-family: Arial, Verdana, 'Bitstream Vera Sans', Helvetica, sans-serif; font-weight: bold; letter-spacing: -0.018em; break-after: avoid; font-size: 16px; margin-left: -18px; border-bottom: 1px solid #dddddd; box-shadow: #f2f2f2 0.1em 0.4em 0.7em 0px; padding: 0.2em 0.3em 0.1em; color: #000000;">OpenModelica Compiler (OMC)<a class="anchor" href="https://github.com/OpenModelica/OpenModelica/releases/tag/v1.12.0#OpenModelicaCompilerOMC" title="Link to this section" style="color: #d7d7d7; border: none; font-size: 0.8em; vertical-align: text-top; visibility: hidden;"></a></h2>
<ul style="font-family: Verdana, Arial, 'Bitstream Vera Sans', Helvetica, sans-serif; font-size: 13px;">
<li>Faster lookup processing</li>
<li>Initializing external objects together with parameters</li>
<li>Handle exceptions in numeric solvers</li>
<li>Support for higher-index discrete clock partitions</li>
<li>Improved unit checking</li>
<li>Improved initialization of start values</li>
<li>Decreased compilation time of models with large size arrays</li>
<li>New approach for homotopy-based initialization (still experimental)</li>
<li>A bunch of fixes: Bugs, regressions, performance issues</li>
<li>Improved Dynamic Tearing by adding constraints for the casual set</li>
<li>Improved module wrapFunctionCalls with one-time evaluation of Constant CSE-variables</li>
<li>Added initOptModule for inlineHomotopy</li>
<li>Added configuration flag tearingStrictness to influence solvability</li>
<li>New methods for inline integration for continuous equations in clocked partitions, now covering: ExplicitEuler, ImplicitEuler, SemiImplicitEuler and ImplicitTrapezoid</li>
<li>Complete implementation of synchronous features in C++ runtime</li>
<li>Refactored linear solver of C++ runtime</li>
<li>Improved Modelica_synchronous_cpp coverage</li>
<li>New common linear solver module, optionally sparse, for the C++ runtime</li>
<li>Coverage of most of the OpenHydraulics library</li>
<li>Improved coverage of ThermoSysPro, IdealizedContact and Chemical libraries</li>
<li>Support of time events for cpp-simulation and enabled time events in cpp-FMUs</li>
<li>Global homotopy method for initialization</li>
<li>Scripting API to compute accumulated errors (1-norm, 2-norm, max. error) of 2 time series</li>
</ul>
<h2 id="GraphicEditorOMEdit" style="font-family: Arial, Verdana, 'Bitstream Vera Sans', Helvetica, sans-serif; font-weight: bold; letter-spacing: -0.018em; break-after: avoid; font-size: 16px; margin-left: -18px; border-bottom: 1px solid #dddddd; box-shadow: #f2f2f2 0.1em 0.4em 0.7em 0px; padding: 0.2em 0.3em 0.1em; color: #000000;">Graphic Editor OMEdit<a class="anchor" href="https://github.com/OpenModelica/OpenModelica/releases/tag/v1.12.0#GraphicEditorOMEdit" title="Link to this section" style="color: #d7d7d7; border: none; font-size: 0.8em; vertical-align: text-top; visibility: hidden;"></a></h2>
<ul style="font-family: Verdana, Arial, 'Bitstream Vera Sans', Helvetica, sans-serif; font-size: 13px;">
<li>Additional advanced visualization features for multibody animation (transparency, textures, change colours by dialog)</li>
<li>An HTML WYSIWYG Editor, e.g. useful for documentation</li>
<li>Support for choices(checkBox=true) annotation.</li>
<li>Support for loadSelector &amp; saveSelector attribute of Dialog annotation.</li>
<li>Panning of icon/diagram view and plot window.</li>
<li>AutoComplete feature in text editing for keywords, types, common Modelica constructs</li>
<li>Follow connector transformation from Diagram View to Icon View.</li>
<li>Further stability improvements</li>
<li>Improved performance for rendering some icons using the interactive API</li>
<li>Improved handling of parameters that cannot be evaluated in Icon annotations</li>
<li>Basic graphic editing support for state machines and transitions (not yet support for showing state internals on diagram layer)</li>
<li>Interactive state manipulation for FMU-based animations</li>
</ul>
<h2 id="FMISupport" style="font-family: Arial, Verdana, 'Bitstream Vera Sans', Helvetica, sans-serif; font-weight: bold; letter-spacing: -0.018em; break-after: avoid; font-size: 16px; margin-left: -18px; border-bottom: 1px solid #dddddd; box-shadow: #f2f2f2 0.1em 0.4em 0.7em 0px; padding: 0.2em 0.3em 0.1em; color: #000000;">FMI Support<a class="anchor" href="https://github.com/OpenModelica/OpenModelica/releases/tag/v1.12.0#FMISupport" title="Link to this section" style="color: #d7d7d7; border: none; font-size: 0.8em; vertical-align: text-top; visibility: hidden;"></a></h2>
<ul style="font-family: Verdana, Arial, 'Bitstream Vera Sans', Helvetica, sans-serif; font-size: 13px;">
<li>A new (stand-alone) FMI- and TLM-based simulation tool OMSimulator, first version (a main deliverable of the OPENCPS project, significant contributions and code donations from SKF)</li>
<li>Graphic configuration editing of composite models consisting of FMUs</li>
<li>Co-simulation/simulation of connected FMUs, TLM objects, Simulink models (via wrappers), Adams models (via wrappers), BEAST models (via wrappers), Modelica models.</li>
</ul>
<h2 id="Otherthings" style="font-family: Arial, Verdana, 'Bitstream Vera Sans', Helvetica, sans-serif; font-weight: bold; letter-spacing: -0.018em; break-after: avoid; font-size: 16px; margin-left: -18px; border-bottom: 1px solid #dddddd; box-shadow: #f2f2f2 0.1em 0.4em 0.7em 0px; padding: 0.2em 0.3em 0.1em; color: #000000;">Other things<a class="anchor" href="https://github.com/OpenModelica/OpenModelica/releases/tag/v1.12.0#Otherthings" title="Link to this section" style="color: #d7d7d7; border: none; font-size: 0.8em; vertical-align: text-top; visibility: hidden;"></a></h2>
<p>&nbsp;</p>
<ul style="font-family: Verdana, Arial, 'Bitstream Vera Sans', Helvetica, sans-serif; font-size: 13px;">
<li>Increased OpenModelica tool interoperability by adding the ZeroMQ communications protocol in addition to the previously available Corba. This also enables Python 3 usage in OMPython on all platforms.</li>
<li>Textual support through the OpenModelica API and graphical support in OMEdit for generation of single or multiple requirement verification scenarios</li>
<li>VVDRlib – a small library for connecting requirements and models together, with notions for mediators, scenarios, design alternatives</li>
<li>Further enhanced OMPython including linearization, now also working with Python 3.¨</li>
<li>Jupyter notebooks also supported with OMPython and Python 3</li>
<li>New enhanced library testing script (libraries.openmodelica.org/branches).</li>
<li>Addition of mutable reference data types in MetaModelica</li>
<li>Support for RedHat/Fedora binary builds of OpenModelica</li>
<li>Support for exporting the system of equations in GraphML (yEd) format for debugging</li>
</ul>
<div id="_mcePaste" class="mcePaste" data-mce-bogus="1" style="position: absolute; left: 0px; top: -25px; width: 1px; height: 1px; overflow: hidden;">
<p class="BulletItem" style="margin-left: .5in; text-indent: -.25in; line-height: 13.0pt; mso-line-height-rule: exactly; mso-list: l0 level1 lfo2; tab-stops: list .5in;"><span lang="EN-US" style="font-size: 10.0pt; mso-bidi-font-size: 12.0pt; font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol;"><span style="font-variant-numeric: normal; font-stretch: normal; font-size: 7pt; line-height: normal; font-family: 'Times New Roman';">&nbsp;&nbsp;</span></span><!--[endif]--><span lang="EN-US">Support for higher-index discrete clock partitions<o:p></o:p></span></p>
<p class="BulletItem" style="margin-left: .5in; text-indent: -.25in; line-height: 13.0pt; mso-line-height-rule: exactly; mso-list: l0 level1 lfo2; tab-stops: list .5in;"><!--[if !supportLists]--><span lang="EN-US" style="font-size: 10.0pt; mso-bidi-font-size: 12.0pt; font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol;">·<span style="font-variant-numeric: normal; font-stretch: normal; font-size: 7pt; line-height: normal; font-family: 'Times New Roman';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><!--[endif]--><span lang="EN-US">Improved unit checking<o:p></o:p></span></p>
<p class="BulletItem" style="margin-left: .5in; text-indent: -.25in; line-height: 13.0pt; mso-line-height-rule: exactly; mso-list: l0 level1 lfo2; tab-stops: list .5in;"><!--[if !supportLists]--><span lang="EN-US" style="font-size: 10.0pt; mso-bidi-font-size: 12.0pt; font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol;">·<span style="font-variant-numeric: normal; font-stretch: normal; font-size: 7pt; line-height: normal; font-family: 'Times New Roman';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><!--[endif]--><span lang="EN-US">Improved initialization of start values<o:p></o:p></span></p>
<p class="BulletItem" style="margin-left: .5in; text-indent: -.25in; line-height: 13.0pt; mso-line-height-rule: exactly; mso-list: l0 level1 lfo2; tab-stops: list .5in;"><!--[if !supportLists]--><span lang="EN-US" style="font-size: 10.0pt; mso-bidi-font-size: 12.0pt; font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol;">·<span style="font-variant-numeric: normal; font-stretch: normal; font-size: 7pt; line-height: normal; font-family: 'Times New Roman';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><!--[endif]--><span lang="EN-US">New approach for homotopy-based&nbsp; initialization (still experimental)<o:p></o:p></span></p>
<p class="BulletItem" style="margin-left: .5in; text-indent: -.25in; line-height: 13.0pt; mso-line-height-rule: exactly; mso-list: l0 level1 lfo2; tab-stops: list .5in;"><!--[if !supportLists]--><span lang="EN-US" style="font-size: 10.0pt; mso-bidi-font-size: 12.0pt; font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol;">·<span style="font-variant-numeric: normal; font-stretch: normal; font-size: 7pt; line-height: normal; font-family: 'Times New Roman';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><!--[endif]--><span lang="EN-US">A bunch of fixes: Bugs, regressions, performance issues<o:p></o:p></span></p>
<p class="BulletItem" style="margin-left: .5in; text-indent: -.25in; line-height: 13.0pt; mso-line-height-rule: exactly; mso-list: l0 level1 lfo2; tab-stops: list .5in;"><!--[if !supportLists]--><span lang="EN-US" style="font-size: 10.0pt; mso-bidi-font-size: 12.0pt; font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol;">·<span style="font-variant-numeric: normal; font-stretch: normal; font-size: 7pt; line-height: normal; font-family: 'Times New Roman';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><!--[endif]--><span lang="EN-US">Improved Dynamic Tearing by adding constraints for the casual set<o:p></o:p></span></p>
<p class="BulletItem" style="margin-left: .5in; text-indent: -.25in; line-height: 13.0pt; mso-line-height-rule: exactly; mso-list: l0 level1 lfo2; tab-stops: list .5in;"><!--[if !supportLists]--><span lang="EN-US" style="font-size: 10.0pt; mso-bidi-font-size: 12.0pt; font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol;">·<span style="font-variant-numeric: normal; font-stretch: normal; font-size: 7pt; line-height: normal; font-family: 'Times New Roman';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><!--[endif]--><span lang="EN-US">Improved module wrapFunctionCalls with one-time evaluation of Constant CSE-variables<o:p></o:p></span></p>
<p class="BulletItem" style="margin-left: .5in; text-indent: -.25in; line-height: 13.0pt; mso-line-height-rule: exactly; mso-list: l0 level1 lfo2; tab-stops: list .5in;"><!--[if !supportLists]--><span lang="EN-US" style="font-size: 10.0pt; mso-bidi-font-size: 12.0pt; font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol;">·<span style="font-variant-numeric: normal; font-stretch: normal; font-size: 7pt; line-height: normal; font-family: 'Times New Roman';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><!--[endif]--><span lang="EN-US">Added initOptModule for inlineHomotopy<o:p></o:p></span></p>
<p class="BulletItem" style="margin-left: .5in; text-indent: -.25in; line-height: 13.0pt; mso-line-height-rule: exactly; mso-list: l0 level1 lfo2; tab-stops: list .5in;"><!--[if !supportLists]--><span lang="EN-US" style="font-size: 10.0pt; mso-bidi-font-size: 12.0pt; font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol;">·<span style="font-variant-numeric: normal; font-stretch: normal; font-size: 7pt; line-height: normal; font-family: 'Times New Roman';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><!--[endif]--><span lang="EN-US">Added configuration flag tearingStrictness to influence solvability<o:p></o:p></span></p>
<p class="BulletItem" style="margin-left: .5in; text-indent: -.25in; line-height: 13.0pt; mso-line-height-rule: exactly; mso-list: l0 level1 lfo2; tab-stops: list .5in;"><!--[if !supportLists]--><span lang="EN-US" style="font-size: 10.0pt; mso-bidi-font-size: 12.0pt; font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol;">·<span style="font-variant-numeric: normal; font-stretch: normal; font-size: 7pt; line-height: normal; font-family: 'Times New Roman';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><!--[endif]--><span lang="EN-US">New methods for inline integration for continuous equations in clocked partitions, now covering: ExplicitEuler, ImplicitEuler, SemiImplicitEuler and ImplicitTrapezoid<o:p></o:p></span></p>
<p class="BulletItem" style="margin-left: .5in; text-indent: -.25in; line-height: 13.0pt; mso-line-height-rule: exactly; mso-list: l0 level1 lfo2; tab-stops: list .5in;"><!--[if !supportLists]--><span lang="EN-US" style="font-size: 10.0pt; mso-bidi-font-size: 12.0pt; font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol;">·<span style="font-variant-numeric: normal; font-stretch: normal; font-size: 7pt; line-height: normal; font-family: 'Times New Roman';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><!--[endif]--><span lang="EN-US">Complete implementation of synchronous features in Cpp runtime<o:p></o:p></span></p>
<p class="BulletItem" style="margin-left: .5in; text-indent: -.25in; line-height: 13.0pt; mso-line-height-rule: exactly; mso-list: l0 level1 lfo2; tab-stops: list .5in;"><!--[if !supportLists]--><span lang="EN-US" style="font-size: 10.0pt; mso-bidi-font-size: 12.0pt; font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol;">·<span style="font-variant-numeric: normal; font-stretch: normal; font-size: 7pt; line-height: normal; font-family: 'Times New Roman';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><!--[endif]--><span lang="EN-US">Refactored linear solver of Cpp runtime<o:p></o:p></span></p>
<p class="BulletItem" style="margin-left: .5in; text-indent: -.25in; line-height: 13.0pt; mso-line-height-rule: exactly; mso-list: l0 level1 lfo2; tab-stops: list .5in;"><!--[if !supportLists]--><span lang="EN-US" style="font-size: 10.0pt; mso-bidi-font-size: 12.0pt; font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol;">·<span style="font-variant-numeric: normal; font-stretch: normal; font-size: 7pt; line-height: normal; font-family: 'Times New Roman';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><!--[endif]--><span lang="EN-US">Improved Modelica_synchronous_cpp coverage<o:p></o:p></span></p>
<p class="BulletItem" style="margin-left: .5in; text-indent: -.25in; line-height: 13.0pt; mso-line-height-rule: exactly; mso-list: l0 level1 lfo2; tab-stops: list .5in;"><!--[if !supportLists]--><span lang="EN-US" style="font-size: 10.0pt; mso-bidi-font-size: 12.0pt; font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol;">·<span style="font-variant-numeric: normal; font-stretch: normal; font-size: 7pt; line-height: normal; font-family: 'Times New Roman';">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span><!--[endif]--><span lang="EN-US">Coverage of most of the OpenHydraulics library<o:p></o:p></span></p>
<span lang="EN-GB" style="font-size: 11.0pt; mso-bidi-font-size: 12.0pt; font-family: 'Times New Roman',serif; mso-fareast-font-family: 'Times New Roman'; mso-ansi-language: EN-GB; mso-fareast-language: EN-US; mso-bidi-language: AR-SA;">Support of time events for cpp-simulation and enabled time events in cpp-FMUs</span></div>