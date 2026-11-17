# PHYS 474 Final Project

This project measures the specific star formation rate (sSFR) enhancement of galaxies in close major-merger pairs, relative to matched isolated controls, using the **Galaxy And Mass Assembly (GAMA) Data Release 4**. The results are compared with the high-redshift (z = 3–9) JWST pair study of [Puskás et al. (2025)](https://arxiv.org/abs/2510.14743).

Course project for PHYS 474 at the University of Waterloo.

## Repository layout

```text
.
├── config.py                  # shared constants: cosmology, cuts, pair and matching criteria
├── 01_load_sample.ipynb       # load GAMA tables, merge, apply sample cuts   -> out/parent.fits
├── 02_find_pairs.ipynb        # find close pairs, flag isolated galaxies     -> out/pairs.fits
├── 03_controls.ipynb          # match 5 controls per paired galaxy           -> out/pairs.fits
├── 04_sfr_magphys.ipynb       # MagPhys sSFR enhancement                     -> out/sfr_magphys.fits
├── 05_sfr_halpha.ipynb        # Hα SFRs, BPT classification, enhancement     -> out/sfr_halpha.fits
├── 06_ssfr_plots.ipynb        # bin by separation, print and plot results
├── data/                      # GAMA FITS tables (not included, see below)
├── out/                       # intermediate tables written by the notebooks
└── figs/                      # figures (PDF and PNG)
```

## Requirements

Python 3.9+ with:

```bash
pip install numpy astropy scipy matplotlib jupyterlab
```

## Data

The GAMA tables are not included in this repository. Download these four tables as FITS files from the [GAMA DR4 Schema Browser](http://www.gama-survey.org/dr4/schema/) and place them in `data/`:

| DMU (version) | Table | Used for |
| --- | --- | --- |
| SpecCat (v27) | `SpecObjv27.fits` | Positions, redshifts, redshift quality |
| StellarMasses (v24) | `StellarMassesLambdarv24.fits` | Stellar masses, r-band absolute magnitudes |
| MagPhys (v06) | `MagPhysv06.fits` | 100 Myr SFRs and their posterior percentiles |
| SpecLineSFR (v05) | `GaussFitSimplev05.fits` | Hα, Hβ, [NII] and [OIII] fluxes and equivalent widths |

## References

- Driver S. P. et al., 2022, MNRAS, 513, 439 — GAMA Data Release 4 ([arXiv:2203.08539](https://arxiv.org/abs/2203.08539))
- Puskás et al., 2025 — [arXiv:2510.14743](https://arxiv.org/abs/2510.14743)

## Acknowledgements

This project uses data from GAMA, a joint European–Australasian project based on spectroscopy from the Anglo-Australian Telescope. The GAMA website is <https://www.gama-survey.org/>.

We acknowledge the limited use of AI-assisted tools in the preparation of this code.
