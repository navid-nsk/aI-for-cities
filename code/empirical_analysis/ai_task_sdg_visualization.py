"""
AI Tasks × SDGs - Multiple Chart Options with BLACK BORDERS
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch, Wedge
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# PDF settings for editable text in Adobe Illustrator
plt.rcParams['pdf.fonttype'] = 42  # TrueType fonts (editable in Illustrator)
plt.rcParams['ps.fonttype'] = 42   # TrueType fonts for PostScript
plt.rcParams['font.family'] = 'DejaVu Sans'  # Universal font that embeds well
plt.rcParams['svg.fonttype'] = 'none'  # Keep text as text in SVG
plt.rcParams['axes.unicode_minus'] = False  # Fix minus sign rendering

# Official UN SDG Colors
SDG_COLORS = {
    1: '#E5243B',   # No Poverty
    2: '#DDA63A',   # Zero Hunger
    3: '#4C9F38',   # Good Health
    4: '#C5192D',   # Quality Education
    5: '#FF3A21',   # Gender Equality
    6: '#26BDE2',   # Clean Water
    7: '#FCC30B',   # Affordable Energy
    8: '#A21942',   # Decent Work
    9: '#FD6925',   # Industry & Innovation
    10: '#DD1367',  # Reduced Inequalities
    11: '#FD9D24',  # Sustainable Cities
    12: '#BF8B2E',  # Responsible Consumption
    13: '#3F7E44',  # Climate Action
    14: '#0A97D9',  # Life Below Water
    15: '#56C02B',  # Life on Land
    16: '#00689D',  # Peace & Justice
}

SDG_NAMES = {
    1: 'No Poverty',
    2: 'Zero Hunger',
    3: 'Good Health',
    4: 'Quality Education',
    5: 'Gender Equality',
    6: 'Clean Water',
    7: 'Affordable Energy',
    8: 'Decent Work',
    9: 'Industry & Innovation',
    10: 'Reduced Inequalities',
    11: 'Sustainable Cities',
    12: 'Responsible Consumption',
    13: 'Climate Action',
    14: 'Life Below Water',
    15: 'Life on Land',
    16: 'Peace & Justice',
}


def load_and_process_data():
    df = pd.read_csv('/mnt/user-data/uploads/ai_task_sdg_table.csv')
    
    sdg_cols = [f'SDG {i}' for i in range(1, 17)]
    
    # Merge Classification + Clustering
    classification_row = df[df['ai_task_descriptive'] == 'Classification'].iloc[0]
    clustering_row = df[df['ai_task_descriptive'] == 'Clustering'].iloc[0]
    
    merged_values = {}
    merged_values['ai_task_descriptive'] = 'Classification/Clustering'
    for col in sdg_cols:
        merged_values[col] = classification_row[col] + clustering_row[col]
    merged_values['Total'] = classification_row['Total'] + clustering_row['Total']
    
    df_filtered = df[~df['ai_task_descriptive'].isin(['Classification', 'Clustering'])].copy()
    df_new = pd.concat([df_filtered, pd.DataFrame([merged_values])], ignore_index=True)
    df_new['Total'] = df_new[sdg_cols].sum(axis=1)
    df_sorted = df_new.sort_values('Total', ascending=False).reset_index(drop=True)
    
    top_7 = df_sorted.head(7)
    nlp_row = df_sorted[df_sorted['ai_task_descriptive'] == 'NLP/Text Analysis']
    
    if len(nlp_row) > 0 and 'NLP/Text Analysis' not in top_7['ai_task_descriptive'].values:
        df_final = pd.concat([top_7, nlp_row], ignore_index=True)
    else:
        df_final = top_7.copy()
    
    return df_final


def get_sdg_data(df):
    sdg_cols = [f'SDG {i}' for i in range(1, 17)]
    tasks = df['ai_task_descriptive'].tolist()
    values = df[sdg_cols].values.astype(float)
    totals = df['Total'].values
    return tasks, values, totals, sdg_cols


# ============================================================
# OPTION 1: Horizontal Stacked Bar (Absolute)
# ============================================================
def create_option1_stacked_bar(df):
    tasks, values, totals, sdg_cols = get_sdg_data(df)
    n_tasks = len(tasks)
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    bar_height = 0.7
    y_pos = np.arange(n_tasks)
    
    left = np.zeros(n_tasks)
    
    for sdg_num in range(1, 17):
        sdg_values = values[:, sdg_num - 1]
        if sdg_values.sum() > 0:
            ax.barh(y_pos, sdg_values, left=left, height=bar_height,
                   color=SDG_COLORS[sdg_num], edgecolor='black', linewidth=0.8)
            
            for i, (val, l) in enumerate(zip(sdg_values, left)):
                if val >= 50:
                    ax.text(l + val/2, i, f'{int(val)}', ha='center', va='center',
                           fontsize=11, color='white', fontweight='bold')
            
            left += sdg_values
    
    for i, total in enumerate(totals):
        ax.text(total + 20, i, f'{int(total):,}', ha='left', va='center',
               fontsize=13, fontweight='bold', color='#333333')
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(tasks, fontsize=13)
    ax.set_xlabel('Number of Articles', fontsize=13)
    ax.set_xlim(0, max(totals) * 1.15)
    ax.invert_yaxis()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(left=False)
    
    ax.set_title('Option 1: Horizontal Stacked Bar (Absolute)',
                fontsize=16, fontweight='bold', pad=15)
    
    legend_handles = [mpatches.Patch(facecolor=SDG_COLORS[i], edgecolor='black', linewidth=0.8, label=f'{i}') 
                     for i in range(1, 17) if values[:, i-1].sum() > 0]
    ax.legend(handles=legend_handles, loc='lower right', ncol=8, fontsize=9,
             title='SDG', title_fontsize=10, frameon=True)
    
    plt.tight_layout()
    fig.savefig('option1_stacked_bar.png', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('option1_stacked_bar.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Saved: option1_stacked_bar")


# ============================================================
# OPTION 2: Horizontal Stacked Bar (Percentage)
# ============================================================
def create_option2_percentage_bar(df):
    tasks, values, totals, sdg_cols = get_sdg_data(df)
    n_tasks = len(tasks)
    percentages = values / totals[:, np.newaxis] * 100
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    bar_height = 0.7
    y_pos = np.arange(n_tasks)
    
    left = np.zeros(n_tasks)
    
    for sdg_num in range(1, 17):
        sdg_pct = percentages[:, sdg_num - 1]
        if sdg_pct.sum() > 0:
            ax.barh(y_pos, sdg_pct, left=left, height=bar_height,
                   color=SDG_COLORS[sdg_num], edgecolor='black', linewidth=0.8)
            
            for i, (pct, l) in enumerate(zip(sdg_pct, left)):
                if pct >= 10:
                    ax.text(l + pct/2, i, f'{pct:.0f}%', ha='center', va='center',
                           fontsize=10, color='white', fontweight='bold')
            
            left += sdg_pct
    
    for i, total in enumerate(totals):
        ax.text(102, i, f'n={int(total):,}', ha='left', va='center',
               fontsize=11, color='#666666', style='italic')
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(tasks, fontsize=13)
    ax.set_xlabel('Percentage (%)', fontsize=13)
    ax.set_xlim(0, 115)
    ax.invert_yaxis()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(left=False)
    
    ax.set_title('Option 2: Horizontal Stacked Bar (Percentage)',
                fontsize=16, fontweight='bold', pad=15)
    
    legend_handles = [mpatches.Patch(facecolor=SDG_COLORS[i], edgecolor='black', linewidth=0.8, label=f'{i}') 
                     for i in range(1, 17) if values[:, i-1].sum() > 0]
    ax.legend(handles=legend_handles, loc='lower right', ncol=8, fontsize=9,
             title='SDG', title_fontsize=10, frameon=True)
    
    plt.tight_layout()
    fig.savefig('option2_percentage_bar.png', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('option2_percentage_bar.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Saved: option2_percentage_bar")


# ============================================================
# OPTION 3: Grouped Bar Chart
# ============================================================
def create_option3_grouped_bar(df):
    tasks, values, totals, sdg_cols = get_sdg_data(df)
    n_tasks = len(tasks)
    
    sdg_totals = values.sum(axis=0)
    top_sdg_indices = np.argsort(sdg_totals)[-6:][::-1]
    top_sdgs = [i + 1 for i in top_sdg_indices]
    
    fig, ax = plt.subplots(figsize=(16, 8))
    
    x = np.arange(n_tasks)
    width = 0.12
    
    for idx, sdg_num in enumerate(top_sdgs):
        offset = (idx - len(top_sdgs)/2 + 0.5) * width
        sdg_values = values[:, sdg_num - 1]
        bars = ax.bar(x + offset, sdg_values, width, 
                     color=SDG_COLORS[sdg_num],
                     edgecolor='black', linewidth=0.8,
                     label=f'SDG {sdg_num}: {SDG_NAMES[sdg_num]}')
    
    ax.set_xticks(x)
    ax.set_xticklabels(tasks, fontsize=11, rotation=25, ha='right')
    ax.set_ylabel('Number of Articles', fontsize=13)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    ax.set_title('Option 3: Grouped Bar Chart (Top 6 SDGs)',
                fontsize=16, fontweight='bold', pad=15)
    
    ax.legend(loc='upper right', fontsize=9, frameon=True)
    
    plt.tight_layout()
    fig.savefig('option3_grouped_bar.png', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('option3_grouped_bar.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Saved: option3_grouped_bar")


# ============================================================
# OPTION 4: Lollipop Chart
# ============================================================
def create_option4_lollipop(df):
    tasks, values, totals, sdg_cols = get_sdg_data(df)
    n_tasks = len(tasks)
    
    fig, ax = plt.subplots(figsize=(14, 8))
    
    y_pos = np.arange(n_tasks)
    
    for i, task in enumerate(tasks):
        task_values = values[i]
        top_3_idx = np.argsort(task_values)[-3:][::-1]
        
        for rank, sdg_idx in enumerate(top_3_idx):
            sdg_num = sdg_idx + 1
            val = task_values[sdg_idx]
            if val > 0:
                x_offset = rank * 0.25
                ax.plot([val, val], [i - 0.2 + x_offset, i - 0.2 + x_offset], 
                       color=SDG_COLORS[sdg_num], linewidth=2)
                ax.plot([0, val], [i - 0.2 + x_offset, i - 0.2 + x_offset], 
                       color=SDG_COLORS[sdg_num], linewidth=1.5, alpha=0.5)
                ax.scatter(val, i - 0.2 + x_offset, s=150, color=SDG_COLORS[sdg_num], 
                          zorder=5, edgecolor='black', linewidth=1.2)
                ax.text(val + 15, i - 0.2 + x_offset, f'SDG{sdg_num}: {int(val)}', 
                       va='center', fontsize=9, color='#333333')
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(tasks, fontsize=12)
    ax.set_xlabel('Number of Articles', fontsize=13)
    ax.invert_yaxis()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(left=False)
    
    ax.set_title('Option 4: Lollipop Chart (Top 3 SDGs per Task)',
                fontsize=16, fontweight='bold', pad=15)
    
    plt.tight_layout()
    fig.savefig('option4_lollipop.png', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('option4_lollipop.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Saved: option4_lollipop")


# ============================================================
# OPTION 5: Bubble Chart
# ============================================================
def create_option5_bubble(df):
    tasks, values, totals, sdg_cols = get_sdg_data(df)
    n_tasks = len(tasks)
    
    fig, ax = plt.subplots(figsize=(16, 9))
    
    active_sdgs = [i for i in range(1, 17) if values[:, i-1].sum() > 10]
    
    for i, task in enumerate(tasks):
        for sdg_num in active_sdgs:
            val = values[i, sdg_num - 1]
            if val > 0:
                size = np.sqrt(val) * 15
                ax.scatter(sdg_num, i, s=size, color=SDG_COLORS[sdg_num],
                          alpha=0.8, edgecolor='black', linewidth=1.2)
                if val >= 30:
                    ax.text(sdg_num, i, f'{int(val)}', ha='center', va='center',
                           fontsize=8, color='white', fontweight='bold')
    
    ax.set_xticks(active_sdgs)
    ax.set_xticklabels([f'SDG {s}' for s in active_sdgs], fontsize=10, rotation=45, ha='right')
    ax.set_yticks(range(n_tasks))
    ax.set_yticklabels(tasks, fontsize=11)
    ax.invert_yaxis()
    ax.set_xlim(0, 17)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    ax.set_title('Option 5: Bubble Chart (Size = Article Count)',
                fontsize=16, fontweight='bold', pad=15)
    
    for size_val in [50, 200, 500]:
        ax.scatter([], [], s=np.sqrt(size_val)*15, c='gray', alpha=0.5,
                  label=f'{size_val}', edgecolor='black', linewidth=1)
    ax.legend(title='Articles', loc='lower right', fontsize=9, frameon=True)
    
    plt.tight_layout()
    fig.savefig('option5_bubble.png', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('option5_bubble.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Saved: option5_bubble")


# ============================================================
# OPTION 6: Diverging Bar Chart
# ============================================================
def create_option6_diverging(df):
    tasks, values, totals, sdg_cols = get_sdg_data(df)
    n_tasks = len(tasks)
    
    sdg11_values = values[:, 10]
    other_values = totals - sdg11_values
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    y_pos = np.arange(n_tasks)
    
    ax.barh(y_pos, sdg11_values, height=0.6, color=SDG_COLORS[11], 
           label='SDG 11: Sustainable Cities', edgecolor='black', linewidth=0.8)
    
    ax.barh(y_pos, -other_values, height=0.6, color='#78909C',
           label='Other SDGs', edgecolor='black', linewidth=0.8)
    
    for i, (sdg11, other) in enumerate(zip(sdg11_values, other_values)):
        if sdg11 > 50:
            ax.text(sdg11/2, i, f'{int(sdg11)}', ha='center', va='center',
                   fontsize=11, color='white', fontweight='bold')
        if other > 50:
            ax.text(-other/2, i, f'{int(other)}', ha='center', va='center',
                   fontsize=11, color='white', fontweight='bold')
    
    ax.set_yticks(y_pos)
    ax.set_yticklabels(tasks, fontsize=12)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_xlabel('← Other SDGs | SDG 11 (Sustainable Cities) →', fontsize=12)
    ax.invert_yaxis()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend(loc='lower right', fontsize=10)
    
    ax.set_title('Option 6: Diverging Bar (SDG 11 vs Others)',
                fontsize=16, fontweight='bold', pad=15)
    
    plt.tight_layout()
    fig.savefig('option6_diverging.png', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('option6_diverging.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Saved: option6_diverging")


# ============================================================
# OPTION 7: Donut Charts (Small Multiples)
# ============================================================
def create_option7_donut(df):
    tasks, values, totals, sdg_cols = get_sdg_data(df)
    n_tasks = len(tasks)
    
    fig, axes = plt.subplots(2, 4, figsize=(16, 8))
    axes = axes.flatten()
    
    for i, (task, ax) in enumerate(zip(tasks, axes)):
        task_values = values[i]
        
        nonzero_mask = task_values > 0
        nonzero_values = task_values[nonzero_mask]
        nonzero_sdgs = [j+1 for j in range(16) if nonzero_mask[j]]
        colors = [SDG_COLORS[s] for s in nonzero_sdgs]
        
        wedges, texts = ax.pie(nonzero_values, colors=colors,
                               wedgeprops=dict(width=0.5, edgecolor='black', linewidth=0.8))
        
        ax.text(0, 0, f'n={int(totals[i]):,}', ha='center', va='center',
               fontsize=11, fontweight='bold')
        
        ax.set_title(task, fontsize=11, fontweight='medium', pad=5)
    
    fig.suptitle('Option 7: Donut Charts (SDG Distribution per Task)',
                fontsize=16, fontweight='bold', y=1.02)
    
    legend_handles = [mpatches.Patch(facecolor=SDG_COLORS[i], edgecolor='black', linewidth=0.8, label=f'SDG {i}') 
                     for i in range(1, 17) if values[:, i-1].sum() > 0]
    fig.legend(handles=legend_handles, loc='lower center', ncol=8, 
              fontsize=9, bbox_to_anchor=(0.5, -0.02))
    
    plt.tight_layout()
    fig.savefig('option7_donut.png', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('option7_donut.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Saved: option7_donut")


# ============================================================
# OPTION 8: Proportional Area Chart
# ============================================================
def create_option8_proportional(df):
    tasks, values, totals, sdg_cols = get_sdg_data(df)
    total_all = totals.sum()
    
    fig, ax = plt.subplots(figsize=(14, 10))
    
    current_y = 0
    
    for i, task in enumerate(tasks):
        task_values = values[i]
        task_total = totals[i]
        
        height = task_total / total_all * 8
        
        current_x = 0
        for sdg_num in range(1, 17):
            val = task_values[sdg_num - 1]
            if val > 0:
                width = val / task_total * 10
                rect = FancyBboxPatch((current_x, current_y), width, height,
                                     facecolor=SDG_COLORS[sdg_num],
                                     edgecolor='black', linewidth=0.8,
                                     boxstyle='round,pad=0.01')
                ax.add_patch(rect)
                
                if width > 0.8 and height > 0.3:
                    ax.text(current_x + width/2, current_y + height/2, 
                           f'{int(val)}', ha='center', va='center',
                           fontsize=9, color='white', fontweight='bold')
                
                current_x += width
        
        ax.text(-0.2, current_y + height/2, task, ha='right', va='center',
               fontsize=11, color='#333333')
        
        ax.text(10.2, current_y + height/2, f'{int(task_total):,}', 
               ha='left', va='center', fontsize=11, fontweight='bold', color='#333333')
        
        current_y += height + 0.1
    
    ax.set_xlim(-4, 11.5)
    ax.set_ylim(-0.2, current_y + 0.2)
    ax.axis('off')
    
    ax.set_title('Option 8: Proportional Area Chart',
                fontsize=16, fontweight='bold', pad=15)
    
    legend_handles = [mpatches.Patch(facecolor=SDG_COLORS[i], edgecolor='black', linewidth=0.8, label=f'SDG {i}') 
                     for i in range(1, 17) if values[:, i-1].sum() > 0]
    ax.legend(handles=legend_handles, loc='lower center', ncol=8,
             fontsize=9, bbox_to_anchor=(0.5, -0.05))
    
    plt.tight_layout()
    fig.savefig('option8_proportional.png', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('option8_proportional.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Saved: option8_proportional")


if __name__ == "__main__":
    print("Loading and processing data...")
    df = load_and_process_data()
    
    print(f"\nFinal 8 AI Tasks:")
    for i, row in df.iterrows():
        print(f"  {i+1}. {row['ai_task_descriptive']} (n={int(row['Total']):,})")
    
    print(f"\nTotal articles: {df['Total'].sum():,}")
    
    print("\n" + "="*50)
    print("Creating 8 chart options with BLACK BORDERS...")
    print("="*50)
    
    create_option1_stacked_bar(df)
    create_option2_percentage_bar(df)
    create_option3_grouped_bar(df)
    create_option4_lollipop(df)
    create_option5_bubble(df)
    create_option6_diverging(df)
    create_option7_donut(df)
    create_option8_proportional(df)
    
    print("\n" + "="*50)
    print("Done! All charts have black borders.")
    print("="*50)
