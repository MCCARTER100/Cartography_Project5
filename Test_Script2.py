import arcpy
from arcpy import env


env.workspace = "G:\SSCI586_Programming\Project4"    
in_data = "G:\SSCI586_Programming\Project4\places\Places1.shp"
in_csv = "G:\SSCI586_Programming\Project4\CA_Taxes1.csv"
gdb_loc = "G:\SSCI586_Programming\Project4"
out_points = "G:\SSCI586_Programming\Project4\places\CA_City_Points.shp"
out_data = "G:\SSCI586_Programming\Project4\places\Places2.shp"


data_type = ""



out_data1 = arcpy.Copy_management(in_data, out_data, data_type) 
    
arcpy.env.overwriteOutput = True 
out_data_copy = arcpy.MakeFeatureLayer_management (out_data1)
in_csv_copy = arcpy.MakeTableView_management (in_csv)

TableName = in_csv_copy 
Field = "NAME"
LayerName = out_data_copy
Field2 = "PlaceName"

cities = arcpy.JoinField_management(LayerName, Field, TableName, Field2)
cities_selection = arcpy.management.SelectLayerByAttribute(cities, "NEW_SELECTION", '"PlaceName" IS NOT NULL')
city_points = arcpy.management.FeatureToPoint(cities_selection, out_points)
arcpy.arcpy.management.AddXY(city_points)
print('process complete')
