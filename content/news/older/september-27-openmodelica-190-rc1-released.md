---
title: "September 27, 2013: OpenModelica 1.9.0 RC1 released"
---
<p>The OpenModelica 1.9.0 RC1 has been released. You can find the Windows builds&nbsp;<a href="https://build.openmodelica.org/omc/builds/windows/releases/1.9.0/RC1/" target="_blank">here</a>. The Linux and MacOS builds are available via the Download menu above.</p>
<p>Many thanks to everybody who contributed!</p>
<h1><span lang="SV">A.1<span style="font: 7pt;"> </span></span><span lang="SV">OpenModelica 1.9.0 RC1, September 2013</span></h1>
<p>The three most important enhancements in the OpenModelica 1.9.0 release:</p>
<ul>
<li>OpenModelica compiler support for most of the Fluid library.</li>
<li>Support for the significantly updated library MSL 3.2.1 final version.</li>
<li>Significantly enhanced graphical user interface in OMEdit.</li>
</ul>
<div>New features: integration of the PySimulator analysis package; Dynamic Optimization with CasADi.</div>
<h2><span lang="SV">A.1.1<span style="font: 7pt;"> </span></span><span lang="SV">OpenModelica Compiler (OMC)</span></h2>
<p>This release mainly includes improvements of the OpenModelica Compiler (OMC), including, but not restricted to the following:</p>
<ul>
<li>A more stable and complete OMC model compiler. The 1.9.0 final version simulates many more models than the previous 1.8.1 version and OpenModelica 1.9.0 beta versions.</li>
<li>Much better simulation support for MSL 3.2.1, now 268 out of 274 example models compile (98%) and 240 (88%) simulate, compared to 30% simulating in the 1.9.0 beta1 release.</li>
<li>Much better simulation for the ModelicaTest 3.2.1 library, now 400 out of 428 models simulate (93%), compared to 32% in November 2012.</li>
<li>Improved tearing algorithm for the compiler backend. Tearing is by default used.</li>
<li>Much faster matching and dynamic state selection algorithms for the compiler backend.</li>
<li>New index reduction algorithm implementation.</li>
<li>New default initialization method that symbolically solves the initialization problem much faster and more accurately. This is the first version that in general initialize hybrid models correctly.</li>
<li>Better class loading from files. The package.order file is now respected and the file structure is more thoroughly examined.</li>
<li>Basic support for pure/impure functions.</li>
<li>It is now possible to translate the error messages in the omc kernel.</li>
<li>Enhanced ModelicaML version with support for value bindings in requirements-driven modeling available for the latest Eclipse and Papyrus versions. GUI specific adaptations. Automated model composition workflows (used for model-based design verification against requirements) are modularized and have improved in terms of performance.</li>
<li>FMI for co-simulation with OMC as master. Improved FMI import/export, model exchange.</li>
<li>Checking (when possible) that variables have been assigned to before they are used in algorithmic code.</li>
<li>Full version of Python scripting.</li>
<li>3D graphics visualization using the Modelica3D library.</li>
<li>The PySimulator package from DLR for additional analysis is integrated with OpenModelica (see Modelica2012 paper), and included in the OpenModelica distribution.</li>
<li>Prototype support for uncertainty computations, special feature enabled by special flag.</li>
<li>Parallel algorithmic Modelica support (ParModelica) for efficient portable parallel algorithmic programming based on the OpenCL standard, for CPUs and GPUs.</li>
<li>Support for optimization of semiLinear according to MSL 3.3 chapter 3.7.2.5 semiLinear.</li>
</ul>
<h2><span lang="SV">A.1.2<span style="font: 7pt;"> </span></span><span lang="SV">OpenModelica Notebook (OMNotebook)</span></h2>
<ul>
<li>The DrModelica interactive document has been updated and the models tested. Almost all models now simulate with OpenModelica.</li>
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
<li>General GUI: backward and forward navigation support in Documentation view, enhanced parameters window with support for Dialog annotation. Most of the images are converted from raster to vector graphics i.e PNG to SVG.</li>
<li>Libraries Browser: better loading of libraries, library tree can now show protected classes, show library items class names as middle ellipses if the class name text is larger, more options via the right click menu for quick usage.</li>
<li>ModelWidget: add the partial class as a replaceable component, look for the default component prefixes and name when adding the component.</li>
<li>GraphicsView: coordinate system manipulation for icon and diagram layers. Show red box for models that do not exist. Show default graphical annotation for the components that doesn’t have any graphical annotations. Better resizing of the components. Properties dialog for primitive shapes i.e Line, Polygon, Rectangle, Ellipse, Text and Bitmap.</li>
<li>File Opening: open one or more Modelica files, allow users to select the encoding while opening the file, convert files to UTF-8 encoding, allow users to open the OpenModelica result files.</li>
<li>Variables Browser: find variables in the variables browser, sorting in the variables browser.</li>
<li>Plot Window: clear all curves of the plot window, preserve the old selected variable and update its value with the new simulation result.</li>
<li>Simulation: support for all the simulation flags, read the simulation output as soon as is is obtained, output window for simulations, options to set matching algorithm and index reduction method for simulation. Display all the files generated during the simulation is now supported. Options to set OMC command line flags.</li>
<li>Options: options for loading libraries via loadModel and loadFile each time GUI starts, save the last open file directory location, options for setting line wrap mode and syntax highlighting.</li>
<li>Modelica Text Editor: preserving user customizations, new search &amp; replace functionality, support for comment/uncomment.</li>
<li>Notifications: show custom dialogs to users allowing them to choose whether they want to see this dialog again or not.</li>
<li>Model Creation: Better support for creating new classes. Easy creation of extends classes or nested classes.</li>
<li>Messages Widget: Multi line error messages are now supported.</li>
<li>Crash Detection: The GUI now automatically detects the crash and writes a stack trace file. The user is given an option to send a crash report along with the stack trace file and few other useful files via email.</li>
<li>Autosave: OMEdit saves the currently edited model regularly, in order to avoid losing edits after GUI or compiler crash. The save interval can be set in the Options menu.</li>
</ul>
<h2><span lang="SV">A.1.7<span style="font: 7pt;"> </span></span><span lang="SV">Optimization</span></h2>
<ul>
<li>Dynamic optimization with XML export to the CaSAdi package is now integrated with OpenModelica. Moreover, a native integrated Dynamic Optimization prototype using Ipopt is now in the OpenModelica release, but currently needs a special flag to be turned on since it needs more testing and refinement before being generally made available.</li>
</ul>
<h2><span lang="SV">A.1.8<span style="font: 7pt;"> </span></span><span lang="SV">FMI Support</span></h2>
<ul>
<li>FMI co-simulation with OpenModelica as master. Improved FMI Import and export for model exchange. Simulation of multiple instances of the FMU is now possible. Partial support for FMI 2.0 model exchange.</li>
</ul>