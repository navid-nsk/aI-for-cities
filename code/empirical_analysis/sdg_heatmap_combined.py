"""
Combined SDG Heatmap with Integrated Sustainability Level
- Single panel design
- Official UN SDG colors
- Sustainability bars integrated on the right
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap, LogNorm
from matplotlib.patches import Rectangle, FancyBboxPatch
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

plt.rcParams['font.family'] = 'Liberation Sans'
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

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
    1: 'No Poverty', 2: 'Zero Hunger', 3: 'Good Health', 4: 'Quality Education',
    5: 'Gender Equality', 6: 'Clean Water', 7: 'Affordable Energy', 8: 'Decent Work',
    9: 'Industry & Innovation', 10: 'Reduced Inequalities', 11: 'Sustainable Cities',
    12: 'Responsible Consumption', 13: 'Climate Action', 14: 'Life Below Water',
    15: 'Life on Land', 16: 'Peace & Justice',
}

MEGATREND_COLORS = {
    'Digital Transformation & Smart Cities': '#1565C0',
    'Climate Change & Environmental Sustainability': '#2E7D32',
    'Urban Mobility & Transportation': '#EF6C00',
    'Urban Development & Land Use': '#7B1FA2',
    'Social Equity & Quality of Life': '#00838F',
    'Urban Resilience & Safety': '#C62828',
}

MEGATREND_SHORT = {
    'Digital Transformation & Smart Cities': 'Digital & Smart Cities',
    'Climate Change & Environmental Sustainability': 'Climate & Environment',
    'Urban Mobility & Transportation': 'Mobility & Transportation',
    'Urban Development & Land Use': 'Urban Development',
    'Social Equity & Quality of Life': 'Social Equity & QoL',
    'Urban Resilience & Safety': 'Resilience & Safety',
}

SUSTAINABILITY_COLORS = {
    'Strong': '#1B5E20',
    'Medium': '#F9A825', 
    'Weak': '#E65100',
}


def load_data():
    df = pd.read_csv('/mnt/user-data/uploads/1767394602600_megatrend_sdg_sustainability_table.csv')
    df_main = df[df['Megatrend'] != 'Total'].copy()
    return df_main


def create_combined_visualization():
    df = load_data()
    
    megatrends = df['Megatrend'].tolist()
    sdg_cols = [str(i) for i in range(1, 17)]
    sdg_matrix = df[sdg_cols].values.astype(float)
    sustainability = df[['Strong', 'Medium', 'Weak']].values
    totals = df['Total'].values
    
    # Figure setup
    fig, ax = plt.subplots(figsize=(18, 9))
    
    # Layout parameters
    n_sdgs = 16
    n_mega = len(megatrends)
    
    # Heatmap area: columns 0-15 for SDGs, column 16 for gap, columns 17-19 for sustainability
    cell_width = 1.0
    gap_width = 0.4
    sust_width = 2.5  # Width for sustainability stacked bar
    
    # Create colormap
    colors_cmap = ['#FFFFFF', '#FFF8E1', '#FFE082', '#FFB300', '#FF8F00', '#E65100']
    cmap = LinearSegmentedColormap.from_list('sdg_heat', colors_cmap, N=256)
    
    # Prepare data for heatmap
    sdg_display = sdg_matrix.copy()
    sdg_display[sdg_display == 0] = np.nan
    vmax = np.nanmax(sdg_display)
    
    # Draw heatmap cells manually for precise control
    for i in range(n_mega):
        for j in range(n_sdgs):
            val = sdg_matrix[i, j]
            
            if val == 0:
                # Zero cells - light gray
                rect = Rectangle((j, i), cell_width, 1, 
                                facecolor='#F5F5F5', edgecolor='white', linewidth=1.5)
                ax.add_patch(rect)
                ax.text(j + 0.5, i + 0.5, '0', ha='center', va='center',
                       fontsize=9, color='#BDBDBD')
            else:
                # Colored cells based on log scale
                norm_val = np.log10(val + 1) / np.log10(vmax + 1)
                color = cmap(norm_val)
                rect = Rectangle((j, i), cell_width, 1,
                                facecolor=color, edgecolor='white', linewidth=1.5)
                ax.add_patch(rect)
                
                # Text color based on background brightness
                if norm_val > 0.6:
                    text_color = 'white'
                    fontweight = 'bold'
                else:
                    text_color = '#333333'
                    fontweight = 'normal'
                
                ax.text(j + 0.5, i + 0.5, f'{int(val)}', ha='center', va='center',
                       fontsize=9, color=text_color, fontweight=fontweight)
    
    # SDG header row with colors
    for j in range(n_sdgs):
        sdg_num = j + 1
        rect = Rectangle((j, -0.8), cell_width, 0.7,
                        facecolor=SDG_COLORS[sdg_num], edgecolor='white', linewidth=1)
        ax.add_patch(rect)
        ax.text(j + 0.5, -0.45, str(sdg_num), ha='center', va='center',
               fontsize=10, color='white', fontweight='bold')
    
    # Megatrend labels and color indicators
    for i, mt in enumerate(megatrends):
        # Color indicator bar
        rect = Rectangle((-0.6, i + 0.1), 0.4, 0.8,
                        facecolor=MEGATREND_COLORS[mt], edgecolor='none')
        ax.add_patch(rect)
        
        # Label
        short_name = MEGATREND_SHORT.get(mt, mt)
        ax.text(-0.8, i + 0.5, short_name, ha='right', va='center',
               fontsize=11, fontweight='medium', color='#333333')
    
    # Sustainability stacked bars (to the right of heatmap)
    sust_x_start = n_sdgs + gap_width
    sust_pct = sustainability / totals[:, np.newaxis] * 100
    
    # Header for sustainability section
    ax.text(sust_x_start + sust_width/2, -0.45, 'Sustainability Level',
           ha='center', va='center', fontsize=11, fontweight='bold', color='#333333')
    
    # Draw stacked bars
    bar_height = 0.7
    for i in range(n_mega):
        y_center = i + 0.5
        y_bar = y_center - bar_height/2
        
        # Calculate widths
        total_pct = 100
        w_strong = (sust_pct[i, 0] / total_pct) * sust_width
        w_medium = (sust_pct[i, 1] / total_pct) * sust_width
        w_weak = (sust_pct[i, 2] / total_pct) * sust_width
        
        # Strong bar
        x_pos = sust_x_start
        if w_strong > 0:
            rect = FancyBboxPatch((x_pos, y_bar), w_strong, bar_height,
                                 facecolor=SUSTAINABILITY_COLORS['Strong'],
                                 edgecolor='white', linewidth=0.5,
                                 boxstyle='round,pad=0,rounding_size=0.05')
            ax.add_patch(rect)
            if sust_pct[i, 0] > 8:
                ax.text(x_pos + w_strong/2, y_center, f'{sust_pct[i, 0]:.0f}%',
                       ha='center', va='center', fontsize=8, color='white', fontweight='bold')
        
        # Medium bar
        x_pos += w_strong
        if w_medium > 0:
            rect = FancyBboxPatch((x_pos, y_bar), w_medium, bar_height,
                                 facecolor=SUSTAINABILITY_COLORS['Medium'],
                                 edgecolor='white', linewidth=0.5,
                                 boxstyle='round,pad=0,rounding_size=0.05')
            ax.add_patch(rect)
            if sust_pct[i, 1] > 8:
                ax.text(x_pos + w_medium/2, y_center, f'{sust_pct[i, 1]:.0f}%',
                       ha='center', va='center', fontsize=8, color='#333333', fontweight='bold')
        
        # Weak bar
        x_pos += w_medium
        if w_weak > 0:
            rect = FancyBboxPatch((x_pos, y_bar), w_weak, bar_height,
                                 facecolor=SUSTAINABILITY_COLORS['Weak'],
                                 edgecolor='white', linewidth=0.5,
                                 boxstyle='round,pad=0,rounding_size=0.05')
            ax.add_patch(rect)
            if sust_pct[i, 2] > 8:
                ax.text(x_pos + w_weak/2, y_center, f'{sust_pct[i, 2]:.0f}%',
                       ha='center', va='center', fontsize=8, color='white', fontweight='bold')
        
        # Total count on the right
        ax.text(sust_x_start + sust_width + 0.2, y_center, f'n={totals[i]:,}',
               ha='left', va='center', fontsize=9, color='#666666', style='italic')
    
    # SDG Legend at bottom
    legend_y = n_mega + 0.8
    cols = 8
    for idx, (sdg_num, sdg_name) in enumerate(SDG_NAMES.items()):
        col = idx % cols
        row = idx // cols
        
        x = col * 2.3 + 0.2
        y = legend_y + 1.0 - row * 0.6
        
        # SDG color box
        rect = Rectangle((x, y), 0.4, 0.4,
                        facecolor=SDG_COLORS[sdg_num], edgecolor='none')
        ax.add_patch(rect)
        
        # SDG number and name
        ax.text(x + 0.2, y + 0.2, str(sdg_num), ha='center', va='center',
               fontsize=8, color='white', fontweight='bold')
        ax.text(x + 0.55, y + 0.2, sdg_name, ha='left', va='center',
               fontsize=8, color='#333333')
    
    # Sustainability legend
    sust_legend_x = n_sdgs + gap_width
    sust_legend_y = legend_y + 0.7
    
    for idx, (level, color) in enumerate(SUSTAINABILITY_COLORS.items()):
        x = sust_legend_x + idx * 0.9
        rect = Rectangle((x, sust_legend_y), 0.3, 0.3,
                        facecolor=color, edgecolor='none')
        ax.add_patch(rect)
        ax.text(x + 0.4, sust_legend_y + 0.15, level, ha='left', va='center',
               fontsize=9, color='#333333')
    
    # Colorbar for heatmap
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=LogNorm(vmin=1, vmax=vmax))
    sm.set_array([])
    cbar_ax = fig.add_axes([0.12, 0.02, 0.25, 0.02])
    cbar = fig.colorbar(sm, cax=cbar_ax, orientation='horizontal')
    cbar.set_label('Articles (log scale)', fontsize=9)
    cbar.ax.tick_params(labelsize=8)
    
    # Set limits and clean up
    ax.set_xlim(-5.5, sust_x_start + sust_width + 1.5)
    ax.set_ylim(-1.2, legend_y + 1.8)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.invert_yaxis()
    
    # Title
    ax.text(n_sdgs/2, -1.6, 'Megatrend Alignment with Sustainable Development Goals',
           ha='center', va='center', fontsize=15, fontweight='bold')
    
    plt.tight_layout()
    
    # Save
    fig.savefig('sdg_heatmap_combined.pdf', format='pdf', dpi=300,
               bbox_inches='tight', facecolor='white', edgecolor='none')
    fig.savefig('sdg_heatmap_combined.png', format='png', dpi=300,
               bbox_inches='tight', facecolor='white', edgecolor='none')
    
    print("Saved: sdg_heatmap_combined.pdf, sdg_heatmap_combined.png")
    plt.close()


if __name__ == "__main__":
    print("Creating combined SDG heatmap visualization...")
    create_combined_visualization()
    print("Done!")
