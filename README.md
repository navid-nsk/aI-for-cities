# AI in Urban Studies: A Systematic Review (2020-2025)

[![DOI](https://img.shields.io/badge/DOI-10.xxxx/xxxxx-blue.svg)](https://doi.org/10.xxxx/xxxxx)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository contains the data, code, and supplementary materials for the systematic literature review:

> **AI for cities: patterns, gaps, and future directions**

## Overview

This systematic review analyzes **7,660 peer-reviewed articles** examining AI applications in urban studies published between 2020 and 2025. The review characterizes the field's thematic structure, methodological landscape, and sustainability orientation.

### Key Findings

- **Geographic Distribution**: 109 countries represented, with China (37.2%), India (11.5%), and USA (5.5%) as top contributors
- **Article Types**: 71.0% empirical studies, 29.0% non-empirical (methodological, review, conceptual)
- **SDG Alignment**: 71.6% aligned with SDG 11 (Sustainable Cities and Communities)
- **AI Methods**: Deep Learning and Machine Learning dominate; Graph Neural Networks remain underutilized
- **AI Tasks**: Prediction/forecasting (23.0%) and classification (18.6%) are primary tasks

## Repository Structure

```
github_repository/
├── data/
│   ├── raw/                          # Original Scopus exports by year
│   │   ├── 2020_research.csv
│   │   ├── 2021_research.csv
│   │   ├── 2022_research.csv
│   │   ├── 2023_research.csv
│   │   ├── 2024_research.csv
│   │   ├── 2025_research.csv
│   │   └── combined_research.csv
│   └── processed/                    # Coded and analyzed datasets
│       ├── clean_research.csv        # Full coded dataset (n=7,660)
│       ├── empirical_clean.csv       # Empirical subset (n=5,441)
│       ├── clean_research_non_empirical.csv  # Non-empirical subset (n=2,219)
│       ├── empirical/                # Empirical analysis tables
│       ├── non_empirical/            # Non-empirical analysis tables
│       └── overview/                 # Overview analysis tables
├── code/
│   ├── empirical_analysis/           # Visualization code for empirical analysis
│   ├── non_empirical_analysis/       # Visualization code for non-empirical analysis
│   └── overview/                     # Overview figure generation
├── figures/
│   ├── empirical/                    # Empirical analysis figures (PDF/PNG)
│   ├── non_empirical/                # Non-empirical analysis figures (PDF/PNG)
│   └── overview/                     # Overview figures (PDF/PNG)
└── docs/
    ├── DATA_DICTIONARY.md            # Variable definitions and coding scheme
    └── METHODOLOGY.md                # Extended methodology documentation
```

## Data Description

### Main Datasets

| File | Description | Records | Variables |
|------|-------------|---------|-----------|
| `clean_research.csv` | Complete coded dataset | 7,660 | 38 |
| `empirical_clean.csv` | Empirical articles subset | 5,441 | 38 |
| `clean_research_non_empirical.csv` | Non-empirical articles subset | 2,219 | 38 |

### Coded Variables

The dataset includes 15 coded variables across 6 categories:

1. **Relevance**: Article relevance to AI + Urban studies
2. **Geography**: Country of first author affiliation (109 countries)
3. **Subject Classification**: Category (163), Cluster (428), Megatrend (6)
4. **AI Methodology**: Method (16 categories) and Task (14 categories)
5. **Article Characteristics**: Type, Methodological approach, Spatial/Temporal scales
6. **Sustainability**: SDG alignment (17 goals), Integration level (3 levels)

See `docs/DATA_DICTIONARY.md` for complete variable definitions.

## Visualization Code

### Requirements

```bash
pip install pandas numpy matplotlib seaborn scipy
```

### Running the Code

```bash
# Generate empirical analysis figures
cd code/empirical_analysis
python create_dca_plot.py
python create_dendrogram.py
python sdg_heatmap_combined.py
python research_characteristics_viz.py
python ai_methods_heatmap.py
python ai_task_sdg_visualization.py

# Generate non-empirical analysis figures
cd code/non_empirical_analysis
python create_dca_plot.py
python create_dendrogram.py
python sdg_heatmap_combined.py
python research_characteristics_viz.py
python ai_methods_heatmap.py
python ai_task_sdg_visualization.py
```

## Figures

### Main Article Figures

| Figure | Description | File |
|--------|-------------|------|
| Figure 1 | Overview of research landscape | `figures/overview/overview_figure.pdf` |
| Figure 2 | Thematic structure of empirical research | `figures/empirical/dca_plot.pdf`, `figures/empirical/dendrogram_final.pdf` |
| Figure 3 | AI methods and tasks analysis | `figures/empirical/ai_methods_heatmap.pdf` |

### Supplementary Figures

| Figure | Description | File |
|--------|-------------|------|
| Figure S2 | DCA of non-empirical research | `figures/non_empirical/dca_plot_non_empirical.pdf` |
| Figure S3 | Non-empirical taxonomy dendrogram | `figures/non_empirical/dendrogram_non_empirical.pdf` |
| Figure S4 | SDG heatmap (non-empirical) | `figures/non_empirical/sdg_heatmap_non_empirical.pdf` |
| Figure S5 | Research characteristics (non-empirical) | `figures/non_empirical/research_characteristics_heatmap.pdf` |
| Figure S6 | AI methods heatmap (non-empirical) | `figures/non_empirical/ai_methods_heatmap.pdf` |
| Figure S7 | AI tasks × SDGs (non-empirical) | `figures/non_empirical/ai_task_sdg_*.pdf` |

## Search Strategy

The systematic review was conducted following PRISMA 2020 guidelines using Scopus database.

### Search String

```
TITLE-ABS-KEY (
  ("AI" OR "Artificial Intelligence" OR "Machine Learning" OR "Deep Learning" OR
   "Neural Network*" OR "CNN" OR "LSTM" OR "Random Forest" OR "SVM" OR
   "Reinforcement Learning" OR "GNN" OR "Transformer" OR "GAN" ...)
  AND
  ("Urban" OR "City" OR "Smart City" OR "Metropolitan" OR "Urban Planning" OR
   "Urban Mobility" OR "Urban Climate" OR "Land Use" ...)
)
AND PUBYEAR > 2019 AND PUBYEAR < 2026
AND DOCTYPE(ar) AND LANGUAGE(english)
```

See `docs/METHODOLOGY.md` for complete search string and inclusion/exclusion criteria.


## License

- **Data**: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- **Code**: [MIT License](LICENSE)

## Contact

For questions or feedback, please open an issue or contact [author email].

## Acknowledgments

This research was supported by [funding information].
