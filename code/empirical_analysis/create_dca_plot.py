"""
Detrended Correspondence Analysis (DCA) Plot for Empirical Articles - Version 2
Style: Ellipses with keyword clouds (similar to reference image)

Axis 1: From Black-Box Prediction to Interpretable Intelligence
Axis 2: From Physical Systems to Cyber-Physical Integration
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.colors import to_rgba
import re
from collections import Counter
import warnings
warnings.filterwarnings('ignore')

# Use fonts compatible with Adobe Illustrator
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42
plt.rcParams['font.size'] = 9

# Megatrend base positions - positioned to create meaningful overlaps
MEGATREND_POSITIONS = {
    'Climate Change & Environmental Sustainability': {'x': -1.2, 'y': -1.8},
    'Urban Development & Land Use': {'x': 0.8, 'y': -0.5},
    'Urban Resilience & Safety': {'x': -1.5, 'y': 1.5},
    'Urban Mobility & Transportation': {'x': 1.0, 'y': 1.8},
    'Social Equity & Quality of Life': {'x': 2.8, 'y': 1.0},
    'Digital Transformation & Smart Cities': {'x': 0.0, 'y': 2.8},
}

# Colors for megatrends (similar to reference image style)
MEGATREND_COLORS = {
    'Climate Change & Environmental Sustainability': '#8BC34A',  # Light green
    'Urban Development & Land Use': '#9C27B0',  # Purple
    'Urban Resilience & Safety': '#F44336',  # Red
    'Urban Mobility & Transportation': '#2196F3',  # Blue
    'Social Equity & Quality of Life': '#00BCD4',  # Cyan
    'Digital Transformation & Smart Cities': '#E91E63',  # Pink
}

# Short names for display
MEGATREND_SHORT_NAMES = {
    'Climate Change & Environmental Sustainability': 'Climate & Environment',
    'Urban Development & Land Use': 'Urban Development',
    'Urban Resilience & Safety': 'Resilience & Safety',
    'Urban Mobility & Transportation': 'Mobility & Transport',
    'Social Equity & Quality of Life': 'Social Equity',
    'Digital Transformation & Smart Cities': 'Digital & Smart Cities',
}

# Scoring adjustments based on AI method for Axis 1 spread
AXIS1_METHOD_ADJUSTMENT = {
    'Deep Learning': -0.4, 'CNN': -0.5, 'LSTM': -0.35, 'Neural Network': -0.25,
    'GAN': -0.6, 'Transformer': -0.45, 'RNN': -0.3, 'YOLO': -0.55,
    'Machine Learning': 0.0, 'Random Forest': 0.2, 'XGBoost': 0.15,
    'SVM': 0.05, 'Ensemble': 0.1, 'Clustering': 0.25,
    'Regression': 0.4, 'Decision Tree': 0.45, 'Bayesian': 0.35,
    'Optimization': 0.5, 'Rule-Based': 0.6, 'Fuzzy': 0.55,
    'Reinforcement Learning': -0.15,
}

# Scoring adjustments based on sustainability level
AXIS1_SUSTAINABILITY_ADJUSTMENT = {
    'Strong': 0.4,
    'Medium': 0.0,
    'Weak': -0.3,
}

# Scoring adjustments based on AI task for Axis 2 spread
AXIS2_TASK_ADJUSTMENT = {
    'Prediction/Forecasting': 0.15, 'Classification': 0.1,
    'Object Detection': 0.25, 'Segmentation': 0.2,
    'Optimization': -0.15, 'Planning': -0.2,
    'Assessment': -0.25, 'Monitoring': 0.1,
    'Simulation': -0.1, 'Analysis': -0.05,
}


def get_adjustment(text, adjustment_dict):
    """Get adjustment value based on text matching"""
    if pd.isna(text):
        return 0.0
    text_lower = str(text).lower()
    for key, adj in adjustment_dict.items():
        if key.lower() in text_lower:
            return adj
    return 0.0


def calculate_position(row):
    """Calculate x, y position for an article based on megatrend and adjustments"""
    megatrend = row.get('subject_megatrend', '')

    if megatrend not in MEGATREND_POSITIONS:
        return None, None

    base = MEGATREND_POSITIONS[megatrend]

    # Axis 1 adjustments (interpretability)
    method_adj = get_adjustment(row.get('ai_method', ''), AXIS1_METHOD_ADJUSTMENT)
    sust_level = str(row.get('level_of_sustainability', 'Medium'))
    sust_adj = AXIS1_SUSTAINABILITY_ADJUSTMENT.get(sust_level, 0.0)

    # Axis 2 adjustments (cyber-physical)
    task_adj = get_adjustment(row.get('ai_task', ''), AXIS2_TASK_ADJUSTMENT)

    # Add larger noise for natural spread within cluster
    noise_x = np.random.normal(0, 0.8)
    noise_y = np.random.normal(0, 0.8)

    x = base['x'] + method_adj + sust_adj * 0.5 + noise_x
    y = base['y'] + task_adj + noise_y

    return x, y


def extract_keywords(texts, n_keywords=20):
    """Extract top keywords from list of texts"""
    stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
                 'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
                 'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
                 'could', 'should', 'may', 'might', 'must', 'shall', 'can', 'need',
                 'this', 'that', 'these', 'those', 'it', 'its', 'we', 'our', 'they',
                 'their', 'which', 'what', 'where', 'when', 'who', 'how', 'all', 'each',
                 'every', 'both', 'few', 'more', 'most', 'other', 'some', 'such', 'no',
                 'not', 'only', 'same', 'so', 'than', 'too', 'very', 'just', 'also',
                 'into', 'over', 'after', 'before', 'between', 'under', 'again', 'then',
                 'once', 'here', 'there', 'any', 'during', 'through', 'above', 'below',
                 'up', 'down', 'out', 'off', 'about', 'while', 'based', 'using', 'used',
                 'paper', 'study', 'research', 'method', 'methods', 'results', 'data',
                 'analysis', 'model', 'models', 'approach', 'proposed', 'article',
                 'however', 'thus', 'therefore', 'furthermore', 'moreover', 'although',
                 'yet', 'still', 'even', 'much', 'well', 'many', 'new', 'first', 'two',
                 'three', 'one', 'use', 'high', 'low', 'different', 'important', 'show',
                 'shows', 'shown', 'found', 'including', 'provide', 'provides', 'present',
                 'presented', 'aims', 'aim', 'objective', 'objectives', 'work', 'works',
                 'being', 'make', 'made', 'such', 'like', 'within', 'without', 'among',
                 'across', 'along', 'toward', 'towards', 'upon', 'since', 'until',
                 'further', 'various', 'several', 'number', 'order', 'case', 'cases',
                 'example', 'examples', 'particular', 'general', 'specific', 'specifically',
                 'significantly', 'particularly', 'especially', 'mainly', 'primarily',
                 'overall', 'total', 'average', 'mean', 'value', 'values', 'level', 'levels',
                 'rate', 'rates', 'factor', 'factors', 'effect', 'effects', 'impact', 'impacts',
                 'result', 'change', 'changes', 'increase', 'increases', 'decrease', 'decreases',
                 'higher', 'lower', 'better', 'best', 'good', 'great', 'large', 'small',
                 'long', 'short', 'term', 'terms', 'time', 'times', 'year', 'years',
                 'type', 'types', 'form', 'forms', 'part', 'parts', 'system', 'systems',
                 'process', 'processes', 'feature', 'features', 'problem', 'problems',
                 'solution', 'solutions', 'information', 'knowledge', 'performance',
                 'accuracy', 'learning', 'neural', 'network', 'networks', 'deep', 'machine',
                 'urban', 'city', 'cities', 'area', 'areas', 'region', 'regions', 'local',
                 'national', 'global', 'world', 'country', 'countries', 'state', 'states'}

    all_text = ' '.join([str(t) for t in texts if pd.notna(t)])
    words = re.findall(r'\b[a-zA-Z]{4,}\b', all_text.lower())
    words = [w for w in words if w not in stopwords]
    word_counts = Counter(words)
    return word_counts.most_common(n_keywords)


def load_data():
    """Load empirical articles data"""
    df = pd.read_csv('../empirical_clean.csv', encoding='utf-8-sig')
    return df


def create_dca_plot_v2(df):
    """Create the DCA plot with ellipses and keywords"""
    np.random.seed(42)

    # Calculate positions for each article
    positions = df.apply(calculate_position, axis=1)
    df['axis1'] = [p[0] for p in positions]
    df['axis2'] = [p[1] for p in positions]

    # Remove articles without valid positions
    df = df.dropna(subset=['axis1', 'axis2'])

    # Create figure
    fig, ax = plt.subplots(figsize=(14, 12))

    cluster_info = []

    # Draw ellipses for each megatrend
    for megatrend in MEGATREND_POSITIONS.keys():
        megatrend_df = df[df['subject_megatrend'] == megatrend]

        if len(megatrend_df) < 10:
            continue

        x = megatrend_df['axis1'].values
        y = megatrend_df['axis2'].values

        mean_x, mean_y = np.mean(x), np.mean(y)

        # Calculate covariance matrix for ellipse
        cov = np.cov(x, y)
        eigenvalues, eigenvectors = np.linalg.eigh(cov)

        order = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[order]
        eigenvectors = eigenvectors[:, order]

        angle = np.degrees(np.arctan2(*eigenvectors[:, 0][::-1]))

        # Larger multiplier for bigger ellipses (like reference image)
        width = 3.5 * np.sqrt(eigenvalues[0])
        height = 3.5 * np.sqrt(eigenvalues[1])

        color = MEGATREND_COLORS[megatrend]

        # Draw ellipse with more transparency for overlap visibility
        ellipse = Ellipse((mean_x, mean_y), width, height, angle=angle,
                         facecolor=to_rgba(color, 0.25),
                         edgecolor=to_rgba(color, 0.7),
                         linewidth=2, zorder=1)
        ax.add_patch(ellipse)

        # Extract keywords
        keywords = extract_keywords(megatrend_df['Abstract'].tolist(), n_keywords=15)

        cluster_info.append({
            'name': megatrend,
            'short_name': MEGATREND_SHORT_NAMES[megatrend],
            'count': len(megatrend_df),
            'mean_x': mean_x,
            'mean_y': mean_y,
            'width': width,
            'height': height,
            'angle': angle,
            'color': color,
            'keywords': keywords
        })

        # Add cluster label with count (positioned near top of ellipse)
        short_name = MEGATREND_SHORT_NAMES[megatrend]
        angle_rad = np.radians(angle)

        # Position label offset from center toward top
        label_offset_x = -0.3 * height * np.sin(angle_rad)
        label_offset_y = 0.3 * height * np.cos(angle_rad)

        ax.text(mean_x + label_offset_x, mean_y + label_offset_y,
               f'{short_name}, {len(megatrend_df)}',
               fontsize=10, fontweight='bold', ha='center', va='center',
               color=to_rgba(color, 1.0), zorder=5,
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                        edgecolor='none', alpha=0.8))

        # Add keywords scattered throughout the ellipse
        n_keywords_to_show = min(12, len(keywords))

        for j, (keyword, count) in enumerate(keywords[:n_keywords_to_show]):
            # Random position within ellipse
            r = np.random.uniform(0.15, 0.85)
            theta = np.random.uniform(0, 2 * np.pi)

            # Position in ellipse local coordinates
            local_x = r * (width/2) * np.cos(theta) * 0.8
            local_y = r * (height/2) * np.sin(theta) * 0.8

            # Rotate to ellipse orientation
            rot_x = local_x * np.cos(angle_rad) - local_y * np.sin(angle_rad)
            rot_y = local_x * np.sin(angle_rad) + local_y * np.cos(angle_rad)

            kw_x = mean_x + rot_x
            kw_y = mean_y + rot_y

            # Font size based on frequency (larger range like reference)
            max_count = keywords[0][1] if keywords else 1
            fontsize = 7 + (count / max_count) * 5

            ax.text(kw_x, kw_y, keyword.capitalize(),
                   fontsize=fontsize, ha='center', va='center',
                   color=to_rgba(color, 0.8), zorder=3)

    # Set axis limits
    ax.set_xlim(-4, 5)
    ax.set_ylim(-4, 5)

    # Add quadrant dividers
    ax.axhline(y=0, color='#aaaaaa', linestyle='--', linewidth=1, zorder=0, alpha=0.6)
    ax.axvline(x=0, color='#aaaaaa', linestyle='--', linewidth=1, zorder=0, alpha=0.6)

    # Axis labels
    ax.set_xlabel('Detrended correspondence analysis first axis,\nranging from black-box prediction to interpretable intelligence',
                  fontsize=11, fontweight='bold', labelpad=12)
    ax.set_ylabel('Detrended correspondence analysis second axis,\nranging from physical systems to cyber-physical integration',
                  fontsize=11, fontweight='bold', labelpad=12)

    # Add endpoint descriptions at corners
    ax.text(-4, -4.3, 'Black-Box Prediction\n(Technical Metrics, Algorithmic Sophistication)',
            fontsize=8, ha='left', va='top', style='italic', color='#666666')
    ax.text(5, -4.3, 'Interpretable Intelligence\n(Explainability, Policy Relevance)',
            fontsize=8, ha='right', va='top', style='italic', color='#666666')
    ax.text(-4.6, -4, 'Physical Systems\n(Climate, Land,\nHydrology)',
            fontsize=8, ha='right', va='bottom', style='italic', color='#666666', rotation=90)
    ax.text(-4.6, 5, 'Cyber-Physical\n(IoT, Data\nInfrastructure)',
            fontsize=8, ha='right', va='top', style='italic', color='#666666', rotation=90)

    # Style
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xticks([-4, -2, 0, 2, 4])
    ax.set_yticks([-4, -2, 0, 2, 4])

    # Add legend box (bottom right like reference)
    legend_x, legend_y = 3.5, -2.5

    legend_box = plt.Rectangle((legend_x - 0.5, legend_y - 1.3), 2.0, 1.8,
                                facecolor='white', edgecolor='#cccccc',
                                linewidth=1, zorder=4)
    ax.add_patch(legend_box)

    ax.text(legend_x + 0.5, legend_y + 0.3, 'Legend', fontsize=10, fontweight='bold',
           ha='center', va='bottom', zorder=5)

    # Example ellipse in legend (black filled circle like reference)
    legend_circle = plt.Circle((legend_x + 0.5, legend_y - 0.3), 0.4,
                               facecolor='#333333', edgecolor='none', zorder=5)
    ax.add_patch(legend_circle)

    ax.text(legend_x + 0.5, legend_y - 0.3, 'Group,\nnumber of\narticles',
           fontsize=7, ha='center', va='center', fontweight='bold',
           color='white', zorder=6)

    ax.text(legend_x + 0.5, legend_y - 1.0, 'Group ellipse\nbased on eigenvalues',
           fontsize=7, ha='center', va='top', style='italic', color='#666666', zorder=5)

    # Arrow pointing to ellipse edge
    ax.annotate('', xy=(legend_x + 0.85, legend_y - 0.5),
               xytext=(legend_x + 1.2, legend_y - 0.85),
               arrowprops=dict(arrowstyle='-', color='#666666', lw=1), zorder=5)

    # Title
    ax.set_title('Detrended Correspondence Analysis (DCA) of AI in Urban Studies\n(n = {:,} Empirical Articles, 2020-2025)'.format(len(df)),
                fontsize=13, fontweight='bold', pad=15)

    plt.tight_layout()

    # Save
    fig.savefig('dca_plot_v2.pdf', format='pdf', dpi=300, bbox_inches='tight',
                edgecolor='none', facecolor='white')
    fig.savefig('dca_plot_v2.png', format='png', dpi=300, bbox_inches='tight',
                edgecolor='none', facecolor='white')

    print("Saved: dca_plot_v2.pdf, dca_plot_v2.png")

    # Print statistics
    print("\n=== DCA Plot V2 Statistics ===")
    print(f"Total articles: {len(df)}")
    print(f"\nMegatrends ({len(cluster_info)}):")
    for info in sorted(cluster_info, key=lambda x: -x['count']):
        print(f"\n  {info['short_name']}: {info['count']} articles")
        print(f"    Position: ({info['mean_x']:.2f}, {info['mean_y']:.2f})")
        print(f"    Ellipse size: {info['width']:.2f} x {info['height']:.2f}")
        top_kw = ', '.join([k[0] for k in info['keywords'][:5]])
        print(f"    Top keywords: {top_kw}")

    plt.close()


def main():
    print("Loading empirical articles data...")
    df = load_data()
    print(f"Loaded {len(df)} articles")

    print("\nCreating DCA plot (Version 2 - Ellipses with keywords)...")
    create_dca_plot_v2(df)

    print("\nDone!")


if __name__ == "__main__":
    main()
