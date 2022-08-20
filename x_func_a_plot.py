import pandas as pd
import plotly.express as px
import numpy as np
from itertools import product


def get_data_x_power_a(x_min, x_max, x_step, a_min, a_max, a_step, key=None):
	if key is None:
		key = lambda a, b: a ** b
	all_data_pairs = np.array(list(product(np.arange(x_min, x_max, x_step), np.arange(a_min, a_max, a_step))))
	res_df = pd.DataFrame({'x': all_data_pairs[:, 0], 'a': all_data_pairs[: , 1], 'y': key(all_data_pairs[:, 0], all_data_pairs[:, 1])})
	return res_df


def plot_x_power_a(df, x_min, x_max, y_min, y_max, output_name = "plot.html"):
	fig = px.line(
		df,
		x="x",
		y="y",
		animation_frame="a",
		range_x=[x_min, x_max],
		range_y=[y_min, y_max]
	)
	fig.write_html(output_name)
	fig.show()


if __name__ == "__main__":
	df = get_data_x_power_a(-10, 10, 0.01, -4, 4, 0.01, key=lambda a, b: np.sin(a)**2 + np.cos(b)**2)
	plot_x_power_a(df, -10, 10, -10, 10)

