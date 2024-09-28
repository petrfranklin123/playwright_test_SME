class BackBtnHeader:

    '''
    Существует 1 метод для взаимодействия 
    1) click_btn - Нажатие по верхней кнопке 
    '''

    def __init__(self, dom):
        self.btn = self.select_element(dom)

    def click_btn(self):
        self.btn.click()

    def select_element(self, dom):
        for div in dom:
            btn = div.query_selector("div.block_page_header__btn-back >> a >> span")
            if btn:
                return btn
                # Получаем текстовое содержимое тега span
                span_text = btn.inner_text()

                # Сравниваем содержимое с требуемым текстом "Назад"
                if span_text == "Назад":
                    return btn
                else:
                    print(f"Текст в span: {span_text}. Ожидался: 'Назад'.")
            else:
                print("Элемент не найден")