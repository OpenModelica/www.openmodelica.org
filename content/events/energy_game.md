---
title: "Simulation Support for the Energy Megagame"
qrcodejs: true
---

## Latest event : Lund, 06 February 2022

{{% qrcode %}}

## How does the simulation process work?

In order to provide a degree of realism and project the impact of the decisions taken in the game, we use simulation support. [OpenModelica](openmodelica.org) is the tool used to generate the simulation results for the game. The input data (solar irradiance, wind speed, hydropower production capacity and nuclear power production capacity for the region, household demand and amount of different types of vehicles) is collected for the Östergotland region.
This data is pre-processed in Python based on the decisions taken in the game and provided to the physical models in Modelica to then obtain the CO2 production, total energy production and other KPIs. The data is then again processed in Python to generate the result graphs.

Example of energy usage projections based on current trends:

![Projected energy production in Östergötland](/images/energy_game_energy_prod.svg)

The models used in the game are from the TransportationModel and [ThermalAndPowerGridSystem](https://github.com/OpenModelica/ThermalAndPowerGridSystem) libraries.

![The energy system model](/images/energy_game_EnrgyGridModel.svg)

![The transport system model](/images/energy_game_TransportationHub.svg)


## How is the data generated?

At the beginning the models are parametrised based on the current data from Sweden and from Östergötland, and future trends are extrapolated based on current plans (eg: [32 new turbines planned](https://www.holmen.com/sv/energi/vindkraft/pagaende-projekt2/klintaberget/) in Östergötland expected to [double energy production](https://rvno.se/vindkraftsprojektet/)) and trends based on previous history (eg: growth in energy demand over previous years for all of Sweden are used to estimate the growth in demand for Östergötland).

The data used is taken from different sources, some data is not available in the exact format needed for the simulation, so some approximations are made (eg: wind speed and solar irradiation are calculated as an average based on several location points from the [Nasa](https://power.larc.nasa.gov/data-access-viewer/) site because there is no single value available for the whole region).

Solar panel numbers are taken from [Hemsol](https://hemsol.se/solceller/ostergotland/) and trends from [Energimyndigheten]( https://www.energimyndigheten.se/nyhetsarkiv/2022/kraftig-okning-av-installerade-solcellsanlaggningar/.
)

Hydropower information is take from [Tekniskaverken](https://www.tekniskaverken.se/om-oss/verksamheten/vattenkraft/vattenkraftverken/) and [Statistik Databasen](https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__EN__EN0203__EN0203A/ProdbrEl/).

Consumption trends are calculated based on the data available on [Mimer](https://mimer.svk.se/) and [Regionfakta](https://www.regionfakta.com/vastra-gotalands-lan/energi/elforbrukning-per-lan/).


At the beginning the models are parametrised based on the current real world status and this data is extrapolated on the next 40 years.

After every round the data for the future is adjusted based on the decisions taken in the game, for example the increase or decrease in public and personal transport, the type of energy used by the population. These changes are considered by counting the cards of different types on the boards and comparing the numbers with the previous rounds.

Some changes are non instantaneous, for example a decision of building a new solar farm will have an effect delayed by 3 years.

After the simulation, the results from the energy grid and transport models are aggregated to compute total energy usage and CO2 emissions.

The next step is to integrate the Wordl3 model into the simulation, to keep track of KPIs on life quality.

## Want to find out more?

If you have more questions or feedback about the simulation please contact [Lena Buffoni](https://liu.se/en/employee/olero90).

For further reading, here are some resources:

* Peter Fritzson, Adrian Pop, Lena Buffoni,, et al (2020). The OpenModelica Integrated Environment for Modeling, Simulation, and Model-Based Development. Modeling, Identification and Control, 41(4):241—295.

* Lena Buffoni, Lennart Ochel, Adrian Pop, Peter Fritzson, Niklas Fors, Görel Hedin, Walid Taha, and Martin Sjölund. Open Source Languages and Methods for Cyber-Physical System Development: Overview and Case Studies Electronics 10, no. 8: 902., April 2021, [doi](https://doi.org/10.3390/electronics10080902)

* Peter Fritzson. Principles of Object Oriented Modeling and Simulation with Modelica 3.3: A Cyber-Physical Approach. 1250 pages. ISBN 9781-118-859124, Wiley IEEE Press, 2014.

* Meadows, D. H., Randers, J., & Meadows, D. L. (2004). Limits to Growth – The 30 Year Update.

* Randers J, Rockström J, Stoknes P-E, et al (2019). Achieving the 17 Sustainable Development Goals within 9 planetary boundaries. Global Sustainability 2, e24, 1–11. [doi](https://doi.org/10.1017/sus.2019.22)

* Modelica Association. Modelica – A Unified Object-Oriented Language for Systems Modeling, Language Specification Version 3.5. February 18, 2021. www.modelica.org

* [Power System Simulation in OpenModelica](https://om.fossee.in/powersystems/pssp/completed-pssp)
