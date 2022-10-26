from bokeh.plotting import figure, output_file, show, ColumnDataSource
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8
import pandas

df = pandas.read_csv('cars.csv')

source = ColumnDataSource(df)

output_file('index.html')

car_list = source.data['Car'].tolist()

p = figure(
    y_range = car_list,
    plot_width=600,
    plot_height=400,
    title='Cars With Top Horsepower',
    x_axis_label = 'Horsepower',
    tools='pan, box_select, zoom_in, zoom_out, save, reset'
)

p.hbar(
    y='Car',
    right='Horsepower',
    left=0,
    height=0.4,
    fill_color=factor_cmap(
        'Car',
        palette= Blues8,
        factors=car_list
    ),
    fill_alpha=0.5,
    source=source
)

hover = HoverTool()
hover.tooltips = """
    <div>
        <h3>@Car</h3>
        <div><strong>Price: </strong>@Price</div>
        <div><strong>HP: </strong>@Horsepower</div>
        <div><img src="@Image" alt="" width="200" /></div>
    </div>
"""


p.add_tools(hover)

show(p)