"""
Hierarchical Taxonomy Dendrogram for Non-Empirical Articles
- Compact, efficient layout
- Proper line weights and clean orthogonal connections
- Full readable text
- Professional academic visualization style
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Use Liberation Sans (Arial-compatible)
plt.rcParams['font.family'] = 'Arial'
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

# Hierarchy data from non-empirical articles analysis
HIERARCHY_DATA = {
    'Digital Transformation & Smart Cities': {
        'count': 875,
        'trends': {
            'Smart Urban Infrastructure': [
                ('Smart Infrastructure', 64),
                ('Smart City Infrastructure', 55),
                ('Urban Infrastructure & Technology', 42),
                ('Urban Infrastructure', 21),
            ],
            'Urban Intelligence & Analytics': [
                ('Urban Intelligence & Analytics', 49),
                ('Urban Analytics', 29),
                ('Data Collection and Analysis', 38),
            ],
            'Urban Governance & Digital Services': [
                ('Urban Governance & Society', 63),
                ('Smart Governance', 28),
                ('Digital Governance', 27),
            ],
            'Mobility & IoT Systems': [
                ('Mobility & Transportation', 44),
                ('IoT', 21),
                ('Urban Management', 21),
            ],
            'Security & Safety Services': [
                ('Security & Safety', 24),
                ('Urban Safety & Security', 19),
                ('Urban Services & Management', 16),
            ],
        }
    },
    'Urban Mobility & Transportation': {
        'count': 479,
        'trends': {
            'Traffic & Congestion Management': [
                ('Mobility & Transportation', 80),
                ('Traffic & Congestion', 79),
                ('Transportation & Mobility', 66),
            ],
            'Intelligent Transportation Systems': [
                ('Intelligent Transportation Systems', 46),
                ('Autonomous Vehicles', 22),
                ('Connected & Autonomous Vehicles', 8),
            ],
            'Parking & Road Infrastructure': [
                ('Mobility & Accessibility', 14),
                ('Parking', 12),
                ('Road Infrastructure', 12),
            ],
            'Public & Shared Transportation': [
                ('Public Transit', 10),
                ('Autonomous & Electric Vehicles', 9),
                ('Bike Sharing', 6),
                ('Ride-hailing', 7),
            ],
        }
    },
    'Climate Change & Environmental Sustainability': {
        'count': 350,
        'trends': {
            'Urban Environment & Sustainability': [
                ('Urban Environment & Sustainability', 32),
                ('Environment & Sustainability', 21),
                ('Urban Planning & Land Use', 21),
            ],
            'Energy & Smart Grid': [
                ('Smart Grid', 26),
                ('Building Energy', 18),
                ('Energy & Smart Grid', 10),
            ],
            'Air Quality & Pollution': [
                ('Air Quality', 23),
                ('Air Quality & Emissions', 14),
                ('Noise Pollution', 8),
            ],
            'Water & Waste Management': [
                ('Solid Waste', 15),
                ('Water Management', 11),
                ('Disaster Risk & Resilience', 9),
            ],
            'Urban Climate': [
                ('Urban Climate', 10),
                ('Heat Island', 8),
                ('Urban Forestry', 7),
            ],
        }
    },
    'Urban Development & Land Use': {
        'count': 227,
        'trends': {
            'Urban Planning & Land Use': [
                ('Urban Planning & Land Use', 55),
                ('Urban Planning', 35),
                ('Urban Morphology', 18),
            ],
            'Land Cover & Detection': [
                ('Land Cover', 19),
                ('Building Detection', 14),
                ('Climate & Environmental Analysis', 11),
            ],
            'Urban Growth & Form': [
                ('Urban Growth & Sprawl', 9),
                ('Urban Growth', 8),
                ('Streetscape & Aesthetics', 8),
            ],
        }
    },
    'Urban Resilience & Safety': {
        'count': 180,
        'trends': {
            'Cybersecurity & Surveillance': [
                ('Cybersecurity', 88),
                ('Video Surveillance', 19),
                ('Surveillance', 6),
            ],
            'Disaster Management': [
                ('Disaster Management', 14),
                ('Flood Risk', 6),
                ('Emergency Response', 6),
            ],
            'Crime & Fire Prevention': [
                ('Crime Prevention', 8),
                ('Fire Detection', 5),
                ('Urban Safety & Resilience', 6),
            ],
        }
    },
    'Social Equity & Quality of Life': {
        'count': 108,
        'trends': {
            'Health & Healthcare': [
                ('Public Health', 10),
                ('Healthcare', 9),
                ('Urban Vitality', 7),
            ],
            'Governance & Community': [
                ('Governance & Society', 8),
                ('Environmental Management & Planning', 5),
                ('Social and Community', 3),
            ],
            'Urban Services & Accessibility': [
                ('Sound Classification', 5),
                ('Accessibility', 4),
                ('Tourism', 3),
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

    # Figure dimensions
    fig_width = 22
    fig_height = 24
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))

    # Spacing parameters
    row_height = 0.011
    gap_between_trends = 0.004
    gap_between_megatrends = 0.015

    # X positions
    x_cluster_label = 0.26
    x_cluster_dot = 0.27
    x_cluster_vert = 0.30
    x_trend_dot = 0.44
    x_trend_label = 0.45
    x_trend_vert = 0.60
    x_mega_dot = 0.72
    x_mega_label = 0.73
    x_mega_vert = 0.88
    x_root = 0.93

    # Line widths
    lw_cluster = 1.0
    lw_trend = 1.8
    lw_megatrend = 2.8
    lw_root = 3.5

    # Font sizes
    fs_cluster = 9
    fs_trend = 10
    fs_megatrend = 11
    fs_root = 13
    fs_header = 12

    # Calculate y positions
    y_current = 0.96

    megatrend_positions = {}

    for mt_idx, (mt_name, mt_data) in enumerate(HIERARCHY_DATA.items()):
        color = MEGATREND_COLORS[mt_name]
        trends = mt_data['trends']

        trend_ys = []

        for trend_idx, (trend_name, clusters) in enumerate(trends.items()):
            cluster_ys = []

            # Draw clusters
            for cluster_idx, (cluster_name, cluster_count) in enumerate(clusters):
                y = y_current
                cluster_ys.append(y)

                # Cluster label
                label = f"{cluster_name} ({cluster_count})"
                ax.text(x_cluster_label, y, label, va='center', ha='right',
                       fontsize=fs_cluster, color='#333333')

                # Cluster dot
                ax.plot(x_cluster_dot, y, 'o', color=color, markersize=5,
                       zorder=10, markeredgecolor='white', markeredgewidth=0.3)

                # Horizontal line
                ax.plot([x_cluster_dot, x_cluster_vert], [y, y], '-',
                       color=color, linewidth=lw_cluster, alpha=0.5, zorder=1)

                y_current -= row_height

            # Vertical connector for clusters
            if len(cluster_ys) > 1:
                ax.plot([x_cluster_vert, x_cluster_vert],
                       [min(cluster_ys), max(cluster_ys)], '-',
                       color=color, linewidth=lw_cluster, alpha=0.5, zorder=1)

            trend_y = np.mean(cluster_ys)
            trend_ys.append(trend_y)

            # Line to trend
            ax.plot([x_cluster_vert, x_trend_dot], [trend_y, trend_y], '-',
                   color=color, linewidth=lw_trend, alpha=0.6, zorder=2)

            # Trend dot
            ax.plot(x_trend_dot, trend_y, 's', color=color, markersize=8,
                   zorder=10, markeredgecolor='white', markeredgewidth=0.5)

            # Trend label
            ax.text(x_trend_label, trend_y, trend_name, va='center', ha='left',
                   fontsize=fs_trend, color='#333333', fontweight='medium')

            # Line to trend vertical
            ax.plot([x_trend_dot, x_trend_vert], [trend_y, trend_y], '-',
                   color=color, linewidth=lw_trend, alpha=0.6, zorder=2)

            if trend_idx < len(trends) - 1:
                y_current -= gap_between_trends

        # Vertical connector for trends
        if len(trend_ys) > 1:
            ax.plot([x_trend_vert, x_trend_vert],
                   [min(trend_ys), max(trend_ys)], '-',
                   color=color, linewidth=lw_trend, alpha=0.6, zorder=2)

        mega_y = np.mean(trend_ys)
        megatrend_positions[mt_name] = mega_y

        # Line to megatrend
        ax.plot([x_trend_vert, x_mega_dot], [mega_y, mega_y], '-',
               color=color, linewidth=lw_megatrend, alpha=0.7, zorder=3)

        # Megatrend dot
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

        # Line to megatrend vertical
        ax.plot([x_mega_dot, x_mega_vert], [mega_y, mega_y], '-',
               color=color, linewidth=lw_megatrend, alpha=0.7, zorder=3)

        if mt_idx < len(HIERARCHY_DATA) - 1:
            y_current -= gap_between_megatrends

    # Vertical connector for megatrends
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
    ax.text(x_root, root_y - 0.04, f'Non-Empirical AI\nin Urban Studies\n(N={total_articles:,})',
           va='top', ha='center', fontsize=fs_root, color='#263238',
           fontweight='bold', linespacing=0.9)

    # Column headers
    header_y = 0.98
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

    # Legend at bottom
    legend_y = y_current - 0.04
    legend_x_start = 0.08

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
        y_pos = legend_y - (i // 3) * 0.018

        ax.add_patch(plt.Rectangle((x_pos, y_pos - 0.004), 0.015, 0.01,
                                   facecolor=color, edgecolor='none'))
        ax.text(x_pos + 0.02, y_pos + 0.001, f'{short_name} ({pct:.1f}%)',
               va='center', ha='left', fontsize=9, color='#333333')

    # Set limits
    ax.set_xlim(0, 1)
    ax.set_ylim(legend_y - 0.05, 1.01)
    ax.axis('off')

    # Title
    ax.text(0.5, 1.005, 'Hierarchical Taxonomy of Non-Empirical AI in Urban Studies Research',
           ha='center', va='bottom', fontsize=16, fontweight='bold',
           transform=ax.transAxes)
    ax.text(0.5, 0.985, 'Subject Clusters \u2192 Research Trends \u2192 Megatrends \u2192 Root',
           ha='center', va='bottom', fontsize=12, color='#666666',
           transform=ax.transAxes)

    plt.subplots_adjust(left=0.02, right=0.98, top=0.98, bottom=0.02)

    # Save
    fig.savefig('dendrogram_non_empirical.pdf', format='pdf', dpi=300, bbox_inches='tight',
               edgecolor='none', facecolor='white')
    fig.savefig('dendrogram_non_empirical.png', format='png', dpi=300, bbox_inches='tight',
               edgecolor='none', facecolor='white')

    print("\nSaved: dendrogram_non_empirical.pdf, dendrogram_non_empirical.png")
    plt.close()


if __name__ == "__main__":
    print("Creating hierarchical dendrogram for non-empirical articles...")
    print("=" * 50)
    create_dendrogram()
    print("=" * 50)
    print("Done!")
