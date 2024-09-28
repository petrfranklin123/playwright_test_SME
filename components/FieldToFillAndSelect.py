# поле для заполнения и выбора 
class FieldToFillAndSelect:

    '''
    Существует 5 методов для взаимодействия 
    1) target - Нажатие по полю 
    2) fill - Ввод текста и выбор первый элемент в списке 
    3) clear_button - Очистка по крестику 
    4) clear - Очистка пустой строкой 
    5) fill_not_selected - Ввод текста, без выбора из списка 
    '''

    def __init__(self, title, dom):
        # self.departments = departments # список div на странице 
        self.title = title
        self.div, self.label, self.input_field = self.select_element(dom)

    def target(self):
        self.input_field.click()
        # time.sleep(2)

    def fill(self, text):
        self.input_field.click() # Выбор текстового поля
        self.input_field.fill(text) # Заполнение тектового поля 
        arr_li = self.select_lis(self.div) # Выбор элементов списка
        arr_li[1].click() # Выбор первого элемента
        self.label.click() # Сброс таргета с поля 

    def clear_button(self):
        button = self.select_button(self.div)
        button.click()
        self.label.click()

    def clear(self):
        self.input_field.click() # Выбор текстового поля
        self.input_field.fill("") # Записываем пустую строку 
        self.label.click()

    def fill_not_selected(self, text):
        self.input_field.click() # Выбор текстового поля
        self.input_field.fill(text) # Заполнение тектового поля 
        # time.sleep(2)

    def select_lis(self, div):
        div.wait_for_selector("ul >> li", timeout=5000) # Ожидаем тег ul и появление в нем тегов li
        arr_li = div.query_selector_all("ul >> li")
        return arr_li

    def select_button(self, div):
        return div.query_selector('button')

    def select_element(self, dom):
        for div in dom:
            label = div.query_selector('label')
            if label:
                # Получим текст внутри тега label
                label_text = label.text_content()
                # Сравним его с заданным названием поля
                if self.title in label_text:
                    # Найдём input внутри второго div
                    input_field = div.query_selector('input')

                    if input_field:
                        return div, label, input_field

