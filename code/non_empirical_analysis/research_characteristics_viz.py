"""
Faceted Heatmap: Research Characteristics by Megatrend for Non-Empirical Articles
Combines: Methodological Approach, Spatial Scale, Temporal Scale, Temporal Focus
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Rectangle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.family'] = 'Arial'
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

# Megatrend colors and names
MEGATREND_COLORS = {
    'Digital Transformation & Smart Cities': '#1565C0',
    'Climate Change & Environmental Sustainability': '#2E7D32',
    'Urban Mobility & Transportation': '#EF6C00',
    'Urban Development & Land Use': '#7B1FA2',
    'Social Equity & Quality of Life': '#00838F',
    'Urban Resilience & Safety': '#C62828',
}

MEGATREND_SHORT = [
    'Digital & Smart Cities',
    'Mobility & Transportation',
    'Climate & Environment',
    'Urban Development',
    'Resilience & Safety',
    'Social Equity & QoL',
]

MEGATREND_FULL = [
    'Digital Transformation & Smart Cities',
    'Urban Mobility & Transportation',
    'Climate Change & Environmental Sustainability',
    'Urban Development & Land Use',
    'Urban Resilience & Safety',
    'Social Equity & Quality of Life',
]

# Data from non-empirical analysis (ordered by article count)
DATA = {
    'Methodological Approach': {
        'categories': ['Quantitative', 'Mixed', 'Qualitative'],
        'values': np.array([
            [481, 116, 278],    # Digital
            [404, 20, 55],      # Mobility
            [282, 25, 43],      # Climate
            [197, 14, 16],      # Development
            [148, 17, 15],      # Resilience
            [61, 17, 30],       # Social
        ])
    },
    'Spatial Scale': {
        'categories': ['Local', 'Global', 'Regional', 'National', 'Individual', 'Supranational'],
        'values': np.array([
            [680, 129, 19, 22, 21, 4],
            [426, 21, 3, 2, 24, 2],
            [293, 26, 6, 2, 20, 3],
            [205, 10, 4, 2, 5, 1],
            [157, 11, 1, 1, 10, 0],
            [81, 16, 0, 0, 10, 1],
        ])
    },
    'Temporal Scale': {
        'categories': ['Present', 'Future', 'Past'],
        'values': np.array([
            [673, 149, 53],
            [377, 69, 32],
            [290, 41, 19],
            [163, 37, 27],
            [142, 19, 19],
            [85, 16, 7],
        ])
    },
    'Temporal Focus': {
        'categories': ['Cross-sectional', 'Longitudinal'],
        'values': np.array([
            [724, 151],
            [367, 111],
            [269, 81],
            [169, 58],
            [123, 57],
            [81, 27],
        ])
    },
}


def create_faceted_heatmap():
    """Create a 2x2 faceted heatmap"""

    fig = plt.figure(figsize=(18, 12))

    gs = fig.add_gridspec(2, 2, wspace=0.35, hspace=0.3,
                          left=0.18, right=0.95, top=0.90, bottom=0.08)

    # Color map - white to teal
    colors_cmap = ['#FFFFFF', '#E0F2F1', '#80CBC4', '#26A69A', '#00796B', '#004D40']
    cmap = LinearSegmentedColormap.from_list('teal_heat', colors_cmap, N=256)

    variables = list(DATA.keys())
    axes = []

    for idx, var_name in enumerate(variables):
        row = idx // 2
        col = idx % 2
        ax = fig.add_subplot(gs[row, col])
        axes.append(ax)

        var_data = DATA[var_name]
        categories = var_data['categories']
        values = var_data['values']

        n_mega = len(MEGATREND_SHORT)
        n_cats = len(categories)

        # Calculate percentages
        row_totals = values.sum(axis=1, keepdims=True)
        percentages = (values / row_totals * 100)

        vmax = percentages.max()

        # Draw heatmap cells
        for i in range(n_mega):
            for j in range(n_cats):
                pct = percentages[i, j]
                val = values[i, j]

                norm_val = pct / vmax if vmax > 0 else 0
                color = cmap(norm_val)

                rect = Rectangle((j, i), 1, 1, facecolor=color,
                                edgecolor='white', linewidth=1.5)
                ax.add_patch(rect)

                if pct >= 50:
                    text_color = 'white'
                    fontweight = 'bold'
                elif pct >= 20:
                    text_color = '#004D40'
                    fontweight = 'bold'
                else:
                    text_color = '#333333'
                    fontweight = 'normal'

                if val >= 100:
                    label = f'{val}\n({pct:.0f}%)'
                elif val > 0:
                    label = f'{val}\n({pct:.1f}%)'
                else:
                    label = '0'
                    text_color = '#BDBDBD'

                ax.text(j + 0.5, i + 0.5, label, ha='center', va='center',
                       fontsize=8, color=text_color, fontweight=fontweight,
                       linespacing=0.9)

        # Category labels on top
        for j, cat in enumerate(categories):
            if len(cat) > 12:
                cat_display = cat.replace('-', '-\n').replace(' ', '\n', 1)
            else:
                cat_display = cat
            ax.text(j + 0.5, -0.15, cat_display, ha='center', va='top',
                   fontsize=9, fontweight='medium', color='#333333')

        # Megatrend labels on left
        if col == 0:
            for i, mt in enumerate(MEGATREND_SHORT):
                rect = Rectangle((-0.4, i + 0.15), 0.25, 0.7,
                                facecolor=MEGATREND_COLORS[MEGATREND_FULL[i]],
                                edgecolor='none')
                ax.add_patch(rect)
                ax.text(-0.55, i + 0.5, mt, ha='right', va='center',
                       fontsize=9, color='#333333')

        # Panel title
        ax.set_title(f'{chr(65 + idx)}. {var_name}', fontsize=12, fontweight='bold',
                    loc='left', pad=15, color='#333333')

        ax.set_xlim(-0.5 if col == 0 else 0, n_cats)
        ax.set_ylim(n_mega, -0.5)
        ax.set_aspect('equal')
        ax.axis('off')

    # Main title
    fig.suptitle('Non-Empirical Research: Characteristics by Megatrend',
                fontsize=16, fontweight='bold', y=0.96)
    fig.text(0.5, 0.92, 'Cell values show article count and percentage within each megatrend',
            ha='center', fontsize=11, color='#666666')

    # Legend at bottom
    legend_y = 0.03
    for i, (mt_short, mt_full) in enumerate(zip(MEGATREND_SHORT, MEGATREND_FULL)):
        x = 0.18 + i * 0.13
        fig.patches.append(mpatches.FancyBboxPatch(
            (x, legend_y), 0.015, 0.02,
            facecolor=MEGATREND_COLORS[mt_full],
            edgecolor='none',
            transform=fig.transFigure,
            boxstyle='round,pad=0.002'
        ))
        fig.text(x + 0.02, legend_y + 0.01, mt_short, fontsize=8,
                va='center', ha='left', color='#333333')

    # Color scale legend
    cbar_ax = fig.add_axes([0.75, 0.03, 0.15, 0.015])
    sm = plt.cm.ScalarMappable(cmap=cmap)
    sm.set_array([])
    cbar = fig.colorbar(sm, cax=cbar_ax, orientation='horizontal')
    cbar.set_ticks([0, 0.5, 1])
    cbar.set_ticklabels(['Low', '', 'High'])
    cbar.ax.tick_params(labelsize=8)
    cbar_ax.set_title('% within megatrend', fontsize=8, pad=3)

    # Save
    fig.savefig('research_characteristics_heatmap.pdf', format='pdf', dpi=300,
               bbox_inches='tight', facecolor='white', edgecolor='none')
    fig.savefig('research_characteristics_heatmap.png', format='png', dpi=300,
               bbox_inches='tight', facecolor='white', edgecolor='none')

    print("Saved: research_characteristics_heatmap.pdf, research_characteristics_heatmap.png")
    plt.close()


if __name__ == "__main__":
    print("Creating faceted heatmap for non-empirical research characteristics...")
    create_faceted_heatmap()
    print("Done!")
