#coding:utf-8
import sys
from histogramequalization import histogramequalization
from edgedetection import edgedetection

picture = [
	"airplanes.image_0314.24bit.bmp",
	"ant.image_0008.24bit.bmp"
]

for i in range(0, len(picture)):
	"""histogram equalization"""
	histogramequalization(picture[i])
	"""edge detection"""
	edgedetection(picture[i])
	"""edge detection after histogram equalization"""
	edgedetection("histogramequalization_" + picture[i])