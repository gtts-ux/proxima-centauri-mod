# Proxima Centauri Mod

An optional, data-only star-system catalogue for [Solar Sim](https://github.com/gtts-ux/solar-sim), requiring version 1.7.0 or newer. It adds the red dwarf Proxima Centauri and confirmed planets Proxima d and b in a separate catalogue.

## Install

Quit Solar Sim. In Terminal:

```sh
sol-sim -u
sol-sim -m"proxima centauri"
sol-sim
```

Inside the app:

```text
/proxima centauri
/planet
/orbit
/proxima b
/camera wide
/camera system
/compare "proxima b" "proxima d"
/time 2026/10/18 13:45
/proxima exit
```

The spelling `/proxima centari` also works. `/proxima` opens this catalogue, `/star` opens the host star and `/proxima c` explains the unconfirmed candidate. `/dwarf` switches directly to the dwarf catalogue. Solar System objects are hidden until you leave Proxima mode. In orbit mode, Left/Right changes camera zoom; the arrow menu also has a Mods section.

You do not need to clone this repository or install pip packages. The app installer requests `proxima-centauri.json` from this repository. When unavailable it uses a bundled package, with an explicit message. `sol-sim --offline -m"proxima centauri"` installs the bundled version without a network request. Re-running `-m` updates the installed data without downgrading newer packages. Updating Solar Sim preserves `mods/`.

## Manual download

Download this repository with Code > Download ZIP. Copy `proxima-centauri.json` to the `mods` folder inside your Solar Sim app folder (create `mods` if necessary), then run `/proxima centauri`. Copy only the JSON file; no mod Python code is loaded or executed. To uninstall, leave Proxima mode and delete that file. Each app copy has its own `mods` folder.

## Model and sources

The orbits use published approximate sizes and periods, with arbitrary phases and a shared illustrative plane. They are **not current observed positions**. Proxima distances are local, star-centered model separations; Earth-to-Proxima distances are not calculated by this simulation. No physical claim is made about the orbital plane or phase.

Planet masses are radial-velocity minimum masses (m sin i). Radii are estimates, not measurements. Days, composition, atmospheres, moons and rings are unknown; no moons or spacecraft are invented. Gravity and density are not presented as measured. Stellar properties use rounded values from the 2016 discovery paper. Alpha Centauri A/B are outside this local model. Proxima c is described as an unconfirmed candidate and is excluded from the orbit model.

Data checked 2026-10-18. Values are rounded for an educational simulation and can change with new research:

- [NASA: Proxima b](https://science.nasa.gov/exoplanet-catalog/proxima-centauri-b/)
- [NASA: Proxima d](https://science.nasa.gov/exoplanet-catalog/proxima-centauri-d/)
- [NASA Exoplanet Archive: candidate status of Proxima c](https://exoplanetarchive.ipac.caltech.edu/docs/removed_targets.html)
- [Anglada-Escudé et al. 2016: host-star properties](https://arxiv.org/abs/1609.03449)

## Development

`python3 -m unittest -v` checks the package without dependencies. On main, GitHub Actions also downloads the checksum-pinned official Solar Sim v1.7.0 ZIP and verifies that `-m` fetches this repository's exact JSON, then exercises activation, orbits, comparisons and exit. Change `version` for a new data release; preserve format 1 and the fixed body names, units and coordinate frame. The Solar Sim installer validates package fields, limits the download size and atomically replaces its local JSON file. This repository contains astronomy data and documentation; it does not distribute executable app extensions.
