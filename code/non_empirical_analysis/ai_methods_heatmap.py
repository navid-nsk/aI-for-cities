"""
AI Methods x Megatrends Heatmap - Yellow color scheme for Non-Empirical Articles
"""

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# PDF settings for editable text in Illustrator
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['svg.fonttype'] = 'none'

# Megatrend colors
MEGATREND_COLORS = {
    'Digital Transformation & Smart Cities': '#1565C0',
    'Climate Change & Environmental Sustainability': '#2E7D32',
    'Urban Mobility & Transportation': '#EF6C00',
    'Social Equity & Quality of Life': '#00838F',
    'Urban Development & Land Use': '#7B1FA2',
    'Urban Resilience & Safety': '#C62828',
}

MEGATREND_SHORT = {
    'Digital Transformation & Smart Cities': 'Digital &\nSmart Cities',
    'Climate Change & Environmental Sustainability': 'Climate &\nEnvironment',
    'Urban Mobility & Transportation': 'Mobility &\nTransportation',
    'Social Equity & Quality of Life': 'Social Equity\n& QoL',
    'Urban Development & Land Use': 'Urban\nDevelopment',
    'Urban Resilience & Safety': 'Resilience\n& Safety',
}

MEGATREND_ORDER = [
    'Digital Transformation & Smart Cities',
    'Urban Mobility & Transportation',
    'Climate Change & Environmental Sustainability',
    'Urban Development & Land Use',
    'Urban Resilience & Safety',
    'Social Equity & Quality of Life',
]


def load_data():
    df = pd.read_csv('ai_method_megatrend_table.csv')
    df = df.rename(columns={df.columns[0]: 'AI_Method'})
    df = df[df['AI_Method'] != 'Total'].copy()
    return df


