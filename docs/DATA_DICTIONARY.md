# Data Dictionary

This document describes all variables in the coded datasets.

## Dataset Files

| File | Description | Records |
|------|-------------|---------|
| `clean_research.csv` | Complete coded dataset | 7,660 |
| `empirical_clean.csv` | Empirical articles only | 5,441 |
| `clean_research_non_empirical.csv` | Non-empirical articles only | 2,219 |

---

## Scopus Metadata Fields (23 variables)

These fields are extracted directly from Scopus database exports.

| Variable | Description | Type | Example |
|----------|-------------|------|---------|
| `Authors` | Author names (abbreviated) | Text | "Zhang, Y., Li, X." |
| `Author full names` | Complete author names | Text | "Zhang, Yong; Li, Xiaoming" |
| `Author(s) ID` | Scopus author identifiers | Text | "57200123456;57200789012" |
| `Title` | Article title | Text | "Deep learning for urban..." |
| `Year` | Publication year | Integer | 2023 |
| `Source title` | Journal/source name | Text | "Sustainable Cities and Society" |
| `Volume` | Journal volume | Text | "85" |
| `Issue` | Journal issue | Text | "4" |
| `Art. No.` | Article number | Text | "104521" |
| `Page start` | Starting page | Integer | 1 |
| `Page end` | Ending page | Integer | 15 |
| `Cited by` | Citation count | Integer | 42 |
| `DOI` | Digital Object Identifier | Text | "10.1016/j.scs.2023.104521" |
| `Link` | Scopus article URL | URL | "https://www.scopus.com/..." |
| `Affiliations` | Author institutions | Text | "Tsinghua University, Beijing..." |
| `Authors with affiliations` | Linked author-affiliation | Text | "Zhang, Y., Tsinghua..." |
| `Abstract` | Article abstract | Text | "This study proposes..." |
| `Funding Texts` | Funding acknowledgments | Text | "This work was supported by..." |
| `Document Type` | Document type | Text | "Article" |
| `Publication Stage` | Publication status | Text | "Final" |
| `Open Access` | OA status | Text | "All Open Access; Gold" |
| `Source` | Database source | Text | "Scopus" |
| `EID` | Scopus unique identifier | Text | "2-s2.0-85123456789" |

---

## Coded Variables (15 variables)

These variables were coded through automated extraction, LLM-assisted classification, and manual verification.

### 1. Relevance Assessment

| Variable | Description | Values |
|----------|-------------|--------|
| `relevant` | Relevance to AI + Urban studies | Yes, No |

### 2. Geographic Classification

| Variable | Description | Values |
|----------|-------------|--------|
| `country_first_author` | Country of first author's institution | 109 countries (e.g., "China", "USA", "India") |

### 3. Subject Classification

| Variable | Description | Values | Count |
|----------|-------------|--------|-------|
| `subject_category` | Primary research subject area | 163 categories | e.g., "Transportation", "Land Use" |
| `subject_cluster` | Detailed subject clustering | 428 clusters | e.g., "Traffic & Congestion" |
| `subject_megatrend` | Broad thematic megatrend | 6 megatrends | See below |

#### Subject Megatrends

| Code | Megatrend | Description | % |
|------|-----------|-------------|---|
| DT | Digital Transformation & Smart Cities | Technology-driven urban innovation | 38.2% |
| CC | Climate Change & Environmental Sustainability | Environmental urban challenges | 26.1% |
| UM | Urban Mobility & Transportation | Movement and accessibility | 13.3% |
| UD | Urban Development & Land Use | Physical urban transformation | 9.6% |
| SE | Social Equity & Quality of Life | Human-centered urbanism | 7.5% |
| UR | Urban Resilience & Safety | Risk and security | 5.3% |

### 4. AI Methodology

| Variable | Description | Values |
|----------|-------------|--------|
| `ai_method` | AI/ML method(s) used | 16+ categories |
| `ai_task` | Primary AI task performed | 14+ categories |

#### AI Method Codes

| Code | Method | Description | % |
|------|--------|-------------|---|
| DL | Deep Learning | Multi-layer neural networks | 10.5% |
| ML | Machine Learning | General ML algorithms | 9.3% |
| CNN | Convolutional Neural Network | Image-focused deep learning | 5.7% |
| RF | Random Forest | Ensemble decision trees | 2.5% |
| NN | Neural Network | Basic neural networks | 2.1% |
| RL | Reinforcement Learning | Agent-based learning | 1.9% |
| LSTM | Long Short-Term Memory | Sequence modeling | 1.2% |
| ENS | Ensemble Methods | Combined models | 1.2% |
| XGB | XGBoost | Gradient boosting | 1.0% |
| GNN | Graph Neural Network | Network-structured data | 1.0% |
| TL | Transfer Learning | Pre-trained model adaptation | 0.9% |
| SVM | Support Vector Machine | Classification/regression | 0.7% |
| FL | Federated Learning | Distributed learning | 0.6% |
| GAN | Generative Adversarial Network | Data generation | 0.5% |
| NLP | Natural Language Processing | Text analysis | 0.5% |
| NS | Not Specified | Method not clearly stated | 3.9% |

#### AI Task Codes

| Code | Task | Description | % |
|------|------|-------------|---|
| PRD | Prediction/Forecasting | Future state estimation | 23.0% |
| CLS | Classification | Category assignment | 18.6% |
| OPT | Optimization | Finding optimal solutions | 8.1% |
| OBD | Object Detection | Identifying objects in images | 3.9% |
| SEG | Segmentation | Pixel-level classification | 2.8% |
| ANL | Analysis | Data analysis and insights | 2.8% |
| SIM | Simulation | System modeling | 2.0% |
| DET | Detection | Anomaly/event detection | 1.5% |
| CLU | Clustering | Group identification | 1.3% |
| REC | Recommendation | Suggesting options | 0.8% |
| GEN | Generation | Content creation | 0.6% |
| NS | Not Specified | Task not clearly stated | 3.3% |
| MUL | Multiple | Multiple tasks combined | 3.1% |

