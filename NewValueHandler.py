class NewValueHandler(object):

    @staticmethod
    def set_new_value():
        return input("Please set a new value:\n")



    @staticmethod
    def set_new_id(bad_input):
        print("The current ID value is: " + bad_input)
        print("The correct format is: 'A123'")
        NewValueHandler.set_new_value()

    @staticmethod
    def set_new_gender(bad_input):
        print("The current gender value is: " + bad_input)
        print("The correct options are: 'M' or 'F'")
        NewValueHandler.set_new_value()

    @staticmethod
    def set_new_age(bad_input):
        print("The current age value is: " + bad_input)
        print("The correct range is: 01 to 99")
        NewValueHandler.set_new_value()

    @staticmethod
    def set_new_sales(bad_input):
        print("The current sales value is: " + bad_input)
        print("The correct range is: 001 to 999")
        NewValueHandler.set_new_value()

    @staticmethod
    def set_new_bmi(bad_input):
        print("The current BMI value is: " + bad_input)
        print("The correct options are: Normal, Overweight, Obesity or Underweight")
        NewValueHandler.set_new_value()

    @staticmethod
    def set_new_income(bad_input):
        print("The current income value is: " + bad_input)
        print("The correct range is: 00-999")
        NewValueHandler.set_new_value()