def create_heatmap(df):
    """Create heatmap with yellow color scheme"""

    # Yellow/Amber color scheme
    colors_cmap = ['#FFFFFF', '#FFFDE7', '#FFF59D', '#FFEE58', '#FDD835', '#F9A825', '#F57F17']
    cmap = LinearSegmentedColormap.from_list('yellow_heat', colors_cmap, N=256)

    # Use available megatrend columns
    available_cols = [col for col in MEGATREND_ORDER if col in df.columns]
    megatrend_cols = available_cols

    df_sorted = df.sort_values('Total', ascending=False).reset_index(drop=True)

    methods = df_sorted['AI_Method'].tolist()
    values = df_sorted[megatrend_cols].values.astype(float)
    totals = df_sorted['Total'].values

    n_methods = len(methods)
    n_mega = len(megatrend_cols)

    # Cell dimensions
    cell_width = 2.8
    cell_height = 0.75

    left_margin = 6.0
    right_margin = 2.8
    top_margin = 3.2
    bottom_margin = 2.0

    fig_width = left_margin + n_mega * cell_width + right_margin
    fig_height = top_margin + n_methods * cell_height + bottom_margin

    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    vmax = values.max() if values.max() > 0 else 1

    x_start = left_margin
    y_start = top_margin

    # Draw heatmap cells
    for i in range(n_methods):
        for j in range(n_mega):
            val = values[i, j]

            x = x_start + j * cell_width
            y = y_start + i * cell_height

            if val == 0:
                color = '#F5F5F5'
                text_color = '#BDBDBD'
                fontweight = 'normal'
            else:
                norm_val = np.log10(val + 1) / np.log10(vmax + 1)
                color = cmap(norm_val)
                if norm_val > 0.6:
                    text_color = '#5D4037'
                    fontweight = 'bold'
                else:
                    text_color = '#5D4037'
                    fontweight = 'bold'

            rect = Rectangle((x, y), cell_width, cell_height, facecolor=color,
                            edgecolor='white', linewidth=2)
            ax.add_patch(rect)

            label = f'{int(val)}' if val > 0 else '0'
            ax.text(x + cell_width/2, y + cell_height/2, label,
                   ha='center', va='center', fontsize=14,
                   color=text_color, fontweight=fontweight)

    # Megatrend headers
    header_box_y = y_start - 0.9
    header_text_y = y_start - 1.8

    for j, mt in enumerate(megatrend_cols):
        x = x_start + j * cell_width

        box_margin = 0.35
        rect = Rectangle((x + box_margin, header_box_y), cell_width - 2*box_margin, 0.65,
                        facecolor=MEGATREND_COLORS.get(mt, '#888888'), edgecolor='none')
        ax.add_patch(rect)

        short_name = MEGATREND_SHORT.get(mt, mt)
        ax.text(x + cell_width/2, header_text_y, short_name,
               ha='center', va='top', fontsize=12, fontweight='bold',
               color='#333333', linespacing=0.85)

    # AI Method labels
    for i, method in enumerate(methods):
        y = y_start + i * cell_height
        ax.text(x_start - 0.5, y + cell_height/2, method,
               ha='right', va='center', fontsize=14, color='#222222', fontweight='medium')

    # Total column
    total_x = x_start + n_mega * cell_width + 0.7

    ax.text(total_x, header_box_y + 0.35, 'Total', ha='left', va='center',
           fontsize=14, fontweight='bold', color='#333333')

    for i, total in enumerate(totals):
        y = y_start + i * cell_height
        ax.text(total_x, y + cell_height/2, f'{int(total):,}',
               ha='left', va='center', fontsize=14, fontweight='bold',
               color='#E65100')

    ax.set_xlim(0, fig_width)
    ax.set_ylim(fig_height, 0)
    ax.axis('off')

    # Title
    ax.text(x_start + (n_mega * cell_width) / 2, 0.8,
           'Non-Empirical Research: AI Methods Across Megatrends',
           ha='center', va='center', fontsize=18, fontweight='bold')

    # Colorbar
    cbar_width = n_mega * cell_width * 0.45
    cbar_height = 0.4
    cbar_x = x_start + (n_mega * cell_width - cbar_width) / 2
    cbar_y = y_start + n_methods * cell_height + 0.8

    n_segments = 100
    for k in range(n_segments):
        norm_val = k / n_segments
        color = cmap(norm_val)
        rect = Rectangle((cbar_x + k * cbar_width/n_segments, cbar_y),
                        cbar_width/n_segments + 0.01, cbar_height,
                        facecolor=color, edgecolor='none')
        ax.add_patch(rect)

    rect = Rectangle((cbar_x, cbar_y), cbar_width, cbar_height,
                    facecolor='none', edgecolor='#999999', linewidth=1)
    ax.add_patch(rect)

    ax.text(cbar_x, cbar_y + cbar_height + 0.25, '1', ha='center', va='bottom',
           fontsize=11, color='#555555')
    ax.text(cbar_x + cbar_width, cbar_y + cbar_height + 0.25, f'{int(vmax)}',
           ha='center', va='bottom', fontsize=11, color='#555555')
    ax.text(cbar_x + cbar_width/2, cbar_y + cbar_height + 0.25,
           'Articles (log scale)', ha='center', va='bottom', fontsize=11, color='#555555')

    plt.tight_layout()

    # Save
    fig.savefig('ai_methods_heatmap.pdf', format='pdf', dpi=300,
               bbox_inches='tight', facecolor='white')
    fig.savefig('ai_methods_heatmap.png', format='png', dpi=300,
               bbox_inches='tight', facecolor='white')

    print("Saved: ai_methods_heatmap.pdf, ai_methods_heatmap.png")
    plt.close()


if __name__ == "__main__":
    print("Loading data...")
    df = load_data()
    print(f"  AI Methods: {len(df)}")
    print(f"  Total articles: {df['Total'].sum():,}")

    print("\nCreating yellow heatmap...")
    create_heatmap(df)

    print("\nDone!")
