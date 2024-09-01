import time
from playwright.sync_api import Playwright, sync_playwright, expect


# ф-я отладки вывода всех элементов 
def print_element(element, indent=0):
    """
    Рекурсивная функция для вывода элемента и всех его вложенных элементов.
    """
    # Выводим имя тега и класс элемента с отступами для вложенности
    print(" " * indent + f"<{element.tag_name} class='{element.get_attribute('class')}'>")
    
    # Получаем и выводим текстовое содержимое элемента, если оно есть
    text = element.text_content().strip()
    if text:
        print(" " * (indent + 2) + text)
    
    # Рекурсивно обходим все вложенные элементы
    children = element.query_selector_all(":scope > *")
    for child in children:
        print_element(child, indent + 2)
    
    # Закрываем тег после вывода всех вложенных элементов
    print(" " * indent + f"</{element.tag_name}>")


# Обычное тектовое поле 
class TypeSimpleInput:

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


# поле для заполнения и выбора 
class FieldToFillAndSelect:

    def __init__(self, title, departments):
        # self.departments = departments # список div на странице 
        self.title = title
        self.div, self.label, self.input_field = self.select_element(departments)

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

    def select_element(self, departments):
        for div in departments:
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

# поле для выбора 
class FieldToSelect:

    def __init__(self, title, departments):
        self.title = title
        self.div, self.label, self.input_field = self.select_element(departments)

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

    def select_element(self, departments):
        for div in departments:
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
# поле для выбора 


# Текстовое поле Код ФРМО 
class CodeFRMO(TypeSimpleInput):
    def __init__(self, departments):
        super().__init__(title = "Код ФРМО", departments = departments)

# Текстовое поле Наименование отделения
class FullNameDepartments(TypeSimpleInput):
    def __init__(self, departments):
        super().__init__(title = "Наименование отделения", departments = departments)

# Текстовое поле Краткое наименование
class ShortNameDepartments(TypeSimpleInput):
    def __init__(self, departments):
        super().__init__(title = "Краткое наименование", departments = departments)

# Текстовое поле Краткое наименование
class TypeDepartment(FieldToFillAndSelect):
    def __init__(self, departments):
        super().__init__(title = "Тип отделения", departments = departments)

# Текстовое поле Руководитель отделения
class DirectorOfDepartment(FieldToFillAndSelect):
    def __init__(self, departments):
        super().__init__(title = "Руководитель отделения", departments = departments)

# Текстовое поле И.О. Руководителя
class NameAndPatronymic(FieldToFillAndSelect):
    def __init__(self, departments):
        super().__init__(title = "И.О. Руководителя", departments = departments)

# Селектор подразделения 
class SelectDepartment(FieldToSelect):
    def __init__(self, departments):
        super().__init__(title = "Подразделение", departments = departments)

# Поля адреса 

# Текстовое поле почтового индекса
class AddrPostalCode(TypeSimpleInput):
    def __init__(self, departments):
        super().__init__(title = "Индекс", departments = departments)

# Поле для заполнения и выбора Регион
class AddrRegion(FieldToFillAndSelect):
    def __init__(self, departments):
        super().__init__(title = "Регион", departments = departments)

# Поле для заполнения и выбора Район
class AddrDistrict(FieldToFillAndSelect):
    def __init__(self, departments):
        super().__init__(title = "Район", departments = departments)

# Способ композиции 
class Departments:

    # def __init__(self, divs):
    #     self.divs = divs # список div на странице 


    def __init__(self, divs):
        # self.divs = page.query_selector_all('div')

        self.Code_FRMO = CodeFRMO(divs)

        self.Full_Name_Departments = FullNameDepartments(divs)

        self.Short_Name_Departments = ShortNameDepartments(divs)

        self.Type_Department = TypeDepartment(divs)

        self.Director_Of_Department = DirectorOfDepartment(divs)

        self.Name_And_Patronymic = NameAndPatronymic(divs)

        self.Select_Department = SelectDepartment(divs)

        self.Addr_Postal_Code = AddrPostalCode(divs)

        self.Addr_Region = AddrRegion(divs)

        self.Addr_District = AddrDistrict(divs)



    # departments = Departments(page = page)

    # departments.Code_FRMO.target()
    # departments.Code_FRMO.fill(text = "1.2.643.5.1.13.13.12.2.24.2081")
    # departments.Code_FRMO.clear()
