import pandas as pd
import numpy as np

# Read data
df = pd.read_csv(r'D:\Navid\Study\Ph.D 2\Thesis\12-ai-and-city\material\empirical_clean.csv')

# Create descriptive AI task categories
def standardize_ai_task_descriptive(task):
    if pd.isna(task):
        return None
    task = str(task).strip()
    task_lower = task.lower()

    # Skip non-informative categories
    if task_lower in ['not specified', 'not applicable/not specified', 'not coverage', 'other', 'not applicable', 'multiple']:
        return None

    # Prediction/Forecasting
    if any(x in task_lower for x in ['prediction', 'forecasting', 'forecast']):
        if 'classification' in task_lower or 'pattern' in task_lower:
            return None  # Skip multi-task combinations
        return 'Prediction & Forecasting'

    # Classification (merge all classification types)
    if 'classification' in task_lower:
        if 'object' not in task_lower:
            return 'Classification'
    if task_lower in ['image classification', 'image recognition and classification', 'image recognition']:
        return 'Classification'

    # Object/Anomaly/Change Detection (comprehensive detection category)
    if any(x in task_lower for x in ['object detection', 'anomaly detection', 'change detection',
                                      'intrusion detection', 'fault detection', 'malware']):
        return 'Object/Anomaly/Change Detection'
    if task_lower == 'detection':
        return 'Object/Anomaly/Change Detection'
    if 'security' in task_lower:
        return 'Object/Anomaly/Change Detection'

    # Optimization & Resource Allocation
    if any(x in task_lower for x in ['optimization', 'scheduling', 'resource allocation',
                                      'resource management', 'route']):
        return 'Optimization & Resource Allocation'

    # Analysis & Assessment
    if 'analysis' in task_lower or 'assessment' in task_lower or 'evaluation' in task_lower:
        if 'causal' in task_lower or 'impact' in task_lower:
            return 'Causal Inference'
        if 'risk' in task_lower:
            return 'Analysis & Assessment'
        if 'feature' in task_lower or 'explainability' in task_lower:
            return 'Analysis & Assessment'
        if 'spatial' in task_lower:
            return 'Mapping/Spatial Analysis'
        if 'text' in task_lower or 'nlp' in task_lower or 'sentiment' in task_lower:
            return 'NLP/Text Analysis'
        if 'image' in task_lower or 'video' in task_lower:
            return 'Image/Video Processing'
        return 'Analysis & Assessment'

    # Image Segmentation
    if 'segmentation' in task_lower:
        return 'Segmentation'

    # Image/Video Processing
    if 'image' in task_lower or 'video' in task_lower or '3d reconstruction' in task_lower:
        return 'Image/Video Processing'

    # Simulation & Modeling
    if any(x in task_lower for x in ['simulation', 'modeling', 'scenario']):
        return 'Simulation/Modeling'

    # Clustering
    if 'clustering' in task_lower:
        return 'Clustering'

    # Pattern Recognition (merge pattern-related tasks)
    if 'pattern' in task_lower or 'recognition' in task_lower:
        return 'Classification'  # Merge with classification as they're related

    # NLP & Text Analysis
    if any(x in task_lower for x in ['nlp', 'text', 'natural language', 'sentiment']):
        return 'NLP/Text Analysis'

    # Decision Support & Planning
    if any(x in task_lower for x in ['decision', 'planning', 'recommendation']):
        return 'Decision Support'

    # Generation & Synthesis
    if any(x in task_lower for x in ['generation', 'synthesis', 'augmentation']):
        return 'Generation'

    # Data Processing
    if 'data' in task_lower and any(x in task_lower for x in ['processing', 'fusion', 'integration', 'collection', 'mining']):
        return 'Data Processing'

    # Monitoring & Tracking
    if 'monitoring' in task_lower or 'tracking' in task_lower:
        return 'Monitoring'

    # Mapping & Spatial Analysis
    if 'mapping' in task_lower or 'spatial' in task_lower:
        return 'Mapping/Spatial Analysis'

    # Causal Inference
    if 'causal' in task_lower:
        return 'Causal Inference'

    # Control & Navigation
    if 'control' in task_lower or 'navigation' in task_lower:
        return 'Control/Navigation'

    # Regression
    if 'regression' in task_lower or 'estimation' in task_lower or 'measurement' in task_lower:
        return 'Regression'

    # Localization/Identification
    if any(x in task_lower for x in ['localization', 'identification', 're-identification']):
        return 'Object/Anomaly/Change Detection'

    return None  # Skip unclassified

