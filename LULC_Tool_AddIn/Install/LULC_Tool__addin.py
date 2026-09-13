import arcpy
import pythonaddins

class ToggleLayer(object):
    def __init__(self):
        self.enabled = True
        self.checked = False

    def onClick(self):
        try:
            mxd = arcpy.mapping.MapDocument("CURRENT")
            
            # Coba tangkap layer yang saat ini sedang di-select (disorot) di Table of Contents
            selected_item = pythonaddins.GetSelectedTOCLayerOrDataFrame()
            
            # Skenario 1: Jika ada layer yang di-select, toggle layer tersebut
            if isinstance(selected_item, arcpy.mapping.Layer):
                selected_item.visible = not selected_item.visible
                arcpy.RefreshTOC()
                arcpy.RefreshActiveView()
                
            # Skenario 2: Jika tidak ada layer yang di-select (atau yang diselect adalah Data Frame),
            # maka jadikan layer paling atas (Top Layer) sebagai default target
            else:
                df = arcpy.mapping.ListDataFrames(mxd)[0]
                layers = arcpy.mapping.ListLayers(mxd, "", df)
                if len(layers) > 0:
                    layers[0].visible = not layers[0].visible
                    arcpy.RefreshTOC()
                    arcpy.RefreshActiveView()
                    
        except Exception:
            pass