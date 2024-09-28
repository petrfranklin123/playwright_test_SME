class BtnBackAndSave:

    '''
    Существует 2 метода для взаимодействия 
    1) click_btn_back - Нажатие по верхней кнопке 
    2) click_btn_save - Нажатие по кнопке сохранения
    '''

    def __init__(self, dom):
        self.btn_back = self.select_element(
                locator = "div >> span", 
                text = "НАЗАД", 
                dom = dom
            )
        self.btn_save = self.select_element(
                locator = "div >> span", 
                text = "Сохранить", 
                dom = dom
            )

    def click_btn_back(self):
        self.btn_back.click()

    def click_btn_save(self):
        self.btn_save.click()

    def select_element(self, locator, text, dom):
        for div in dom:
            btn = div.query_selector(locator)
            if btn:
                # Получаем текстовое содержимое тега span
                span_text = btn.inner_text()
                print(f"Элемент {span_text} и {text}")
                # Сравниваем содержимое с требуемым текстом "Назад"
                if span_text == text:
                    return btn

        print(f"Элемент {text} не найден")