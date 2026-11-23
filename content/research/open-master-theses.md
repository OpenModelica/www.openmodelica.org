---
title: "Open Master Theses"
date: 2022-12-12
---

These projects are suitable for students with skill and interest in advanced programming.\
If you are interested in one of the projects, please send a copy of your CV and course transcript, to the contacts indicated for the project you are interested in.

## Compiler Construction

### Package manager

We currently have a package manager in OpenModelica generating and using this [index file](https://libraries.openmodelica.org/index/v1/index.json).

However, the OMEdit GUI integration needs to be improved and new features are necessary (such as proper dependency resolution). This work is probably suitable for a 15/16 ECTS thesis.

Contact: [Martin Sjölund](https://www.ida.liu.se/~marsj34/)

### Investigating the language server protocol in the context of declarative Equation-Oriented languages

This thesis project aims to investigate language servers in the context of simulation tools. We are interested in examining if there are any domain-specific difficulties in this context compared to other domains. Based on existing empiric knowledge and interviews with experts in simulation tools, we hope that you can investigate what guidelines and experiences are to be gained when examining language servers in the context equation oriented languages.

Contact: [John Tinnerholm](mailto:john.tinnerholm@liu.se)

### Julia integration

There is ongoing work to translate our MetaModelica code to Julia code. We have many ideas on what this could be used for, including JIT-compiling Julia code instead of generating C-code or using our own slow function interpreter. Contact us for our current thoughts and ideas of formulating a thesis for this.

Contact: [Martin Sjölund](https://www.ida.liu.se/~marsj34/) or [](https://www.ida.liu.se/department/contact/search.en.shtml?NAME=lena)[Peter Fritzson](https://www.ida.liu.se/%7Epetfr/) or [Adrian Pop](https://www.ida.liu.se/%7Eadrpo/)

**Efficient and correct handling of arrays**

The current handling of arrays in OpenModelica achieves somewhat good performance, but it does so by scalarizing arrays into individual operations. A simple array operation like x = {1,2,3} + {4,5,6} will thus become x\[1\] = 1+4, x\[2\] = 2+5, etc. For large arrays, this causes lots of C-code to be emitted and compilation speed can grow to minutes (or more for very large arrays) for something that can efficiently be compiled as a simple for-loop. Work is ongoing to preserve these array operations and OpenModelica has functions in a C runtime for this void add_real_array(const real_array_t \*a,const real_array_t \*b,real_array_t\* dest), but the code generator is not advanced enough to utlize these functions (it allocates temporary arrays in many cases). The topic of this thesis would be to enhance the code generator to avoid memory allocations as much as possible (including possibly re-using memory of temporary arrays in arrX \* arrY + arrZ) and to rewrite the runtime code for arrays (there is one implementation for integers, reals, booleans, records, etc) possibly by simply writing the C-code for them directly instead of having a C-file with the implementations.

Contact: [Martin Sjölund](https://www.ida.liu.se/~marsj34/) or [](https://www.ida.liu.se/department/contact/search.en.shtml?NAME=lena)[Peter Fritzson](https://www.ida.liu.se/%7Epetfr/) or [Adrian Pop](https://www.ida.liu.se/%7Eadrpo/)

**Prototype Implementation and Evaluation of a Model Equation Reduction Method (new, September-2016)**

**[Click for more details](/open-theses/Ausschreibungen_MER-Evalutation.pdf)**

**Efficient IR for the OpenModelica Compiler (2 theses finished on this topic)**

The master thesis project should develop a new IR for OpenModelica for more efficient code generation. While introducing a more efficient IR, it would also be advisable to make certain operations more efficient. This includes some optimizations such as dead code / use of uninitialized variables that are currently performed elsewhere in the compiler. One of the other gains would be to make interpretation of functions more efficient.

[Click for more details](/open-theses/2016_Efficient_IR_for_OpenModelica_compiler_v1.pdf)\
Contact: [Martin Sjölund](https://www.ida.liu.se/~marsj34/) or [](https://www.ida.liu.se/department/contact/search.en.shtml?NAME=lena)[Peter Fritzson](https://www.ida.liu.se/%7Epetfr/) or [Lena Buffoni](https://www.ida.liu.se/department/contact/search.en.shtml?NAME=Lena+Buffoni)

### Type Inferencing and Python to Modelica Translation

The goal of this master thesis project is to design and implement a Python to Modelica translator including type inferencing techniques to infer types in dynamically typed Python programs to be used in statically typed Modelica programs. This also includes inferencing shapes of array types. The goal is to be able to call translated Python programs from Modelica. The implementation approach can with a high probability be built on the MetaModelica and OMCCp systems.\
[Click for more details.](/open-theses/2012TranslatorPythonToModelica-v1.pdf)\
Contact: [Lena Buffoni](https://www.ida.liu.se/department/contact/search.en.shtml?NAME=Lena+Buffoni) or [Peter Fritzson](https://www.ida.liu.se/%7Epetfr/)

### External Function Interface Python-Modelica

The goal of this master thesis project is to design and implement a Python – Modelica external function interface. It should be possible to call Python programs from Modelica, and Modelica programs from Python. The Modelica side of the external function interface may involve Modelica, MetaModelica, and C programming, whereas the Python side may involve Python and C programming.\
Contact: [Lena Buffoni](https://www.ida.liu.se/department/contact/search.en.shtml?NAME=Lena+Buffoni) or [Peter Fritzson](https://www.ida.liu.se/%7Epetfr/)

### OpenModelica OCAML Code Generator

The goal of this master thesis project is to create one more code generator using the existing C code generators as inspiration. This code generator should generate code for the functional language OCAML.\
[Click for more details](https://www.ida.liu.se/%7Epelab/xjobb/PeterFritzson/2010-OpenModelica-OCAML-codegenerator.pdf)\
Contact: [Adrian Pop](https://www.ida.liu.se/%7Eadrpo/) or [Peter Fritzson](https://www.ida.liu.se/%7Epetfr/)

### OpenModelica Translator to Scicos

The goal of this master thesis is to improve the interoperability of the OpenModelica platform, by implementing export possibility of (Open)Modelica models to to a smaller Modelica subset accepted by Scicos. A transformation module that transforms (Open)Modelica AST to Scicos Modelica AST is needed.\
Contact: [Peter Fritzson](https://www.ida.liu.se/%7Epetfr/)

### Advanced Refactoring for Modelica in Eclipse Plugin (First part finished, second part available)

A refactoring is a transformation of e program that improves its structure and understandbility. Earlier basic refac-toring support in MDT has been developed, including the unique property of preserving comments and indenta-tion. The goal of this master thesis project is to develop several advanced refactorings on top of the basic refactoring functio-nality and apply these refactorings to the 150 000 line OpenModelica compiler.\
[Click for more details](https://www.ida.liu.se/%7Epelab/xjobb/PeterFritzson/2010ModelicaEclipseRefactoring.pdf)\
Contact: [Adrian Pop](https://www.ida.liu.se/%7Eadrpo/) or [Peter Fritzson](https://www.ida.liu.se/%7Epetfr/)

### CUDA Code Generation and Runtime Support for Parallel Extensions of the OpenModelica Compiler

This project centers around code parallelization. The goal is to improve the existing OpenCL/CUDA style explicit programming extensions for the OpenModelica compiler and to add CUDA code generation and runtime support for these new explicit parallel programming constructs in order to achieve speedups on NVIDIA GPUs.\
[Click for more details.](/open-theses/2012ModelicaCUDAParallellization_v1.pdf)\
Contact: [Mahder Gebremedhin](https://www.ida.liu.se/department/contact/contactcard.en.shtml?mahge83) or [Peter Fritzson](https://www.ida.liu.se/%7Epetfr/)

### Parallel Autotuning Compilation for Algorithmic Modelica on Nvidia 2 teraflop 2050 GPU

Currently the Open Modelca Compiler (OMC) compiles Modelica/MetaModelica into C-code via several optimizing steps. There has earlier been developed several parallel code generator prototypes in the OpenModelica system including generation of OpenCL code for Nvidia. However, static compilation schemes sometimes fail to parallelize due to conservative assumptions of dependencies.\
The goal of this master thesis project is to design and implement an efficient parallel autotuning compilation scheme from Modelica to the NVIDIA Fermi GPGPU. The development need not be done from scratch, it can build upon existing implementations.\
[Click for more details.](/open-theses/2012ModelicaParallelAutoTuning%20v1.pdf)\
Contact: [Mahder Gebremedhin](https://www.ida.liu.se/department/contact/contactcard.en.shtml?mahge83), [Lena Buffoni](https://www.ida.liu.se/department/contact/contactcard.en.shtml?olero90) or [Peter Fritzson](https://www.ida.liu.se/%7Epetfr/)

## Graphical User Inferfaces

### Requirement modeling in OMEdit

An extension of Modelica for expressing requirements is being developed. It incudes a new type of relationship between Modelica components, introducing a new level of complexity to Modelica models. In order to simplify the design and visualization od such models we propose to implement different views for displaying and hiding the requirement level of the models. The goal of the thesis is to develop an interface for visualizing the new extensions as well as for hiding them from view when necessary.\
[Click for more details](/open-theses/Assertion%20modeling%20in%20OMEdit.pdf)\
Contact: [Lena Buffoni](https://www.ida.liu.se/department/contact/contactcard.en.shtml?olero90) or [Peter Fritzson](https://www.ida.liu.se/%7Epetfr/)

## ModelicaML

### Moving ModelicaML to a Professional Open-source Project Level

The ModelicaML prototype, which has been developed for the last 4 years, was primarily used as a platform for prototyping new ideas.\
Today ModelicaML implementation has reached a good level of maturity.\
The main objective of this project is to move the ModelicaML implementation to a professional open-source project level.\
[Click for more details](/open-theses/2013_02_modelicaml_product.pdf)\
Contact: [Adrian Pop](https://www.ida.liu.se/%7Eadrpo/) or [Peter Fritzson](https://www.ida.liu.se/%7Epetfr/)

### Design and Implementation of the ModelicaML Support in Papyrus MDT

Modelica Modeling Language (ModelicaML) is a graphical modeling language for the description of time-continuous and time-discrete/event-based system dynamics. ModelicaML is defined as an extended subset of UML. This subset enables the generation of executable Modelica code. Presently, ModelicaML is implemented as a prototype that only supports the obsolete version Papyrus MDT 0.7.4. Based on this prototype, the task of this project is to design and implement the support for ModelicaML for the latest Papyrus version 1.x.\
[Click for more details](/open-theses/2011_Thesis_ModelicaML_migration_to_new_Acceleo%20_v01.pdf)\
Contact: [Adrian Pop](https://www.ida.liu.se/%7Eadrpo/) or [Peter Fritzson](https://www.ida.liu.se/%7Epetfr/)

### FMI Support in ModelicaML (New)

Modelica Modeling Language (ModelicaML) is a graphical modeling language for the description of time-continuous and time-discrete/event-based system dynamics. ModelicaML is defined as an extended subset of UML. This subset enables the generation of executable Modelica code. The main task of this project is enabling the design verification by using models (system component-, scenario- or requirement-models, etc.) that were created in different tools or formalisms and were exported in the FMI format.\
[Click for more details](/open-theses/2013_02_ModelicaML_FMI_support_v01.doc)\
Contact: [Adrian Pop](https://www.ida.liu.se/%7Eadrpo/) or [Peter Fritzson](https://www.ida.liu.se/%7Epetfr/)

### Moving ModelicaML to a Professional, Open-Source Project Level (New)

Modelica Modeling Language (ModelicaML) is a graphical modeling language for the description of time-continuous and time-discrete/event-based system dynamics. ModelicaML is defined as an extended subset of UML. This subset enables the generation of executable Modelica code. The ModelicaML prototype, which has been developed for the last 4 years, was primarily used as a platform for prototyping new ideas. Today ModelicaML implementation has reached a good level of maturity. The main objective of this project is to move the ModelicaML implementation to a professional open-source project level.\
Contact: [Adrian Pop](https://www.ida.liu.se/%7Eadrpo/) or [Peter Fritzson](https://www.ida.liu.se/%7Epetfr/)

## Advanced Applications

### Automatisk Modelica kodgenerering för processimulering (New)

Normal 0 14 false false false IT X-NONE X-NONE MicrosoftInternetExplorer4

Modelica Code generation from configuration application data

PAID WORK

[Click for more details](/open-theses/exjobbfrontwaymodelicakodgenereringv3.pdf)\
Contact: [Anders Nilsson](mailto:anders.nilsson@frontway.se): CEO, Frontway AB

### Development of a high-fidelity non-linear rotorcraft dynamics model using OpenModelica framework

The goal of this master thesis is to develop a high-fidelity non-linear rotorcraft dynamics model using OpenModelica framework for real-time usage under Linux on the LinkQuad platform - a Micro Air Vehicle quadrotor system.

[Click for more details.](/open-theses/2012-UAVHelicopter-OpenModelica-Control-v3.pdf)

Contact: [Lena Buffoni](https://www.ida.liu.se/department/contact/contactcard.en.shtml?olero90) or [Peter Fritzson](https://www.ida.liu.se/%7Epetfr/)</p>
