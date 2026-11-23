---
title: "Simulation Support for the Energy Megagame"
qrcodejs: true
---

> [!IMPORTANT]
> Draft: the parts marked **TODO (Lena)** still need to be filled in or checked.

The Energy Megagame is a serious game about the transition to a sustainable energy system.
It was developed in the research project [Att vända strömmen (Switching the Current)](https://liu.se/en/research/switching-the-current), a cross-disciplinary project of Linköping University, the University of Skövde and Jönköping University.
The project aims to create increased understanding of different stakeholders' perspectives on energy systems, society, environment and climate.

In a megagame, 20 to 100 participants play together.
Each player or team takes the role of an actor in a region, such as the regional council, a municipality, the forestry and construction sectors, the regional industry, banks, media, researchers and the population with low, middle and high income.
A game takes a full day: an introductory round, three to five rounds of 45 to 60 minutes, a debriefing after each round, and a summary of the results at the end.

OpenModelica simulates the energy system and the transport of the region, to show the players the effects of their decisions over the next decades.

**TODO (Lena):** check the description above, and add the funding (the Swedish Energy Agency, 2021 to 2024?) and the people involved if wanted.

{{% qrcode %}}

## Events

| Date | Place | Participants | Results |
| --- | --- | --- | --- |
| November 2022 | **TODO (Lena)** | about 20 | |
| December 2022 and January 2023 | **TODO (Lena)** | 20 to 40 (two games) | |
| 6 February 2023 | Lund | **TODO (Lena)** | |
| November 2023 | Uddevalla | more than 70 high school students | [Simulation dashboard](/events/energy_game_uddevalla) |
| **TODO (Lena)** | | | |

**TODO (Lena):** complete the table, and add the games after November 2023.
The old version of this page said "Lund, 06 February 2022", but the page was written in February 2023; which year is right?

## How does the simulation work?

The simulation gives the game a degree of realism and projects the impact of the decisions taken in the game.
[OpenModelica](https://openmodelica.org) simulates the models, and Python scripts prepare the input data and draw the result graphs.

After each round:

1. The players make their decisions on the game boards.
2. The game leaders count the cards on the boards and collect the decisions with forms.
3. The data is exported to Excel and extrapolated to the input data for the models.
4. OpenModelica simulates the models.
5. Python scripts generate the graphs, which are shown to the players, also on this website through a QR code.

The simulation cannot change the past: each round starts from the historical data and the results of the earlier rounds, and adds the trends from the new decisions.
Some decisions take effect only after a delay; for example, a new solar farm produces energy three years after the decision to build it.

Example of energy usage projections based on current trends; the blue line marks the current year:

![Energy production projections, the blue line marks the current year](/images/energy_game_energy_prod.jpg)

## The models

The models used in the game are from the TransportationModel and [ThermalAndPowerGridSystem](https://github.com/OpenModelica/ThermalAndPowerGridSystem) libraries.

**TODO (Lena):** is the TransportationModel library public? If so, add a link.

### Energy grid model

The energy grid model is parametrised with regional data: solar irradiation, wind speed, hydropower and nuclear power production capacity, household energy demand, and the number of vehicles of each type.

![The energy system model](/images/energy_game_EnrgyGridModel.svg)

### Transportation model

The transportation model calculates the CO2 emissions of transport.
It is parametrised with regional numbers and then with the decisions taken in the game.
It was developed by Linköping University, Modelicon and Politecnico di Milano.

**TODO (Lena):** check the partners, and link them if wanted.

![The transport system model](/images/energy_game_TransportationHub.svg)

### Biomass model

The biomass model describes the forest: its age distribution, the CO2 it stores, and the biomass that can be harvested.
Based on historical data, more than 3 % of the biomass volume can be harvested each year.
It was developed in a master thesis in 2023.

**TODO (Lena):** check the description, add a link to the master thesis, and add a picture of the model if there is one.

The results of the energy grid, transport and biomass models are combined to compute the total energy usage and the CO2 emissions.
The goal is the one of the Swedish parliament: Sweden shall be carbon neutral by 2045.

## How is the data generated?

At the beginning, the models are parametrised with the current data from Sweden and from Östergötland, and this data is extrapolated over the next 40 years.
Future trends are extrapolated from current plans, for example [32 new wind turbines planned](https://www.holmen.com/en/newsroom/press/news/holmen-applies-to-develop-wind-power-in-ostergotland/) in Östergötland that are expected to [double the energy production](https://rvno.se/vindkraftsprojektet/).
Other trends are based on the history, for example the growth in energy demand over the previous years for all of Sweden is used to estimate the growth in demand for Östergötland.

The data comes from different sources.
Some data is not available in the exact format needed for the simulation, so some approximations are made.
For example, wind speed and solar irradiation are averages over several locations from the [NASA POWER](https://power.larc.nasa.gov/data-access-viewer/) site, because there is no single value for the whole region.

- Solar panel numbers are taken from [Hemsol](https://hemsol.se/solceller/ostergotland/), and their trends from [Energimyndigheten](https://www.energimyndigheten.se/nyhetsarkiv/2022/kraftig-okning-av-installerade-solcellsanlaggningar/).
- Hydropower information is taken from [Tekniska verken](https://www.tekniskaverken.se/om-oss/verksamheten/vattenkraft/vattenkraftverken/) and [Statistikdatabasen](https://www.statistikdatabasen.scb.se/pxweb/sv/ssd/START__EN__EN0203__EN0203A/ProdbrEl/).
- Consumption trends are calculated from the data on [Mimer](https://mimer.svk.se/) and [Regionfakta](https://www.regionfakta.com/vastra-gotalands-lan/energi/elforbrukning-per-lan/).

After every round, the data for the future is adjusted to the decisions taken in the game, for example more or less public and private transport, or the type of energy used by the population.
These changes are found by counting the cards of each type on the boards and comparing the numbers with the previous rounds.

**TODO (Lena):** the game in Uddevalla is in Västra Götaland, not in Östergötland.
Was the region changed for that game, and is the data still from the sources above?
The Regionfakta link already goes to Västra Götaland.

## History of the simulation

- November 2022: first game with about 20 people.
  One person collected the data, and the models crashed on unexpected parameters.
- December 2022 and January 2023: second and third games with 20 to 40 people.
  More detailed parametrisation and data generation with scripts based on the results of each round.
  Some graphs could be generated, but only after the round was over.
- May 2023: a biomass model in Modelica, developed in a master thesis.
- November 2023: a larger step size and a much faster simulation, and forms to collect the data faster.
  Tested with 70 players.

Next steps:

- Calculate more indicators, for example wellbeing or happiness.
  The World3 model could keep track of quality of life.
  **TODO (Lena):** link to the World3 model used.
- Integrate a climate and environment model, for example Earth3.
- More interactive visualisation, with nicer graphs and better handling of scaling.
- Close the loop, for example to control imports better.

**TODO (Lena):** update this section with what happened after November 2023.

## Want to find out more?

If you have more questions or feedback about the simulation, please contact [Lena Buffoni](https://liu.se/en/employee/olero90).

Lena Buffoni presented the simulation at the OpenModelica Workshop 2024: [OpenModelica use for forecasting in the MegaGame Energy Project](/images/M_images/OpenModelicaWorkshop_2024/11_LenaBuffoni-Energy-MegaGame-OM-workshop.pdf) (slides).

**TODO (Lena):** add publications about the game or the simulation, if there are any.

For further reading:

- Peter Fritzson, Adrian Pop, Lena Buffoni, et al.
  The OpenModelica Integrated Environment for Modeling, Simulation, and Model-Based Development.
  Modeling, Identification and Control, 41(4):241–295, 2020.
- Lena Buffoni, Lennart Ochel, Adrian Pop, Peter Fritzson, Niklas Fors, Görel Hedin, Walid Taha, and Martin Sjölund.
  Open Source Languages and Methods for Cyber-Physical System Development: Overview and Case Studies.
  Electronics 10, no. 8: 902, April 2021.
  [doi:10.3390/electronics10080902](https://doi.org/10.3390/electronics10080902)
- Peter Fritzson.
  Principles of Object Oriented Modeling and Simulation with Modelica 3.3: A Cyber-Physical Approach.
  1250 pages. ISBN 9781-118-859124, Wiley IEEE Press, 2014.
- D. H. Meadows, J. Randers, and D. L. Meadows.
  Limits to Growth – The 30 Year Update. 2004.
- J. Randers, J. Rockström, P.-E. Stoknes, et al.
  Achieving the 17 Sustainable Development Goals within 9 planetary boundaries.
  Global Sustainability 2, e24, 1–11, 2019.
  [doi:10.1017/sus.2019.22](https://doi.org/10.1017/sus.2019.22)
- Modelica Association.
  Modelica – A Unified Object-Oriented Language for Systems Modeling, Language Specification Version 3.5.
  February 18, 2021.
  [www.modelica.org](https://www.modelica.org)
- [Power System Simulation in OpenModelica](https://om.fossee.in/powersystems/pssp/completed-pssp)
