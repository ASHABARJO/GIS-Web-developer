
                pip install gdal


import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from osgeo import gdal
from matplotlib.widgets import Slider, Button
from mpl_toolkits.axes_grid1 import make_axes_locatable


class RasterViewer:

  def __init__(self, raster_path):
    self.raster_path = raster_path
    self.dataset = gdal.Open(raster_path)
    self.bands = [
        self.dataset.GetRasterBand(i + 1).ReadAsArray()
        for i in range(self.dataset.RasterCount)
    ]
    self.current_band_combination = [1, 2, 3]  # Default RGB bands

    # Initialize the viewer window
    self.fig, self.ax = plt.subplots()
    self.img = self.ax.imshow(self.get_rgb_image(), cmap='gray')
    self.setup_slider()

  def get_rgb_image(self):
    rgb_image = np.stack(
        [self.bands[i - 1] for i in self.current_band_combination], axis=-1)
    return rgb_image

  def update_image(self, val):
    self.img.set_array(self.get_rgb_image())
    self.fig.canvas.draw_idle()

  def setup_slider(self):
    ax_slider = plt.axes([0.1, 0.01, 0.65, 0.03],
                         facecolor='lightgoldenrodyellow')
    slider = Slider(ax_slider,
                    'Band Combination',
                    1,
                    self.dataset.RasterCount,
                    valinit=1,
                    valstep=1)
    slider.on_changed(self.update_band_combination)

  def update_band_combination(self, val):
    self.current_band_combination = [
        int(val),
        int(val) % self.dataset.RasterCount + 1,
        int(val) % self.dataset.RasterCount + 2
    ]
    self.update_image(val)

  def show(self):
    plt.show()


# Example usage
if __name__ == "__main__":
  raster_viewer = RasterViewer("path/to/your/raster/image.tif")
  raster_viewer.show()


class ShapefileAttributeChart:

  def __init__(self, shapefile_path):
    self.shapefile_path = shapefile_path
    self.gdf = gpd.read_file(shapefile_path)

  def plot_attribute_chart(self, attribute_column):
    plt.figure()
    self.gdf[attribute_column].plot(kind='bar')
    plt.title(f"{attribute_column} Distribution")
    plt.xlabel("Feature Index")
    plt.ylabel(attribute_column)
    plt.show()


# Example usage
if __name__ == "__main__":
  shapefile_chart = ShapefileAttributeChart("path/to/your/shapefile.shp")
  shapefile_chart.plot_attribute_chart("your_attribute_column_name")
