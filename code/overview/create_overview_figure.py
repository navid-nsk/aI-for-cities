"""
Overview Figure for AI and Urban Studies Research (2020-2025)
Creates a multi-panel figure with:
- Panel A: Articles per year with SDG color breakdown
- Panel B: World map with top 10 countries and SDG donut charts
- SDG Legend below panels A and B
- Panel C: Article types with sustainability levels
- Panel D: Sankey diagram (article_type × methodological_approach × spatial_scale)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Wedge, FancyBboxPatch, Circle
from matplotlib.collections import PatchCollection
import warnings
warnings.filterwarnings('ignore')

# For world map
import geopandas as gpd

# Use fonts compatible with Adobe Illustrator
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['pdf.fonttype'] = 42  # TrueType fonts for Illustrator compatibility
plt.rcParams['ps.fonttype'] = 42
plt.rcParams['font.size'] = 9
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['xtick.labelsize'] = 8
plt.rcParams['ytick.labelsize'] = 8

# Official SDG colors (from UN SDG branding guidelines)
SDG_COLORS = {
    'SDG 1 (No Poverty)': '#E5243B',
    'SDG 2 (Zero Hunger)': '#DDA63A',
    'SDG 3 (Health)': '#4C9F38',
    'SDG 4 (Education)': '#C5192D',
    'SDG 5 (Gender Equality)': '#FF3A21',
    'SDG 6 (Water)': '#26BDE2',
    'SDG 7 (Energy)': '#FCC30B',
    'SDG 8 (Economic Growth)': '#A21942',
    'SDG 9 (Infrastructure)': '#FD6925',
    'SDG 10 (Reduced Inequalities)': '#DD1367',
    'SDG 11 (Sustainable Cities)': '#FD9D24',
    'SDG 12 (Responsible Consumption)': '#BF8B2E',
    'SDG 13 (Climate)': '#3F7E44',
    'SDG 14 (Life Below Water)': '#0A97D9',
    'SDG 15 (Life on Land)': '#56C02B',
    'SDG 16 (Peace & Justice)': '#00689D',
    'SDG 17 (Partnerships)': '#19486A',
}

# Short SDG labels for legend (official UN SDG names)
SDG_SHORT_LABELS = {
    'SDG 1 (No Poverty)': '1 - No Poverty',
    'SDG 2 (Zero Hunger)': '2 - Zero Hunger',
    'SDG 3 (Health)': '3 - Good Health and Well-being',
    'SDG 4 (Education)': '4 - Quality Education',
    'SDG 5 (Gender Equality)': '5 - Gender Equality',
    'SDG 6 (Water)': '6 - Clean Water and Sanitation',
    'SDG 7 (Energy)': '7 - Affordable and Clean Energy',
    'SDG 8 (Economic Growth)': '8 - Decent Work and Economic Growth',
    'SDG 9 (Infrastructure)': '9 - Industry, Innovation and Infrastructure',
    'SDG 10 (Reduced Inequalities)': '10 - Reduced Inequalities',
    'SDG 11 (Sustainable Cities)': '11 - Sustainable Cities and Communities',
    'SDG 12 (Responsible Consumption)': '12 - Responsible Consumption and Production',
    'SDG 13 (Climate)': '13 - Climate Action',
    'SDG 14 (Life Below Water)': '14 - Life Below Water',
    'SDG 15 (Life on Land)': '15 - Life on Land',
    'SDG 16 (Peace & Justice)': '16 - Peace, Justice and Strong Institutions',
    'SDG 17 (Partnerships)': '17 - Partnerships for the Goals',
}

# SDG order for legend (numerical order 1-17)
SDG_ORDER = [
    'SDG 1 (No Poverty)',
    'SDG 2 (Zero Hunger)',
    'SDG 3 (Health)',
    'SDG 4 (Education)',
    'SDG 5 (Gender Equality)',
    'SDG 6 (Water)',
    'SDG 7 (Energy)',
    'SDG 8 (Economic Growth)',
    'SDG 9 (Infrastructure)',
    'SDG 10 (Reduced Inequalities)',
    'SDG 11 (Sustainable Cities)',
    'SDG 12 (Responsible Consumption)',
    'SDG 13 (Climate)',
    'SDG 14 (Life Below Water)',
    'SDG 15 (Life on Land)',
    'SDG 16 (Peace & Justice)',
    'SDG 17 (Partnerships)',
]

# Sustainability level colors
SUSTAINABILITY_COLORS = {
    'Strong': '#2E7D32',
    'Medium': '#FFA726',
    'Weak': '#EF5350'
}

def load_data():
    """Load the clean research data"""
    df = pd.read_csv('../clean_research.csv', encoding='utf-8-sig')
    # Merge USA and United States
    df['country_clean'] = df['country_first_author'].replace({'United States': 'USA'})
    return df

def create_panel_a(ax, df):
    """Panel A: Articles per year with SDG color breakdown"""
    # Get year-SDG crosstab
    year_sdg = pd.crosstab(df['Year'], df['sdg_alignment'])

    # Sort SDGs by total count for consistent ordering
    sdg_order = df['sdg_alignment'].value_counts().index.tolist()
    year_sdg = year_sdg[sdg_order]

    years = year_sdg.index.tolist()

    # Create stacked bar chart
    bottom = np.zeros(len(years))

    for sdg in sdg_order:
        values = year_sdg[sdg].values
        color = SDG_COLORS.get(sdg, '#888888')
        ax.bar(years, values, bottom=bottom, color=color, edgecolor='black', linewidth=0.3, width=0.7)
        bottom += values

    # Add total count labels on top of each bar
    for i, year in enumerate(years):
        total = year_sdg.loc[year].sum()
        ax.annotate(f'{total:,}', xy=(year, total + 30), ha='center', va='bottom',
                   fontsize=9, fontweight='bold')

    ax.set_xlabel('Year', fontsize=10)
    ax.set_ylabel('Number of Articles', fontsize=10)
    ax.set_title('A', loc='left', fontweight='bold', fontsize=14, x=-0.05)
    ax.set_xticks(years)
    ax.set_xticklabels(years, fontsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim(0, max(bottom) * 1.1)

    return sdg_order

def draw_donut_on_map(ax, x, y, size, sdg_counts, total):
    """Draw a donut chart at specified position on map"""
    # Calculate angles for each SDG
    angles = []
    colors = []
    start_angle = 90

    # Sort by count to draw larger segments first
    sorted_sdgs = sorted(sdg_counts.items(), key=lambda x: x[1], reverse=True)

    for sdg, count in sorted_sdgs:
        if count > 0:
            angle = (count / total) * 360
            angles.append((start_angle, angle, SDG_COLORS.get(sdg, '#888888')))
            start_angle -= angle

    # Draw wedges (outer ring)
    outer_radius = size
    inner_radius = size * 0.55

    for start, angle, color in angles:
        wedge = Wedge((x, y), outer_radius, start - angle, start,
                      width=outer_radius - inner_radius,
                      facecolor=color, edgecolor='white', linewidth=0.3)
        ax.add_patch(wedge)

    # Add white center circle
    center_circle = Circle((x, y), inner_radius * 0.95, facecolor='white', edgecolor='none')
    ax.add_patch(center_circle)

    # Add count text in center
    ax.text(x, y, f'{total:,}', ha='center', va='center', fontsize=5, fontweight='bold')

def create_panel_b(ax, df):
    """Panel B: World map with top 10 countries and SDG donut charts"""
    # Load world map - download if needed
    try:
        world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
    except:
        # Fallback: try to download
        world = gpd.read_file("https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip")

    # Country name mapping for matching
    country_mapping = {
        'USA': 'United States of America',
        'UK': 'United Kingdom',
        'South Korea': 'South Korea',
        'Iran': 'Iran',
        'Turkey': 'Turkey',
        'Russia': 'Russia',
        'Vietnam': 'Vietnam',
        'Czech Republic': 'Czechia',
        'UAE': 'United Arab Emirates',
    }

    # Get article counts per country
    country_counts = df['country_clean'].value_counts()

    # Map counts to world dataframe
    def get_count(country_name):
        # Direct match first
        if country_name in country_counts.index:
            return country_counts[country_name]
        # Try mapping
        for clean_name, geo_name in country_mapping.items():
            if country_name == geo_name:
                return country_counts.get(clean_name, 0)
        # Partial match
        for country in country_counts.index:
            if country.lower() in country_name.lower() or country_name.lower() in country.lower():
                return country_counts[country]
        return 0

    world['article_count'] = world['name'].apply(get_count)

    # Create log-scale normalization for better color distribution
    max_count = world['article_count'].max()

    # Plot base map (countries without articles)
    world[world['article_count'] == 0].plot(ax=ax, color='#f5f5f5', edgecolor='#cccccc', linewidth=0.2)

    # Plot countries with articles using log color scale
    countries_with_articles = world[world['article_count'] > 0].copy()
    countries_with_articles['log_count'] = np.log1p(countries_with_articles['article_count'])
    countries_with_articles.plot(ax=ax, column='log_count', cmap='YlOrRd',
                                  edgecolor='#999999', linewidth=0.2,
                                  legend=False)

    # Add colorbar
    sm = plt.cm.ScalarMappable(cmap='YlOrRd', norm=plt.Normalize(vmin=0, vmax=np.log1p(max_count)))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=ax, shrink=0.4, aspect=15, pad=0.01, orientation='vertical')
    # Set colorbar ticks to show actual counts
    tick_values = [0, 10, 50, 100, 500, 1000, 2000, 3000]
    tick_positions = [np.log1p(v) for v in tick_values if v <= max_count]
    tick_labels = [str(v) for v in tick_values if v <= max_count]
    cbar.set_ticks(tick_positions)
    cbar.set_ticklabels(tick_labels)
    cbar.set_label('Articles', fontsize=8)
    cbar.ax.tick_params(labelsize=6)

    # Top 10 countries for donut charts
    top_10 = country_counts.head(10)

    # Positions for labels and donuts (longitude, latitude)
    # Positioned outside countries to avoid overlap
    label_positions = {
        'China': {'label': (155, 42), 'centroid': (105, 35), 'label_offset': (0, -9)},
        'India': {'label': (100, 0), 'centroid': (78, 22), 'label_offset': (0, -9)},
        'USA': {'label': (-135, 55), 'centroid': (-100, 40), 'label_offset': (0, -9)},
        'Saudi Arabia': {'label': (30, 45), 'centroid': (45, 24), 'label_offset': (0, -9)},
        'South Korea': {'label': (155, 20), 'centroid': (128, 36), 'label_offset': (0, -9)},
        'Italy': {'label': (-15, 58), 'centroid': (12, 43), 'label_offset': (0, -9)},
        'Pakistan': {'label': (50, 48), 'centroid': (70, 30), 'label_offset': (0, -9)},
        'Spain': {'label': (-35, 45), 'centroid': (-4, 40), 'label_offset': (0, -9)},
        'Germany': {'label': (5, 68), 'centroid': (10, 51), 'label_offset': (0, -9)},
        'Australia': {'label': (165, -40), 'centroid': (134, -25), 'label_offset': (0, -9)},
    }

    # Draw donut charts for top 10 countries
    for country, count in top_10.items():
        if country in label_positions:
            pos = label_positions[country]
            label_pos = pos['label']
            centroid = pos['centroid']

            # Get SDG breakdown for this country
            country_sdgs = df[df['country_clean'] == country]['sdg_alignment'].value_counts().to_dict()

            # Draw line from country to label position
            ax.plot([centroid[0], label_pos[0]], [centroid[1], label_pos[1]],
                   color='#555555', linewidth=0.6, linestyle='-', zorder=1)

            # Draw donut at label position
            draw_donut_on_map(ax, label_pos[0], label_pos[1], 7, country_sdgs, count)

            # Add country label below donut
            ax.text(label_pos[0] + pos['label_offset'][0],
                   label_pos[1] + pos['label_offset'][1],
                   country, ha='center', va='top', fontsize=6, fontweight='bold')

    ax.set_xlim(-180, 180)
    ax.set_ylim(-60, 85)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('B', loc='left', fontweight='bold', fontsize=14, x=-0.02)

def create_sdg_legend(ax, sdgs_in_data):
    """Create SDG color legend in numerical order"""
    ax.axis('off')

    # Use numerical SDG order, but only include SDGs that appear in data
    sdgs_to_show = [sdg for sdg in SDG_ORDER if sdg in sdgs_in_data]

    # Create legend patches
    patches = []
    labels = []

    for sdg in sdgs_to_show:
        color = SDG_COLORS.get(sdg, '#888888')
        patches.append(mpatches.Patch(facecolor=color, edgecolor='black', linewidth=0.5))
        labels.append(SDG_SHORT_LABELS.get(sdg, sdg))

    # Create legend with multiple columns
    ncols = min(8, len(patches))
    legend = ax.legend(patches, labels, loc='center', ncol=ncols, frameon=False,
                      fontsize=7, handlelength=1.2, handleheight=1.0,
                      columnspacing=1.0, handletextpad=0.4)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

def create_panel_c(ax, df):
    """Panel C: Article types with sustainability levels"""
    # Get article type counts with sustainability breakdown
    article_sust = pd.crosstab(df['article_type'], df['level_of_sustainability'])

    # Sort by total count
    article_sust['total'] = article_sust.sum(axis=1)
    article_sust = article_sust.sort_values('total', ascending=True)
    totals = article_sust['total'].copy()
    article_sust = article_sust.drop('total', axis=1)

    # Take top 8 article types for cleaner visualization
    article_sust = article_sust.tail(8)
    totals = totals[article_sust.index]

    # Create horizontal stacked bar chart
    article_types = article_sust.index.tolist()
    y_pos = np.arange(len(article_types))

    left = np.zeros(len(article_types))

    for sust_level in ['Strong', 'Medium', 'Weak']:
        if sust_level in article_sust.columns:
            values = article_sust[sust_level].values
            color = SUSTAINABILITY_COLORS[sust_level]
            ax.barh(y_pos, values, left=left, color=color, edgecolor='black',
                   linewidth=0.3, label=sust_level, height=0.65)
            left += values

    # Add total count labels
    for i, total in enumerate(totals):
        ax.annotate(f'{total:,}', xy=(total + 30, i), ha='left', va='center', fontsize=8)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(article_types, fontsize=8)
    ax.set_xlabel('Number of Articles', fontsize=10)
    ax.set_title('C', loc='left', fontweight='bold', fontsize=14, x=-0.15)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlim(0, max(left) * 1.15)

    # Add legend
    ax.legend(loc='lower right', frameon=True, fontsize=8,
             title='Sustainability Level', title_fontsize=9,
             framealpha=0.9, edgecolor='#cccccc')

def create_panel_d(ax, df):
    """Panel D: Sankey diagram for article_type × methodological_approach × spatial_scale"""

    # Prepare data - use all 4 article types
    top_article_types = ['Empirical', 'Methodological', 'Review/Survey', 'Conceptual/Theoretical']
    methodological = ['Quantitative', 'Mixed', 'Qualitative']
    top_spatial = df['spatial_scale'].value_counts().head(4).index.tolist()

    # Filter data
    df_filtered = df[
        (df['article_type'].isin(top_article_types)) &
        (df['methodological_approach'].isin(methodological)) &
        (df['spatial_scale'].isin(top_spatial))
    ].dropna(subset=['article_type', 'methodological_approach', 'spatial_scale']).copy()

    # Create flow data
    flow1 = df_filtered.groupby(['article_type', 'methodological_approach']).size().reset_index(name='count')
    flow2 = df_filtered.groupby(['methodological_approach', 'spatial_scale']).size().reset_index(name='count')

    # Colors for article types
    article_colors = {
        'Empirical': '#66c2a5',
        'Methodological': '#fc8d62',
        'Review/Survey': '#8da0cb',
        'Conceptual/Theoretical': '#e78ac3',
    }
    method_colors = {'Quantitative': '#4292c6', 'Mixed': '#807dba', 'Qualitative': '#df65b0'}
    spatial_colors = {
        top_spatial[0]: '#1b9e77',
        top_spatial[1]: '#d95f02',
        top_spatial[2]: '#7570b3',
        top_spatial[3]: '#e7298a',
    }

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    # Calculate counts and positions
    article_counts = df_filtered['article_type'].value_counts().reindex(top_article_types).fillna(0)
    method_counts = df_filtered['methodological_approach'].value_counts().reindex(methodological).fillna(0)
    spatial_counts = df_filtered['spatial_scale'].value_counts().reindex(top_spatial).fillna(0)

    total = len(df_filtered)

    # X positions for three columns
    x1, x2, x3 = 0.15, 0.5, 0.85
    node_width = 0.06

    # Calculate node heights and positions
    def calculate_positions(counts, total_height=0.75, start_y=0.88):
        positions = {}
        y = start_y
        for name, count in counts.items():
            if count > 0:
                height = max((count / total) * total_height, 0.03)
                positions[name] = {'y_top': y, 'y_bottom': y - height, 'y_center': y - height/2, 'height': height}
                y -= height + 0.015
        return positions

    article_positions = calculate_positions(article_counts)
    method_positions = calculate_positions(method_counts)
    spatial_positions = calculate_positions(spatial_counts)

    # Draw nodes
    def draw_node(x, pos_dict, name, color, label_side='left'):
        if name not in pos_dict:
            return
        pos = pos_dict[name]
        rect = plt.Rectangle((x - node_width/2, pos['y_bottom']), node_width, pos['height'],
                             facecolor=color, edgecolor='black', linewidth=0.5, zorder=3)
        ax.add_patch(rect)

        if label_side == 'left':
            ax.text(x - node_width/2 - 0.01, pos['y_center'], name,
                   ha='right', va='center', fontsize=7, zorder=4)
        elif label_side == 'right':
            ax.text(x + node_width/2 + 0.01, pos['y_center'], name,
                   ha='left', va='center', fontsize=7, zorder=4)
        else:  # center
            ax.text(x, pos['y_center'], name,
                   ha='center', va='center', fontsize=6, fontweight='bold',
                   color='white', zorder=4)

    # Draw all nodes
    for name in top_article_types:
        draw_node(x1, article_positions, name, article_colors.get(name, '#888888'), 'left')
    for name in methodological:
        draw_node(x2, method_positions, name, method_colors.get(name, '#888888'), 'center')
    for name in top_spatial:
        draw_node(x3, spatial_positions, name, spatial_colors.get(name, '#888888'), 'right')

    # Draw flows with bezier curves
    def draw_flow(x_start, x_end, y_start_top, y_start_bottom, y_end_top, y_end_bottom, color, alpha=0.4):
        from matplotlib.patches import PathPatch
        from matplotlib.path import Path

        # Control points for bezier curve
        ctrl_x = (x_start + x_end) / 2

        # Create path for the flow band
        vertices = [
            (x_start, y_start_top),
            (ctrl_x, y_start_top),
            (ctrl_x, y_end_top),
            (x_end, y_end_top),
            (x_end, y_end_bottom),
            (ctrl_x, y_end_bottom),
            (ctrl_x, y_start_bottom),
            (x_start, y_start_bottom),
            (x_start, y_start_top),
        ]

        codes = [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4,
                Path.LINETO, Path.CURVE4, Path.CURVE4, Path.CURVE4, Path.CLOSEPOLY]

        path = Path(vertices, codes)
        patch = PathPatch(path, facecolor=color, edgecolor='none', alpha=alpha, zorder=1)
        ax.add_patch(patch)

    # Track y offsets for stacking flows
    article_offsets = {name: 0 for name in top_article_types}
    method_offsets_left = {name: 0 for name in methodological}
    method_offsets_right = {name: 0 for name in methodological}
    spatial_offsets = {name: 0 for name in top_spatial}

    # Draw flows from article_type to methodological_approach
    for _, row in flow1.iterrows():
        art = row['article_type']
        meth = row['methodological_approach']
        count = row['count']

        if art in article_positions and meth in method_positions:
            flow_height_art = (count / article_counts[art]) * article_positions[art]['height']
            flow_height_meth = (count / method_counts[meth]) * method_positions[meth]['height']

            y_art_top = article_positions[art]['y_top'] - article_offsets[art]
            y_art_bottom = y_art_top - flow_height_art

            y_meth_top = method_positions[meth]['y_top'] - method_offsets_left[meth]
            y_meth_bottom = y_meth_top - flow_height_meth

            draw_flow(x1 + node_width/2, x2 - node_width/2,
                     y_art_top, y_art_bottom, y_meth_top, y_meth_bottom,
                     article_colors.get(art, '#888888'), alpha=0.35)

            article_offsets[art] += flow_height_art
            method_offsets_left[meth] += flow_height_meth

    # Draw flows from methodological_approach to spatial_scale
    for _, row in flow2.iterrows():
        meth = row['methodological_approach']
        spat = row['spatial_scale']
        count = row['count']

        if meth in method_positions and spat in spatial_positions:
            flow_height_meth = (count / method_counts[meth]) * method_positions[meth]['height']
            flow_height_spat = (count / spatial_counts[spat]) * spatial_positions[spat]['height']

            y_meth_top = method_positions[meth]['y_top'] - method_offsets_right[meth]
            y_meth_bottom = y_meth_top - flow_height_meth

            y_spat_top = spatial_positions[spat]['y_top'] - spatial_offsets[spat]
            y_spat_bottom = y_spat_top - flow_height_spat

            draw_flow(x2 + node_width/2, x3 - node_width/2,
                     y_meth_top, y_meth_bottom, y_spat_top, y_spat_bottom,
                     method_colors.get(meth, '#888888'), alpha=0.35)

            method_offsets_right[meth] += flow_height_meth
            spatial_offsets[spat] += flow_height_spat

    # Add column headers
    ax.text(x1, 0.95, 'Article Type', ha='center', va='bottom', fontsize=10, fontweight='bold')
    ax.text(x2, 0.95, 'Methodological\nApproach', ha='center', va='bottom', fontsize=10, fontweight='bold')
    ax.text(x3, 0.95, 'Spatial Scale', ha='center', va='bottom', fontsize=10, fontweight='bold')

    ax.axis('off')
    ax.set_title('D', loc='left', fontweight='bold', fontsize=14, x=-0.02)

def main():
    """Create the complete overview figure"""
    print("Loading data...")
    df = load_data()
    print(f"Loaded {len(df)} articles")

    # Create figure with custom layout
    fig = plt.figure(figsize=(16, 12))

    # Define grid layout
    gs = fig.add_gridspec(3, 2, height_ratios=[1.2, 0.1, 1],
                          width_ratios=[0.8, 1.2],
                          hspace=0.25, wspace=0.15,
                          left=0.06, right=0.98, top=0.95, bottom=0.05)

    # Panel A: Articles per year
    print("Creating Panel A...")
    ax_a = fig.add_subplot(gs[0, 0])
    sdg_order = create_panel_a(ax_a, df)

    # Panel B: World map
    print("Creating Panel B...")
    ax_b = fig.add_subplot(gs[0, 1])
    create_panel_b(ax_b, df)

    # SDG Legend
    print("Creating SDG Legend...")
    ax_legend = fig.add_subplot(gs[1, :])
    create_sdg_legend(ax_legend, sdg_order)

    # Panel C: Article types with sustainability
    print("Creating Panel C...")
    ax_c = fig.add_subplot(gs[2, 0])
    create_panel_c(ax_c, df)

    # Panel D: Sankey diagram
    print("Creating Panel D...")
    ax_d = fig.add_subplot(gs[2, 1])
    create_panel_d(ax_d, df)

    # Save as PDF
    output_path = 'overview_figure.pdf'
    print(f"Saving to {output_path}...")
    fig.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight',
                edgecolor='none', facecolor='white')

    # Also save as PNG for quick preview
    fig.savefig('overview_figure.png', format='png', dpi=300, bbox_inches='tight',
                edgecolor='none', facecolor='white')

    print("Done! Files saved: overview_figure.pdf, overview_figure.png")
    plt.close()

if __name__ == "__main__":
    main()
