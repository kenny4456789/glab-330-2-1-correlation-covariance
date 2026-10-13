# GLAB 330.2.1 - Correlation Coefficient and Covariance

**Course:** Per Scholas - AI-Native Business Intelligence  
**Assignment:** Basic Example for Correlation Coefficient and Covariance

## What I did

I compared three days of temperature and ice cream sales. I did the calculations and made two graphs to see the pattern.

## Data I used

| Day | Temperature (°C) | Ice cream sales |
| --- | ---: | ---: |
| Day 1 | 20 | 100 |
| Day 2 | 25 | 120 |
| Day 3 | 15 | 80 |

## My calculations

**1. Find the averages.** I added the three temperatures and divided by 3: `(20 + 25 + 15) / 3 = 20°C`. I did the same thing for sales: `(100 + 120 + 80) / 3 = 100`.

**2. Find how far each value is from its average.** For temperature, I got `0, 5, -5`. For ice cream sales, I got `0, 20, -20`.

**3. Multiply the differences.** For each day, I multiplied the temperature difference by the sales difference:

| Day | Temperature difference | Sales difference | Multiplied together |
| --- | ---: | ---: | ---: |
| Day 1 | 0 | 0 | 0 |
| Day 2 | 5 | 20 | 100 |
| Day 3 | -5 | -20 | 100 |
| **Total** | | | **200** |

**4. Calculate covariance.** I added the products and divided by the number of days: `200 / 3 = 66.67`. The covariance is positive. That tells me the temperature and sales went in the same direction in this example.

**5. Calculate the standard deviations.** This measures how spread out the values are from their averages. Using the method in the lab, the temperature standard deviation is about `4.08`, and the sales standard deviation is about `16.33`.

- Temperature: `sqrt((0² + 5² + (-5)²) / 3) = 4.08`
- Sales: `sqrt((0² + 20² + (-20)²) / 3) = 16.33`

**6. Calculate correlation.** I divided the covariance by the two standard deviations multiplied together. Using the unrounded numbers, I got **+1.00**. That means the three points have a perfect positive straight-line relationship.

**7. Make graphs.** I created one graph to compare the three days and another one that plots temperature against sales. Both show that higher temperatures went along with more ice cream sales.

## My results

| What I calculated | My answer |
| --- | ---: |
| Average temperature | 20°C |
| Average sales | 100 |
| Covariance | **66.67** |
| Temperature standard deviation | 4.08 |
| Sales standard deviation | 16.33 |
| Correlation coefficient | **+1.00** |

## Graphs

### Temperature and sales over three days

![Temperature and ice cream sales by day](charts/daily_temperature_and_sales.png)

This graph shows the temperature and sales for each day. Day 2 had the highest temperature and the most sales, while Day 3 had the lowest temperature and the fewest sales. The dashed lines show the averages.

### Correlation scatter plot

![Scatter plot of temperature and ice cream sales](charts/correlation_scatter_plot.png)

Each dot represents one day. The dots form an upward straight line, which matches the correlation of +1.00.

## What I learned

At first I thought covariance and correlation was the same thing. Now I get that covariance shows which way the numbers move, and correlation shows how strong the connection is. I got 66.67 for covariance and +1 for correlation, which matches the graph since hotter days had more ice cream sales.

## How to run my Python project

1. Install Python 3.
2. Install the graphing library with `pip install -r requirements.txt`.
3. Run `python correlation_covariance.py`.
4. The program prints the answers, saves them to `results.txt`, and creates the graphs in the `charts` folder.

## Files in this project

- `correlation_covariance.py` - my calculations and graph-making code, with comments explaining the steps.
- `results.txt` - the results when the program runs.
- `charts/` - the two graphs in PNG and SVG formats.
- `requirements.txt` - the Python package needed to run the graphs.
- `README.md` - my explanation of the lab.

**Reference:** Per Scholas, *Guided Lab 330.2.1 - Basic Example for Correlation Coefficient and Covariance*.
