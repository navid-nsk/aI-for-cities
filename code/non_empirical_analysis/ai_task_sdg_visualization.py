"""
AI Tasks x SDGs Visualization for Non-Empirical Articles
- Horizontal stacked bar charts (absolute and percentage)
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# PDF settings for editable text in Adobe Illustrator
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['svg.fonttype'] = 'none'

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


def load_data():
    df = pd.read_csv('ai_task_sdg_table.csv')
    return df


def get_sdg_data(df):
    sdg_cols = [f'SDG {i}' for i in range(1, 17)]
    # Filter to only existing columns
    existing_cols = [col for col in sdg_cols if col in df.columns]

    tasks = df['ai_task_descriptive'].tolist()

    # Create values array with all 16 SDGs
    values = np.zeros((len(tasks), 16))
    for i, col in enumerate(sdg_cols):
        if col in df.columns:
            values[:, i] = df[col].values

    totals = df['Total'].values
    return tasks, values, totals, sdg_cols


def create_stacked_bar_absolute(df):
    """Create horizontal stacked bar chart with absolute values"""
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
                if val >= 30:
                    ax.text(l + val/2, i, f'{int(val)}', ha='center', va='center',
                           fontsize=10, color='white', fontweight='bold')

            left += sdg_values

    for i, total in enumerate(totals):
        ax.text(total + 10, i, f'{int(total):,}', ha='left', va='center',
               fontsize=12, fontweight='bold', color='#333333')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(tasks, fontsize=12)
    ax.set_xlabel('Number of Articles', fontsize=12)
    ax.set_xlim(0, max(totals) * 1.15)
    ax.invert_yaxis()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(left=False)

    ax.set_title('Non-Empirical Research: AI Tasks by SDG Alignment (Absolute)',
                fontsize=14, fontweight='bold', pad=15)

    legend_handles = [mpatches.Patch(facecolor=SDG_COLORS[i], edgecolor='black', linewidth=0.8, label=f'{i}')
                     for i in range(1, 17) if values[:, i-1].sum() > 0]
    ax.legend(handles=legend_handles, loc='lower right', ncol=8, fontsize=9,
             title='SDG', title_fontsize=10, frameon=True)

    plt.tight_layout()
    fig.savefig('ai_task_sdg_absolute.png', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('ai_task_sdg_absolute.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Saved: ai_task_sdg_absolute")


def create_stacked_bar_percentage(df):
    """Create horizontal stacked bar chart with percentages"""
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
                if pct >= 8:
                    ax.text(l + pct/2, i, f'{pct:.0f}%', ha='center', va='center',
                           fontsize=9, color='white', fontweight='bold')

            left += sdg_pct

    for i, total in enumerate(totals):
        ax.text(102, i, f'n={int(total):,}', ha='left', va='center',
               fontsize=10, color='#666666', style='italic')

    ax.set_yticks(y_pos)
    ax.set_yticklabels(tasks, fontsize=12)
    ax.set_xlabel('Percentage (%)', fontsize=12)
    ax.set_xlim(0, 115)
    ax.invert_yaxis()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(left=False)

    ax.set_title('Non-Empirical Research: AI Tasks by SDG Alignment (Percentage)',
                fontsize=14, fontweight='bold', pad=15)

    legend_handles = [mpatches.Patch(facecolor=SDG_COLORS[i], edgecolor='black', linewidth=0.8, label=f'{i}')
                     for i in range(1, 17) if values[:, i-1].sum() > 0]
    ax.legend(handles=legend_handles, loc='lower right', ncol=8, fontsize=9,
             title='SDG', title_fontsize=10, frameon=True)

    plt.tight_layout()
    fig.savefig('ai_task_sdg_percentage.png', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('ai_task_sdg_percentage.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Saved: ai_task_sdg_percentage")


def create_bubble_chart(df):
    """Create bubble chart showing AI Task x SDG relationship"""
    tasks, values, totals, sdg_cols = get_sdg_data(df)
    n_tasks = len(tasks)

    fig, ax = plt.subplots(figsize=(16, 9))

    active_sdgs = [i for i in range(1, 17) if values[:, i-1].sum() > 5]

    for i, task in enumerate(tasks):
        for sdg_num in active_sdgs:
            val = values[i, sdg_num - 1]
            if val > 0:
                size = np.sqrt(val) * 12
                ax.scatter(sdg_num, i, s=size, color=SDG_COLORS[sdg_num],
                          alpha=0.8, edgecolor='black', linewidth=1)
                if val >= 20:
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

    ax.set_title('Non-Empirical Research: AI Tasks x SDGs (Bubble Size = Article Count)',
                fontsize=14, fontweight='bold', pad=15)

    for size_val in [20, 100, 300]:
        ax.scatter([], [], s=np.sqrt(size_val)*12, c='gray', alpha=0.5,
                  label=f'{size_val}', edgecolor='black', linewidth=1)
    ax.legend(title='Articles', loc='lower right', fontsize=9, frameon=True)

    plt.tight_layout()
    fig.savefig('ai_task_sdg_bubble.png', dpi=300, bbox_inches='tight', facecolor='white')
    fig.savefig('ai_task_sdg_bubble.pdf', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("Saved: ai_task_sdg_bubble")


if __name__ == "__main__":
    print("Loading and processing data...")
    df = load_data()

    print(f"\nAI Tasks: {len(df)}")
    for i, row in df.iterrows():
        print(f"  {i+1}. {row['ai_task_descriptive']} (n={int(row['Total']):,})")

    print(f"\nTotal articles: {df['Total'].sum():,}")

    print("\n" + "="*50)
    print("Creating visualizations...")
    print("="*50)

    create_stacked_bar_absolute(df)
    create_stacked_bar_percentage(df)
    create_bubble_chart(df)

    print("\n" + "="*50)
    print("Done! All charts created.")
    print("="*50)