# Apply standardization
df['ai_task_descriptive'] = df['ai_task'].apply(standardize_ai_task_descriptive)

# Filter out None values
df_filtered = df[df['ai_task_descriptive'].notna()].copy()

# Create SDG mapping - match actual values in data
sdg_mapping = {
    'SDG 1 (No Poverty)': 'SDG 1',
    'SDG 2 (Zero Hunger)': 'SDG 2',
    'SDG 3 (Health)': 'SDG 3',
    'SDG 4 (Education)': 'SDG 4',
    'SDG 5 (Gender Equality)': 'SDG 5',
    'SDG 6 (Water)': 'SDG 6',
    'SDG 7 (Energy)': 'SDG 7',
    'SDG 8 (Economic Growth)': 'SDG 8',
    'SDG 9 (Infrastructure)': 'SDG 9',
    'SDG 10 (Reduced Inequalities)': 'SDG 10',
    'SDG 11 (Sustainable Cities)': 'SDG 11',
    'SDG 12 (Responsible Consumption)': 'SDG 12',
    'SDG 13 (Climate)': 'SDG 13',
    'SDG 14 (Life Below Water)': 'SDG 14',
    'SDG 15 (Life on Land)': 'SDG 15',
    'SDG 16 (Peace & Justice)': 'SDG 16'
}

# Map SDG values to simplified format
df_filtered['sdg_simple'] = df_filtered['sdg_alignment'].map(sdg_mapping)

# Create crosstab
crosstab = pd.crosstab(df_filtered['ai_task_descriptive'], df_filtered['sdg_simple'])

# Reorder SDG columns
sdg_order = [f'SDG {i}' for i in range(1, 17)]
existing_sdgs = [sdg for sdg in sdg_order if sdg in crosstab.columns]
crosstab = crosstab[existing_sdgs]

# Add total column
crosstab['Total'] = crosstab.sum(axis=1)

# Sort by total descending
crosstab = crosstab.sort_values('Total', ascending=False)

print('AI Task Categories Created:')
print(crosstab)
print()
print('Total articles:', crosstab['Total'].sum())

# Save CSV
crosstab.to_csv(r'D:\Navid\Study\Ph.D 2\Thesis\12-ai-and-city\material\empirical_analysis\ai_task_sdg_table.csv')

# Create markdown table
md_content = """# AI Tasks by SDG Alignment

## Table: Frequency of AI Tasks across Sustainable Development Goals

| AI Task | SDG 1 | SDG 2 | SDG 3 | SDG 4 | SDG 5 | SDG 6 | SDG 7 | SDG 8 | SDG 9 | SDG 10 | SDG 11 | SDG 12 | SDG 13 | SDG 14 | SDG 15 | SDG 16 | Total |
|---------|-------|-------|-------|-------|-------|-------|-------|-------|-------|--------|--------|--------|--------|--------|--------|--------|-------|
"""

for task, row in crosstab.iterrows():
    values = []
    for sdg in sdg_order:
        if sdg in row.index:
            val = int(row[sdg]) if sdg in row.index else 0
            values.append(f'{val:,}' if val >= 1000 else str(val))
        else:
            values.append('0')
    total = int(row['Total'])
    total_str = f'{total:,}' if total >= 1000 else str(total)
    md_content += f"| {task} | {' | '.join(values)} | {total_str} |\n"

# Add total row
total_row = crosstab.sum()
total_values = []
for sdg in sdg_order:
    if sdg in total_row.index:
        val = int(total_row[sdg])
        total_values.append(f'**{val:,}**' if val >= 1000 else f'**{val}**')
    else:
        total_values.append('**0**')
grand_total = int(total_row['Total'])
grand_total_str = f'**{grand_total:,}**' if grand_total >= 1000 else f'**{grand_total}**'
md_content += f"| **Total** | {' | '.join(total_values)} | {grand_total_str} |\n"

md_content += """
---

## SDG Legend

| SDG | Name |
|-----|------|
| SDG 1 | No Poverty |
| SDG 2 | Zero Hunger |
| SDG 3 | Good Health and Well-being |
| SDG 4 | Quality Education |
| SDG 5 | Gender Equality |
| SDG 6 | Clean Water and Sanitation |
| SDG 7 | Affordable and Clean Energy |
| SDG 8 | Decent Work and Economic Growth |
| SDG 9 | Industry, Innovation and Infrastructure |
| SDG 10 | Reduced Inequalities |
| SDG 11 | Sustainable Cities and Communities |
| SDG 12 | Responsible Consumption and Production |
| SDG 13 | Climate Action |
| SDG 14 | Life Below Water |
| SDG 15 | Life on Land |
| SDG 16 | Peace, Justice and Strong Institutions |

---

## Key Findings

"""

