"""
Faceted Heatmap: Research Characteristics by Megatrend
Combines: Methodological Approach, Spatial Scale, Temporal Scale, Temporal Focus
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap, LogNorm
from matplotlib.patches import Rectangle, FancyBboxPatch
import numpy as np
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.family'] = 'Liberation Sans'
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
    'Climate & Environment',
    'Mobility & Transportation',
    'Urban Development',
    'Social Equity & QoL',
    'Resilience & Safety',
]

MEGATREND_FULL = [
    'Digital Transformation & Smart Cities',
    'Climate Change & Environmental Sustainability',
    'Urban Mobility & Transportation',
    'Urban Development & Land Use',
    'Social Equity & Quality of Life',
    'Urban Resilience & Safety',
]

# Data from the frequency tables
DATA = {
    'Methodological Approach': {
        'categories': ['Quantitative', 'Mixed', 'Qualitative'],
        'values': np.array([
            [1745, 281, 26],    # Digital
            [1450, 176, 19],    # Climate
            [480, 53, 6],       # Mobility
            [399, 61, 10],      # Social
            [452, 40, 14],      # Development
            [222, 4, 2],        # Resilience
        ])
    },
    'Spatial Scale': {
        'categories': ['Local', 'Global', 'Regional', 'National', 'Individual', 'Supranational'],
        'values': np.array([
            [1712, 124, 57, 44, 103, 12],
            [1188, 141, 150, 110, 37, 19],
            [487, 19, 11, 7, 14, 1],
            [335, 30, 41, 24, 37, 3],
            [379, 33, 47, 34, 9, 4],
            [204, 7, 7, 3, 7, 0],
        ])
    },
    'Temporal Scale': {
        'categories': ['Present', 'Future', 'Past'],
        'values': np.array([
            [1461, 474, 117],
            [1046, 426, 173],
            [361, 152, 26],
            [367, 66, 37],
            [287, 136, 83],
            [169, 39, 20],
        ])
    },
    'Temporal Focus': {
        'categories': ['Cross-sectional', 'Longitudinal'],
        'values': np.array([
            [1572, 480],
            [1093, 552],
            [437, 102],
            [375, 95],
            [304, 202],
            [179, 49],
        ])
    },
}


def create_faceted_heatmap():
    """Create a 2x2 faceted heatmap"""
    
    fig = plt.figure(figsize=(18, 12))
    
    # Create grid - 2x2 for the 4 variables
    # Add extra space on left for megatrend labels
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
        
        # Calculate percentages (row-wise)
        row_totals = values.sum(axis=1, keepdims=True)
        percentages = (values / row_totals * 100)
        
        # Find max for this variable for color scaling
        vmax = percentages.max()
        
        # Draw heatmap cells
        for i in range(n_mega):
            for j in range(n_cats):
                pct = percentages[i, j]
                val = values[i, j]
                
                # Color based on percentage
                norm_val = pct / vmax if vmax > 0 else 0
                color = cmap(norm_val)
                
                rect = Rectangle((j, i), 1, 1, facecolor=color, 
                                edgecolor='white', linewidth=1.5)
                ax.add_patch(rect)
                
                # Text: show both count and percentage
                if pct >= 50:
                    text_color = 'white'
                    fontweight = 'bold'
                elif pct >= 20:
                    text_color = '#004D40'
                    fontweight = 'bold'
                else:
                    text_color = '#333333'
                    fontweight = 'normal'
                
                # Format based on value size
                if val >= 1000:
                    label = f'{val:,}\n({pct:.0f}%)'
                elif val >= 100:
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
            # Wrap long category names
            if len(cat) > 12:
                cat_display = cat.replace('-', '-\n').replace(' ', '\n', 1)
            else:
                cat_display = cat
            ax.text(j + 0.5, -0.15, cat_display, ha='center', va='top',
                   fontsize=9, fontweight='medium', color='#333333')
        
        # Megatrend labels on left (only for left column)
        if col == 0:
            for i, mt in enumerate(MEGATREND_SHORT):
                # Color indicator
                rect = Rectangle((-0.4, i + 0.15), 0.25, 0.7,
                                facecolor=MEGATREND_COLORS[MEGATREND_FULL[i]], 
                                edgecolor='none')
                ax.add_patch(rect)
                ax.text(-0.55, i + 0.5, mt, ha='right', va='center',
                       fontsize=9, color='#333333')
        
        # Panel title
        ax.set_title(f'{chr(65 + idx)}. {var_name}', fontsize=12, fontweight='bold',
                    loc='left', pad=15, color='#333333')
        
        # Set limits
        ax.set_xlim(-0.5 if col == 0 else 0, n_cats)
        ax.set_ylim(n_mega, -0.5)
        ax.set_aspect('equal')
        ax.axis('off')
    
    # Main title
    fig.suptitle('Research Characteristics by Megatrend', 
                fontsize=16, fontweight='bold', y=0.96)
    fig.text(0.5, 0.92, 'Cell values show article count and percentage within each megatrend',
            ha='center', fontsize=11, color='#666666')
    
    # Legend for megatrends at bottom
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


def create_stacked_bar_version():
    """Alternative: Stacked bar chart version"""
    
    fig, axes = plt.subplots(1, 4, figsize=(20, 8), sharey=True)
    
    # Define colormaps for each variable
    color_schemes = {
        'Methodological Approach': ['#1565C0', '#42A5F5', '#90CAF9'],  # Blues
        'Spatial Scale': ['#2E7D32', '#66BB6A', '#A5D6A7', '#C8E6C9', '#E8F5E9', '#F1F8E9'],  # Greens
        'Temporal Scale': ['#E65100', '#FF9800', '#FFE0B2'],  # Oranges
        'Temporal Focus': ['#6A1B9A', '#BA68C8'],  # Purples
    }
    
    variables = list(DATA.keys())
    
    for ax_idx, var_name in enumerate(variables):
        ax = axes[ax_idx]
        
        var_data = DATA[var_name]
        categories = var_data['categories']
        values = var_data['values']
        colors = color_schemes[var_name]
        
        n_mega = len(MEGATREND_SHORT)
        
        # Calculate percentages
        row_totals = values.sum(axis=1, keepdims=True)
        percentages = (values / row_totals * 100)
        
        y_pos = np.arange(n_mega)
        
        # Stacked horizontal bars
        left = np.zeros(n_mega)
        for j, cat in enumerate(categories):
            bars = ax.barh(y_pos, percentages[:, j], left=left, height=0.7,
                          color=colors[j], label=cat, edgecolor='white', linewidth=0.5)
            
            # Add percentage labels for segments > 10%
            for i, (pct, l) in enumerate(zip(percentages[:, j], left)):
                if pct > 12:
                    ax.text(l + pct/2, i, f'{pct:.0f}%', ha='center', va='center',
                           fontsize=8, color='white' if pct > 30 else '#333333',
                           fontweight='bold')
            
            left += percentages[:, j]
        
        ax.set_xlim(0, 100)
        ax.set_ylim(-0.5, n_mega - 0.5)
        ax.invert_yaxis()
        
        if ax_idx == 0:
            ax.set_yticks(y_pos)
            ax.set_yticklabels(MEGATREND_SHORT, fontsize=9)
        
        ax.set_xlabel('Percentage', fontsize=10)
        ax.set_title(var_name, fontsize=11, fontweight='bold', pad=10)
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1),
                 ncol=min(3, len(categories)), fontsize=8, frameon=False)
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
    
    fig.suptitle('Research Characteristics by Megatrend', 
                fontsize=14, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    
    fig.savefig('research_characteristics_bars.pdf', format='pdf', dpi=300,
               bbox_inches='tight', facecolor='white')
    fig.savefig('research_characteristics_bars.png', format='png', dpi=300,
               bbox_inches='tight', facecolor='white')
    
    print("Saved: research_characteristics_bars.pdf, research_characteristics_bars.png")
    plt.close()


if __name__ == "__main__":
    print("Creating faceted heatmap...")
    create_faceted_heatmap()
    
    print("\nCreating stacked bar alternative...")
    create_stacked_bar_version()
    
    print("\nDone!")