### 5. Article Characteristics

| Variable | Description | Values |
|----------|-------------|--------|
| `article_type` | Type of research contribution | 4 types |
| `methodological_approach` | Research methodology | 3 types |
| `spatial_scale` | Geographic scope | 6 scales |
| `temporal_scale` | Time orientation | 3 scales |
| `temporal_focus` | Data collection approach | 2 types |

#### Article Type Codes

| Code | Type | Description | % |
|------|------|-------------|---|
| EMP | Empirical | Original data collection and analysis | 71.0% |
| MTH | Methodological | New method or algorithm development | 19.7% |
| REV | Review/Survey | Literature review or survey | 6.2% |
| CON | Conceptual/Theoretical | Framework or theory development | 3.1% |

#### Methodological Approach Codes

| Code | Approach | Description | % |
|------|----------|-------------|---|
| QNT | Quantitative | Statistical/computational analysis | 82.5% |
| MIX | Mixed | Combined quantitative and qualitative | 10.8% |
| QAL | Qualitative | Interpretive/descriptive analysis | 6.7% |

#### Spatial Scale Codes

| Code | Scale | Description | % |
|------|-------|-------------|---|
| LOC | Local | City or neighborhood level | 80.2% |
| GLB | Global | Worldwide or multi-country | 7.4% |
| REG | Regional | Sub-national region | 4.5% |
| IND | Individual | Building or person level | 3.9% |
| NAT | National | Country level | 3.3% |
| SUP | Supranational | Multi-country region (EU, etc.) | 0.7% |

#### Temporal Scale Codes

| Code | Scale | Description | % |
|------|-------|-------------|---|
| PRS | Present | Current/recent time focus | 77.0% |
| FUT | Future | Projection/forecasting focus | 17.2% |
| PST | Past | Historical analysis | 5.8% |

#### Temporal Focus Codes

| Code | Focus | Description | % |
|------|-------|-------------|---|
| CRS | Cross-sectional | Single point in time | 74.3% |
| LNG | Longitudinal | Multiple time points | 25.7% |

### 6. Sustainability Assessment

| Variable | Description | Values |
|----------|-------------|--------|
| `sdg_alignment` | UN Sustainable Development Goal alignment | 17 SDGs |
| `level_of_sustainability` | Degree of sustainability integration | 3 levels |

#### SDG Alignment Codes

| Code | SDG | Full Name | % |
|------|-----|-----------|---|
| SDG1 | SDG 1 | No Poverty | 0.1% |
| SDG2 | SDG 2 | Zero Hunger | 0.2% |
| SDG3 | SDG 3 | Good Health and Well-being | 5.9% |
| SDG4 | SDG 4 | Quality Education | 0.2% |
| SDG5 | SDG 5 | Gender Equality | 0.1% |
| SDG6 | SDG 6 | Clean Water and Sanitation | 1.9% |
| SDG7 | SDG 7 | Affordable and Clean Energy | 6.0% |
| SDG8 | SDG 8 | Decent Work and Economic Growth | 0.3% |
| SDG9 | SDG 9 | Industry, Innovation and Infrastructure | 8.7% |
| SDG10 | SDG 10 | Reduced Inequalities | 0.8% |
| SDG11 | SDG 11 | Sustainable Cities and Communities | 71.6% |
| SDG12 | SDG 12 | Responsible Consumption and Production | 0.5% |
| SDG13 | SDG 13 | Climate Action | 2.3% |
| SDG14 | SDG 14 | Life Below Water | 0.0% |
| SDG15 | SDG 15 | Life on Land | 0.8% |
| SDG16 | SDG 16 | Peace, Justice and Strong Institutions | 0.7% |

#### Sustainability Integration Level Codes

| Code | Level | Description | Criteria | % |
|------|-------|-------------|----------|---|
| STR | Strong | Explicit sustainability framework | Explicit SDG reference; impact assessment; long-term considerations | 43.9% |
| MED | Medium | Implicit sustainability considerations | Efficiency improvements; resource optimization | 41.6% |
| WEK | Weak | Technical focus without sustainability | Purely technical; no sustainability mention | 14.6% |

---

## Derived Analysis Variables

Additional variables computed for analysis:

| Variable | Description | Source |
|----------|-------------|--------|
| `has_funding` | Whether article has funding acknowledgment | Derived from `Funding Texts` |
| `is_open_access` | Whether article is open access | Derived from `Open Access` |
| `citation_quartile` | Citation quartile within dataset | Derived from `Cited by` |

---

## Missing Data

| Variable | Missing Rate | Handling |
|----------|--------------|----------|
| `Abstract` | 0% | Required for inclusion |
| `Funding Texts` | 56.1% | Coded as "No Funding" |
| `DOI` | 1.4% | Not imputed |
| `Cited by` | 0% | Zero citations coded as 0 |

---

## Data Quality Notes

1. **Country Attribution**: Based on first author's institutional affiliation
2. **SDG Alignment**: Single primary SDG assigned per article
3. **AI Method**: May contain multiple methods separated by commas
4. **Temporal Coverage**: Publication years 2020-2025
5. **Language**: English-language articles only
6. **Document Type**: Peer-reviewed journal articles only

---

*Data Dictionary for AI in Urban Studies Systematic Review (2020-2025)*
