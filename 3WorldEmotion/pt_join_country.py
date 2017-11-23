# coding:utf-8
# version:python2.7.0
# author:kyh
# point spatial join to country
import os
import arcpy
from arcpy import env


# 导入XY坐标文件。传入txt文件，返回shp文件
def Add_xy_point(pt_file):
    table = pt_file
    in_x_field = "Field8"
    in_y_field = "Field9"
    out_layer = "face0_layer"

    print "Add x,y Point"
    arcpy.MakeXYEventLayer_management(table=table, in_x_field=in_x_field, in_y_field=in_y_field, out_layer=out_layer)

    return Layer_to_feature(r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\face0.shp")


# 将图层文件转换为要素。传入图层文件
def Layer_to_feature(layer):
    print "Convert to shp"
    out_feature = None
    arcpy.FeatureToPoint_management(layer, out_feature)
    return out_feature


# 空间连接，传入
def Spatial_join(target_features,join_features,out_feature_class):
    join_features = r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\ne_10m_admin_0_countries.shp"
    out_feature_class = r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\EmotionMap.mdb\face0_intersect"

    field_mapping_target = arcpy.FieldMappings()
    field_mapping_target.addTable(target_features)

    field_mapping_join = arcpy.FieldMappings()
    field_mapping_join.addTable(join_features)
    ADMIN_index = field_mapping_join.findFieldMapIndex("ADMIN")
    field_mapping_target.addFieldMap(field_mapping_join.getFieldMap(ADMIN_index))

    print "Spatial Join"
    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class, field_mapping=field_mapping_target,
                               match_option="INTERSECT")


print "Select"
arcpy.Select_analysis("face0_intersect", "face0_select", '[ADMIN] IS Null')

target_features = r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\EmotionMap.mdb\face0_select"
join_features = r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\ne_10m_admin_0_countries.shp"
out_feature_class = r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\EmotionMap.mdb\face0_intersect_select"

field_mapping_target = arcpy.FieldMappings()
field_mapping_target.addTable(target_features)

field_mapping_join = arcpy.FieldMappings()
field_mapping_join.addTable(join_features)
ADMIN_index = field_mapping_join.findFieldMapIndex("ADMIN")
field_mapping_target.addFieldMap(field_mapping_join.getFieldMap(ADMIN_index))

print "Spatial Join"
arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class, field_mapping=field_mapping_target,
                           match_option="CLOSEST")
arcpy.DeleteFeatures_management(target_features)

print "Delete Field"
arcpy.DeleteField_management(out_feature_class, "ADMIN")

in_features = r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\EmotionMap.mdb\face0_intersect"
out_layer = "face0_intersect_layer"
arcpy.MakeFeatureLayer_management(in_features, out_layer)

in_layer = out_layer
in_field = "TARGET_FID"

in_features = r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\EmotionMap.mdb\face0_intersect_select"
out_layer = "face0_intersect_select_layer"
arcpy.MakeFeatureLayer_management(in_features, out_layer)

join_table = out_layer
join_field = "TARGET_FID"

print "Join Field"
arcpy.AddJoin_management(in_layer, in_field, join_table, join_field)

in_table = in_layer
in_field = "ADMIN"
expression = "Update(!face0_intersect.ADMIN!, !face0_intersect_select.ADMIN_1!)"
expression_type = "PYTHON_9.3"
code_block = """
def Update(field1,field2):
  if field1 is not None:
    return field1
  else:
    return field2
    """

print "Calculate Field"
arcpy.CalculateField_management(in_table, in_field, expression, expression_type, code_block)

print "Remove Field"
arcpy.RemoveJoin_management(in_layer, join_table)

arcpy.DeleteFeatures_management(join_table)

if __name__ == '__main__':
    env.workspace = r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\EmotionMap.mdb"
    Add_xy_point(r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\face0.txt")
