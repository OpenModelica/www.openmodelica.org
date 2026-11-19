---
title: "Industrial Products"
aliases: ["/openmodelicaworld/related-products"]
---

An important benefit of being a company member in the Open Source Modelica Consortium is OEM licensing which allows including the OpenModelica software in commercial products shipped to customers.

## Bosch Rexroth Control Edge Designer and Testing Framework

Bosch Rexroth is using OpenModelica in an in-house tool, the Control Edge Designer, for the design, analysis and optimization of hydraulic valves.
The purpose of this tool is to provide an intuitive workflow for the development of mobile valves to shorten the time to market for customer-tailored products.
Therefore, the considered valve models are provided as Modelica models and the simulation, which is executed in the background is based on OpenModelica technology.
The picture shows the Control Edge Designer.

![BR-CED](/images/BR-CED.JPG)

Another application of OpenModelica at Bosch Rexroth is utilization within a testing framework for the development of Rexroth Hydraulic, Valve and Pump libraries.
OpenModelica is used to verify the correct behavior of the model components.
Furthermore Bosch Rexroth is also developing an in-house tool for system simulation, including OpenModelica, to provide an intuitive state of the art simulation tool to Rexroth customers and sales engineers.

## Bosch Rexroth Controller Code Generation Based on FMI

Real-time and embedded use cases are important for Bosch Rexroth.
In this context, especially the execution of Modelica and FMU based models on Rexroth controller hardware is an important area of research.
The picture shows the OpenModelica based tool chain for controller code generation from FMI.

![BR-CodeGenerationBasedOnFMI](/images/BR-CodeGenerationBasedOnFMI.PNG)

## Molten-salt-powered once-through steam generator industrial usage of OpenModelica

The Horizon 2020 PreFlexMS project aims at the design of an innovative, highly flexible concentrated solar power plant with thermal storage.
One key feature of the project is the design of a once-through steam generator powered by the hot molten salts produced by the solar field, which is expected to have higher operational flexibility than the state-of-the-art circulation boilers used in similar plants, and thus be able to better cope with future scenarios in which flat-rate incentives are replaced by variable price of energy.

Various dynamic models of the system with different level of detail were built using the Modelica language and the open source ThermoPower library, with some project-specific extensions.
The models, that have about 300 states and 7000 equations, were initially developed with a commercial Modelica tool.
Later on, OpenModelica was successfully used to export royalty-free FMUs of the model for use by other partners.

![HP modelica](/images/HP_modelica.png)

## [ABB OPTIMAX®](https://new.abb.com/power-generation/power-plant-optimization)

ABB OPTIMAX® provides advanced model based control products for power generation and water utilities.
Plant models are typically formulated in Modelica and deployed through FMI 2.0.
The optimizing control applications maximize the efficiency and provide more flexibility to large conventional power plants that face frequent load ramps and start-ups.
Moreover they aggregate small renewable units to large virtual power plants.
This enables renewables to provide grid services like power/frequency control, achieving grid stability despite of high penetration of renewable power and raising revenues.
ABB uses several compatible Modelica tools, including OpenModelica, depending on specific application needs.
OpenModelica provides outstanding debugging features that help to save a lot of time during model development.

![ABB](/images/ABB.png)

## Generation of code for real-time optimizing control almost one tenth of German power production

Since March 2015, OpenModelica is used as part of [ABB's OPTIMAX PowerFit](https://new.abb.com/process-automation/energy-industries/digital/solutions/abb-ability-energy-management-and-optimization-optimax) product to generate code for real-time optimizing control.
Meanwhile this code controls within seconds about 5000 MW (approx. 7.5%) of the German power production.
Of these, about 1500 MW are generated from more than 2500 small sun-, wind- and biogas power plants (a rapidly increasing number), which are controlled and coordinated to act like one bigger power plant in the energy system.

[&nbsp;](https://www.wolfram.com/system-modeler/)

## [MIKE by DHI, www.mikebydhi.com, WEST Water Quality](https://www.mikebydhi.com)

Modeling and simulation environment that includes a large part of the OpenModelica compiler using the OEM license.
The picture shows a water treatment effluent and sludge simulation.

![mikebydhi](/images/mikebydhi.png)
