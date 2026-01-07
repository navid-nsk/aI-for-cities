"""
Polished Hierarchical Taxonomy Dendrogram
- Compact, efficient layout
- Proper line weights and clean orthogonal (right-angle) connections throughout
- Full readable text
- Professional academic visualization style
- ALL data from Table 1 included
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Use Liberation Sans (Arial-compatible, available on Linux)
plt.rcParams['font.family'] = 'Liberation Sans'
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
plt.rcParams['axes.linewidth'] = 0.5

# Refined color palette for megatrends
MEGATREND_COLORS = {
    'Digital Transformation & Smart Cities': '#1565C0',       # Blue
    'Climate Change & Environmental Sustainability': '#2E7D32', # Green
    'Urban Mobility & Transportation': '#EF6C00',              # Orange
    'Urban Development & Land Use': '#7B1FA2',                 # Purple
    'Social Equity & Quality of Life': '#00838F',              # Teal
    'Urban Resilience & Safety': '#C62828',                    # Red
}

# Complete data from hierarchy_table.md Table 1
HIERARCHY_DATA = {
    'Digital Transformation & Smart Cities': {
        'count': 2052,
        'trends': {
            'Smart Urban Infrastructure': [
                ('Urban Infrastructure & Technology', 272),
                ('Smart Infrastructure', 192),
                ('Smart City Infrastructure', 63),
                ('Urban Infrastructure', 36),
            ],
            'Urban Intelligence & Data Analytics': [
                ('Urban Intelligence & Analytics', 95),
                ('Urban Analytics', 34),
                ('Remote Sensing & Image Analysis', 14),
            ],
            'Smart Mobility Systems': [
                ('Mobility & Transportation', 110),
                ('Urban Mobility', 77),
                ('Transportation and Mobility', 70),
                ('Traffic Management', 52),
            ],
            'Urban Planning & Governance': [
                ('Urban Planning & Land Use', 73),
                ('Urban Planning', 62),
                ('Safety and Governance', 52),
                ('Urban Governance & Society', 45),
            ],
            'Smart Services & Security': [
                ('Security & Safety', 45),
                ('Urban Living & Quality of Life', 37),
                ('Smart Grid', 36),
                ('Urban Services', 30),
            ],
        }
    },
    'Climate Change & Environmental Sustainability': {
        'count': 1646,
        'trends': {
            'Urban Environment & Ecology': [
                ('Urban Environment & Sustainability', 442),
                ('Environment & Sustainability', 65),
                ('Environmental Quality', 33),
            ],
            'Air Quality & Emissions': [
                ('Air Quality', 81),
                ('Carbon Emissions', 28),
                ('Air Quality & Emissions', 18),
            ],
            'Urban Climate & Heat': [
                ('Urban Climate and Environment', 48),
                ('Climate and Microclimate', 44),
                ('Heat Island', 31),
                ('Urban Heat & Climate', 29),
            ],
            'Green & Blue Infrastructure': [
                ('Infrastructure and Utilities', 44),
                ('Green Infrastructure', 18),
                ('Green Spaces', 16),
                ('Water Quality', 11),
            ],
            'Energy Management': [
                ('Energy Management', 29),
                ('Smart Grid & Energy', 22),
                ('Building Energy', 14),
                ('Smart Grid', 12),
            ],
            'Urban Planning for Sustainability': [
                ('Urban Planning & Land Use', 70),
                ('Urban Infrastructure & Technology', 56),
                ('Mobility & Transportation', 42),
            ],
        }
    },
    'Urban Mobility & Transportation': {
        'count': 539,
        'trends': {
            'Public & Shared Transportation': [
                ('Transportation & Mobility', 129),
                ('Public Transit', 10),
                ('Public Transit & Shared Mobility', 6),
                ('Bike Sharing', 5),
            ],
            'Intelligent Transportation Systems': [
                ('Intelligent Transportation Systems', 63),
                ('Traffic Management', 15),
                ('Traffic & Congestion', 14),
                ('Traffic Safety', 13),
            ],
            'Urban Mobility Patterns': [
                ('Urban Mobility', 70),
                ('Mobility & Transportation', 53),
                ('Walkability', 8),
                ('Mobility & Accessibility', 7),
            ],
            'Autonomous & Connected Vehicles': [
                ('Traffic Prediction', 9),
                ('Parking', 7),
                ('Autonomous Vehicles', 5),
                ('EV Infrastructure', 4),
            ],
        }
    },
    'Urban Development & Land Use': {
        'count': 506,
        'trends': {
            'Land Use Planning': [
                ('Urban Planning & Land Use', 133),
                ('Urban Planning', 56),
                ('Land Use and Housing', 28),
                ('Urban Expansion', 24),
            ],
            'Urban Growth Dynamics': [
                ('Urban Growth & Sprawl', 38),
                ('Urban Growth', 17),
                ('Land Cover', 14),
                ('Urban Sprawl', 5),
            ],
            'Environmental Planning': [
                ('Climate & Environmental Analysis', 39),
                ('Remote Sensing & Image Analysis', 17),
                ('Environmental Management & Planning', 10),
            ],
            'Urban Form & Design': [
                ('Urban Form', 8),
                ('Streetscape & Aesthetics', 7),
                ('Urban Design', 6),
                ('Urban Morphology', 4),
            ],
        }
    },
    'Social Equity & Quality of Life': {
        'count': 470,
        'trends': {
            'Health & Well-being': [
                ('Health & Quality of Life', 34),
                ('Health & Well-being', 13),
                ('Public Health', 8),
                ('Urban Health', 7),
            ],
            'Urban Governance & Policy': [
                ('Environmental Management & Planning', 44),
                ('Urban Governance & Society', 43),
                ('Governance & Society', 17),
            ],
            'Quality of Life & Livability': [
                ('Urban Living & Quality of Life', 22),
                ('Urban Environment & Sustainability', 19),
                ('Green Spaces', 12),
                ('Walkability', 9),
            ],
            'Social Dynamics': [
                ('Social and Community', 7),
                ('Streetscape Analysis', 7),
                ('Urban Vitality', 6),
                ('Mental Health', 6),
            ],
        }
    },
    'Urban Resilience & Safety': {
        'count': 228,
        'trends': {
            'Disaster Management': [
                ('Disaster Management', 35),
                ('Flood Risk', 7),
                ('Flood Management', 6),
                ('Landslide Risk', 2),
            ],
            'Urban Safety & Security': [
                ('Urban Safety & Resilience', 54),
                ('Security & Safety', 42),
                ('Urban Safety & Security', 15),
                ('Cybersecurity', 9),
            ],
            'Emergency Response': [
                ('Crime Prevention', 6),
                ('Fire Detection', 6),
                ('Surveillance', 4),
                ('Emergency Management', 2),
            ],
        }
    },
}


def create_dendrogram():
    """Create a clean, professional hierarchical dendrogram"""
    
    # Count items
    total_clusters = sum(
        sum(len(clusters) for clusters in mt['trends'].values())
        for mt in HIERARCHY_DATA.values()
    )
    total_trends = sum(len(mt['trends']) for mt in HIERARCHY_DATA.values())
    total_articles = sum(mt['count'] for mt in HIERARCHY_DATA.values())
    
    print(f"Total clusters: {total_clusters}")
    print(f"Total trends: {total_trends}")
    print(f"Total megatrends: {len(HIERARCHY_DATA)}")
    print(f"Total articles: {total_articles}")
    
    # Figure dimensions - tall format for many items
    fig_width = 22
    fig_height = 28
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    
    # Spacing parameters
    row_height = 0.0095  # Height per cluster row
    gap_between_trends = 0.003
    gap_between_megatrends = 0.012
    
    # X positions
    x_cluster_label = 0.26   # Right edge of cluster labels
    x_cluster_dot = 0.27     # Cluster dots
    x_cluster_vert = 0.30    # Vertical connector for clusters
    x_trend_dot = 0.44       # Trend dots
    x_trend_label = 0.45     # Left edge of trend labels
    x_trend_vert = 0.60      # Vertical connector for trends
    x_mega_dot = 0.72        # Megatrend dots
    x_mega_label = 0.73      # Left edge of megatrend labels
    x_mega_vert = 0.88       # Vertical connector for megatrends
    x_root = 0.93            # Root position
    
    # Line widths
    lw_cluster = 1.0
    lw_trend = 1.8
    lw_megatrend = 2.8
    lw_root = 3.5
    
    # Font sizes
    fs_cluster = 8.5
    fs_trend = 9.5
    fs_megatrend = 11
    fs_root = 13
    fs_header = 12
    
    # Calculate y positions
    y_current = 0.97  # Start from top
    
    megatrend_positions = {}  # Store megatrend y positions for final connection
    
    for mt_idx, (mt_name, mt_data) in enumerate(HIERARCHY_DATA.items()):
        color = MEGATREND_COLORS[mt_name]
        trends = mt_data['trends']
        
        trend_ys = []  # Store trend y positions for megatrend connection
        
        for trend_idx, (trend_name, clusters) in enumerate(trends.items()):
            cluster_ys = []  # Store cluster y positions for trend connection
            
            # Draw clusters
            for cluster_idx, (cluster_name, cluster_count) in enumerate(clusters):
                y = y_current
                cluster_ys.append(y)
                
                # Cluster label (right-aligned)
                label = f"{cluster_name} ({cluster_count})"
                ax.text(x_cluster_label, y, label, va='center', ha='right',
                       fontsize=fs_cluster, color='#333333')
                
                # Cluster dot
                ax.plot(x_cluster_dot, y, 'o', color=color, markersize=5,
                       zorder=10, markeredgecolor='white', markeredgewidth=0.3)
                
                # Horizontal line from dot to vertical connector
                ax.plot([x_cluster_dot, x_cluster_vert], [y, y], '-',
                       color=color, linewidth=lw_cluster, alpha=0.5, zorder=1)
                
                y_current -= row_height
            
            # Trend vertical connector (connects all clusters in this trend)
            if len(cluster_ys) > 1:
                ax.plot([x_cluster_vert, x_cluster_vert], 
                       [min(cluster_ys), max(cluster_ys)], '-',
                       color=color, linewidth=lw_cluster, alpha=0.5, zorder=1)
            
            # Calculate trend y position (center of its clusters)
            trend_y = np.mean(cluster_ys)
            trend_ys.append(trend_y)
            
            # Horizontal line from cluster vertical to trend
            ax.plot([x_cluster_vert, x_trend_dot], [trend_y, trend_y], '-',
                   color=color, linewidth=lw_trend, alpha=0.6, zorder=2)
            
            # Trend dot (square marker)
            ax.plot(x_trend_dot, trend_y, 's', color=color, markersize=8,
                   zorder=10, markeredgecolor='white', markeredgewidth=0.5)
            
            # Trend label
            ax.text(x_trend_label, trend_y, trend_name, va='center', ha='left',
                   fontsize=fs_trend, color='#333333', fontweight='medium')
            
            # Horizontal line from trend to trend vertical connector
            ax.plot([x_trend_dot, x_trend_vert], [trend_y, trend_y], '-',
                   color=color, linewidth=lw_trend, alpha=0.6, zorder=2)
            
            # Add gap between trends
            if trend_idx < len(trends) - 1:
                y_current -= gap_between_trends
        
        # Trend vertical connector (connects all trends in this megatrend)
        if len(trend_ys) > 1:
            ax.plot([x_trend_vert, x_trend_vert],
                   [min(trend_ys), max(trend_ys)], '-',
                   color=color, linewidth=lw_trend, alpha=0.6, zorder=2)
        
        # Calculate megatrend y position
        mega_y = np.mean(trend_ys)
        megatrend_positions[mt_name] = mega_y
        
        # Horizontal line from trend vertical to megatrend
        ax.plot([x_trend_vert, x_mega_dot], [mega_y, mega_y], '-',
               color=color, linewidth=lw_megatrend, alpha=0.7, zorder=3)
        
        # Megatrend dot (larger circle)
        ax.plot(x_mega_dot, mega_y, 'o', color=color, markersize=14,
               zorder=10, markeredgecolor='white', markeredgewidth=1)
        
        # Megatrend label
        short_names = {
            'Digital Transformation & Smart Cities': 'Digital & Smart Cities',
            'Climate Change & Environmental Sustainability': 'Climate & Environment',
            'Urban Mobility & Transportation': 'Mobility & Transportation',
            'Urban Development & Land Use': 'Urban Development',
            'Social Equity & Quality of Life': 'Social Equity & QoL',
            'Urban Resilience & Safety': 'Resilience & Safety',
        }
        short_name = short_names.get(mt_name, mt_name)
        ax.text(x_mega_label, mega_y, f"{short_name}\n(n={mt_data['count']:,})",
               va='center', ha='left', fontsize=fs_megatrend,
               color=color, fontweight='bold', linespacing=0.9)
        
        # Horizontal line from megatrend to megatrend vertical connector
        ax.plot([x_mega_dot, x_mega_vert], [mega_y, mega_y], '-',
               color=color, linewidth=lw_megatrend, alpha=0.7, zorder=3)
        
        # Add gap between megatrends
        if mt_idx < len(HIERARCHY_DATA) - 1:
            y_current -= gap_between_megatrends
    
    # Megatrend vertical connector (connects all megatrends to root)
    mega_ys = list(megatrend_positions.values())
    ax.plot([x_mega_vert, x_mega_vert], [min(mega_ys), max(mega_ys)], '-',
           color='#37474F', linewidth=lw_megatrend, alpha=0.8, zorder=3)
    
    # Root connection
    root_y = np.mean(mega_ys)
    ax.plot([x_mega_vert, x_root], [root_y, root_y], '-',
           color='#37474F', linewidth=lw_root, alpha=0.9, zorder=4)
    
    # Root node
    ax.plot(x_root, root_y, 'o', color='#263238', markersize=22,
           zorder=10, markeredgecolor='white', markeredgewidth=1.5)
    
    # Root label
    ax.text(x_root, root_y - 0.04, f'AI in Urban Studies\n(N={total_articles:,})',
           va='top', ha='center', fontsize=fs_root, color='#263238',
           fontweight='bold', linespacing=0.9)
    
    # Column headers
    header_y = 0.99
    ax.text(x_cluster_label - 0.08, header_y, 'Subject Clusters',
           ha='center', va='bottom', fontsize=fs_header,
           fontweight='bold', color='#455A64')
    ax.text(x_trend_dot + 0.07, header_y, 'Research Trends',
           ha='center', va='bottom', fontsize=fs_header,
           fontweight='bold', color='#455A64')
    ax.text(x_mega_dot + 0.07, header_y, 'Megatrends',
           ha='center', va='bottom', fontsize=fs_header,
           fontweight='bold', color='#455A64')
    ax.text(x_root, header_y, 'Root',
           ha='center', va='bottom', fontsize=fs_header,
           fontweight='bold', color='#455A64')
    
    # Legend at bottom - horizontal layout
    legend_y = y_current - 0.03
    legend_x_start = 0.08
    legend_spacing = 0.15
    
    for i, mt_name in enumerate(HIERARCHY_DATA.keys()):
        color = MEGATREND_COLORS[mt_name]
        short_names = {
            'Digital Transformation & Smart Cities': 'Digital & Smart Cities',
            'Climate Change & Environmental Sustainability': 'Climate & Environment',
            'Urban Mobility & Transportation': 'Mobility & Transport.',
            'Urban Development & Land Use': 'Urban Development',
            'Social Equity & Quality of Life': 'Social Equity & QoL',
            'Urban Resilience & Safety': 'Resilience & Safety',
        }
        short_name = short_names.get(mt_name, mt_name)
        count = HIERARCHY_DATA[mt_name]['count']
        pct = count / total_articles * 100
        
        x_pos = legend_x_start + (i % 3) * 0.30
        y_pos = legend_y - (i // 3) * 0.015
        
        # Color patch
        ax.add_patch(plt.Rectangle((x_pos, y_pos - 0.003), 0.015, 0.008,
                                   facecolor=color, edgecolor='none'))
        # Label
        ax.text(x_pos + 0.02, y_pos + 0.001, f'{short_name} ({pct:.1f}%)',
               va='center', ha='left', fontsize=9, color='#333333')
    
    # Set limits
    ax.set_xlim(0, 1)
    ax.set_ylim(legend_y - 0.04, 1.02)
    ax.axis('off')
    
    # Title
    ax.text(0.5, 1.015, 'Hierarchical Taxonomy of AI in Urban Studies Research',
           ha='center', va='bottom', fontsize=16, fontweight='bold',
           transform=ax.transAxes)
    ax.text(0.5, 0.995, 'Subject Clusters → Research Trends → Megatrends → Root',
           ha='center', va='bottom', fontsize=12, color='#666666',
           transform=ax.transAxes)
    
    plt.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)
    
    # Save
    fig.savefig('dendrogram_final.pdf', format='pdf', dpi=300, bbox_inches='tight',
               edgecolor='none', facecolor='white')
    fig.savefig('dendrogram_final.png', format='png', dpi=300, bbox_inches='tight',
               edgecolor='none', facecolor='white')
    
    print("\nSaved: dendrogram_final.pdf, dendrogram_final.png")
    plt.close()


if __name__ == "__main__":
    print("Creating hierarchical dendrogram...")
    print("=" * 50)
    create_dendrogram()
    print("=" * 50)
    print("Done!")
