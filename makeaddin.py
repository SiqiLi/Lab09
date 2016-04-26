import os
import re
import zipfile

current_path = os.path.dirname(os.path.abspath(__file__))

out_zip_name = os.path.join(current_path, 
                            os.path.basename(current_path) + ".esriaddin")

BACKUP_FILE_PATTERN = re.compile(".*_addin_[0-9]+[.]py$", re.IGNORECASE)

def looks_like_a_backup(filename):
    return bool(BACKUP_FILE_PATTERN.match(filename))

with zipfile.ZipFile(out_zip_name, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    for filename in ('config.xml', 'README.txt', 'makeaddin.py'):
        zip_file.write(os.path.join(current_path, filename), filename)
    dirs_to_add = ['Images', 'Install']
    for directory in dirs_to_add:
        for (path, dirs, files) in os.walk(os.path.join(current_path,
                                                        directory)):
            archive_path = os.path.relpath(path, current_path)
            found_file = False
            for file in (f for f in files if not looks_like_a_backup(f)):
                archive_file = os.path.join(archive_path, file)
                print archive_file
                zip_file.write(os.path.join(path, file), archive_file)
                found_file = True
            if not found_file:
                zip_file.writestr(os.path.join(archive_path,
                                               'placeholder.txt'),
                                  "(Empty directory)")
# Import arcpy module
import arcpy


# Local variables:
union = "\\\\hd.ad.syr.edu\\01\\e51673\\Documents\\Desktop\\Courses\\ERE693 GIS-Modeling\\Lab_09\\lab09Process.gdb\\union"
T6_N = "\\\\hd.ad.syr.edu\\01\\e51673\\Documents\\Desktop\\Courses\\ERE693 GIS-Modeling\\Lab_09\\lab09Process.gdb\\T6_N"
BMPs = "\\\\hd.ad.syr.edu\\01\\e51673\\Documents\\Desktop\\Courses\\ERE693 GIS-Modeling\\Lab_09\\Lab06Data.gdb\\BMPs"
T6_N_points = "\\\\hd.ad.syr.edu\\01\\e51673\\Documents\\Desktop\\Courses\\ERE693 GIS-Modeling\\Lab_09\\lab09Process.gdb\\T6_N_points"

# Process: Polygon to Raster
arcpy.PolygonToRaster_conversion(union, "TotalNitrogen", T6_N, "CELL_CENTER", "NONE", "40")

# Process: Point to Raster
arcpy.PointToRaster_conversion(BMPs, "TN_Eff_Ex", T6_N_points, "MOST_FREQUENT", "NONE", "40")

