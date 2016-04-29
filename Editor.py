from Validator import *
from Person import *


class Editor(object):

    def __init__(self):
        self._raw_data = None
        self._good_data = {}

    def set_raw(self, new_data):
        self._raw_data = new_data

    def edit(self):
        while len(self._raw_data) > 0:
            s = self._raw_data[0]
            (print("Bad data: \n" + s))
            self.edit_or_delete(s)
        print ("All bad data has been handled")

    def edit_or_delete(self, a_string):
        i = input("Press 'E' to edit the data, press 'D' to delete it.\n")
        if i == 'E' or i == 'e':
            self.validate(a_string)
        elif i == 'D' or i == 'd':
            self.remove_from_raw(a_string)
        else:
            self.edit_or_delete(a_string)

    def remove_from_raw(self, the_string):
        if the_string in self._raw_data:
            self._raw_data.remove(the_string)

    def validate(self, a_string):
        list_ = Validator.clean_input(a_string)

        id_ = list_[0]
        if len(list_) > 1:
            gender = list_[1]
        else:
            gender = ""
        if len(list_) > 2:
            age = list_[2]
        else:
            age = ""
        if len(list_) > 3:
            sales = list_[3]
        else:
            sales = ""
        if len(list_) > 4:
            bmi = list_[4]
        else:
            bmi = ""
        if len(list_) > 5:
            income = list_[5]
        else:
            income = ""

        while not DataValidator.has_valid_id(id_):
            id_ = DataCleaner.clean_id(self.set_new_value(id_, "A123", "id"))

        while not DataValidator.has_valid_gender(gender):
            gender = DataCleaner.clean_gender(self.set_new_value(gender, "M", "gender"))

        while not DataValidator.has_valid_age(age):
            age = DataCleaner.clean_age(self.set_new_value(age, "01", "age"))

        while not DataValidator.has_valid_sales(sales):
            sales = DataCleaner.clean_sales(self.set_new_value(sales, "001", "sales"))

        while not DataValidator.has_valid_bmi(bmi):
            bmi = DataCleaner.clean_bmi(self.set_new_value(bmi, "Normal, Overweight, Obesity, Underweight", "bmi"))

        while not DataValidator.has_valid_income(income):
            income = DataCleaner.clean_income(self.set_new_value(income, "00-100", "income"))

        p = Person(DataCleaner.clean_id(id_), DataCleaner.clean_gender(gender), DataCleaner.clean_age(age), DataCleaner.clean_sales(sales), DataCleaner.clean_bmi(bmi), DataCleaner.clean_income(income))

        self._good_data.update({p.get_id(): p})
        self._raw_data.remove(a_string)

    def set_new_value(self, bad_input, correct_input, value):
        print("The current " + value + " is: " + bad_input)
        return input("The correct format is: " + correct_input + "\nSet a new " + value + ":\n")




    def export_good_data(self):
        return self._good_data

    def export_bad_data(self):
        return self._raw_data