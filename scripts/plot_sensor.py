import csv

# Load data
x = []
y = []
with open('data/sensor_data.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        x.append(float(row['time']))
        y.append(float(row['value']))

# Determine plot dimensions
width = 400
height = 200
margin = 40

x_min, x_max = min(x), max(x)
y_min, y_max = min(y), max(y)

# Scale functions
scale_x = lambda v: margin + (v - x_min) / (x_max - x_min) * (width - 2*margin)
scale_y = lambda v: height - margin - (v - y_min) / (y_max - y_min) * (height - 2*margin)

# Build polyline points
points = " ".join(f"{scale_x(xi):.2f},{scale_y(yi):.2f}" for xi, yi in zip(x, y))

svg_content = f"""<svg xmlns='http://www.w3.org/2000/svg' width='{width}' height='{height}'>
  <rect width='100%' height='100%' fill='white'/>
  <polyline fill='none' stroke='blue' stroke-width='2' points='{points}' />
  <line x1='{margin}' y1='{height-margin}' x2='{width-margin}' y2='{height-margin}' stroke='black'/>
  <line x1='{margin}' y1='{margin}' x2='{margin}' y2='{height-margin}' stroke='black'/>
</svg>"""

with open('plots/sensor_plot.svg', 'w') as f:
    f.write(svg_content)

print('Plot saved to plots/sensor_plot.svg')
