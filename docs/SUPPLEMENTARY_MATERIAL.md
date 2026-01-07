# Supplementary Material

**Artificial Intelligence in Urban Studies: A Systematic Review of Research Trajectories, Methodological Patterns, and Sustainability Orientations (2020-2025)**

---

## Table of Contents

1. [Extended Methodology](#1-extended-methodology)
2. [Non-Empirical Research Analysis](#2-non-empirical-research-analysis)
3. [Supplementary Tables](#3-supplementary-tables)
4. [Supplementary Figures](#4-supplementary-figures)

---

# 1. Extended Methodology

## 1.1 Systematic Review Protocol

This systematic literature review follows the PRISMA 2020 (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines. The review protocol was designed to comprehensively capture the intersection of artificial intelligence and urban studies research published between 2020 and 2025.

### Figure S1: PRISMA Flow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        IDENTIFICATION                           │
├─────────────────────────────────────────────────────────────────┤
│  Records identified through Scopus database search              │
│  (n = 8,430)                                                    │
│  • 2020: 618    • 2023: 1,363                                   │
│  • 2021: 921    • 2024: 1,801                                   │
│  • 2022: 1,188  • 2025: 2,539                                   │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                        SCREENING                                │
├─────────────────────────────────────────────────────────────────┤
│  Records screened for relevance                                 │
│  (n = 8,430)                                                    │
│                                                                 │
│  Exclusion criteria applied:                                    │
│  • Not relevant to AI + Urban studies (n = 770)                 │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                        ELIGIBILITY                              │
├─────────────────────────────────────────────────────────────────┤
│  Full-text articles assessed for eligibility                    │
│  (n = 7,660)                                                    │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                         INCLUDED                                │
├─────────────────────────────────────────────────────────────────┤
│  Studies included in quantitative synthesis                     │
│  (n = 7,660)                                                    │
│                                                                 │
│  Split into:                                                    │
│  • Empirical studies (n = 5,441, 71.0%)                         │
│  • Non-empirical studies (n = 2,219, 29.0%)                     │
└─────────────────────────────────────────────────────────────────┘
```

## 1.2 Database Selection Rationale

**Scopus** was selected as the primary database for this systematic review based on several considerations:

- **Comprehensive disciplinary coverage**: Scopus provides strong indexing of engineering, computer science, environmental science, and urban studies journals—the core disciplines at the intersection of AI and urban research
- **Rigorous content selection**: The database employs an independent Content Selection and Advisory Board that applies consistent quality criteria
- **Structured metadata**: Scopus exports include standardized fields essential for systematic analysis, including funding acknowledgments, author affiliations, and citation data
- **Established use in bibliometric research**: Scopus has been validated as a reliable source for large-scale research assessments and systematic reviews

The database indexes over 27,000 peer-reviewed journals from more than 7,000 publishers, ensuring comprehensive coverage of the relevant literature.

## 1.3 Complete Search String

The following search string was executed in Scopus to identify relevant articles:

```
TITLE-ABS-KEY (
  (
    "AI" OR "A.I." OR "Artificial Intelligence" OR
    "Machine Learning" OR "Deep Learning" OR
    "Neural Network*" OR "CNN" OR "Convolutional Neural Network*" OR
    "Recurrent Neural Network*" OR "RNN" OR "LSTM" OR
    "Random Forest" OR "Support Vector Machine*" OR "SVM" OR
    "Reinforcement Learning" OR "Computer Vision" OR
    "Natural Language Processing" OR "NLP" OR
    "Predictive Model*" OR "Classification Algorithm*" OR
    "Clustering Algorithm*" OR "Regression Model*" OR
    "Ensemble Learning" OR "Transfer Learning" OR
    "Generative Adversarial Network*" OR "GAN" OR
    "Graph Neural Network*" OR "GNN" OR
    "Transformer" OR "BERT" OR "GPT"
  )
  AND
  (
    "Urban" OR "City" OR "Cities" OR "Smart City" OR "Smart Cities" OR
    "Metropolitan" OR "Municipal" OR "Town" OR
    "Urban Planning" OR "Urban Development" OR "Urban Design" OR
    "Urban Environment" OR "Urban Infrastructure" OR
    "Urban Transport*" OR "Urban Mobility" OR "Urban Traffic" OR
    "Urban Sustainability" OR "Sustainable City" OR "Sustainable Cities" OR
    "Urban Governance" OR "Urban Management" OR
    "Urban Health" OR "Urban Climate" OR "Urban Heat" OR
    "Urban Land" OR "Land Use" OR "Urban Growth" OR "Urban Expansion" OR
    "Urban Safety" OR "Urban Security" OR "Urban Crime" OR
    "Urban Energy" OR "Urban Water" OR "Urban Waste"
  )
)
AND PUBYEAR > 2019 AND PUBYEAR < 2026
AND DOCTYPE(ar)
AND LANGUAGE(english)
```

### Table S1: Search Filters Applied

| Filter | Value |
|--------|-------|
| Database | Scopus |
| Publication Years | 2020-2025 |
| Document Type | Article |
| Language | English |
| Search Fields | Title, Abstract, Keywords |

## 1.4 Inclusion and Exclusion Criteria

### Table S2: Inclusion Criteria

| Code | Criterion | Description |
|------|-----------|-------------|
| IC1 | Publication type | Peer-reviewed journal articles |
| IC2 | Temporal scope | Published between January 2020 and December 2025 |
| IC3 | Thematic focus | Focus on AI/ML applications in urban contexts |
| IC4 | Language | Written in English |
| IC5 | Content quality | Contains abstract with sufficient methodological information |
| IC6 | Contribution type | Presents original research, methodology, or systematic review |

### Table S3: Exclusion Criteria

| Code | Criterion | Description | Articles Excluded |
|------|-----------|-------------|-------------------|
| EC1 | Document type | Conference papers, book chapters, editorials, letters | Pre-filtered in Scopus |
| EC2 | Thematic relevance | Non-urban AI applications (purely medical, agricultural without urban link) | ~400 |
| EC3 | Methodological clarity | Articles without clear AI/ML methodology | ~250 |
| EC4 | Duplication | Duplicate entries | ~50 |
| EC5 | Language | Non-English publications | Pre-filtered in Scopus |
| EC6 | Tangential mention | Articles with only tangential mention of AI or urban topics | ~70 |
| **Total** | | | **770** |

## 1.5 Data Extraction Framework

### Table S4: Scopus Metadata Fields Extracted

| # | Field Name | Description | Data Type |
|---|------------|-------------|-----------|
| 1 | Authors | Author names (abbreviated format) | Text |
| 2 | Author full names | Complete author names | Text |
| 3 | Author(s) ID | Scopus author identifiers | Numeric |
| 4 | Title | Article title | Text |
| 5 | Year | Publication year | Numeric |
| 6 | Source title | Journal/source name | Text |
| 7 | Volume | Journal volume number | Text |
| 8 | Issue | Journal issue number | Text |
| 9 | Art. No. | Article number | Text |
| 10 | Page start | Starting page | Numeric |
| 11 | Page end | Ending page | Numeric |
| 12 | Cited by | Citation count | Numeric |
| 13 | DOI | Digital Object Identifier | Text |
| 14 | Link | Scopus article URL | URL |
| 15 | Affiliations | Author institutional affiliations | Text |
| 16 | Authors with affiliations | Linked author-affiliation data | Text |
| 17 | Abstract | Article abstract | Text |
| 18 | Funding Texts | Funding acknowledgments | Text |
| 19 | Document Type | Type of document (Article) | Text |
| 20 | Publication Stage | Final/In Press | Text |
| 21 | Open Access | Open access status | Text |
| 22 | Source | Database source (Scopus) | Text |
| 23 | EID | Scopus unique identifier | Text |

### Table S5: Data Quality Metrics

| Metric | Value | Percentage |
|--------|-------|------------|
| Articles with DOI | 7,555 | 98.6% |
| Articles with Abstract | 7,660 | 100% |
| Open Access articles | 4,225 | 55.2% |
| Articles with Funding information | 3,365 | 43.9% |
| Articles with Author affiliations | 7,658 | 99.97% |

## 1.6 Complete Coding Scheme

A total of **15 variables** were coded for each article through a combination of automated extraction, LLM-assisted classification, and manual verification.

### Table S6: Complete Coding Scheme Overview

| # | Category | Variable Name | Description | Codes/Values | Coding Method |
|---|----------|---------------|-------------|--------------|---------------|
| 1 | Relevance | relevant | Relevance to AI + Urban studies | Yes, No | Manual screening |
| 2 | Geography | country_first_author | Country of first author's institution | 109 countries | Automated + Manual |
| 3 | Subject Classification | subject_category | Primary research subject area | 163 categories | LLM-assisted coding |
| 4 | Subject Classification | subject_cluster | Detailed subject clustering | 428 clusters | LLM-assisted coding |
| 5 | Subject Classification | subject_megatrend | Broad thematic megatrend | 6 megatrends | Hierarchical clustering |
| 6 | AI Methodology | ai_method | AI/ML method(s) used | 16 categories | Keyword extraction + Manual |
| 7 | AI Methodology | ai_task | Primary AI task performed | 14 categories | Keyword extraction + Manual |
| 8 | Research Focus | main_goal | Primary research objective | Open-ended | LLM-assisted extraction |
| 9 | Sustainability | sdg_alignment | UN Sustainable Development Goal alignment | 17 SDGs | LLM-assisted + Manual |
| 10 | Article Characteristics | article_type | Type of research contribution | 4 types | Manual coding |
| 11 | Article Characteristics | methodological_approach | Research methodology type | 3 types | Manual coding |
| 12 | Spatial-Temporal | spatial_scale | Geographic scope of study | 6 scales | Manual coding |
| 13 | Spatial-Temporal | temporal_scale | Time orientation | 3 scales | Manual coding |
| 14 | Spatial-Temporal | temporal_focus | Data collection approach | 2 types | Manual coding |
| 15 | Sustainability | level_of_sustainability | Degree of sustainability integration | 3 levels | Manual coding |

### Table S7: AI Method Codes

| Code | AI Method | Description | Example Applications | Count | % |
|------|-----------|-------------|---------------------|-------|---|
| DL | Deep Learning | Multi-layer neural networks | Image recognition, pattern detection | 802 | 10.5% |
| ML | Machine Learning | General ML algorithms | Prediction, classification | 716 | 9.3% |
| CNN | Convolutional Neural Network | Image-focused deep learning | Satellite imagery, object detection | 436 | 5.7% |
| RF | Random Forest | Ensemble decision trees | Land use classification, prediction | 188 | 2.5% |
| NN | Neural Network | Basic neural networks | Pattern recognition | 158 | 2.1% |
| RL | Reinforcement Learning | Agent-based learning | Traffic optimization, resource allocation | 145 | 1.9% |
| LSTM | Long Short-Term Memory | Sequence modeling | Time series prediction, traffic forecasting | 93 | 1.2% |
| ENS | Ensemble Methods | Combined models | Improved accuracy predictions | 91 | 1.2% |
| XGB | XGBoost | Gradient boosting | Tabular data prediction | 79 | 1.0% |
| GNN | Graph Neural Network | Network-structured data | Transportation networks, social networks | 75 | 1.0% |
| TL | Transfer Learning | Pre-trained model adaptation | Limited data scenarios | 67 | 0.9% |
| SVM | Support Vector Machine | Classification/regression | Land cover classification | 54 | 0.7% |
| FL | Federated Learning | Distributed learning | Privacy-preserving urban analytics | 48 | 0.6% |
| GAN | Generative Adversarial Network | Data generation | Urban simulation, image synthesis | 42 | 0.5% |
| NLP | Natural Language Processing | Text analysis | Policy analysis, social media mining | 38 | 0.5% |
| NS | Not Specified | Method not clearly stated | - | 297 | 3.9% |

### Table S8: AI Task Codes

| Code | AI Task | Description | Example Applications | Count | % |
|------|---------|-------------|---------------------|-------|---|
| PRD | Prediction/Forecasting | Future state estimation | Traffic flow, energy demand, air quality | 1,760 | 23.0% |
| CLS | Classification | Category assignment | Land use, building type, vehicle type | 1,425 | 18.6% |
| OPT | Optimization | Finding optimal solutions | Route planning, resource allocation | 621 | 8.1% |
| OBD | Object Detection | Identifying objects in images | Vehicles, buildings, pedestrians | 295 | 3.9% |
| SEG | Segmentation | Pixel-level classification | Urban area mapping, road extraction | 215 | 2.8% |
| ANL | Analysis | Data analysis and insights | Pattern discovery, trend analysis | 212 | 2.8% |
| SIM | Simulation | System modeling | Urban growth, traffic simulation | 154 | 2.0% |
| DET | Detection | Anomaly/event detection | Crime hotspots, pollution events | 117 | 1.5% |
| CLU | Clustering | Group identification | Urban typologies, behavior patterns | 98 | 1.3% |
| REC | Recommendation | Suggesting options | Route, location, policy recommendations | 65 | 0.8% |
| GEN | Generation | Content creation | Synthetic data, urban designs | 45 | 0.6% |
| NS | Not Specified | Task not clearly stated | - | 256 | 3.3% |
| MUL | Multiple | Multiple tasks combined | - | 234 | 3.1% |

### Table S9: Article Type Codes

| Code | Article Type | Description | Criteria | Count | % |
|------|--------------|-------------|----------|-------|---|
| EMP | Empirical | Original data collection and analysis | Contains primary data, case studies, experiments | 5,441 | 71.0% |
| MTH | Methodological | New method or algorithm development | Proposes new AI method, framework, or system | 1,508 | 19.7% |
| REV | Review/Survey | Literature review or survey | Synthesizes existing research | 472 | 6.2% |
| CON | Conceptual/Theoretical | Framework or theory development | Proposes concepts without empirical testing | 239 | 3.1% |

### Table S10: Methodological Approach Codes

| Code | Approach | Description | Typical Methods | Count | % |
|------|----------|-------------|-----------------|-------|---|
| QNT | Quantitative | Statistical/computational analysis | ML models, statistical analysis, simulations | 6,321 | 82.5% |
| MIX | Mixed | Combined quantitative and qualitative | Surveys + ML, interviews + analysis | 824 | 10.8% |
| QAL | Qualitative | Interpretive/descriptive analysis | Case studies, expert interviews, policy analysis | 514 | 6.7% |

### Table S11: Spatial Scale Codes

| Code | Scale | Description | Examples | Count | % |
|------|-------|-------------|----------|-------|---|
| LOC | Local | City or neighborhood level | Single city case study, district analysis | 6,147 | 80.2% |
| GLB | Global | Worldwide or multi-country | Cross-country comparison, global datasets | 567 | 7.4% |
| REG | Regional | Sub-national region | Province, state, metropolitan area | 346 | 4.5% |
| IND | Individual | Building or person level | Individual building, personal mobility | 297 | 3.9% |
| NAT | National | Country level | National urban systems, country-wide analysis | 251 | 3.3% |
| SUP | Supranational | Multi-country region | EU, ASEAN, continental analysis | 50 | 0.7% |

### Table S12: Level of Sustainability Integration Codes

| Code | Level | Description | Criteria | Count | % |
|------|-------|-------------|----------|-------|---|
| STR | Strong | Explicit sustainability framework | Explicit reference to sustainability goals/SDGs; Environmental/social impact assessment; Long-term sustainability considerations; Policy implications for sustainability | 3,359 | 43.9% |
| MED | Medium | Implicit sustainability considerations | Efficiency improvements mentioned; Resource optimization focus; Environmental monitoring without explicit sustainability framing; Indirect sustainability benefits | 3,184 | 41.6% |
| WEK | Weak | Technical focus without sustainability | Purely technical/methodological focus; No mention of sustainability implications; Short-term optimization only; No environmental/social considerations | 1,116 | 14.6% |

### Table S13: SDG Alignment Codes

| Code | SDG | Full Name | Urban Relevance | Count | % |
|------|-----|-----------|-----------------|-------|---|
| SDG1 | SDG 1 | No Poverty | Urban poverty, informal settlements | 8 | 0.1% |
| SDG2 | SDG 2 | Zero Hunger | Urban food systems, food security | 17 | 0.2% |
| SDG3 | SDG 3 | Good Health and Well-being | Urban health, air quality, healthcare access | 455 | 5.9% |
| SDG4 | SDG 4 | Quality Education | Educational infrastructure, smart campuses | 14 | 0.2% |
| SDG5 | SDG 5 | Gender Equality | Gender-inclusive urban planning | 4 | 0.1% |
| SDG6 | SDG 6 | Clean Water and Sanitation | Urban water systems, wastewater | 144 | 1.9% |
| SDG7 | SDG 7 | Affordable and Clean Energy | Urban energy, smart grids, renewables | 457 | 6.0% |
| SDG8 | SDG 8 | Decent Work and Economic Growth | Urban economy, employment | 20 | 0.3% |
| SDG9 | SDG 9 | Industry, Innovation and Infrastructure | Urban infrastructure, smart systems | 665 | 8.7% |
| SDG10 | SDG 10 | Reduced Inequalities | Urban equity, accessibility | 60 | 0.8% |
| SDG11 | SDG 11 | Sustainable Cities and Communities | Urban sustainability, planning, transport | 5,485 | 71.6% |
| SDG12 | SDG 12 | Responsible Consumption and Production | Waste management, circular economy | 40 | 0.5% |
| SDG13 | SDG 13 | Climate Action | Urban climate, heat islands, emissions | 175 | 2.3% |
| SDG14 | SDG 14 | Life Below Water | Coastal urban areas, marine urban interface | 2 | 0.0% |
| SDG15 | SDG 15 | Life on Land | Urban green spaces, biodiversity | 58 | 0.8% |
| SDG16 | SDG 16 | Peace, Justice and Strong Institutions | Urban safety, governance, crime | 56 | 0.7% |

### Table S14: Subject Megatrend Codes

| Code | Megatrend | Description | Key Topics | Count | % |
|------|-----------|-------------|------------|-------|---|
| DT | Digital Transformation & Smart Cities | Technology-driven urban innovation | IoT, digital twins, smart infrastructure, sensors | 2,927 | 38.2% |
| CC | Climate Change & Environmental Sustainability | Environmental urban challenges | Air quality, carbon emissions, green infrastructure, UHI | 1,996 | 26.1% |
| UM | Urban Mobility & Transportation | Movement and accessibility | Traffic prediction, autonomous vehicles, public transit | 1,018 | 13.3% |
| UD | Urban Development & Land Use | Physical urban transformation | Land cover change, urban expansion, zoning | 733 | 9.6% |
| SE | Social Equity & Quality of Life | Human-centered urbanism | Public health, accessibility, well-being, equity | 578 | 7.5% |
| UR | Urban Resilience & Safety | Risk and security | Disaster management, crime prediction, emergency response | 408 | 5.3% |

## 1.7 Coding Process and Quality Assurance

The coding process employed a multi-stage workflow combining automated extraction, LLM-assisted classification, and manual verification:

**Stage 1: Automated Extraction**
- Country attribution from author affiliations
- AI method keyword matching from title/abstract
- AI task keyword extraction
- Initial SDG classification based on keyword presence

**Stage 2: LLM-Assisted Classification**
- Subject category assignment using large language model
- Subject cluster identification
- Main goal extraction from abstracts
- SDG alignment verification and refinement

**Stage 3: Manual Coding**
- Article type classification
- Methodological approach determination
- Spatial and temporal scale assessment
- Sustainability level evaluation
- Quality control verification

**Stage 4: Validation**
- Random 10% sample double-coded by independent reviewers
- Inter-coder reliability assessment with discrepancy resolution
- Automated consistency checks for logical inconsistencies
- Domain expert review of complete coding scheme

### Table S15: Quality Assurance Measures

| Quality Measure | Description | Implementation |
|-----------------|-------------|----------------|
| Double coding | Independent verification of coding accuracy | 10% random sample coded by two reviewers |
| Consistency checks | Logical validation of coded values | Automated checks for incompatible code combinations |
| Outlier review | Examination of edge cases | Manual review of articles with unusual coding patterns |
| Expert validation | Domain expertise verification | Review of coding scheme by urban studies and AI experts |

---

# 2. Non-Empirical Research Analysis

The main article focuses on the 5,441 empirical studies that present original data collection and analysis. This supplementary section provides comprehensive analysis of the 2,219 non-empirical articles (29.0% of the corpus) comprising methodological contributions, systematic reviews/surveys, and conceptual/theoretical frameworks. Non-empirical research plays a critical role in shaping the field's theoretical foundations, methodological innovations, and research directions.

## 2.1 Overview of Non-Empirical Research

Non-empirical articles in our corpus serve three primary functions: developing new AI methods and frameworks for urban applications (methodological), synthesizing existing knowledge to identify research gaps and trends (reviews/surveys), and proposing theoretical frameworks for understanding AI-urban interactions (conceptual). These contributions, while not presenting primary data, fundamentally shape how the field develops and are often highly cited reference works.

### Table S16: Non-Empirical Article Composition

| Article Type | Count | Percentage | Description |
|--------------|-------|------------|-------------|
| Methodological | 1,508 | 68.0% | New AI method or framework development |
| Review/Survey | 472 | 21.3% | Literature synthesis and trend analysis |
| Conceptual/Theoretical | 239 | 10.8% | Framework or theory development |
| **Total** | **2,219** | **100%** | |

The dominance of methodological articles (68.0%) reflects the rapid evolution of AI techniques and the continuous development of urban-specific adaptations. Review articles, though fewer in number, demonstrate substantial citation impact, with the top 10 most-cited non-empirical articles averaging 491 citations compared to 24.4 for the non-empirical corpus overall.

## 2.2 Temporal Trends

Non-empirical research has grown substantially over the study period, though with different patterns than empirical research. The temporal distribution reveals peak activity in 2023 (37.4% of non-empirical articles), potentially reflecting the lag between methodological innovation and systematic synthesis of emerging fields.

### Table S17: Annual Distribution of Non-Empirical Articles

| Year | Articles | % of Total | Year-over-Year Growth |
|------|----------|------------|----------------------|
| 2020 | 97 | 4.4% | - |
| 2021 | 293 | 13.2% | +202.1% |
| 2022 | 287 | 12.9% | -2.0% |
| 2023 | 829 | 37.4% | +188.9% |
| 2024 | 186 | 8.4% | -77.6% |
| 2025 | 527 | 23.7% | +183.3% |

The substantial spike in 2023 corresponds to the maturation of deep learning applications in urban contexts and the emergence of foundation models (large language models, vision transformers), prompting both methodological innovation and comprehensive reviews of the rapidly evolving landscape.

## 2.3 Geographic Distribution

Geographic patterns in non-empirical research largely mirror empirical production, with China and India maintaining dominant positions. However, notable differences emerge in the relative contributions of specific countries, reflecting differential research priorities and institutional capacities for theoretical and methodological work.

### Table S18: Top 15 Countries in Non-Empirical Research

| Rank | Country | Articles | % of Total | Comparison to Empirical % |
|------|---------|----------|------------|---------------------------|
| 1 | China | 747 | 33.7% | -3.5% |
| 2 | India | 258 | 11.6% | +0.1% |
| 3 | USA | 123 | 5.5% | 0% |
| 4 | Saudi Arabia | 100 | 4.5% | +0.5% |
| 5 | UK | 66 | 3.0% | -0.3% |
| 6 | South Korea | 64 | 2.9% | +0.2% |
| 7 | Italy | 63 | 2.8% | +0.1% |
| 8 | Spain | 39 | 1.8% | +0.3% |
| 9 | Germany | 39 | 1.8% | +0.1% |
| 10 | Pakistan | 38 | 1.7% | +0.1% |
| 11 | Australia | 37 | 1.7% | -0.3% |
| 12 | Singapore | 37 | 1.7% | +0.5% |
| 13 | Portugal | 34 | 1.5% | +0.3% |
| 14 | Morocco | 29 | 1.3% | +0.2% |
| 15 | Canada | 27 | 1.2% | -0.1% |

Saudi Arabia and Singapore show notably higher proportions in non-empirical research compared to their empirical contributions, suggesting strategic investment in developing methodological frameworks for smart city initiatives. Singapore's strong showing (1.7% vs. 1.2% in empirical) reflects its position as a testbed for urban AI innovation and its emphasis on developing transferable frameworks.

## 2.4 Thematic Structure

Non-empirical research exhibits a distinct thematic profile emphasizing infrastructure and security topics that require methodological innovation before empirical deployment.

### Table S19: Subject Megatrend Distribution in Non-Empirical Research

| Megatrend | Articles | % of Total | Comparison to Empirical |
|-----------|----------|------------|-------------------------|
| Digital Transformation & Smart Cities | 875 | 39.4% | +1.2% |
| Urban Mobility & Transportation | 479 | 21.6% | +8.3% |
| Climate Change & Environmental Sustainability | 350 | 15.8% | -10.3% |
| Urban Development & Land Use | 227 | 10.2% | +0.6% |
| Urban Resilience & Safety | 180 | 8.1% | +2.8% |
| Social Equity & Quality of Life | 108 | 4.9% | -3.0% |

**Key Observations:**

The substantially higher proportion of Mobility & Transportation research in non-empirical studies (+8.3 percentage points versus empirical) reflects the methodological intensity of autonomous vehicle research, traffic prediction frameworks, and intelligent transportation system architectures. Conversely, Climate Change & Environmental Sustainability shows notably lower non-empirical representation (-10.3 points), suggesting this domain relies more heavily on empirical data collection and monitoring applications than on novel algorithmic development.

Urban Resilience & Safety shows higher non-empirical representation (+2.8 points), driven by cybersecurity framework development (88 articles) and disaster management methodologies—domains where theoretical and architectural contributions precede implementation.

### Table S20: Top 20 Subject Categories in Non-Empirical Research

| Rank | Subject Category | Articles | % of Total |
|------|------------------|----------|------------|
| 1 | Transportation | 482 | 21.7% |
| 2 | Infrastructure | 176 | 7.9% |
| 3 | Land Use | 154 | 6.9% |
| 4 | Safety/Crime | 133 | 6.0% |
| 5 | Governance | 127 | 5.7% |
| 6 | Urban Design | 115 | 5.2% |
| 7 | Other | 102 | 4.6% |
| 8 | Environment | 101 | 4.6% |
| 9 | Energy | 81 | 3.7% |
| 10 | Urban Climate | 49 | 2.2% |
| 11 | Safety | 38 | 1.7% |
| 12 | Digital Infrastructure and IoT | 37 | 1.7% |
| 13 | Water | 30 | 1.4% |
| 14 | Waste Management | 29 | 1.3% |
| 15 | Public Health | 27 | 1.2% |
| 16 | Transportation and Mobility | 26 | 1.2% |
| 17 | Urban Governance | 22 | 1.0% |
| 18 | ICT Infrastructure | 21 | 0.9% |
| 19 | Urban Sensing | 21 | 0.9% |
| 20 | Urban Security & Surveillance | 21 | 0.9% |

The prominence of Transportation (21.7%) in non-empirical research—substantially higher than in empirical work—reflects the methodological complexity of traffic prediction, autonomous navigation, and multimodal transportation optimization. These applications require sophisticated algorithm development and architectural innovation before empirical deployment.

## 2.5 SDG Alignment

Non-empirical research demonstrates somewhat stronger engagement with infrastructure-related SDGs, reflecting the methodological focus on developing systems and frameworks.

### Table S21: SDG Alignment in Non-Empirical Research

| SDG | Full Name | Articles | % of Total | Diff. from Empirical |
|-----|-----------|----------|------------|---------------------|
| 11 | Sustainable Cities and Communities | 1,508 | 68.0% | -3.6% |
| 9 | Industry, Innovation and Infrastructure | 337 | 15.2% | +6.5% |
| 7 | Affordable and Clean Energy | 132 | 5.9% | -0.1% |
| 3 | Good Health and Well-being | 82 | 3.7% | -2.2% |
| 16 | Peace, Justice and Strong Institutions | 40 | 1.8% | +1.1% |
| 6 | Clean Water and Sanitation | 32 | 1.4% | -0.5% |
| 13 | Climate Action | 31 | 1.4% | -0.9% |
| 12 | Responsible Consumption and Production | 20 | 0.9% | +0.4% |
| 10 | Reduced Inequalities | 13 | 0.6% | -0.2% |
| 15 | Life on Land | 12 | 0.5% | -0.3% |
| 8 | Decent Work and Economic Growth | 5 | 0.2% | -0.1% |
| 4 | Quality Education | 4 | 0.2% | 0% |
| 2 | Zero Hunger | 3 | 0.1% | -0.1% |

The notably higher SDG 9 (Industry, Innovation and Infrastructure) alignment in non-empirical research (+6.5 percentage points) reflects the emphasis on developing infrastructure-oriented methodologies, smart city architectures, and digital twin frameworks. This pattern aligns with the methodological nature of these contributions—they focus on building the technical foundations upon which empirical applications operate.

SDG 16 (Peace, Justice and Strong Institutions) also shows higher non-empirical representation (+1.1 points), driven by cybersecurity frameworks and urban governance architectures that require theoretical development before implementation.

## 2.6 AI Methods and Tasks

Non-empirical research exhibits distinctive methodological patterns reflecting its focus on framework development and system architecture rather than empirical application.

### Table S22: Top 15 AI Methods in Non-Empirical Research

| Rank | AI Method | Articles | % of Total | Diff. from Empirical |
|------|-----------|----------|------------|---------------------|
| 1 | Deep Learning | 237 | 10.7% | +0.2% |
| 2 | Not Specified | 161 | 7.3% | +3.4% |
| 3 | Machine Learning | 111 | 5.0% | -4.3% |
| 4 | CNN | 90 | 4.1% | -1.6% |
| 5 | Reinforcement Learning | 27 | 1.2% | -0.7% |
| 6 | GNN | 24 | 1.1% | +0.1% |
| 7 | Machine Learning, Deep Learning | 23 | 1.0% | +0.1% |
| 8 | Other ML | 22 | 1.0% | -0.2% |
| 9 | LSTM | 18 | 0.8% | -0.4% |
| 10 | Not Coverage | 18 | 0.8% | +0.1% |
| 11 | CNN, Deep Learning | 17 | 0.8% | +0.1% |
| 12 | AI | 16 | 0.7% | +0.2% |
| 13 | Transformer | 15 | 0.7% | +0.2% |
| 14 | Deep Learning, CNN | 15 | 0.7% | +0.1% |
| 15 | Federated Learning | 14 | 0.6% | +0.1% |

The higher proportion of "Not Specified" methods (+3.4 points) in non-empirical research reflects the nature of review articles and conceptual frameworks that discuss AI broadly rather than applying specific techniques. The relatively higher representation of emerging methods like Transformers (+0.2 points) and Federated Learning (+0.1 points) indicates that non-empirical work often introduces cutting-edge approaches to the urban AI discourse before widespread empirical adoption.

### Table S23: Top 15 AI Tasks in Non-Empirical Research

| Rank | AI Task | Articles | % of Total | Diff. from Empirical |
|------|---------|----------|------------|---------------------|
| 1 | Classification | 394 | 17.8% | -0.8% |
| 2 | Prediction/Forecasting | 389 | 17.5% | -5.5% |
| 3 | Not Specified | 199 | 9.0% | +5.7% |
| 4 | Optimization | 181 | 8.2% | +0.1% |
| 5 | Multiple | 121 | 5.5% | +2.4% |
| 6 | Segmentation | 95 | 4.3% | +1.5% |
| 7 | Object Detection | 87 | 3.9% | 0% |
| 8 | Analysis | 47 | 2.1% | -0.7% |
| 9 | Simulation | 34 | 1.5% | -0.5% |
| 10 | Clustering | 27 | 1.2% | -0.1% |
| 11 | Classification, Anomaly Detection | 23 | 1.0% | +0.2% |
| 12 | NLP/Text Analysis | 22 | 1.0% | +0.5% |
| 13 | Detection | 21 | 0.9% | -0.6% |
| 14 | Anomaly Detection | 21 | 0.9% | +0.1% |
| 15 | Prediction | 19 | 0.9% | -0.3% |

The notably lower Prediction/Forecasting representation (-5.5 points) and higher "Not Specified" (+5.7 points) and "Multiple" (+2.4 points) categories reflect the broader, more integrative nature of non-empirical contributions. Reviews and conceptual papers often discuss multiple tasks or address AI capabilities at a general level rather than applying specific prediction models.

## 2.7 Research Characteristics

### Table S24: Methodological Approach Comparison

| Approach | Non-Empirical | Empirical | Difference |
|----------|---------------|-----------|------------|
| Quantitative | 70.9% | 86.4% | -15.5% |
| Qualitative | 19.7% | 3.1% | +16.6% |
| Mixed | 9.4% | 10.5% | -1.1% |

The substantially higher qualitative proportion in non-empirical research (+16.6 points) reflects the nature of review articles, conceptual frameworks, and theoretical contributions that synthesize existing knowledge through interpretive analysis rather than quantitative modeling.

### Table S25: Spatial Scale Comparison

| Scale | Non-Empirical | Empirical | Difference |
|-------|---------------|-----------|------------|
| Local | 83.0% | 79.0% | +4.0% |
| Global | 9.6% | 6.5% | +3.1% |
| Individual | 4.1% | 3.8% | +0.3% |
| Regional | 1.5% | 5.6% | -4.1% |
| National | 1.3% | 4.2% | -2.9% |
| Supranational | 0.5% | 0.9% | -0.4% |

Non-empirical research shows higher global-scale representation (+3.1 points), reflecting the tendency of reviews and conceptual frameworks to synthesize international research and develop globally applicable frameworks. The lower regional and national representation indicates that empirical studies more frequently address specific sub-national policy contexts.

### Table S26: Temporal Focus Comparison

| Focus | Non-Empirical | Empirical | Difference |
|-------|---------------|-----------|------------|
| Cross-sectional | 78.1% | 72.6% | +5.5% |
| Longitudinal | 21.9% | 27.4% | -5.5% |

The higher cross-sectional proportion in non-empirical research reflects the nature of methodological proposals and reviews that typically present framework snapshots rather than tracking implementation over time.

## 2.8 Sustainability Assessment

### Table S27: Sustainability Integration Levels

| Level | Non-Empirical | Empirical | Difference |
|-------|---------------|-----------|------------|
| Strong | 33.7% | 47.5% | -13.8% |
| Medium | 49.8% | 38.9% | +10.9% |
| Weak | 16.5% | 13.6% | +2.9% |

Non-empirical research demonstrates notably weaker sustainability integration compared to empirical studies (-13.8 points in "Strong" integration). This pattern suggests that methodological innovation and framework development often prioritize technical performance metrics over explicit sustainability considerations. Methodological articles in particular tend to emphasize algorithmic improvements rather than sustainability outcomes, creating a potential disconnect between technical advancement and sustainable urban development goals.

This finding has implications for research policy: funders and reviewers might explicitly encourage sustainability framing in methodological contributions to ensure that novel AI approaches are developed with urban sustainability objectives in mind from the outset.

## 2.9 Citation Analysis

Non-empirical articles demonstrate substantially higher citation impact than empirical studies, driven by influential review papers that serve as reference works for the field.

### Table S28: Citation Metrics Comparison

| Metric | Non-Empirical | Empirical | Difference |
|--------|---------------|-----------|------------|
| Total Citations | 54,247 | 91,579 | - |
| Mean Citations | 24.4 | 16.8 | +45% |
| Median Citations | 8 | 5 | +60% |
| Max Citations | 1,879 | 1,142 | +65% |
| Articles with 0 Citations | 17.5% | 19.2% | -1.7% |
| Articles with 100+ Citations | 6.4% | 3.8% | +2.6% |

### Table S29: Top 10 Most-Cited Non-Empirical Articles

| Rank | Title | Year | Citations | Country | Type |
|------|-------|------|-----------|---------|------|
| 1 | Digital Twin: Enabling Technologies, Challenges and Open Research | 2020 | 1,879 | UK | Review |
| 2 | Digital Twin in the IoT Context: A Survey on Technical Features... | 2020 | 613 | France | Review |
| 3 | The Metaverse as a Virtual Form of Smart Cities: Opportunities... | 2022 | 516 | France | Conceptual |
| 4 | Enabling technologies and sustainable smart cities | 2020 | 515 | India | Review |
| 5 | Future smart cities requirements, emerging technologies... | 2022 | 496 | Australia | Review |
| 6 | A systematic review of a digital twin city... | 2021 | 483 | China | Review |
| 7 | Deep learning for smart industry: Efficient manufacture... | 2021 | 434 | Hong Kong | Methodological |
| 8 | Urban computing leveraging location-based social network... | 2020 | 356 | China | Review |
| 9 | Machine learning for internet of things data analysis... | 2020 | 315 | USA | Review |
| 10 | Applications of artificial intelligence in transport... | 2020 | 304 | UK | Review |

The top-cited articles reveal thematic priorities in the field's theoretical development: digital twins dominate the most influential works, followed by smart city enabling technologies and metaverse applications. Notably, 8 of the top 10 articles are reviews/surveys, confirming their role as foundational reference works.

## 2.10 Publication Venues

### Table S30: Top 10 Publication Venues for Non-Empirical Research

| Rank | Journal/Source | Articles | % of Total |
|------|----------------|----------|------------|
| 1 | IEEE Access | 100 | 4.5% |
| 2 | Sustainability (Switzerland) | 74 | 3.3% |
| 3 | Sensors | 53 | 2.4% |
| 4 | Applied Sciences (Switzerland) | 37 | 1.7% |
| 5 | IEEE Internet of Things Journal | 36 | 1.6% |
| 6 | Sustainable Cities and Society | 35 | 1.6% |
| 7 | Remote Sensing | 29 | 1.3% |
| 8 | IEEE Transactions on Intelligent Transportation Systems | 28 | 1.3% |
| 9 | Electronics (Switzerland) | 26 | 1.2% |
| 10 | Expert Systems with Applications | 22 | 1.0% |

IEEE Access dominates non-empirical publication (4.5%), reflecting its open-access model and broad scope accommodating methodological innovations and reviews. The prominence of Sustainability and Sustainable Cities and Society indicates that sustainability-focused venues actively publish non-empirical contributions despite the overall lower sustainability integration documented earlier.

## 2.11 Funding Analysis

### Table S31: Funding Overview

| Metric | Non-Empirical | Empirical | Difference |
|--------|---------------|-----------|------------|
| Total Articles | 2,219 | 5,441 | - |
| With Funding | 1,299 (58.5%) | 3,365 (61.8%) | -3.3% |
| Without Funding | 920 (41.5%) | 2,076 (38.2%) | +3.3% |

Non-empirical research shows slightly lower funding rates than empirical studies, potentially reflecting the lower resource requirements of review and conceptual work compared to primary data collection.

### Table S32: Top 10 Funding Sources for Non-Empirical Research

| Rank | Funding Source | Articles | % of Funded |
|------|----------------|----------|-------------|
| 1 | National Natural Science Foundation of China (NSFC) | 307 | 23.6% |
| 2 | National Key R&D Program (China) | 103 | 7.9% |
| 3 | Saudi Arabia Funding | 92 | 7.1% |
| 4 | Chinese Ministry of Education | 62 | 4.8% |
| 5 | European Union / Horizon 2020 | 60 | 4.6% |
| 6 | Korean Government | 58 | 4.5% |
| 7 | National Research Foundation Korea (NRF) | 42 | 3.2% |
| 8 | US National Science Foundation (NSF) | 38 | 2.9% |
| 9 | China Scholarship Council | 21 | 1.6% |
| 10 | Canadian NSERC | 19 | 1.5% |

Chinese funding sources (NSFC, National Key R&D, Ministry of Education) collectively support approximately 36% of all funded non-empirical research, consistent with China's dominant position in the corpus.

### Table S33: Funding Rate by Country

| Rank | Country | Total | With Funding | Funding Rate |
|------|---------|-------|--------------|--------------|
| 1 | South Korea | 64 | 44 | 68.8% |
| 2 | Spain | 39 | 26 | 66.7% |
| 3 | China | 747 | 493 | 66.0% |
| 4 | Germany | 39 | 25 | 64.1% |
| 5 | USA | 123 | 70 | 56.9% |
| 6 | UK | 66 | 36 | 54.5% |
| 7 | Saudi Arabia | 100 | 54 | 54.0% |
| 8 | Pakistan | 38 | 19 | 50.0% |
| 9 | Italy | 63 | 31 | 49.2% |
| 10 | India | 258 | 116 | 45.0% |

South Korea demonstrates the highest funding rate (68.8%) for non-empirical research, reflecting strong national investment in smart city research infrastructure. India's notably lower funding rate (45.0%) suggests that substantial non-empirical contributions emerge from unfunded research, potentially limiting the scope and depth of these contributions.

### Table S34: Citation Impact of Funding

| Metric | Funded | Unfunded | Difference |
|--------|--------|----------|------------|
| Count | 1,299 | 920 | - |
| Mean Citations | 26.5 | 21.6 | +23% |
| Median Citations | 11 | 5 | +120% |

Funded non-empirical articles receive 23% more citations on average and demonstrate substantially higher median citations (+120%), indicating that funding enables more impactful non-empirical contributions.

### Table S35: Funding Rate by Article Type

| Article Type | Total | Funded | Funding Rate |
|--------------|-------|--------|--------------|
| Methodological | 1,508 | 973 | 64.5% |
| Review/Survey | 472 | 229 | 48.5% |
| Conceptual/Theoretical | 239 | 97 | 40.6% |

Methodological articles show the highest funding rate (64.5%), reflecting funder interest in novel AI method development. Conceptual/theoretical work demonstrates the lowest funding rate (40.6%), suggesting these contributions often emerge from unfunded scholarly activity rather than project-based research.

### Table S36: Funding Rate by Subject Megatrend

| Subject Megatrend | Total | Funded | Funding Rate |
|-------------------|-------|--------|--------------|
| Climate Change & Environmental Sustainability | 350 | 227 | 64.9% |
| Urban Mobility & Transportation | 479 | 281 | 58.7% |
| Digital Transformation & Smart Cities | 875 | 507 | 57.9% |
| Urban Development & Land Use | 227 | 130 | 57.3% |
| Urban Resilience & Safety | 180 | 98 | 54.4% |
| Social Equity & Quality of Life | 108 | 56 | 51.9% |

Climate Change & Environmental Sustainability shows the highest non-empirical funding rate (64.9%), indicating strong funder interest in environmental methodologies. Social Equity & Quality of Life demonstrates the lowest rate (51.9%), consistent with patterns observed in empirical research showing relative underfunding of equity-oriented urban AI work.

## 2.12 Funder Research Priorities

Analysis of research priorities across top funders reveals distinct strategic orientations in non-empirical research.

### Table S37: Funder SDG Priorities in Non-Empirical Research

| Funder | Articles | SDG 11 (%) | SDG 9 (%) | SDG 7 (%) | Distinctive Focus |
|--------|----------|------------|-----------|-----------|-------------------|
| NSFC (China) | 307 | 72.3% | 15.0% | 3.9% | Transportation methods |
| National Key R&D (China) | 107 | 72.0% | 17.8% | 4.7% | Strategic planning |
| Saudi Arabia | 93 | 68.8% | 12.9% | 7.5% | Traffic & governance |
| EU / Horizon 2020 | 71 | 62.0% | 16.9% | 9.9% | Energy & cybersecurity |
| Chinese Min. of Education | 59 | 67.8% | 13.6% | 5.1% | University-based methods |
| NRF Korea | 41 | 58.5% | 17.1% | 7.3% | Most diversified |
| US NSF | 36 | 69.4% | 13.9% | 5.6% | Climate methods |
| Korean Government | 35 | 60.0% | 20.0% | 5.7% | Smart city governance |
| China Scholarship Council | 21 | 76.2% | 9.5% | 4.8% | Highest SDG 11 focus |
| Canadian NSERC | 19 | 63.2% | 31.6% | 5.3% | Highest Infrastructure focus |

**Key Findings:**

- **NRF Korea** demonstrates the most diversified SDG portfolio (lowest SDG 11 at 58.5%), with notable SDG 16 (Peace & Justice) emphasis at 7.3%
- **Canadian NSERC** shows the strongest infrastructure orientation (SDG 9 at 31.6%)—nearly double any other funder
- **EU/Horizon 2020** leads in energy research (SDG 7 at 9.9%) and demonstrates unique cybersecurity emphasis
- **China Scholarship Council** shows highest SDG 11 concentration (76.2%), reflecting international students' focus on core urban sustainability methodologies

### Table S38: Funder Research Cluster Priorities

| Funder | Top Cluster | Second Cluster | Third Cluster |
|--------|-------------|----------------|---------------|
| NSFC | Mobility & Transportation (10.7%) | Urban Planning & Land Use (7.5%) | Cybersecurity (5.2%) |
| National Key R&D | Urban Planning & Land Use (9.3%) | Mobility & Transportation (5.6%) | Transportation & Mobility (4.7%) |
| Saudi Arabia | Traffic & Congestion (7.5%) | Mobility & Transportation (6.5%) | Urban Governance & Society (6.5%) |
| EU / Horizon 2020 | Cybersecurity (7.0%) | Governance & Society (4.2%) | Traffic & Congestion (4.2%) |
| NRF Korea | Cybersecurity (7.3%) | Governance & Society (4.9%) | Environment & Sustainability (4.9%) |
| US NSF | Smart Infrastructure (8.3%) | Transportation & Mobility (8.3%) | Mobility & Transportation (8.3%) |
| Korean Government | Environment & Sustainability (5.7%) | Smart City Infrastructure (5.7%) | Digital Governance (5.7%) |
| Canadian NSERC | Smart City Infrastructure (10.5%) | Cybersecurity (10.5%) | Traffic & Congestion (10.5%) |

**Cybersecurity as Emerging Priority:** A notable finding is the prominence of cybersecurity research in non-empirical work funded by EU/Horizon 2020, NRF Korea, and Canadian NSERC. This reflects growing recognition that urban digital infrastructure requires robust security frameworks, and that methodological development in this domain precedes empirical implementation.

## 2.13 Key Insights from Non-Empirical Analysis

1. **Methodological Dominance**: 68% of non-empirical articles propose new AI methods or frameworks, reflecting the rapid evolution of urban AI techniques and continuous need for methodological innovation.

2. **Higher Citation Impact**: Non-empirical articles average 24.4 citations versus 16.8 for empirical work (+45%), driven by influential review papers that serve as foundational references. The top 10 most-cited non-empirical articles average 491 citations.

3. **Infrastructure Focus**: SDG 9 (Industry, Innovation and Infrastructure) representation is 6.5 percentage points higher in non-empirical versus empirical research, reflecting emphasis on developing infrastructure-oriented methodologies and smart city architectures.

4. **Cybersecurity Emergence**: Cybersecurity emerges as a distinctive research cluster in non-empirical work, particularly for EU, Korean, and Canadian funders, indicating methodological development preceding empirical deployment.

5. **Weaker Sustainability Integration**: Non-empirical research shows 13.8 percentage points lower "Strong" sustainability integration compared to empirical studies, suggesting methodological innovation often prioritizes technical performance over explicit sustainability considerations.

6. **Transportation Methodological Focus**: Transportation research accounts for 21.7% of non-empirical articles (higher than empirical), reflecting the methodological complexity of traffic prediction, autonomous navigation, and intelligent transportation systems.

7. **Digital Twin Prominence**: The most-cited non-empirical articles focus on digital twins and smart city enabling technologies, indicating these concepts drive substantial theoretical attention.

8. **Funding Patterns**: Methodological articles show highest funding rate (64.5%) while conceptual work is often unfunded (40.6% funded), suggesting funders prioritize algorithm development over theoretical contributions.

---

# 3. Supplementary Tables

## Table S39: Complete Country Distribution (Top 50)

| Rank | Country | Total | Empirical | Non-Empirical | % Empirical |
|------|---------|-------|-----------|---------------|-------------|
| 1 | China | 2,849 | 2,102 | 747 | 73.8% |
| 2 | India | 884 | 626 | 258 | 70.8% |
| 3 | USA | 419 | 296 | 123 | 70.6% |
| 4 | UK | 252 | 186 | 66 | 73.8% |
| 5 | Saudi Arabia | 244 | 144 | 100 | 59.0% |
| 6 | Italy | 224 | 161 | 63 | 71.9% |
| 7 | South Korea | 193 | 129 | 64 | 66.8% |
| 8 | Germany | 176 | 137 | 39 | 77.8% |
| 9 | Spain | 158 | 119 | 39 | 75.3% |
| 10 | Australia | 152 | 115 | 37 | 75.7% |
| 11 | Pakistan | 123 | 85 | 38 | 69.1% |
| 12 | Iran | 116 | 91 | 25 | 78.4% |
| 13 | Portugal | 104 | 70 | 34 | 67.3% |
| 14 | Singapore | 103 | 66 | 37 | 64.1% |
| 15 | Turkey | 99 | 79 | 20 | 79.8% |
| 16 | France | 97 | 67 | 30 | 69.1% |
| 17 | Canada | 95 | 68 | 27 | 71.6% |
| 18 | Malaysia | 92 | 66 | 26 | 71.7% |
| 19 | Japan | 88 | 64 | 24 | 72.7% |
| 20 | Indonesia | 82 | 58 | 24 | 70.7% |
| 21 | Egypt | 77 | 48 | 29 | 62.3% |
| 22 | Morocco | 76 | 47 | 29 | 61.8% |
| 23 | Brazil | 75 | 53 | 22 | 70.7% |
| 24 | Poland | 73 | 57 | 16 | 78.1% |
| 25 | Netherlands | 71 | 55 | 16 | 77.5% |
| 26 | Greece | 62 | 44 | 18 | 71.0% |
| 27 | Vietnam | 56 | 42 | 14 | 75.0% |
| 28 | Sweden | 50 | 36 | 14 | 72.0% |
| 29 | Romania | 44 | 30 | 14 | 68.2% |
| 30 | Belgium | 43 | 33 | 10 | 76.7% |
| 31 | Czech Republic | 42 | 32 | 10 | 76.2% |
| 32 | Switzerland | 41 | 32 | 9 | 78.0% |
| 33 | Nigeria | 40 | 26 | 14 | 65.0% |
| 34 | Taiwan | 38 | 28 | 10 | 73.7% |
| 35 | Denmark | 36 | 28 | 8 | 77.8% |
| 36 | Austria | 35 | 27 | 8 | 77.1% |
| 37 | Mexico | 32 | 21 | 11 | 65.6% |
| 38 | Finland | 30 | 21 | 9 | 70.0% |
| 39 | Norway | 29 | 22 | 7 | 75.9% |
| 40 | Algeria | 28 | 17 | 11 | 60.7% |
| 41 | Colombia | 27 | 18 | 9 | 66.7% |
| 42 | Thailand | 26 | 19 | 7 | 73.1% |
| 43 | Hong Kong | 24 | 16 | 8 | 66.7% |
| 44 | New Zealand | 22 | 15 | 7 | 68.2% |
| 45 | Chile | 21 | 15 | 6 | 71.4% |
| 46 | South Africa | 20 | 13 | 7 | 65.0% |
| 47 | Iraq | 19 | 10 | 9 | 52.6% |
| 48 | Bangladesh | 18 | 11 | 7 | 61.1% |
| 49 | Ireland | 17 | 12 | 5 | 70.6% |
| 50 | UAE | 16 | 9 | 7 | 56.3% |

## Table S40: AI Method × Megatrend Cross-tabulation (Top 10 Methods)

| AI Method | Digital & Smart Cities | Climate & Environment | Mobility & Transport | Urban Development | Resilience & Safety | Social Equity |
|-----------|----------------------|---------------------|---------------------|------------------|--------------------|--------------|
| Deep Learning | 304 | 196 | 142 | 74 | 52 | 34 |
| Machine Learning | 318 | 162 | 99 | 62 | 38 | 37 |
| CNN | 159 | 141 | 40 | 54 | 26 | 16 |
| Random Forest | 62 | 71 | 16 | 28 | 4 | 7 |
| Neural Network | 65 | 29 | 22 | 13 | 14 | 15 |
| Reinforcement Learning | 48 | 9 | 74 | 5 | 7 | 2 |
| LSTM | 31 | 18 | 29 | 8 | 3 | 4 |
| Ensemble | 32 | 35 | 10 | 10 | 2 | 2 |
| XGBoost | 28 | 32 | 7 | 7 | 2 | 3 |
| GNN | 22 | 5 | 43 | 2 | 2 | 1 |

## Table S41: AI Task × SDG Cross-tabulation (Major Tasks)

| AI Task | SDG 3 | SDG 6 | SDG 7 | SDG 9 | SDG 11 | SDG 13 | SDG 16 |
|---------|-------|-------|-------|-------|--------|--------|--------|
| Prediction/Forecasting | 113 | 30 | 135 | 168 | 1,212 | 63 | 4 |
| Classification | 125 | 60 | 95 | 168 | 895 | 49 | 14 |
| Optimization | 15 | 21 | 103 | 82 | 364 | 11 | 4 |
| Object Detection | 10 | 2 | 6 | 34 | 230 | 5 | 5 |
| Segmentation | 5 | 10 | 12 | 50 | 129 | 3 | 0 |
| Simulation | 10 | 5 | 26 | 20 | 87 | 5 | 0 |
| Clustering | 16 | 3 | 5 | 15 | 53 | 2 | 1 |

---

# 4. Supplementary Figures

This section describes the figures generated for non-empirical research analysis. All figures are available in both PDF (vector) and PNG (raster) formats in the supplementary files.

## Figure S2: Detrended Correspondence Analysis of Non-Empirical Research

**File:** `dca_plot_non_empirical.pdf/png`

This figure presents a Detrended Correspondence Analysis (DCA) visualization of the 2,219 non-empirical articles, revealing the conceptual structure of methodological, review, and theoretical contributions. The analysis identifies two fundamental axes:

- **Axis 1 (Horizontal):** Ranges from black-box prediction approaches (left) to interpretable intelligence frameworks (right), capturing the spectrum of algorithmic transparency in non-empirical contributions
- **Axis 2 (Vertical):** Ranges from physical systems focus (bottom) to cyber-physical integration (top), distinguishing infrastructure-oriented from digital-first methodological approaches

Six megatrend clusters are represented as ellipses based on eigenvalue decomposition, with size proportional to article count and position determined by the constituent articles' methodological characteristics. Keyword clouds within each ellipse indicate dominant terminology extracted from abstracts.

Key observations:
- Digital Transformation & Smart Cities (n=875) occupies the cyber-physical, technical-predictive quadrant
- Climate & Environment (n=350) demonstrates stronger interpretable intelligence orientation
- Social Equity & Quality of Life (n=108), though smallest, shows the most interpretable and socially-embedded positioning

## Figure S3: Hierarchical Taxonomy Dendrogram

**File:** `dendrogram_non_empirical.pdf/png`

This figure presents a hierarchical dendrogram visualizing the taxonomic structure of non-empirical AI and urban research. The visualization proceeds from left (subject clusters) through intermediate levels (research trends) to right (megatrends and root), illustrating how 71 distinct subject clusters aggregate into 23 research trends and 6 megatrends.

Notable hierarchical patterns:
- **Cybersecurity** (88 articles) emerges as the dominant cluster within Urban Resilience & Safety, substantially larger than video surveillance (19) or disaster management (14)
- **Smart Infrastructure** clusters dominate Digital Transformation, with Smart Infrastructure (64), Smart City Infrastructure (55), and Urban Infrastructure & Technology (42) forming a coherent methodological domain
- **Transportation** themes fragment across multiple megatrends, appearing in Mobility & Transportation (traffic, autonomous vehicles), Digital Transformation (intelligent systems), and even Climate & Environment (transportation emissions)

## Figure S4: SDG Alignment Heatmap with Sustainability Integration

**File:** `sdg_heatmap_non_empirical.pdf/png`

This figure presents a combined heatmap showing: (1) the distribution of non-empirical articles across megatrends and SDGs (main panel), and (2) sustainability integration levels by megatrend (right panel).

The heatmap reveals:
- **SDG 11 dominance**: All megatrends show >50% SDG 11 alignment, with Digital & Smart Cities reaching 875 articles
- **SDG 9 as secondary priority**: Infrastructure-oriented SDG 9 shows consistently higher representation in non-empirical versus empirical research
- **Climate & Environment sustainability**: This megatrend shows strongest sustainability integration (97.4% strong), while Digital & Smart Cities shows weakest (21.6% strong)

## Figure S5: Research Characteristics Faceted Heatmap

**File:** `research_characteristics_heatmap.pdf/png`

A 2×2 faceted heatmap presenting four research characteristic dimensions across the six megatrends:

**Panel A: Methodological Approach**
- Quantitative methods dominate all megatrends (60-85%)
- Social Equity shows notably higher qualitative adoption (27.8%)

**Panel B: Spatial Scale**
- Local scale predominates (78-90%) across megatrends
- Digital & Smart Cities shows highest global-scale representation (14.7%)

**Panel C: Temporal Scale**
- Present-focused research dominates (77-83%)
- Climate & Environment shows highest past-oriented research (5.4%)

**Panel D: Temporal Focus**
- Cross-sectional designs predominate (68-83%)
- Resilience & Safety shows highest longitudinal proportion (31.7%)

## Figure S6: AI Methods Heatmap

**File:** `ai_methods_heatmap.pdf/png`

A heatmap visualizing the distribution of top 15 AI methods across six megatrends, using log-scaled color intensity to accommodate the wide range of article counts. Cell values indicate absolute article counts.

Key patterns:
- **Deep Learning** dominates across all megatrends, with highest concentration in Digital & Smart Cities (107)
- **Reinforcement Learning** shows distinctive Mobility & Transportation concentration (15), reflecting autonomous vehicle research
- **GNN** shows modest but notable representation (24 total), with highest concentration in Digital & Smart Cities (13)

## Figure S7: AI Tasks × SDGs Visualization (Three Panels)

**Files:** `ai_task_sdg_absolute.pdf/png`, `ai_task_sdg_percentage.pdf/png`, `ai_task_sdg_bubble.pdf/png`

Three complementary visualizations of the relationship between AI tasks and SDG alignment:

**Panel A: Absolute Stacked Bar Chart**
Horizontal stacked bars showing absolute article counts for each AI task, with color segments representing SDG contributions. Classification (394) and Prediction/Forecasting (389) dominate, with SDG 11 comprising the largest segment across all tasks.

**Panel B: Percentage Stacked Bar Chart**
Normalized version showing SDG composition within each task. Optimization shows notably higher SDG 9 representation (28%), while Classification and Segmentation show stronger SDG 11 concentration (>70%).

**Panel C: Bubble Chart**
Bubble plot with tasks on the y-axis and SDGs on the x-axis, bubble size proportional to article count. This visualization highlights the concentration of research activity in the SDG 11 × (Classification/Prediction) intersection while revealing sparse coverage of SDGs 1, 2, 4, 5, and 14.

---

## References

1. Page, M. J. et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. BMJ 372 (2021).

2. Baas, J., Schotten, M., Plume, A., Côté, G. & Karimi, R. Scopus as a curated, high-quality bibliometric data source for academic research in quantitative science studies. Quantitative Science Studies 1, 377-386 (2020).

3. Gilardi, F., Alizadeh, M. & Kubli, M. ChatGPT outperforms crowd workers for text-annotation tasks. Proceedings of the National Academy of Sciences 120, e2305016120 (2023).

4. Delgado-Chaves, F. M. et al. Transforming literature screening: The emerging role of large language models in systematic reviews. Proceedings of the National Academy of Sciences 122, e2411962122 (2025).

5. Greenacre, M. Correspondence analysis in practice. (Chapman and Hall/CRC, 2017).

---

*Supplementary Material for: Artificial Intelligence in Urban Studies: A Systematic Review of Research Trajectories, Methodological Patterns, and Sustainability Orientations (2020-2025)*
