# Methodology: Systematic Literature Review on AI and Urban Studies

*A comprehensive review of artificial intelligence applications in urban research (2020-2025)*

---

## 1. Overview of the Systematic Review Process

This systematic literature review follows the PRISMA (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) guidelines to examine the intersection of Artificial Intelligence (AI) and urban studies research published between 2020 and 2025.

### Figure 1: Flowchart of the Review Process

```
┌─────────────────────────────────────────────────────────────────┐
│                    IDENTIFICATION                                │
├─────────────────────────────────────────────────────────────────┤
│  Records identified through Scopus database search               │
│  (n = 8,430)                                                    │
│  • 2020: 618    • 2023: 1,363                                   │
│  • 2021: 921    • 2024: 1,801                                   │
│  • 2022: 1,188  • 2025: 2,539                                   │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      SCREENING                                   │
├─────────────────────────────────────────────────────────────────┤
│  Records screened for relevance                                  │
│  (n = 8,430)                                                    │
│                                                                  │
│  Exclusion criteria applied:                                     │
│  • Not relevant to AI + Urban studies (n = 770)                 │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                      ELIGIBILITY                                 │
├─────────────────────────────────────────────────────────────────┤
│  Full-text articles assessed for eligibility                     │
│  (n = 7,660)                                                    │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                       INCLUDED                                   │
├─────────────────────────────────────────────────────────────────┤
│  Studies included in quantitative synthesis                      │
│  (n = 7,660)                                                    │
│                                                                  │
│  Split into:                                                     │
│  • Empirical studies (n = 5,441)                                │
│  • Non-empirical studies (n = 2,219)                            │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Search Strategy

### 2.1 Database
**Scopus** was selected as the primary database for this systematic review due to its:
- Comprehensive coverage of peer-reviewed scientific literature
- Strong indexing of engineering, computer science, environmental science, and urban studies journals
- Structured metadata export capabilities with standardized fields
- Reliable citation tracking functionality
- Coverage of over 27,000 journals from more than 7,000 publishers

### 2.2 Search String

The following search string was used in Scopus:

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

### 2.3 Search Filters Applied

| Filter | Value |
|--------|-------|
| Database | Scopus |
| Publication Years | 2020-2025 |
| Document Type | Article |
| Language | English |
| Search Fields | Title, Abstract, Keywords |

---

## 3. Search Results

### Table 1: Search Hits and Included Articles by Year

| Year | Initial Scopus Hits | After Relevance Screening | Included in Review | Exclusion Rate |
|------|---------------------|---------------------------|--------------------| --------------|
| 2020 | 618 | 574 | 574 | 7.1% |
| 2021 | 921 | 860 | 860 | 6.6% |
| 2022 | 1,188 | 945 | 945 | 20.5% |
| 2023 | 1,363 | 1,173 | 1,173 | 13.9% |
| 2024 | 1,801 | 1,713 | 1,713 | 4.9% |
| 2025 | 2,539 | 2,395 | 2,395 | 5.7% |
| **Total** | **8,430** | **7,660** | **7,660** | **9.1%** |

### Table 2: Summary of Article Selection

| Stage | Articles | Percentage |
|-------|----------|------------|
| Initial database search | 8,430 | 100% |
| Excluded (not relevant) | 770 | 9.1% |
| **Final included** | **7,660** | **90.9%** |

---

## 4. Inclusion and Exclusion Criteria

### Table 3: Inclusion Criteria

| Criterion | Description |
|-----------|-------------|
| IC1 | Peer-reviewed journal articles |
| IC2 | Published between January 2020 and December 2025 |
| IC3 | Focus on AI/ML applications in urban contexts |
| IC4 | Written in English |
| IC5 | Contains abstract with sufficient information |
| IC6 | Presents original research, methodology, or review |

### Table 4: Exclusion Criteria

| Criterion | Description | Articles Excluded |
|-----------|-------------|-------------------|
| EC1 | Conference papers, book chapters, editorials, letters | Pre-filtered in Scopus |
| EC2 | Non-urban AI applications (e.g., purely medical, agricultural without urban link) | ~400 |
| EC3 | Articles without clear AI/ML methodology | ~250 |
| EC4 | Duplicate entries | ~50 |
| EC5 | Non-English publications | Pre-filtered in Scopus |
| EC6 | Articles with only tangential mention of AI or urban | ~70 |
| **Total Excluded** | | **770** |

---

## 5. Data Extraction

### 5.1 Scopus Metadata Fields Extracted

### Table 5: Extracted Scopus Fields (23 Fields)

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

### 5.2 Data Quality Metrics

| Metric | Value | Percentage |
|--------|-------|------------|
| Articles with DOI | 7,555 | 98.6% |
| Articles with Abstract | 7,660 | 100% |
| Open Access articles | 4,225 | 55.2% |
| Articles with Funding information | 3,365 | 43.9% |
| Articles with Author affiliations | 7,658 | 99.97% |

---

## 6. Coding Scheme

### 6.1 Overview of Coded Variables

A total of **15 variables** were coded for each article through a combination of automated extraction and manual verification.

### Table 6: Complete Coding Scheme

| # | Category | Variable Name | Description | Codes/Values | Coding Method |
|---|----------|---------------|-------------|--------------|---------------|
| 1 | **Relevance** | relevant | Relevance to AI + Urban studies | Yes, No | Manual screening |
| 2 | **Geography** | country_first_author | Country of first author's institution | 111 countries | Automated + Manual |
| 3 | **Subject Classification** | subject_category | Primary research subject area | 163 categories | AI-assisted coding |
| 4 | **Subject Classification** | subject_cluster | Detailed subject clustering | 428 clusters | AI-assisted coding |
| 5 | **Subject Classification** | subject_megatrend | Broad thematic megatrend | 6 megatrends | Hierarchical clustering |
| 6 | **AI Methodology** | ai_method | AI/ML method(s) used | Multiple (see Table 7) | Keyword extraction + Manual |
| 7 | **AI Methodology** | ai_task | Primary AI task performed | Multiple (see Table 8) | Keyword extraction + Manual |
| 8 | **Research Focus** | main_goal | Primary research objective | Open-ended | AI-assisted extraction |
| 9 | **Sustainability** | sdg_alignment | UN Sustainable Development Goal alignment | 17 SDGs | AI-assisted + Manual |
| 10 | **Article Characteristics** | article_type | Type of research contribution | 4 types (see Table 9) | Manual coding |
| 11 | **Article Characteristics** | methodological_approach | Research methodology type | 3 types (see Table 10) | Manual coding |
| 12 | **Spatial-Temporal** | spatial_scale | Geographic scope of study | 6 scales (see Table 11) | Manual coding |
| 13 | **Spatial-Temporal** | temporal_scale | Time orientation | 3 scales | Manual coding |
| 14 | **Spatial-Temporal** | temporal_focus | Data collection approach | 2 types | Manual coding |
| 15 | **Sustainability** | level_of_sustainability | Degree of sustainability integration | 3 levels (see Table 12) | Manual coding |

---

### 6.2 Detailed Code Definitions

### Table 7: AI Method Codes

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
| OTH | Other | Other methods | Various | 2,331 | 30.4% |

### Table 8: AI Task Codes

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
| OTH | Other | Other tasks | Various | 1,163 | 15.2% |

### Table 9: Article Type Codes

| Code | Article Type | Description | Criteria | Count | % |
|------|--------------|-------------|----------|-------|---|
| EMP | Empirical | Original data collection and analysis | Contains primary data, case studies, experiments | 5,441 | 71.0% |
| MTH | Methodological | New method or algorithm development | Proposes new AI method, framework, or system | 1,508 | 19.7% |
| REV | Review/Survey | Literature review or survey | Synthesizes existing research | 472 | 6.2% |
| CON | Conceptual/Theoretical | Framework or theory development | Proposes concepts without empirical testing | 239 | 3.1% |

### Table 10: Methodological Approach Codes

| Code | Approach | Description | Typical Methods | Count | % |
|------|----------|-------------|-----------------|-------|---|
| QNT | Quantitative | Statistical/computational analysis | ML models, statistical analysis, simulations | 6,321 | 82.5% |
| MIX | Mixed | Combined quantitative and qualitative | Surveys + ML, interviews + analysis | 824 | 10.8% |
| QAL | Qualitative | Interpretive/descriptive analysis | Case studies, expert interviews, policy analysis | 514 | 6.7% |

### Table 11: Spatial Scale Codes

| Code | Scale | Description | Examples | Count | % |
|------|-------|-------------|----------|-------|---|
| LOC | Local | City or neighborhood level | Single city case study, district analysis | 6,147 | 80.2% |
| GLB | Global | Worldwide or multi-country | Cross-country comparison, global datasets | 567 | 7.4% |
| REG | Regional | Sub-national region | Province, state, metropolitan area | 346 | 4.5% |
| IND | Individual | Building or person level | Individual building, personal mobility | 297 | 3.9% |
| NAT | National | Country level | National urban systems, country-wide analysis | 251 | 3.3% |
| SUP | Supranational | Multi-country region | EU, ASEAN, continental analysis | 50 | 0.7% |

### Table 12: Level of Sustainability Integration Codes

| Code | Level | Description | Criteria | Count | % |
|------|-------|-------------|----------|-------|---|
| STR | Strong | Explicit sustainability framework | - Explicit reference to sustainability goals/SDGs<br>- Environmental/social impact assessment<br>- Long-term sustainability considerations<br>- Policy implications for sustainability | 3,359 | 43.9% |
| MED | Medium | Implicit sustainability considerations | - Efficiency improvements mentioned<br>- Resource optimization focus<br>- Environmental monitoring without explicit sustainability framing<br>- Indirect sustainability benefits | 3,184 | 41.6% |
| WEK | Weak | Technical focus without sustainability | - Purely technical/methodological focus<br>- No mention of sustainability implications<br>- Short-term optimization only<br>- No environmental/social considerations | 1,116 | 14.6% |

### Table 13: SDG Alignment Codes

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

### Table 14: Subject Megatrend Codes

| Code | Megatrend | Description | Key Topics | Count | % |
|------|-----------|-------------|------------|-------|---|
| DT | Digital Transformation & Smart Cities | Technology-driven urban innovation | IoT, digital twins, smart infrastructure, sensors | 2,927 | 38.2% |
| CC | Climate Change & Environmental Sustainability | Environmental urban challenges | Air quality, carbon emissions, green infrastructure, UHI | 1,996 | 26.1% |
| UM | Urban Mobility & Transportation | Movement and accessibility | Traffic prediction, autonomous vehicles, public transit | 1,018 | 13.3% |
| UD | Urban Development & Land Use | Physical urban transformation | Land cover change, urban expansion, zoning | 733 | 9.6% |
| SE | Social Equity & Quality of Life | Human-centered urbanism | Public health, accessibility, well-being, equity | 578 | 7.5% |
| UR | Urban Resilience & Safety | Risk and security | Disaster management, crime prediction, emergency response | 408 | 5.3% |

---

## 7. Coding Process

### 7.1 Coding Workflow

```
Step 1: Automated Extraction
├── Extract country from affiliations
├── Extract AI method keywords from title/abstract
├── Extract AI task keywords from title/abstract
└── Initial SDG classification based on keywords

