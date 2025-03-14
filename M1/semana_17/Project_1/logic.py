class Rubric:


    def __init__(self, name="", rubric_type="", category="", amount=0):
        self.name = name
        self.rubric_type = rubric_type
        self.category = category
        self.amount = amount
        self.attributes_names = ('name', 
                                'rubric_type', 
                                'category', 
                                'amount')


    def __str__(self):
        return f"{self.name} ({self.rubric_type}): {self.category} - ${self.amount:.2f}"


    def validate_rubric(self):
        if not self.name:
            return False, "-E-(validate_rubric): Rubric's name cannot be empty."
        if self.rubric_type not in ['Expense', 'Income']:
            return False, "-E-(validate_rubric): Rubric's type must be 'Expense' or 'Income'."
        if not self.category:
            return False, "-E-(validate_rubric): Category cannot be empty."
        if self.amount <= 0: 
            return False, "-E-(validate_rubric): Amount must be greater than zero."
        return True, "-I-(validate_rubric): Valid rubric."
    

    def update_amount(self, new_amount):
        if new_amount > 0:
            old_amount = self.amount
            self.amount = new_amount
            return True, f"-I-(update_amount): Amount for rubric {self.name} updated correctly from '{old_amount}' to '{new_amount}'."
        else:
            return False, f"-E-(update_amount): Amount must be greater than zero."


    def update_category(self, new_category):
        if new_category:
            old_category = new_category
            self.category = new_category
            return True, f"-I-(update_category): Category updated correctly from '{old_category}' to '{new_category}'."
        else:
            return False, "-E-(update_category): Category can not be empty."
    

    def is_expense(self):
        return self.rubric_type == 'Expense'


    def is_income(self):
        return self.rubric_type == 'Income'


def transform_objects_list_to_table_data(data_obj_list):
    if data_obj_list is not None and len(data_obj_list):
        return [[obj.category, obj.rubric_type, obj.name, obj.amount] for obj in data_obj_list]
    else:
        return []
    
def get_categories_from_csv_data(data_obj_list):
    if data_obj_list is not None and len(data_obj_list):
        return {obj.category:obj.rubric_type for obj in data_obj_list}
    else:
        return {}
