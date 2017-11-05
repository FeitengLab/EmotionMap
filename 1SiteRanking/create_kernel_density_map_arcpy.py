# coding:utf-8
# version:python2.7.3
# author:kyh
# import x,y data from txt and create kernel density map
import arcpy
from arcpy.sa import *
from arcpy import env


def read_point_data(filepath,i):
    # Read data file and create shp file
    with open(filepath, 'r') as pt_file:
        pt=arcpy.Point()
        ptGeoms=[]
        i=0
        for line in pt_file.readlines():
            i=i+1
            pt.X = float(line.split('\t')[7])
            pt.Y = float(line.split('\t')[8])
            ptGeoms.append(arcpy.PointGeometry(pt))

        arcpy.CopyFeatures_management(ptGeoms, "D://Users//KYH//Documents//ArcGIS//FlickrPhoto//World_Flickr{0}.shp".format(i))


if __name__ == '__main__':
    arcpy.CheckOutExtension('Spatial')
    env.workspace=("D:\Users\KYH\Documents\ArcGIS\FlickrPhoto")
    for i in range(0,25):
        if (i==5) or (i==22):
            continue
        read_point_data("D:\\Users\\KYH\\Desktop\\EmotionMap\\FlickrEmotionData\\3faces_emotion\\faceflickr{0}.txt".format(i))
        # Kernel Density Analysis
        out_kernel_density=KernelDensity("World_Flickr{0}.shp".format(i),"NONE")
        out_kernel_density.save("D:\Users\KYH\Documents\ArcGIS\FlickrPhoto\kd_Face{0}".format(i))

