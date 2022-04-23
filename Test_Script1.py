import arcpy
from arcpy import env


env.workspace = "G:\SSCI586_Programming\Project4"    
in_data = "G:\SSCI586_Programming\Project4\places\Places1.shp"
in_csv = "G:\SSCI586_Programming\Project4\CA_Taxes.csv"
out_data = "G:\SSCI586_Programming\Project4\places\Places2.shp"
data_type = ""

arcpy.Copy_management(in_data, out_data, data_type)    
arcpy.env.overwriteOutput = True 
in_data_copy = arcpy.MakeFeatureLayer_management (in_data)
in_csv_copy = arcpy.MakeTableView_management (in_csv)

LayerName = in_csv_copy 
Field = "PlaceName"
TableName = in_data_copy
Field2 = "NAME"

arcpy.AddJoin_management (LayerName, Field, TableName, Field2)
