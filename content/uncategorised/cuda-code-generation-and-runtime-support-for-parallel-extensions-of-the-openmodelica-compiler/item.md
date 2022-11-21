---
title: "CUDA Code Generation and Runtime Support for Parallel Extensions of the OpenModelica Compiler."
---
<!--StartFragment-->

<p class="MsoTitle">
  <span style="font-size: 19px;">Target architecture: NVIDIA Tesla M2050 GPU (Fermi): 2 teraflop GPU</span>
</p>

<p class="Author">
  <span style="mso-ansi-language: EN-US;">Contact: Peter Fritzson (<a href="mailto:peter.fritzson@liu.se">peter.fritzson@liu.se</a>, tel: 0708-281484) <br /> or Mahder Gebremedhin (<a href="mailto:mahder.gebremedhin@liu.se">mahder.gebremedhin@liu.se</a>, tel: 0760831822)<br /> PELAB – Programming Environment Lab, Institutionen för Datavetenskap<br /> </span><span style="font-family: &quot;Courier New&quot;; mso-ansi-language: EN-US;">www.openmodelica.org</span><span style="mso-ansi-language: EN-US;"></span>
</p>

<p class="MsoBodyText">
  <span style="font-size: 12.0pt;">PELAB, together with the Open Source Modelica Consortium (an international open source effort supported by 38 organizations, see www.openmodelica.org) the OpenModelica environment including the OpenModelica Compiler (OMC) of the Modelica language including MetaModelica extensions is developed. The development is open source under the OSMC-PL and GNU V3 licenses.</span>
</p>

<p class="MsoBodyText">
  <span style="font-size: 12.0pt;">Currently OMC compiles Modelica/MetaModelica into C-code via several optimizing steps. The development is supported by an Eclipse plug-in MDT (Modelica Development Tooling), also including a debugger, and a template language already used for developing code generators to C and C#. </span>
</p>

<p class="MsoBodyText">
  <span style="font-size: 12.0pt;">There has earlier been developed several parallel code generator prototypes for the OpenModelica compiler. Some of these are related to automatic parallelization and code generation while others focused on explicit parallelization and code generation.</span>
</p>

<p class="MsoBodyText">
  <span style="font-size: 12.0pt;">The most recent work was resulted in OpenCL/CUDA style explicit parallel programming extensions for the OpenModelica compiler to achieve data parallelism on modern GPGPUs. For example a new parallel for loop that distributes its computations across GPU processors and cores has been implemented. In addition support has been added for the different memory locations of the OpenCL memory model (data-parallel variables with different characteristics), OpenCL kernel functions and OpenCL parallel functions. This implementation generates OpenCL code for the parallel extensions. </span>
</p>

<p class="MsoBodyText">
  <span style="font-size: 12.0pt;">The goal of this master thesis project is to improve the currently available extensions and to add CUDA code generation and runtime support for these new explicit parallel programming constructs in order to achieve speedups on NVIDIA GPUs. For example the parallel for loop mentioned earlier should be adapted to operate with CUDA, CUDA kernel functions should be supported etc.</span>
</p>

<p class="MsoBodyText">
  <span style="font-size: 12.0pt;">If there is time, support for NVIDA’s BLAS (Basic Linear Algebra Subprograms) implementation, CUBLAS will be added to the OpenModelica compiler as an option to the currently available sequential FORTRAN LAPACK interface.</span>
</p>

<p class="MsoBodyTextIndent">
  <span style="font-size: 12.0pt;"> </span>
</p>

<p class="MsoBodyText">
  <span style="font-size: 12.0pt;">The master thesis project requires knowledge of compiler construction, parallel programming, as well as some experience and interest in advanced programming.</span>
</p>

<p class="MsoBodyText">
   
</p>


  


<p class="MsoBodyText">
  References:
</p>

<p class="Reference" style="text-align: left; mso-list: l0 level1 lfo1;" align="left">
  <span style="mso-list: Ignore;">[1]<span style="font: 7.0pt &quot;Times New Roman&quot;;"> </span></span>Mahder Gebremedhin. ParModelica: Extending the Algorithmic Subset of Modelica with Explicit Parallel Language Constructs for Multi-core Simulation. Master thesis 2011.
</p>

<p class="Reference" style="margin-top: 0cm; mso-list: none;">
  <span style="mso-ansi-language: EN;" lang="EN"><span style="mso-spacerun: yes;"> </span>http://liu.diva-portal.org/smash/record.jsf?searchId=1&pid=diva2:451473.</span>
</p>

<p class="Reference" style="mso-list: l0 level1 lfo1;">
  <span style="mso-list: Ignore;">[2]<span style="font: 7.0pt &quot;Times New Roman&quot;;"> </span></span>Afshin Hemmati Moghadam, "Modelica PARallel benchmark suite (MPAR) - a test suite for evaluating the performance of parallel simulations of Modelica models," Linköping University, Linköping, Sweden, Master Thesis LIU-IDA/LITH-EX-A— 11/042—SE, 2011.<span style="mso-ansi-language: EN;" lang="EN">.</span>
</p>

<p class="Reference" style="text-align: left; mso-list: l0 level1 lfo1;" align="left">
  <span style="mso-list: Ignore;">[3]<span style="font: 7.0pt &quot;Times New Roman&quot;;"> </span></span>Per Östlund. Simulation of Modelica Models on the CUDA Architecture. Master thesis 2010. <span style="mso-ansi-language: EN;" lang="EN">http://urn.kb.se/resolve?urn=urn:nbn:se:liu:diva-52060 .</span>
</p>

<p class="Reference" style="mso-list: l0 level1 lfo1;">
  <span style="mso-list: Ignore;">[4]<span style="font: 7.0pt &quot;Times New Roman&quot;;"> </span></span><span style="mso-ansi-language: SV;" lang="SV">Hans Zima and Barbara Chapman. </span>Supercompilers for parallel and vector computers . http://portal.acm.org/citation.cfm?id=89627.
</p>

<p class="Reference" style="mso-list: l0 level1 lfo1;">
  <span style="mso-list: Ignore;">[5]<span style="font: 7.0pt &quot;Times New Roman&quot;;"> </span></span>Peter Aronsson. Automatic Parallelization of Equation-Based Simulation Programs. PhD thesis 2006. <span style="mso-ansi-language: EN;" lang="EN">http://urn.kb.se/resolve?urn=urn:nbn:se:liu:diva-7446.</span>
</p>

<!--EndFragment-->