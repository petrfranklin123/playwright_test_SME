class DatePickerSimple:

    '''
    Существует 1 метод для взаимодействия 
    1) click_btn - Нажатие по верхней кнопке 
    '''

    def __init__(self, dom):
        self.btn = self.select_element(dom)

    def click_btn(self):
        self.btn.click()

    def select_element(self, dom):
        # return dom.query_selector("button >> span", has_text="Сохранить")
        
        for div in dom:
            btn = div.query_selector("button >> span")
            if btn:
                return btn
                # Получаем текстовое содержимое тега span
                span_text = btn.inner_text()

                # Сравниваем содержимое с требуемым текстом "Сохранить"
                if span_text == "Сохранить":
                    return btn
                else:
                    print(f"Текст в span: {span_text}. Ожидался: 'Назад'.")
            else:
                print("Элемент не найден")