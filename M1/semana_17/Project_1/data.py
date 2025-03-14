import csv
from logic import Rubric


def export_current_data_to_output_CSV(list_of_objs, csv_path):
    if(len(list_of_objs)):
        try:
            with open(csv_path, 'w', encoding='utf-8', newline='') as file:
                test_obj = list_of_objs[0]
                headers = test_obj.attributes_names
                writer = csv.writer(file)
                writer.writerow(headers)
                for obj in list_of_objs:
                    tmp_attributes_list = []
                    for header in headers:
                        tmp_attributes_list.append(str(getattr(obj, str(header))))
                    writer.writerow(tmp_attributes_list)
        except IOError:
            print(f'-E-(export_current_data_to_output_CSV): An error showed up while trying to write the csv file \'{csv_path}\''
                f'-I-(export_current_data_to_output_CSV): Please verify the output directory exists,' 
                f'and also check that the path for the file \'{csv_path}\' has write permissions.\n' 
                f'HINT: Write permissions can be affected if you are trying to write the file while'
                f'its already open by dome other program.'
            )
    else:
        print(f'-E-(export_current_data_to_output_CSV): No available objs data yet. Please introduce manually one or more objs, or import a CSV file before running this function.\n')


def import_existing_data_from_CSV(csv_path):
    rubrics_list = []
    try: 
        counter = 0
        with open(csv_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if(counter == 0):
                    counter += 1
                else:
                    name = row[0]
                    rubric_type = row[1]
                    category = row[2]
                    try:
                        amount = float(row[3])
                    except ValueError:
                        print(f"-E-(import_existing_data_from_CSV): Category '{name}' cannot be imported from cvs since its amount '{row[3]}' is not valid.")
                        continue
                    tmp_obj = Rubric(name, rubric_type, category, amount)
                    is_valid, error_message = tmp_obj.validate_rubric()
                    if is_valid:
                        rubrics_list.append(tmp_obj)
                        print(f"-I-(import_existing_data_from_CSV): {rubric_type} Category '{name}' imported successfully.")
                    else:
                        print(f"-E-(import_existing_data_from_CSV): Error adding {rubric_type}: {error_message}")
        return rubrics_list
    except IOError:
        print(f'-E-(import_existing_data_from_CSV): An error showed up while trying to read the csv file \'{csv_path}\''
              f'-I-(import_existing_data_from_CSV): Please verify that \'{csv_path}\' exists and is readable.\n'
        ) 