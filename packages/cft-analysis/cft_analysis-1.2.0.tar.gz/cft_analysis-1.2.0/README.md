# cft-analysis

[![PyPI](https://img.shields.io/pypi/v/cft-analysis)](https://pypi.org/project/cft-analysis/)
![GitHub](https://img.shields.io/github/license/mad-lab-fau/cft-analysis)
[![Lint](https://github.com/mad-lab-fau/cft-analysis/actions/workflows/lint.yml/badge.svg)](https://github.com/mad-lab-fau/cft-analysis/actions/workflows/lint.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/mad-lab-fau/cft-analysis)

Python package for the analysis of data collected during the Cold Face Test (CFT) study.

## Description

This package contains various helper functions to work with the dataset (including [`tpcp`](https://github.com/mad-lab-fau/tpcp) `Dataset` representations) and to process data. Additionally, it contains different analysis experiments performed with the dataset.

## Repository Structure
The repository is structured as follows:

```bash
├── cft_analysis/                                   # cft-analysis Python package
└── experiments/                                    # Folder with conducted analysis experiments; each experiment has its own subfolder
    └── 2022_scientific_reports/                    # Analysis for the 2022 Scientific Reports Paper (see below)
        ├── data/                                   # Processed data and extracted parameters
        ├── notebooks/                              # Notebooks for data processing, analysis and plotting
        │   ├── data_processing/            
        │   │   ├── ECG_Processing_Feature_Computation.ipynb    # Processing and feature extraction from ECG data
        │   │   ├── Questionnaire_Processing.ipynb              # Processing of questionnaire data
        │   │   └── Saliva_Processing.ipynb                     # Processing of saliva data
        │   ├── analysis/                   
        │   │   ├── Subject_Exclusion.ipynb         # Checks whether (and which) subjects need to be excluded from further analysis
        │   │   ├── Demographics.ipynb              # Analysis of general information of study population: Age, Gender, BMI, ...
        │   │   ├── ECG_Analysis.ipynb              # Descriptive and statistical analysis of ECG data
        │   │   ├── Questionnaire_Analysis.ipynb    # Descriptive and statistical analysis of questionnaire data
        │   │   └── Saliva_Analysis.ipynb           # Descriptive and statistical analysis of saliva data
        │   └── plotting/
        ├── results/                                # Plots and statistical results exported by the notebooks in the "analysis" and "plotting" folders
        └── config.json                             # 

```

## Installation
If you want to use this package to reproduce the analysis results then clone the repository and install the 
package via [poetry](https://python-poetry.org):
```bash
git clone git@github.com:mad-lab-fau/cft-analysis.git
cd cft-analysis
poetry install # alternative: pip install .
```
This creates a new python venv in the `cft-analysis/.venv` folder. Next, register a new IPython kernel for the venv:
```bash
cd cft-analysis
poetry run poe register_ipykernel
```

Finally, go to the `experiments` folder and run the Jupyter Notebooks. 

## Experiments
Currently, this repository contains the following experiments:

### 2022 – Scientific Reports
Analysis of the [CFT Dataset](https://osf.io/8fb6n/) for the paper [Vagus Activation by Cold Face Test Reduces Acute Psychosocial Stress Responses](https://www.nature.com/articles/s41598-022-23222-9), published in *Scientific Reports*.

#### Usage
In order to run the code, first download the CFT Dataset, e.g. from [OSF](https://osf.io/8fb6n/). Then, create a file named `config.json` in the folder `/experiments/2022_scientific_reports` with the following content:
```json
{
    "base_path": "<path-to-dataset>"
}
```
This config file is parsed by all notebooks to extract the path to the dataset.   
**NOTE**: This file is ignored by git because the path to the dataset depends on the local configuration!

The files in the `data` folder are created by running the notebooks in the `data_processing` folder. The files in the `result` folder are created by running the notebooks in the `analysis` and the `plotting` folders.




