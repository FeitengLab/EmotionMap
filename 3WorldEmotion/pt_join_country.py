# coding:utf-8
# version:python2.7.0
# author:kyh
# point spatial join to country
import os
import arcpy
from arcpy import env


# 导入XY坐标文件。传入txt文件，返回shp文件
def Add_xy_point(pt_file, shp_file):
    table = pt_file
    in_x_field = "Field8"
    in_y_field = "Field9"
    out_layer = "face0_layer"

    print "Add x,y Point"
    arcpy.MakeXYEventLayer_management(table=table, in_x_field=in_x_field, in_y_field=in_y_field, out_layer=out_layer)

    Layer_to_feature(out_layer, shp_file)


# 将图层文件转换为要素。传入图层文件
def Layer_to_feature(layer, shp_file):
    print "Convert to shp"
    arcpy.FeatureToPoint_management(layer, shp_file)


# 空间连接，传入点文件，面文件，空间连接后的文件
def Spatial_join(target_features, join_features, out_feature_class, match_option):
    # 保留点文件的属性
    field_mapping_target = arcpy.FieldMappings()
    field_mapping_target.addTable(target_features)

    # 查找面文件所需的属性
    field_mapping_join = arcpy.FieldMappings()
    field_mapping_join.addTable(join_features)
    ADMIN_index = field_mapping_join.findFieldMapIndex("ADMIN")
    field_mapping_target.addFieldMap(field_mapping_join.getFieldMap(ADMIN_index))

    print "Spatial Join"
    arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class, field_mapping=field_mapping_target,
                               match_option=match_option)


def Select_feature(in_features, out_features, where_clause):
    print "Select"
    arcpy.Select_analysis(in_features, out_features, where_clause)


def Delete_field(out_feature_class):
    print "Delete Field"
    arcpy.DeleteField_management(out_feature_class, "ADMIN_1")


def Join_field(in_features, join_table):
    in_layer = "face0_intersect_layer"
    arcpy.MakeFeatureLayer_management(in_features, in_layer)

    in_field = "TARGET_FID"

    out_layer = "face0_intersect_select_layer"
    arcpy.MakeFeatureLayer_management(join_table, out_layer)

    join_field = "TARGET_FID"

    print "Join Field"
    arcpy.AddJoin_management(in_layer, in_field, join_table, join_field)

    return in_layer


def Update_field(layer):
    in_table = layer
    in_field = "face0_intersect.ADMIN"
    expression = "Update(!face0_intersect.ADMIN!, !face0_select_intersect.ADMIN_1!)"
    expression_type = "PYTHON_9.3"
    code_block = """def Update(field1,field2):
        if field1 is not None:
            return field1
        else:
            return field2"""

    print "Calculate Field"
    arcpy.CalculateField_management(in_table, in_field, expression, expression_type, code_block)

def Remove_field(in_layer):
    print "Remove Field"
    arcpy.RemoveJoin_management(in_layer)

    arcpy.FeatureClassToFeatureClass_conversion(in_layer,env.workspace,"Final")

if __name__ == '__main__':
    env.workspace = r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\EmotionMap.mdb"
    pt_shp = r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\face0.shp"
    Add_xy_point(r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\face0.txt",pt_shp)

    country_shp = r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\ne_10m_admin_0_countries.shp"
    spatial_join_class = r"face0_intersect"
    Spatial_join(pt_shp, country_shp, spatial_join_class, "INTERSECT")

    Select_feature("face0_intersect", "face0_select", '[ADMIN] IS Null')

    country_shp = r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\ne_10m_admin_0_countries.shp"
    Spatial_join("face0_select", country_shp, "face0_select_intersect", "CLOSEST")
    Delete_field("face0_intersect")

    layer = Join_field("face0_intersect", "face0_select_intersect")
    Update_field(layer)
    Remove_field(layer)

'''
    cursor=arcpy.da.SearchCursor("Final","*")
    for row in cursor:
        print row[25]
        '''
