---
title: "Roadmap"
weight: 3
---

The [milestones on GitHub]({{< param "roadmap" >}}) show the plans for the next releases and their current status.
The [release notes](https://github.com/OpenModelica/OpenModelica/releases) describe what each release contains.

## Releases

| Date | Version | Highlights | Release notes |
|---|---|---|---|
| July 2026 | 1.27.0 | Experimental MCP server in OMEdit for interaction with AI agents. OMEdit uses Qt6 instead of Qt5. State machines supported by the new frontend. Reverse model lookup. More responsive editing of diagrams. | [release notes](https://github.com/OpenModelica/OpenModelica/releases/tag/v1.27.0) |
| December 2025 | 1.26.0 | OMEdit loads and saves models with syntax errors. `break` to remove modifiers and for selective model extension. Less restrictive rules for conditional components. Old deprecated solvers removed in favour of gbode. | [release notes](https://github.com/OpenModelica/OpenModelica/releases/tag/v1.26.0) |
| March 2025 | 1.25.0 | Hierarchical parameter editing, Reload package and Open Class in text view in OMEdit. The old graphical editing mode is dropped. Co-simulation FMUs work with the stiff CVODE solver. | [release notes](https://github.com/OpenModelica/OpenModelica/releases/tag/v1.25.0) |
| September 2024 | 1.24.0 | OMEdit works with Qt5 and Qt6. Much faster adding and removing of components and connections in large models. New flag `--exposeLocalIOs` for FMU outputs. | [release notes](https://github.com/OpenModelica/OpenModelica/releases/tag/v1.24.0) |
| May 2024 | 1.23.0 | Proper rounding of decimal numbers. Base Modelica flat output. Editing of top-level model parameters and duplicating classes in OMEdit. | [release notes](https://github.com/OpenModelica/OpenModelica/releases/tag/v1.23.0) |
| November 2023 | 1.22.0 | New instance-based architecture of OMEdit active by default, with conditional connectors and parameter dialogs depending on Boolean parameters. Better handling and rendering of connections. | [release notes](https://github.com/OpenModelica/OpenModelica/releases/tag/v1.22.0) |
| April 2023 | 1.21.0 | The gbode solver becomes an alternative to dassl. Experimental instance-based architecture of OMEdit. Improved OMMatlab interface. | [release notes](https://github.com/OpenModelica/OpenModelica/releases/tag/v1.21.0) |
| December 2022 | 1.20.0 | Automatic installation of the Modelica Standard Library with the package manager. New general-purpose ODE solver gbode. FMI import works again. | [release notes](https://github.com/OpenModelica/OpenModelica/releases/tag/v1.20.0) |
| May 2022 | 1.19.0 | Package management and conversion scripts integrated in OMEdit. Full support of the synchronous features, in particular the Modelica.Clocked library. | [release notes](https://github.com/OpenModelica/OpenModelica/releases/tag/v1.19.0) |
| September 2021 | 1.18.0 | The new frontend flattens 100% of the models of MSL 3.2.3 and 4.0.0. Full support of the spatialDistribution() operator. Data reconciliation integrated in OMEdit. | [release notes](https://github.com/OpenModelica/OpenModelica/releases/tag/v1.18.0) |
| March 2021 | 1.17.0 | The new frontend is the default for all tools. Support for MSL 3.2.3 and MSL 4.0.0. clang instead of gcc on Windows for much faster compilation. Direct support of macOS discontinued. | [release notes](https://github.com/OpenModelica/OpenModelica/releases/tag/v1.17.0) |
| October 2020 | 1.16.0 | Graphical support of replaceable classes in OMEdit. CVODE solver, also in FMI co-simulation. Support of encrypted libraries for Consortium members. | [release notes](https://github.com/OpenModelica/OpenModelica/releases/tag/v1.16.0) |
| December 2019 | 1.14.0 | The new frontend is the default and flattens models 10 to 20 times faster on average. | [release notes](https://github.com/OpenModelica/OpenModelica/releases/tag/v1.14.0) |
| December 2018 | 1.13.0 | OMSimulator 2.0 with SSP support. Model and library encryption. Julia and basic Matlab scripting APIs. OMSysIdent parameter estimation. The new fast frontend is available for testing. | [release notes](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/githubreleases.html#release-notes-for-openmodelica-1-13-0) |
| October 2017 | 1.12.0 | Better library coverage. Small footprint real-time embedded code gen, Modelica Device Drivers library, OMSimulator FMI and TLM stand-alone co-simulation and simulation. Graphical editing of state machines. Binary Linux builds, Enhanced OMPython for control system development, Further enhanced DAEMode sparse solver support. | [release notes](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/githubreleases.html#release-notes-for-openmodelica-1-12-0) |
| Febr 2017 | 1.11.0 | 3D Animation. 64bit. Support for models with half a million equations, OMWebbook for web-based simulation. | [release notes](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/githubreleases.html#release-notes-for-openmodelica-1-11-0) |
| March 2016 | 1.9.4 | Initial support for synchronous models with clocked equations. Faster simulation and compiler frontend. Undo/Redo in OMEdit. | [release notes](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/githubreleases.html#release-notes-for-openmodelica-1-9-4) |
| March 2015 | 1.9.2 | FMI 2.0 model exchange, faster OMEdit GUI with OMC linked as a DLL. | [release notes](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/githubreleases.html#release-notes-for-openmodelica-1-9-2) |
| October 2014 | 1.9.1 | Improved library support. Dynamic debugger for equation-based models. Dynamic optimization with collocation. | [release notes](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/githubreleases.html#release-notes-for-openmodelica-1-9-1) |
| October 2013 | 1.9.0 | A more stable and complete compiler. 245 of the 274 example models of MSL 3.2.1 simulate. | [release notes](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/githubreleases.html#release-notes-for-openmodelica-1-9-0) |
| April 2012 | 1.8.1 | Support for operator overloading, faster compilation, ModelicaML with valuebindings, Python Scripting. | [release notes](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/githubreleases.html#release-notes-for-openmodelica-1-8-1) |
| November 2011 | 1.8.0 | Media flattening. FMI 1.0 import and export. Better MSL 3.1 support and bug fixes in OMEdit and OMOptim | [release notes](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/githubreleases.html#openmodelica-1-8-0-november-2011) |
| April 2011 | 1.7.0 | Better MSL 3.1 support, OMOptim optimization subsystem, performance analyzer, improvements in graphical editor OMEdit and in ModelicaML. | [release notes](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/githubreleases.html#openmodelica-1-7-0-april-2011) |
| December 2010 | 1.6.0 | Better support for Modelica Standard Library 3.1. New graphical editor OMEdit, Stream Connectors, etc. | [release notes](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/githubreleases.html#openmodelica-1-6-0-november-2010) |
| July 2010 | 1.5.0 | Full flattening support for the MultiBody library. Interactive simulation. UML-Modelica modeling with ModelicaML. | [release notes](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/githubreleases.html#openmodelica-1-5-0-july-2010) |
| Jan 2009 | 1.4.5 |  | [release notes](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/githubreleases.html#openmodelica-1-4-5-january-2009) |
| May 2006 | 1.4.0 | OMC is translated to MetaModelica, in which all compiler development is now done. | [release notes](https://openmodelica.org/doc/OpenModelicaUsersGuide/latest/githubreleases.html#openmodelica-1-4-0-may-2006) |

There were no official releases 1.10.0 and 1.15.0; their development versions were released as 1.11.0 and 1.16.0.

## History

- Fall 2014. Partial support for Modelica 3.3 synchronous features
- Spring 2014. Comment- and indentation preserving unparsing.
- Spring 2014. FMI 2.0 support.
- April 2014. Switching to Bootstrapped compiler, release 1.9.2.
  Further improved performance and coverage.
- Spring 2014. Better coverage for Modelica libraries including MSL 3.2.1, ModelicaTest 3.2.1, PetriNet, Buildings, PowerSystems, OpenHydraulics, ThermoPower, ThermoSysPro, PlanarMechanics, etc.
- February 2014. Integrated Modelica debugger.
- December 2012. Most of Media, Fluid and Multibody libraries simulating.
- November 2012. OMEdit graphic editor enhancements.
- October 2012. FMI co-simulation.
- October 2012. Most of Fluid library flattening.
- October 2012. Most of libraries ThermoSysPro and Thermopower simulating.
- March 2011. ModelicaML Eclipse plugin in new Papyrus framework.
- March 2011. Performance analyzer in OpenModelica
- March 2011. OMOptim Optimization subsystem in OpenModelica
- Feb 2011. 3rd Annual OpenModelica Workshop in Linköping, Sweden.
- June 2010. Prototype support for interactive simulation.
- Feb 2010. OpenModelica also available under standard GPL license.
- Feb 2010. 2nd Annual OpenModelica Workshop in Linköping, Sweden.
- June 2009. Start of OPENPROD ITEA2 11 million €, 28-partner project including substantial OpenModelica development.
- Feb 2009. First Annual OpenModelica Workshop in Linköping, Sweden.
- Dec 2008. MathCore joins OSMC and contributes 1 man-year of source code.
- June 2008. Adrian Pop full-time as OSMC Technical Coordinator.
  Development accelerates.
- Feb 2008. OpenModelica Development Server operational.
- Dec 2007. Creation of the Open Source Modelica Consortium, initially 7 organizational members.
