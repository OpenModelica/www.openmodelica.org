---
title: "Simulation Support for Energy Megagame in Lund"
qrcodejs: true
---



In order to provide a degree of realism and project the impact of the decisions taken in the game, we use simulation support. OpenModelica is the tool used to generate the simulation results for the game. The data is then processed in Python to generate the result graphs.


The models used in the game are from the TransportationModel and ThermalAndPowerGridSystem libraries.

![The energy system model](/images/energy_game_EnrgyGridModel.svg)

At the beginning the models are parametrised based on the current data from Sweden and from Östergötland, weather data such as solar irradiation and wind power is forecast for the future based on previous Nasa readings. Trends for energy consumption are based on data from previous years. This data is extrapolated on the next 40 years at the start of the game.

After every round the data for the future is adjusted based on the decisions taken in the game, for example the increase or decrease in public and personal transport, the type of energy used by the population. These changes are considered by counting the cards of different types on the boards and comparing the numbers with the previous rounds.

The simulation results from the energy grid and transport models are aggregated to compute total energy usage and CO2 emissions.

The next step is to integrate the Wordl3 model into the simulation, to keep track of KPIs on life quality.



Resources:

* Peter Fritzson, Adrian Pop, Lena Buffoni,, et al (2020). The OpenModelica Integrated Environment for Modeling, Simulation, and Model-Based Development. Modeling, Identification and Control, 41(4):241—295.

* Lena Buffoni, Lennart Ochel, Adrian Pop, Peter Fritzson, Niklas Fors, Görel Hedin, Walid Taha, and Martin Sjölund. Open Source Languages and Methods for Cyber-Physical System Development: Overview and Case Studies Electronics 10, no. 8: 902., April 2021, [doi](https://doi.org/10.3390/electronics10080902)

* Peter Fritzson. Principles of Object Oriented Modeling and Simulation with Modelica 3.3: A Cyber-Physical Approach. 1250 pages. ISBN 9781-118-859124, Wiley IEEE Press, 2014.

* Meadows, D. H., Randers, J., & Meadows, D. L. (2004). Limits to Growth – The 30 Year Update.

* Randers J, Rockström J, Stoknes P-E, et al (2019). Achieving the 17 Sustainable Development Goals within 9 planetary boundaries. Global Sustainability 2, e24, 1–11. [doi](https://doi.org/10.1017/sus.2019.22)

* Modelica Association. Modelica – A Unified Object-Oriented Language for Systems Modeling, Language Specification Version 3.5. February 18, 2021. www.modelica.org

* Peter Fritzson et al. [Energy Library](https://github.com/OpenModelica/ThermalAndPowerGridSystem)

* [Power System Simulation in OpenModelica](https://om.fossee.in/powersystems/pssp/completed-pssp)



{{% qrcode %}}
