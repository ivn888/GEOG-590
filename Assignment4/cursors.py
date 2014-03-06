import arcpy
import os

def add_field(fc, field_name, field_type="TEXT"):
    arcpy.AddField_management(in_table=fc, field_name=field_name, field_type=field_type)
    return ''

def add_id(fc, id_field, starting_index):
    add_field(fc, id_field, "LONG")
    

def combine_feature_classes(path, output_name = "output.shp"):
    arcpy.env.workspace = path
    all_feature_classes = arcpy.ListFeatureClasses()
    if len(all_feature_classes) == 0:
        return
    if len([ f for f in all_feature_classes if f[:len(output_name)].lower() == output_name.lower()]) == 0:
        arcpy.CreateFeatureclass_management(out_path=path, out_name=output_name, template=all_feature_classes[0])
        add_field(output_name, "Source_FC")
    
    output_rows = arcpy.InsertCursor(output_name)
    for fc in all_feature_classes:
        print 'Copying', fc
        src_fields = [ f for f in arcpy.ListFields(fc) if f.editable ]
        src_rows = arcpy.SearchCursor(fc)
        
        for src_row in src_rows:
            output_row = output_rows.newRow()
            for field in src_fields:
                output_row.setValue(field.name, src_row.getValue(field.name))
            output_row.setValue('Source_FC', os.path.splitext(str(fc))[0])
            output_rows.insertRow(output_row)

        src = os.path.splitext(str(fc))[0]

    return output_name

if __name__ == '__main__':
    combine_feature_classes('C:/users/jroebuck/projects/geog-590/assignment4', "output.shp", 1000)