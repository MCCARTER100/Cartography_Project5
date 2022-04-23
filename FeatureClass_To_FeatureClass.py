import arcpy
from arcpy import env


env.workspace = "G:\SSCI586_Programming\Project4"
places_folder = "G:\SSCI586_Programming\Project4\places"
in_data = "G:\SSCI586_Programming\Project4\tl_2021_06_place.shp"
arcpy.conversion.FeatureClassToFeatureClass(in_data, places_folder, "places.shp")
