---
title: "SIMS-tutorials"
---

The conference starts Wednesday 7th October with 3 tutorials. Registration will start in front of Visionen (<https://www.ida.liu.se/department/location/search.en.shtml?keyword=Visionen>) on the Linköping University campus. Afterwards we will split up in groups for the tutorials and walk to the respective rooms.

Those who will only be attending the tutorials and/or know the location of the rooms, can go to the tutorial rooms directly.

The tutorials will be starting at 13:30.

3 Tutorials will be given:

Tutorial 1: Principles of Object-Oriented Modelingand Simulation of Dynamic Systems with Modelica.

**Tutor**: Dr. Lena Buffoni (Linköping University) **Room**: Donald Knuth, Building B, First Floor (<https://www.ida.liu.se/department/location/search.sv.shtml?keyword=Donald+Knuth>)

Object-Oriented modelling is a fast-growing area of modelling and simulation that provides a structured, computer-supported way of doing mathematical and equation-based modelling. Modelica is today the most promising modelling and simulation language in that it effectively unifies and generalizes previous object-oriented modelling languages and provides a sound basis for the basic concepts.

The Modelica modelling language and technology is being warmly received by the world community in modelling and simulation with major applications in virtual prototyping. It is bringing about a revolution in this area, based on its ease of use, visual design of models with combination of lego-like predefined model building blocks, its ability to define model libraries with reusable components, its support for modelling and simulation of complex applications involving parts from several application domains, and many more useful facilities. To draw an analogy, Modelica is currently in a similar phase as Java early on, before the language became well known, but for virtual prototyping instead of Internet programming.

The tutorial presents an object-oriented component-based approach to computer supported mathematical modelling and simulation through the powerful Modelica language and its associated technology. Modelica can be viewed as an almost universal approach to high level computational modelling and simulation, by being able to represent a range of application areas and providing general notation as well as powerful abstractions and efficient implementations.

The tutorial gives an introduction to the Modelica language to people who are familiar with basic programming concepts. It gives a basic introduction to the concepts of modelling and simulation, as well as the basics of object-oriented component-based modelling for the novice, and an overview of modelling and simulation in a number of application areas.

The tutorial has several goals:

• Being easily accessible for people who do not previously have a background in modelling, simulation.

• Introducing the concepts of physical modelling, object-oriented modelling and component-based modelling and simulation.

• Giving an introduction to the Modelica language.

• Demonstrating modelling examples from several application areas.

Giving a possibility for hands-on exercises.

Tutorial 2: FMI 2.0 Model Exchange, Cosimulation– Theory and Practice

**Tutors**: MSc Adeel Asghar (Linköping University) **Room**: Alan Turing, Building E, First Floor (<https://www.ida.liu.se/department/location/search.en.shtml?keyword=Alan%20Turing>)

FMI (Functional Mockup Interface), [https://www.fmi-standard.org](https://www.fmi-standard.org/), is a rather recently developed open standard for model interchange and tool interoperability which simplifies whole product modelling and model-based development. It was initially developed in the ITEA2 MODELISAR project [https://www.modelisar.org](https://www.modelisar.org/)) The first version, FMI 1.0, was published in 2010, followed by FMI 2.0 in July 2014. As of today, development of the standard continues through the participation of 16 companies and research institutes. FMI is supported by over 73 tools and is used by automotive and non-automotive organizations throughout Europe, Asia and North America.

The intention of FMI is that a modelling environment can generate C-Code from a dynamic system model that can be exported to other modelling and simulation environments either in source or binary form.

Models are described by differential, algebraic and discrete equations with time-, state- and step- events. In particular, all Modelica 3.2.2 models are supported and all Modelica variable attributes (like units and display units) as well as description texts can be exchanged. The models to be treated by this interface can be large for usage in offline or online simulation or can be used in embedded control systems on micro-processors. It is possible to utilize several instances of a model and to connect models hierarchically.

A model is independent of the target simulator since it does not use a simulator specific header file as in other approaches. A model is distributed in one zip-file with the extension \".fmu\" (Functional Mockup Unit) that contains several files:

• An xml-file contains the definition of all variables in the model and other model information. It is then possible to run the model on a target system without this information, i.e., with no unnecessary overhead.

• All needed model equations are provided with a small set of easy to use C-functions.

• Additional data can be included in the zip-file, especially maps and tables needed by the model.

In this tutorial you will be introduced to the FMI standard and you will be able to do hands-on exercises regarding model FMI export, import, and co-simulation.

Tutorial 3: Collaborative Modelling and Cosimulation using Crescendo: Tools and techniques for Designing Embedded Systems

**Tutor**: Prof. Peter Gorm Larsen (Aarhus University, Denmark) **Room**: AHA-rummet, Building E, First Floor (<https://www.ida.liu.se/department/location/search.en.shtml?keyword=AHA%20rumet>)

The embedded systems market is a lively place, and there is growing demand for rapid innovation of products that make exploit new materials, sensors and computing hardware, often through clever and complex software. In this context, developers have to form creative teams out of disparate disciplines but the semantic gaps between disciplines cost time and money because misunderstandings are often only detected when the physical product is built and software fails to control it properly. How can model-based development work if these teams of specialist engineers describe different parts of the product and its environment in very different ways, and can formal techniques help?

We have been developing practical methods for collaborative creation of “co-models” composed of discrete-event models of control devices/software and continuous-time models of the controlled devices and the environment, bridging gaps between software and other engineering disciplines. Reconciled operational semantics permit co-models to be “co-simulated”, allowing us to explore the design spaces of physics and software together, so that we can trade off alternatives on such bases as performance, energy consumption and cost before committing to a solution.

Our tutorial mixes lectures, discussions and opportunities for hands-on tool-based modelling using the new Crescendo toolset linking Overture-VDM and 20-sim tools. We will introduce the principles of co-modelling and co-simulation and give participants the opportunity to experiment with co-model creation and modification. We will present the experience gained in developing Crescendo, and with its industry application in the DESTECS project ([www.destecs.org](https://www.destecs.org/)).
