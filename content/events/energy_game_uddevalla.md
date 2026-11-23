---
title: "Simulation Dashboard: Energy Megagame in Uddevalla 2023"
qrcodejs: true
---

> [!IMPORTANT]
> Draft: the parts marked **TODO (Lena)** still need to be filled in or checked.

This dashboard showed the simulation results to the players of the Energy Megagame "Att vända strömmen" in Uddevalla in November 2023, with more than 70 high school students.
See [Simulation Support for the Energy Megagame](/events/energy_game) for the game and how the simulation works.

**TODO (Lena):** add the exact date and the place or organiser of the game.

The results below are from the start of the game (round 0), for the year 2023.

**TODO (Lena):** were the results of the later rounds shown here too? If so, say that this page shows the state before the first round, or add the final results.

{{% qrcode %}}

## Energy flows

The energy forecast shows how the energy flows from the sources (hydro, solar, wind, biomass, waste, fossil gas and fuel, and imports from outside the region) through electricity to households, industry and transport.

**TODO (Lena):** which year does the forecast show?

{{< load-plotly >}}
{{< plotly json="/images/megagame_simulation/sankey.json" height="400px" >}}

## Forest

**TODO (Lena):** one or two sentences on what the forest figures show and how players can read them.

{{< figure src="/images/megagame_simulation/fig_forest_co2_distrib.png" width="600" alt="Forest CO2 distribution" caption="Forest CO2 distribution" >}}
{{< figure src="/images/megagame_simulation/fig_forest_age_distrib.png" width="600" alt="Forest age distribution" caption="Forest age distribution" >}}

## Energy sources and CO2

**TODO (Lena):** one or two sentences on what the figures show, for example the CO2 budget the players have to stay within.

{{< figure src="/images/megagame_simulation/energy_sources.png" width="600" alt="Energy sources" caption="Energy sources" >}}
{{< figure src="/images/megagame_simulation/co2_consumption.png" width="600" alt="CO2 consumption" caption="CO2 consumption" >}}
