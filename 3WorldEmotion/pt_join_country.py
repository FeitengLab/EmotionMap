# coding:utf-8
# version:python2.7.0
# author:kyh
# point spatial join to country
import os
import arcpy
import csv
from arcpy import env

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


# 导入XY坐标文件。传入txt文件，返回shp文件
def Add_xy_point(pt_file, shp_file):
    table = pt_file
    in_x_field = "Field2"
    in_y_field = "Field3"
    out_layer = "face{0}_layer".format(index)

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

def Find_near_feature(in_features,near_features):
    print "Find nearest feature"
    arcpy.Near_analysis(in_features,near_features)

def Delete_field(out_feature_class):
    print "Delete Field"
    arcpy.DeleteField_management(out_feature_class, "ADMIN_1")


def Join_field(in_features, join_table):
    in_layer = "face{0}_intersect_layer".format(index)
    arcpy.MakeFeatureLayer_management(in_features, in_layer)

    in_field = "TARGET_FID"

    out_layer = "face{0}_intersect_select_layer".format(index)
    arcpy.MakeFeatureLayer_management(join_table, out_layer)

    join_field = "TARGET_FID"

    print "Join Field"
    arcpy.AddJoin_management(in_layer, in_field, join_table, join_field)

    return in_layer


def Update_field(layer):
    in_table = layer
    in_field = "face{0}_intersect.ADMIN".format(index)
    expression = "Update(!face{0}_intersect.ADMIN!, !face{0}_select_intersect.ADMIN_1!)".format(index, index)
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

    arcpy.FeatureClassToFeatureClass_conversion(in_layer, env.workspace, "face{0}".format(index))


def Delete_file():
    print "Delete File"
    arcpy.Delete_management("face{0}_intersect".format(index))
    arcpy.Delete_management("face{0}_select".format(index))
    arcpy.Delete_management("face{0}_select_intersect".format(index))


def Write_csv(file):
    print "Write File"
    #cursor = arcpy.da.SearchCursor("face{0}_intersect".format(index), "*")
    cursor = arcpy.da.SearchCursor("face{0}_select".format(index), "*")
    with open(file, "wb") as file:
        writer = csv.writer(file, delimiter="\t")
        for row in cursor:
            row_new = []
            row_new.append(row[7])
            row_new.append(row[10])
            writer.writerow(row_new)


if __name__ == '__main__':
    global index
    index = 98
    end = 134

    env.workspace = r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\Country2\EmotionMap.mdb"
    folder_path = r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\Country2"
    while True:
        try:
            print index
            '''
            pt_shp = folder_path + r"\face{0}.shp".format(index)
            Add_xy_point(folder_path + r"\facept{0}.txt".format(index), pt_shp)
            '''
            country_shp = folder_path + r"\ne_10m_admin_0_countries.shp"
            '''
            spatial_join_class = r"face{0}_intersect".format(index)
            Spatial_join(pt_shp, country_shp, spatial_join_class, "INTERSECT")

            Select_feature("face{0}_intersect".format(index), "face{0}_select".format(index), '[ADMIN] IS Null')
            '''
            #Spatial_join("face{0}_select".format(index), country_shp, "face{0}_select_intersect".format(index),
                         #"CLOSEST")
            '''
            layer = Join_field("face{0}_intersect".format(index), "face{0}_select_intersect".format(index))
            Update_field(layer)
            Remove_field(layer)

            Delete_file()

            '''
            #Write_csv(folder_path + r"\face_s_{0}.csv".format(index))
            Find_near_feature(r"{0}\face{1}_select".format(env.workspace,index),country_shp)
            arcpy.Near_analysis(r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\Country\EmotionMap.mdb\face{0}_select".format(index),
                                r"D:\Users\KYH\Documents\ArcGIS\EmotionMap\Country\ne_10m_admin_0_countries.shp")

            index = index + 1
            if index > end:
                break
        except Exception as e:
            with open('log.txt', 'a') as log:
                log.writelines("{0},{1}".format(index, e))
                index = index + 1
        finally:
            if index > end:
                break
