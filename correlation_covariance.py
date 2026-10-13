"""GLAB 330.2.1: Population covariance and Pearson correlation.

The three observations are taken directly from the Per Scholas guided lab.
Run: python correlation_covariance.py
"""

from math import sqrt
from pathlib import Path

import matplotlib
matplotlib.use('Agg')  # Generate images without opening a desktop window.
import matplotlib.pyplot as plt


# Step 1: Store the temperature and sales for the same three days.
days = [1, 2, 3]
temperatures = [20, 25, 15]  # Degrees Celsius
sales = [100, 120, 80]      # Ice creams sold


def calculate_statistics(x, y):
    """Calculate population covariance, population SDs and correlation by hand."""
    if len(x) != len(y) or len(x) < 2:
        raise ValueError('X and Y must have the same length (at least two).')

    n = len(x)
    # Step 2: Compute the mean (average) of each variable.
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    # Step 3: Subtract each mean to find the deviations for every observation.
    dx = [value - mean_x for value in x]
    dy = [value - mean_y for value in y]

    # Step 4: Multiply corresponding deviations and add their products.
    products = [a * b for a, b in zip(dx, dy)]
    # The lab uses population covariance (divide by N, not N-1).
    covariance = sum(products) / n

    # Step 5: Find population variances and take square roots for SDs.
    variance_x = sum(value ** 2 for value in dx) / n
    variance_y = sum(value ** 2 for value in dy) / n
    sd_x = sqrt(variance_x)
    sd_y = sqrt(variance_y)
    if sd_x == 0 or sd_y == 0:
        raise ValueError('Correlation is undefined if a variable does not vary.')

    # Step 6: Standardize the covariance to obtain Pearson correlation.
    correlation = covariance / (sd_x * sd_y)

    return {
        'n': n, 'mean_x': mean_x, 'mean_y': mean_y,
        'dx': dx, 'dy': dy, 'products': products,
        'covariance': covariance, 'variance_x': variance_x,
        'variance_y': variance_y, 'sd_x': sd_x, 'sd_y': sd_y,
        'correlation': correlation,
    }


def make_charts(output_folder, stats):
    """Save the lab's day-by-day chart and scatter plot with a trend line."""
    output_folder.mkdir(exist_ok=True, parents=True)

    # First chart: separate y-axes keep both different measurement units readable.
    fig, ax_temp = plt.subplots(figsize=(8.5, 4.7))
    ax_sales = ax_temp.twinx()
    l1 = ax_temp.plot(days, temperatures, 'o-', color='#157a9e', linewidth=2,
                      label='Temperature (°C)')
    l2 = ax_sales.plot(days, sales, 's-', color='#df862f', linewidth=2,
                       label='Ice cream sales')
    ax_temp.axhline(stats['mean_x'], color='#157a9e', linestyle='--', alpha=0.7,
                    label='Mean temperature (20°C)')
    ax_sales.axhline(stats['mean_y'], color='#df862f', linestyle='--', alpha=0.7,
                     label='Mean sales (100)')
    ax_temp.set(title='Temperature and Ice Cream Sales Over Three Days',
                xlabel='Day', ylabel='Temperature (°C)', xticks=days,
                ylim=(10, 30))
    ax_sales.set_ylabel('Ice cream sales')
    ax_sales.set_ylim(65, 135)
    ax_temp.grid(alpha=0.2)
    handles, labels = ax_temp.get_legend_handles_labels()
    h2, l2labels = ax_sales.get_legend_handles_labels()
    ax_temp.legend(handles + h2, labels + l2labels, loc='upper left', fontsize=8)
    fig.tight_layout()
    fig.savefig(output_folder / 'daily_temperature_and_sales.png', dpi=170)
    fig.savefig(output_folder / 'daily_temperature_and_sales.svg')
    plt.close(fig)

    # Second chart: plotted pairs + trend line clearly show the positive pattern.
    fig, ax = plt.subplots(figsize=(8.5, 4.7))
    ax.scatter(temperatures, sales, marker='o', s=75, color='#157a9e',
               zorder=3, label='Daily observations')
    # y = 4x + 20 follows exactly from these three data points.
    sorted_temps = sorted(temperatures)
    trend_sales = [4 * t + 20 for t in sorted_temps]
    ax.plot(sorted_temps, trend_sales, '--', color='#df862f', linewidth=2,
            label='Trend line: sales = 4 × temperature + 20')
    for day, t, s in zip(days, temperatures, sales):
        ax.annotate(f'Day {day}', (t, s), xytext=(6, 7),
                    textcoords='offset points', fontsize=9)
    ax.set(title='Correlation Between Temperature and Ice Cream Sales',
           xlabel='Temperature (°C)', ylabel='Ice cream sales',
           xlim=(12, 28), ylim=(70, 130))
    ax.grid(alpha=0.2)
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(output_folder / 'correlation_scatter_plot.png', dpi=170)
    fig.savefig(output_folder / 'correlation_scatter_plot.svg')
    plt.close(fig)


def main():
    stats = calculate_statistics(temperatures, sales)
    folder = Path(__file__).resolve().parent
    make_charts(folder / 'charts', stats)

    # Present every intermediate calculation so the assignment is easy to review.
    lines = [
        'GLAB 330.2.1 - Covariance and Correlation',
        '=========================================',
        'Day | Temp (X) | Sales (Y) | X-mean(X) | Y-mean(Y) | Product',
    ]
    for day, x, y, dx, dy, product in zip(
            days, temperatures, sales, stats['dx'], stats['dy'], stats['products']):
        lines.append(f'{day:>3} | {x:>8} | {y:>9} | {dx:>9.0f} | {dy:>9.0f} | {product:>7.0f}')
    lines.extend([
        '',
        f"Mean temperature: {stats['mean_x']:.2f} °C",
        f"Mean sales: {stats['mean_y']:.2f}",
        f"Sum of deviation products: {sum(stats['products']):.0f}",
        f"Population covariance: {stats['covariance']:.2f}",
        f"Population variance, temperature: {stats['variance_x']:.2f}",
        f"Population variance, sales: {stats['variance_y']:.2f}",
        f"Population standard deviation, temperature: {stats['sd_x']:.4f}",
        f"Population standard deviation, sales: {stats['sd_y']:.4f}",
        f"Pearson correlation coefficient (r): {stats['correlation']:.4f}",
        '',
        'Interpretation: The covariance is positive, so higher temperatures are',
        'associated with higher ice cream sales. r = +1 means these three',
        'observations have a perfect positive linear association.',
        'Correlation describes an association; it does not prove causation.',
    ])
    report_text = '\n'.join(lines) + '\n'
    print(report_text)
    (folder / 'results.txt').write_text(report_text, encoding='utf-8')


if __name__ == '__main__':
    main()
