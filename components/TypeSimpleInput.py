# Обычное тектовое поле 
class TypeSimpleInput:

    '''
    Существует 5 методов для взаимодействия 
    1) target - Нажатие по полю 
    2) fill - Ввод текста
    3) clear - Очистка пустой строкой 
    '''

    def __init__(self, title, departments):
        self.title = title
        self.input_field = self.select_element(departments)

    def target(self):
        self.input_field.click()
        # time.sleep(2)

    def fill(self, text):
        self.input_field.fill(text)
        # time.sleep(2)

    def clear(self):
        self.input_field.fill("")
        # time.sleep(2)


    def select_element(self, departments):
        # for div in departments.divs:
        for div in departments:
            label = div.query_selector('label')
            if label:
                # Получим текст внутри тега span
                label_text = label.text_content()
                # Сравним его с заданным названием поля
                if self.title in label_text:
                    # Найдём input внутри второго div
                    input_field = div.query_selector('input')
                    if input_field:
                        return input_field
