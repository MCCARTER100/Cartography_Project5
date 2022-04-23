import arcpy
from arcpy import env


env.workspace = "G:\SSCI586_Programming\Project4"    
in_data = "G:\SSCI586_Programming\Project4\places\Places1.shp"
in_csv = "G:\SSCI586_Programming\Project4\CA_Taxes1.csv"
gdb_loc = "G:\SSCI586_Programming\Project4"
out_dbf = "CA_Taxes.dbf"
out_data = "G:\SSCI586_Programming\Project4\places\Places2.shp"

data_type = ""

in_dbf1 = arcpy.conversion.TableToTable(in_csv, gdb_loc, out_dbf)
