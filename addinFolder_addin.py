import arcpy
import pythonaddins
# Import arcpy module
import arcpy


# Local variables:
union = "\\\\hd.ad.syr.edu\\01\\e51673\\Documents\\Desktop\\Courses\\ERE693 GIS-Modeling\\Lab_09\\lab09Process.gdb\\union"
T6_N = "\\\\hd.ad.syr.edu\\01\\e51673\\Documents\\Desktop\\Courses\\ERE693 GIS-Modeling\\Lab_09\\lab09Process.gdb\\T6_N"
BMPs = "\\\\hd.ad.syr.edu\\01\\e51673\\Documents\\Desktop\\Courses\\ERE693 GIS-Modeling\\Lab_09\\Lab06Data.gdb\\BMPs"
T6_N_points = "\\\\hd.ad.syr.edu\\01\\e51673\\Documents\\Desktop\\Courses\\ERE693 GIS-Modeling\\Lab_09\\lab09Process.gdb\\T6_N_points"


class ToolClass10(object):
    """Implementation for addinFolder_addin.tool_1 (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "NONE" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onMouseDown(self, x, y, button, shift):
        pass
    def onMouseDownMap(self, x, y, button, shift):
        pass
    def onMouseUp(self, x, y, button, shift):
        pass
    def onMouseUpMap(self, x, y, button, shift):
        pass
    def onMouseMove(self, x, y, button, shift):
        pass
    def onMouseMoveMap(self, x, y, button, shift):
        pass
    def onDblClick(self):
        # Process: Polygon to Raster
        arcpy.PolygonToRaster_conversion(union, "TotalNitrogen", T6_N, "CELL_CENTER", "NONE", "40")
    def onKeyDown(self, keycode, shift):
        pass
    def onKeyUp(self, keycode, shift):
        pass
    def deactivate(self):
        pass
    def onCircle(self, circle_geometry):
        pass
    def onLine(self, line_geometry):
        pass
    def onRectangle(self, rectangle_geometry):
        pass

class ToolClass2(object):
    """Implementation for addinFolder_addin.tool (Tool)"""
    def __init__(self):
        self.enabled = True
        self.shape = "NONE" # Can set to "Line", "Circle" or "Rectangle" for interactive shape drawing and to activate the onLine/Polygon/Circle event sinks.
    def onMouseDown(self, x, y, button, shift):
        pass
    def onMouseDownMap(self, x, y, button, shift):
        pass
    def onMouseUp(self, x, y, button, shift):
        pass
    def onMouseUpMap(self, x, y, button, shift):
        pass
    def onMouseMove(self, x, y, button, shift):
        pass
    def onMouseMoveMap(self, x, y, button, shift):
        pass
    def onDblClick(self):
        # Process: Polygon to Raster
        arcpy.PolygonToRaster_conversion(union, "TotalNitrogen", T6_N, "CELL_CENTER", "NONE", "40")
    def onKeyDown(self, keycode, shift):
        pass
    def onKeyUp(self, keycode, shift):
        pass
    def deactivate(self):
        pass
    def onCircle(self, circle_geometry):
        pass
    def onLine(self, line_geometry):
        pass
    def onRectangle(self, rectangle_geometry):
        pass