# Calculate key findings
total_articles = crosstab['Total'].sum()

# Top AI tasks
top_tasks = crosstab.nlargest(5, 'Total')
md_content += f"1. **{top_tasks.index[0]}** is the most common AI task ({top_tasks['Total'].iloc[0]:,} articles, {top_tasks['Total'].iloc[0]/total_articles*100:.1f}% of total)\n\n"

# SDG 11 dominance
sdg11_total = crosstab['SDG 11'].sum() if 'SDG 11' in crosstab.columns else 0
md_content += f"2. **SDG 11 (Sustainable Cities and Communities)** dominates with {sdg11_total:,} articles ({sdg11_total/total_articles*100:.1f}% of all AI task applications)\n\n"

# Second most common task
md_content += f"3. **{top_tasks.index[1]}** is the second most common task ({top_tasks['Total'].iloc[1]:,} articles, {top_tasks['Total'].iloc[1]/total_articles*100:.1f}%)\n\n"

# Optimization focus
if 'Optimization & Resource Allocation' in crosstab.index:
    opt_row = crosstab.loc['Optimization & Resource Allocation']
    opt_sdg7 = opt_row['SDG 7'] if 'SDG 7' in opt_row.index else 0
    opt_sdg11 = opt_row['SDG 11'] if 'SDG 11' in opt_row.index else 0
    opt_total = opt_row['Total']
    md_content += f"4. **Optimization & Resource Allocation** is heavily linked to SDG 7 (Energy, {opt_sdg7/opt_total*100:.1f}%) and SDG 11 (Cities, {opt_sdg11/opt_total*100:.1f}%)\n\n"

# Detection tasks
if 'Object/Anomaly/Change Detection' in crosstab.index:
    det_row = crosstab.loc['Object/Anomaly/Change Detection']
    det_sdg11 = det_row['SDG 11'] if 'SDG 11' in det_row.index else 0
    det_sdg9 = det_row['SDG 9'] if 'SDG 9' in det_row.index else 0
    det_total = det_row['Total']
    md_content += f"5. **Object/Anomaly/Change Detection** is primarily applied in SDG 11 ({det_sdg11/det_total*100:.1f}%) and SDG 9 (Infrastructure, {det_sdg9/det_total*100:.1f}%)\n\n"

# SDG 3 (Health) focus
if 'SDG 3' in crosstab.columns:
    sdg3_total = crosstab['SDG 3'].sum()
    sdg3_pred = crosstab.loc['Prediction & Forecasting', 'SDG 3'] if 'Prediction & Forecasting' in crosstab.index and 'SDG 3' in crosstab.columns else 0
    sdg3_class = crosstab.loc['Classification', 'SDG 3'] if 'Classification' in crosstab.index and 'SDG 3' in crosstab.columns else 0
    md_content += f"6. **SDG 3 (Health)** research primarily uses Prediction & Forecasting ({sdg3_pred/sdg3_total*100:.1f}%) and Classification ({sdg3_class/sdg3_total*100:.1f}%)\n\n"

# SDG 7 (Energy) focus
if 'SDG 7' in crosstab.columns:
    sdg7_total = crosstab['SDG 7'].sum()
    sdg7_pred = crosstab.loc['Prediction & Forecasting', 'SDG 7'] if 'Prediction & Forecasting' in crosstab.index and 'SDG 7' in crosstab.columns else 0
    sdg7_opt = crosstab.loc['Optimization & Resource Allocation', 'SDG 7'] if 'Optimization & Resource Allocation' in crosstab.index and 'SDG 7' in crosstab.columns else 0
    md_content += f"7. **SDG 7 (Energy)** research emphasizes Prediction & Forecasting ({sdg7_pred/sdg7_total*100:.1f}%) and Optimization ({sdg7_opt/sdg7_total*100:.1f}%)\n"

# Save markdown
with open(r'D:\Navid\Study\Ph.D 2\Thesis\12-ai-and-city\material\empirical_analysis\ai_task_sdg_table.md', 'w', encoding='utf-8') as f:
    f.write(md_content)

print('\nFiles saved:')
print('- ai_task_sdg_table.csv')
print('- ai_task_sdg_table.md')
