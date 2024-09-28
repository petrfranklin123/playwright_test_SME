# поле для выбора 
import time
class DatePickerSimple:

    '''
    Существует 5 методов для взаимодействия 
    1) target - Нажатие по полю 
    2) clear_button - Очистка по крестику 
    3) select - Передается строка, по которой будет выполняться сравнение в выпадающем списке
    '''

    def __init__(self, title, dom, page):
        self.page = page
        self.title = title
        self.div, self.label, self.input_field, self.icon = self.select_element(dom)

    def target(self):
        self.input_field.click()

    def target_icon(self):
        self.icon.click()

    def fill(self, text):
        self.input_field.click()
        for key in text:
            self.input_field.press(key)

    def clear(self):
        self.input_field.fill("")

    def select_datepicker_today(self):
        self.input_field.fill("")
        self.input_field.click() # Вызов дейтпикера
        datepicker = self.page.wait_for_selector("div.mx-datepicker-content") # ждем появления дейтпикера 
        datepicker.query_selector("tbody >> td.cell.today").click() # выбираем сегодняшний день     

    def select_datepicker_target_date(self, target_date):
        self.input_field.fill("")
        self.input_field.click() # Вызов дейтпикера
        datepicker = self.page.wait_for_selector("div.mx-datepicker-content") # ждем появления дейтпикера 
        today = datepicker.query_selector("tbody >> td.cell.today") # выбираем сегодняшний день 

        back_year_button = datepicker.query_selector("button.mx-btn.mx-btn-text.mx-btn-icon-double-left")
        forward_year_button = datepicker.query_selector("button.mx-btn.mx-btn-text.mx-btn-icon-double-right")
        back_month_button = datepicker.query_selector("button.mx-btn.mx-btn-text.mx-btn-icon-left")
        forward_month_button = datepicker.query_selector("button.mx-btn.mx-btn-text.mx-btn-icon-right")


        today_split = today.get_attribute('title').split(".") 
        target_date_split = target_date.split(".")           
        difference = []                                      
        # Если -, то вперед, если + то назад
        for i, key in enumerate(today_split):
            difference.append(int(today_split[i]) - int(target_date_split[i]))

        # Если больше 0, то идем назад, если меньше - вперед 
        if difference[1] == 0:
            pass
        elif difference[1] > 0:
            for i in range(difference[1]):
                back_month_button.click()
        else:
            difference[1] = difference[1] * (-1)
            for i in range(difference[1]):
                forward_month_button.click()

        if difference[2] == 0:
            pass
        elif difference[2] > 0:
            for i in range(difference[2]):
                back_year_button.click()
        else:
            difference[2] = difference[2] * (-1)
            for i in range(difference[2]):
                forward_year_button.click() 

        # Выбор целевой даты в дейтпикере 
        target_date_from_datepicker = datepicker.query_selector(f"tbody >> td.cell[title='{target_date}']")
        target_date_from_datepicker.click()


    def select_element(self, dom):
        for div in dom:
            label = div.query_selector('label')
            if label:
                # Получим текст внутри тега label
                label_text = label.text_content()
                # Сравним его с заданным названием поля
                if self.title in label_text:
                    
                    # Найдём поле input и i
                    input_field = div.query_selector("input.mx-input")
                    icon = div.query_selector("i.mx-icon-calendar")

                    if input_field:
                        return div, label, input_field, icon
