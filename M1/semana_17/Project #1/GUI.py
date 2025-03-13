import FreeSimpleGUI as sg # type: ignore
from logica import Rubro
from logica import transform_objects_list_to_table_data


def create_main_window(): 
    data_obj_list = []
    BTN1 = sg.Button("Agregar Categoria", key='ADD_CATEGORY', size=(20, 1))
    BTN2 = sg.Button("Agregar Gasto", key='ADD_EXPENSE', size=(20, 1))
    BTN3 = sg.Button("Agregar Ingreso", key='ADD_INCOME', size=(20, 1))
    button_column = [[BTN1], [BTN2], [BTN3],]
    headings = ["   Rubro   ", "   Tipo   ", "   Categoria   ", "   Monto   "]
    data = transform_objects_list_to_table_data(data_obj_list)
    TBL1 = sg.Table(values=data, headings=headings, auto_size_columns=True, 
                display_row_numbers=True, justification='right', num_rows=10, 
                key='TABLE', size=(None, 200))
    layout = [[sg.Column(button_column), sg.VSeparator(), sg.Column([[TBL1]])]]
    WIN1 = sg.Window("Gestion de Finanzas Personales", layout, resizable=True)
    category_dict = {}
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
                rubric_type = "Ingreso" 
            else:
                rubric_type = "Gasto"
            available_categories = [cat for cat, income_or_expense in category_dict.items() if income_or_expense == rubric_type]
            if available_categories:
                data_obj_list.extend(create_add_rubric_window(available_categories, rubric_type))
                data = transform_objects_list_to_table_data(data_obj_list)
                WIN1['TABLE'].update(values=data)
            else:
                sg.popup(f"Error: Por favor agregue almenos una categoria antes de añadir un rubro tipo '{rubric_type}'.")


def create_add_category_window():
    LBL1 = sg.Text("Ingrese una nueva categoria:")
    TXTBOX1 = sg.InputText(key='CATEGORY')
    layout_row_1 = [[LBL1], [TXTBOX1],]
    CHKBOX1 = sg.Checkbox("Ingreso", key='CHKBOX1', enable_events=True)
    CHKBOX2 = sg.Checkbox("Gasto", key='CHKBOX2', enable_events=True, default=True)
    BTN4 = sg.Button("Guardar")
    BTN5 = sg.Button("Cancelar")
    layout_row_2 = [CHKBOX1, CHKBOX2, BTN4, BTN5]
    layout = [[layout_row_1], [layout_row_2]]
    WIN2 = sg.Window("Agregar Categoria", layout, modal=True)
    categories = {}
    while True:
        event, values = WIN2.read()
        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            break
        elif event == 'CHKBOX2':
            if values['CHKBOX2']:
                WIN2['CHKBOX1'].update(value=False)
        elif event == 'CHKBOX1':
            if values['CHKBOX1']:
                WIN2['CHKBOX2'].update(value=False)
        elif event == "Guardar":
            if values['CHKBOX1']:
                new_type = "Ingreso"
            else:
                new_type = "Gasto"
            category = values['CATEGORY'].strip()
            if category:
                categories[category] = new_type
                sg.popup(f"Categoria '{category}' agregada.")
            else:
                sg.popup("Error agregando categoria: La categoria no puede estar vacia.")
    WIN2.Close()
    return categories


def create_add_rubric_window(data_for_drop_down_list, rubric_type):
    LBL2 = sg.Text(f"Ingrese un nuevo rubro de tipo '{rubric_type}':")
    TXTBOX2_EVENT_KEY = rubric_type.upper()
    TXTBOX2 = sg.InputText(key=TXTBOX2_EVENT_KEY, size=(54,1))
    LBL3 = sg.Text(f"Monto del nuevo {rubric_type}:")
    TXTBOX3 = sg.InputText(key='AMOUNT', size=(54,1))
    LBL4 = sg.Text(f"Seleccionar categoria del nuevo {rubric_type}:")
    DROP_DOWN1 = sg.Combo(data_for_drop_down_list, key='DROP_DOWN', size=(16,1))
    BTN6 = sg.Button("Guardar")
    BTN7 = sg.Button("Cancelar")
    layout_row_1 = [[LBL2], [TXTBOX2],]
    layout_row_2 = [[LBL3], [TXTBOX3],]
    layout_row_3 = [LBL4, sg.VSeparator(), DROP_DOWN1,]
    layout_row_4 = [BTN6, BTN7]
    layout = [[layout_row_1], [layout_row_2], [layout_row_3], [layout_row_4]]
    WIN3 = sg.Window(f"Agregar {rubric_type}", layout, modal=True)
    objs_list = []
    while True:
        event, values = WIN3.read()
        if event == sg.WINDOW_CLOSED or event == "Cancelar":
            break
        if event == "Guardar":
            tmp_name = ''
            tmp_category = ''
            tmp_amount = 0
            if values[TXTBOX2_EVENT_KEY]:
                tmp_name = values[TXTBOX2_EVENT_KEY]
            if values['AMOUNT']:
                try:
                    tmp_amount = float(values['AMOUNT'])
                except ValueError:
                    sg.popup("Error: por favor ingrese un monto valido.")
                    continue
            if values['DROP_DOWN']:
                tmp_category = values['DROP_DOWN']
            tmp_obj = Rubro(tmp_category, rubric_type, tmp_name, tmp_amount)
            is_valid, error_message = tmp_obj.validar_rubro()
            if is_valid:
                objs_list.append(tmp_obj)
                sg.popup(f"{rubric_type} '{tmp_name}' agregado.")
            else:
                sg.popup(f"Error adding {rubric_type}: {error_message}")

    WIN3.close()
    return objs_list


create_main_window()