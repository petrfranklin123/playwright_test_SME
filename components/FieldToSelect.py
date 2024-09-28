# поле для выбора 
class FieldToSelect:

    '''
    Существует 5 методов для взаимодействия 
    1) target - Нажатие по полю 
    2) clear_button - Очистка по крестику 
    3) select - Передается строка, по которой будет выполняться сравнение в выпадающем списке
    '''

    def __init__(self, title, dom):
        self.title = title
        self.div, self.label, self.input_field = self.select_element(dom)

    def target(self):
        self.input_field.click()

    def select(self, search_string):
        self.input_field.click()
        arr_li = self.select_lis(self.div) # Выбор элементов списка
        arr_li[self.search_item(arr_li, search_string)].click() # Выбор элемента по совпадению 
        self.label.click() # Сброс таргета с поля 

    def clear_button(self):
        button = self.select_button(self.div)
        button.click()
        self.label.click()

    def search_item(self, arr_li, search_string):
        for i, s in enumerate(arr_li):
            if search_string in s.text_content():
                return i
        return 0 # если нет совпадения, то выбираем первый элемент


    def select_lis(self, div):
        self.input_field.click() # таргет по селектору, чтобы получить список
        ul = div.query_selector("div.select-area >> div:nth-child(2)")
        if ul:
            arr_li = ul.query_selector_all('div')
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
                    
                    # Найдём поле 
                    input_field = div.query_selector("div.select-area")

                    if input_field:
                        return div, label, input_field
