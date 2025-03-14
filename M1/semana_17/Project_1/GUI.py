import FreeSimpleGUI as sg # type: ignore
from logic import Rubric
from logic import transform_objects_list_to_table_data
from logic import get_categories_from_csv_data
from data import import_existing_data_from_CSV
from data import export_current_data_to_output_CSV

def create_main_window(): 
    csv_path = r'C:\Users\jodav\Documents\Curso_Progra_Lyfter\Lyfter-JosueNunez\M1\semana_17\Project_1\control.csv'
    data_obj_list = []
    data_from_csv = import_existing_data_from_CSV(csv_path)
    category_dict = {}
    if data_from_csv is not None:
        data_obj_list = data_from_csv
        category_dict = get_categories_from_csv_data(data_obj_list)
    BTN1 = sg.Button("Add Category", key='ADD_CATEGORY', size=(20, 1))
    BTN2 = sg.Button("Add Expense", key='ADD_EXPENSE', size=(20, 1))
    BTN3 = sg.Button("Add Income", key='ADD_INCOME', size=(20, 1))
    button_column = [[BTN1], [BTN2], [BTN3],]
    headings = ["   Category   ", "   Type   ", "   Rubric Name   ", "   Amount   "]
    data = transform_objects_list_to_table_data(data_obj_list)
    TBL1 = sg.Table(values=data, headings=headings, auto_size_columns=True, 
                display_row_numbers=True, justification='right', num_rows=10, 
                key='TABLE', size=(None, 200))
    layout = [[sg.Column(button_column), sg.VSeparator(), sg.Column([[TBL1]])]]
    WIN1 = sg.Window("Personal Finance Management System", layout, resizable=True)
    while True: 
        event, values = WIN1.read()
        tmp_categories = {}
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'ADD_CATEGORY':
            tmp_categories = (create_add_category_window())
            for tmp_cat in tmp_categories:
                category_dict[tmp_cat] = tmp_categories[tmp_cat]
        elif event == 'ADD_EXPENSE' or event == 'ADD_INCOME':
            if event == 'ADD_INCOME': 
                rubric_type = "Income" 
            else:
                rubric_type = "Expense"
            available_categories = [cat for cat, income_or_expense in category_dict.items() if income_or_expense == rubric_type]
            if available_categories:
                data_obj_list.extend(create_add_rubric_window(available_categories, rubric_type))
                data = transform_objects_list_to_table_data(data_obj_list)
                WIN1['TABLE'].update(values=data)
                export_current_data_to_output_CSV(data_obj_list, csv_path)
            else:
                sg.popup(f"-E-(create_main_window): Please add at least one category of type '{rubric_type}' before adding a new rubric.")


def create_add_category_window():
    LBL1 = sg.Text("Add a new category:")
    TXTBOX1 = sg.InputText(key='CATEGORY')
    layout_row_1 = [[LBL1], [TXTBOX1],]
    CHKBOX1 = sg.Checkbox("Income", key='CHKBOX1', enable_events=True)
    CHKBOX2 = sg.Checkbox("Expense", key='CHKBOX2', enable_events=True, default=True)
    BTN4 = sg.Button("Save")
    BTN5 = sg.Button("Cancel")
    layout_row_2 = [CHKBOX1, CHKBOX2, BTN4, BTN5]
    layout = [[layout_row_1], [layout_row_2]]
    WIN2 = sg.Window("Add Category", layout, modal=True)
    categories = {}
    while True:
        event, values = WIN2.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        elif event == 'CHKBOX2':
            if values['CHKBOX2']:
                WIN2['CHKBOX1'].update(value=False)
        elif event == 'CHKBOX1':
            if values['CHKBOX1']:
                WIN2['CHKBOX2'].update(value=False)
        elif event == "Save":
            if values['CHKBOX1']:
                new_type = "Income"
            else:
                new_type = "Expense"
            category = values['CATEGORY'].strip()
            if category:
                categories[category] = new_type
                sg.popup(f"-I-(create_add_category_window): Category '{category}' added successfully.")
            else:
                sg.popup("-E-(create_add_category_window): Category cannot be empty.")
    WIN2.Close()
    return categories


def create_add_rubric_window(data_for_drop_down_list, rubric_type):
    LBL2 = sg.Text(f"Add a new '{rubric_type}' type rubric:")
    TXTBOX2_EVENT_KEY = rubric_type.upper()
    TXTBOX2 = sg.InputText(key=TXTBOX2_EVENT_KEY, size=(54,1))
    LBL3 = sg.Text(f"Add the amount of the new {rubric_type}:")
    TXTBOX3 = sg.InputText(key='AMOUNT', size=(54,1))
    LBL4 = sg.Text(f"Select the category for the new {rubric_type}:")
    DROP_DOWN1 = sg.Combo(data_for_drop_down_list, key='DROP_DOWN', size=(16,1))
    BTN6 = sg.Button("Save")
    BTN7 = sg.Button("Cancel")
    layout_row_1 = [[LBL2], [TXTBOX2],]
    layout_row_2 = [[LBL3], [TXTBOX3],]
    layout_row_3 = [LBL4, sg.VSeparator(), DROP_DOWN1,]
    layout_row_4 = [BTN6, BTN7]
    layout = [[layout_row_1], [layout_row_2], [layout_row_3], [layout_row_4]]
    WIN3 = sg.Window(f"Add {rubric_type}", layout, modal=True)
    objs_list = []
    while True:
        event, values = WIN3.read()
        if event == sg.WINDOW_CLOSED or event == "Cancel":
            break
        if event == "Save":
            tmp_name = ''
            tmp_category = ''
            tmp_amount = 0
            if values[TXTBOX2_EVENT_KEY]:
                tmp_name = values[TXTBOX2_EVENT_KEY]
            if values['AMOUNT']:
                try:
                    tmp_amount = float(values['AMOUNT'])
                except ValueError:
                    sg.popup("-E-(create_add_rubric_window): Please provide a valid amount.")
                    continue
            if values['DROP_DOWN']:
                tmp_category = values['DROP_DOWN']
            tmp_obj = Rubric(tmp_name, rubric_type, tmp_category, tmp_amount)
            is_valid, error_message = tmp_obj.validate_rubric()
            if is_valid:
                objs_list.append(tmp_obj)
                sg.popup(f"-I-(create_add_rubric_window): Successfully added new rubric '{tmp_name}' as type '{rubric_type}'.")
            else:
                sg.popup(f"-E-(create_add_rubric_window): Error adding {rubric_type}: {error_message}")

    WIN3.close()
    return objs_list