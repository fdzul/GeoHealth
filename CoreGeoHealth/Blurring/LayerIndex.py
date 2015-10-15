# -*- coding: utf-8 -*-
"""
/***************************************************************************

                                 GeoHealth
                                 A QGIS plugin

                              -------------------
        begin                : 2014-08-20
        copyright            : (C) 2014 by Etienne Trimaille
        email                : etienne@trimaille.eu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from GeoHealth import *

"""Class to know if an intersection exist between a QgsGeometry and a QgsVectorLayer"""

class LayerIndex:
    
    def __init__(self, layer):
        self.__layer = layer        
        self.__index = QgsSpatialIndex()
        for ft in layer.getFeatures():
            self.__index.insertFeature(ft)
        
    def contains(self, point):
        """Return true if the point intersects the layer"""
        intersects = self.__index.intersects(point.boundingBox())
        for i in intersects:
            request = QgsFeatureRequest().setFilterFid(i)
            feat = self.__layer.getFeatures(request).next()
            tmpGeom = QgsGeometry(feat.geometry())
            if point.intersects(tmpGeom):
                return True
        return False
    
    def countIntersection(self,bufferGeom,nb):
        """Return true if the buffer intersects enough entities"""
        count = 0
        intersects = self.__index.intersects(bufferGeom.boundingBox())
        for i in intersects:
            request = QgsFeatureRequest().setFilterFid(i)
            feat = self.__layer.getFeatures(request).next()
            tmpGeom = QgsGeometry(feat.geometry())
            if bufferGeom.intersects(tmpGeom):
                count += 1
                if count >= nb:
                    return True
        return False