Step 2: AI-Assisted Classification
├── Subject category assignment using LLM
├── Subject cluster identification
├── Main goal extraction
└── SDG alignment verification

Step 3: Manual Coding
├── Article type classification
├── Methodological approach
├── Spatial and temporal scales
├── Sustainability level assessment
└── Quality control verification

Step 4: Validation
├── Random sample verification (10%)
├── Inter-coder reliability check
└── Consistency review
```

### 7.2 Quality Assurance

| Quality Measure | Description |
|-----------------|-------------|
| Double coding | 10% random sample coded by two reviewers |
| Consistency checks | Automated checks for logical consistency |
| Outlier review | Manual review of edge cases |
| Expert validation | Domain expert review of coding scheme |

---

## 8. Data Analysis Framework

### 8.1 Descriptive Analysis
- Temporal trends (publication growth rates)
- Geographic distribution (country-level analysis)
- Subject area mapping (category and cluster analysis)
- AI method and task distributions

### 8.2 Cross-tabulation Analysis
- Country × AI methods
- Country × SDG alignment
- Article type × Sustainability level
- AI method × Subject megatrend
- Funder × Research topics/SDGs

### 8.3 Funding Analysis
- Funding source identification and classification
- Funding rate by country and subject area
- Citation impact of funded vs. unfunded research
- Funder research priority mapping

### 8.4 Trend Analysis
- Year-over-year growth patterns
- Emerging AI methods over time
- Shifting research priorities
- Geographic diversification trends

---

## 9. Output Files

### 9.1 Dataset Files

| File Name | Description | Records | Variables |
|-----------|-------------|---------|-----------|
| clean_research.csv | Full coded dataset | 7,660 | 38 |
| empirical_clean.csv | Empirical articles subset | 5,441 | 38 |
| clean_research_non_empirical.csv | Non-empirical articles subset | 2,219 | 38 |

### 9.2 Analysis Output Files (Overview folder)

| File Name | Description |
|-----------|-------------|
| research_statistics.md | Comprehensive descriptive statistics |
| funding_analysis.md | Funding source analysis |
| funder_topics_sdgs_analysis.md | Funder research priorities |
| methodology.md | This methodology document |
| funder_sdg_coverage.csv | Funder × SDG matrix |
| funder_cluster_coverage.csv | Funder × Topic cluster matrix |
| funder_ai_methods_coverage.csv | Funder × AI methods matrix |
| country_top_subjects.csv | Country research specializations |
| top13_country_specializations.csv | Top 13 country detailed analysis |
| overview_figure.pdf | Multi-panel visualization |
| overview_figure.png | Multi-panel visualization (PNG) |

---

## 10. Limitations

| Limitation | Description | Mitigation |
|------------|-------------|------------|
| Single database | Only Scopus used; may miss articles indexed elsewhere | Scopus selected for comprehensive coverage of relevant disciplines |
| Language bias | Only English articles included | English is dominant language in AI research |
| Temporal boundary | Data collection has a cutoff date | Clear documentation of search date |
| Coding subjectivity | Some variables require judgment | Detailed coding guidelines, inter-coder checks |
| Search string sensitivity | May not capture all AI terminology | Broad search terms, iterative refinement |
| Publication bias | May underrepresent negative results | Acknowledged as limitation |

---

## 11. Summary Statistics

| Metric | Value |
|--------|-------|
| Total articles analyzed | 7,660 |
| Countries represented | 109 |
| Unique journals | 1,547 |
| Time span | 2020-2025 |
| Empirical studies | 5,441 (71.0%) |
| Non-empirical studies | 2,219 (29.0%) |
| Open Access articles | 4,225 (55.2%) |
| Total citations | 145,826 |
| Mean citations per article | 19.0 |
| Median citations | 6 |
| Articles with funding | 3,365 (43.9%) |

---

*Methodology document for: Systematic Literature Review on AI Applications in Urban Studies (2020-2025)*
