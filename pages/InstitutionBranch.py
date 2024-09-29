from components.FieldToFillAndSelect import FieldToFillAndSelect
from components.FieldToSelect import FieldToSelect
from components.TypeSimpleInput import TypeSimpleInput
from components.BtnBackAndSave import BtnBackAndSave

import time

# Текстовое поле Код ФРМО 
class CodeFRMO(TypeSimpleInput):
    def __init__(self, institution_branch):
        super().__init__(title = "Код ФРМО", dom = institution_branch)

# Текстовое поле Наименование подразделения
class FullName(TypeSimpleInput):
    def __init__(self, institution_branch):
        super().__init__(title = "Наименование подразделения", dom = institution_branch)

# Текстовое поле Краткое наименование
class ShortName(TypeSimpleInput):
    def __init__(self, institution_branch):
        super().__init__(title = "Краткое наименование", dom = institution_branch)

# Текстовое поле Руководитель подразделения 
class DirectorOfStructure(FieldToFillAndSelect):
    def __init__(self, institution_branch):
        super().__init__(title = "Руководитель подразделения", dom = institution_branch)

# Текстовое поле И.О. Руководителя
class NameAndPatronymic(FieldToFillAndSelect):
    def __init__(self, institution_branch):
        super().__init__(title = "И.О. Руководителя", dom = institution_branch)

# Поля адреса 

# Текстовое поле почтового индекса
class AddrPostalCode(TypeSimpleInput):
    def __init__(self, institution_branch):
        super().__init__(title = "Индекс", dom = institution_branch)

# Поле для заполнения и выбора Регион
class AddrRegion(FieldToFillAndSelect):
    def __init__(self, institution_branch):
        super().__init__(title = "Регион", dom = institution_branch)

# Поле для заполнения и выбора Район
class AddrDistrict(FieldToFillAndSelect):
    def __init__(self, institution_branch):
        super().__init__(title = "Район", dom = institution_branch)

# Поле для заполнения и выбора Город
class AddrCity(FieldToFillAndSelect):
    def __init__(self, institution_branch):
        super().__init__(title = "Город", dom = institution_branch)

# Поле для заполнения и выбора Населенный пункт
class AddrSettlement(FieldToFillAndSelect):
    def __init__(self, institution_branch):
        super().__init__(title = "Населенный пункт", dom = institution_branch)

# Поле для заполнения и выбора Второй населенный пункт
class AddrSettlementSecond(FieldToFillAndSelect):
    def __init__(self, institution_branch):
        super().__init__(title = "Второй населенный пункт", dom = institution_branch)

# Поле для заполнения и выбора Улица
class AddrStreet(FieldToFillAndSelect):
    def __init__(self, institution_branch):
        super().__init__(title = "Улица", dom = institution_branch)

# Поле для заполнения и выбора Дом
class AddrHouse(FieldToFillAndSelect):
    def __init__(self, institution_branch):
        super().__init__(title = "Дом", dom = institution_branch)

# Текстовое поле Строение
class AddrStructure(TypeSimpleInput):
    def __init__(self, institution_branch):
        super().__init__(title = "Строение", dom = institution_branch)

# Текстовое поле Корпус
class AddrFrame(TypeSimpleInput):
    def __init__(self, institution_branch):
        super().__init__(title = "Корпус", dom = institution_branch)

# Поля адреса 

# Текстовое поле Телефон
class PhoneStr(TypeSimpleInput):
    def __init__(self, institution_branch):
        super().__init__(title = "Телефон", dom = institution_branch)

# Текстовое поле Описание к теелфону
class DescribePhone(TypeSimpleInput):
    def __init__(self, institution_branch):
        super().__init__(title = "Описание к телефону", dom = institution_branch)

# Селектор Округа МО 
class DistrictsMo(FieldToSelect):
    def __init__(self, institution_branch):
        super().__init__(title = "Округа МО", dom = institution_branch)

# Селектор Подчиненность
class SubordinationMo(FieldToSelect):
    def __init__(self, institution_branch):
        super().__init__(title = "Подчиненность", dom = institution_branch)

# Кнопка Назад в шапке 
class BtnBackAndSaveForm(BtnBackAndSave):
    def __init__(self, institution_branch):
        super().__init__(dom = institution_branch)

        

# Способ композиции 
class InstitutionBranch:

    def __init__(self, page):

        # Ожидание того, пока не появится полностью адрес
        self.divs = self.wait_address_and_get_div(page)

        # иницализация всех объектов на странице 
        self.init_object_from_page()


    def wait_address_and_get_div(self, page): 

        page.goto("http://localhost/institution/branch/create")

        time.sleep(3)

        # page.wait_for_selector(".justify-content-center .d-flex.justify-content-between .fias-index.form-group", state='attached', timeout=5000) # 

        # address = page.locator(".justify-content-center .d-flex.justify-content-between").nth(2).wait_for(state="visible", timeout=3000)

        # # address.nth(2).wait_for(state="visible", timeout="3000")

        # locator = page.locator(".justify-content-center .d-flex.justify-content-between .fias-index.form-group")

        # # Дождаться, пока элемент появится в DOM
        # locator.wait_for(state="attached", timeout=10000)

        # # Дождаться, пока элемент станет видимым
        # locator.wait_for(state="visible", timeout=10000)





        divs = page.query_selector_all('div') 

        return divs
    
    def init_object_from_page(self):

        self.Code_FRMO = CodeFRMO(self.divs)

        self.Full_Name = FullName(self.divs)

        self.Short_Name = ShortName(self.divs)

        # self.Type_Department = TypeDepartment(self.divs)

        self.Director_Of_Structure = DirectorOfStructure(self.divs)

        self.Name_And_Patronymic = NameAndPatronymic(self.divs)

        self.Addr_Postal_Code = AddrPostalCode(self.divs)

        self.Addr_Region = AddrRegion(self.divs)

        self.Addr_District = AddrDistrict(self.divs)

        self.Addr_City = AddrCity(self.divs)

        self.Addr_Settlement = AddrSettlement(self.divs)

        self.Addr_Settlement_Second = AddrSettlementSecond(self.divs)

        self.Addr_Street = AddrStreet(self.divs)

        self.Addr_House = AddrHouse(self.divs)

        self.Addr_Structure = AddrStructure(self.divs)

        self.Addr_Frame = AddrFrame(self.divs)

        self.Phone_Str = PhoneStr(self.divs)

        self.Describe_Phone = DescribePhone(self.divs)

        self.Districts_Mo = DistrictsMo(self.divs)

        self.Subordination_Mo = SubordinationMo(self.divs)

        self.Btn_Back_And_Save_Form = BtnBackAndSaveForm(self.divs)