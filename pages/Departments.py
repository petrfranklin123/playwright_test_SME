from components.FieldToFillAndSelect import FieldToFillAndSelect
from components.FieldToSelect import FieldToSelect
from components.TypeSimpleInput import TypeSimpleInput
from components.DatePickerSimple import DatePickerSimple


# Текстовое поле Код ФРМО 
class CodeFRMO(TypeSimpleInput):
    def __init__(self, departments):
        super().__init__(title = "Код ФРМО", dom = departments)

# Текстовое поле Наименование отделения
class FullName(TypeSimpleInput):
    def __init__(self, departments):
        super().__init__(title = "Наименование отделения", dom = departments)

# Текстовое поле Краткое наименование
class ShortName(TypeSimpleInput):
    def __init__(self, departments):
        super().__init__(title = "Краткое наименование", dom = departments)

# Селектор Тип отделения
class TypeDepartment(FieldToFillAndSelect):
    def __init__(self, departments):
        super().__init__(title = "Тип отделения", dom = departments)

# Селектор Руководитель отделения
class DirectorOfStructure(FieldToFillAndSelect):
    def __init__(self, departments):
        super().__init__(title = "Руководитель отделения", dom = departments)

# Селектор И.О. Руководителя
class NameAndPatronymic(FieldToFillAndSelect):
    def __init__(self, departments):
        super().__init__(title = "И.О. Руководителя", dom = departments)

# Селектор подразделения 
class SelectInstitutionBranch(FieldToSelect):
    def __init__(self, departments):
        super().__init__(title = "Подразделение", dom = departments)

# Поля адреса 

# Текстовое поле почтового индекса
class AddrPostalCode(TypeSimpleInput):
    def __init__(self, departments):
        super().__init__(title = "Индекс", dom = departments)

# Поле для заполнения и выбора Регион
class AddrRegion(FieldToFillAndSelect):
    def __init__(self, departments):
        super().__init__(title = "Регион", dom = departments)

# Поле для заполнения и выбора Район
class AddrDistrict(FieldToFillAndSelect):
    def __init__(self, departments):
        super().__init__(title = "Район", dom = departments)

# Поле для заполнения и выбора Город
class AddrCity(FieldToFillAndSelect):
    def __init__(self, departments):
        super().__init__(title = "Город", dom = departments)

# Поле для заполнения и выбора Населенный пункт
class AddrSettlement(FieldToFillAndSelect):
    def __init__(self, departments):
        super().__init__(title = "Населенный пункт", dom = departments)

# Поле для заполнения и выбора Второй населенный пункт
class AddrSettlementSecond(FieldToFillAndSelect):
    def __init__(self, departments):
        super().__init__(title = "Второй населенный пункт", dom = departments)

# Поле для заполнения и выбора Улица
class AddrStreet(FieldToFillAndSelect):
    def __init__(self, departments):
        super().__init__(title = "Улица", dom = departments)

# Поле для заполнения и выбора Дом
class AddrHouse(FieldToFillAndSelect):
    def __init__(self, departments):
        super().__init__(title = "Дом", dom = departments)

# Текстовое поле Строение
class AddrStructure(TypeSimpleInput):
    def __init__(self, departments):
        super().__init__(title = "Строение", dom = departments)

# Текстовое поле Корпус
class AddrFrame(TypeSimpleInput):
    def __init__(self, departments):
        super().__init__(title = "Корпус", dom = departments)

# Поля адреса 

# Текстовое поле Телефон
class PhoneStr(TypeSimpleInput):
    def __init__(self, departments):
        super().__init__(title = "Телефон", dom = departments)

# Текстовое поле Описание к теелфону
class DescribePhone(TypeSimpleInput):
    def __init__(self, departments):
        super().__init__(title = "Описание к телефону", dom = departments)

# Дейтпикер Дата создания
class DateCreation(DatePickerSimple):
    def __init__(self, departments, page):
        super().__init__(title = "Дата создания", dom = departments, page = page)





# Способ композиции 
class Departments:

    def __init__(self, page):

        # Ожидание того, пока не появится полностью адрес
        self.divs = self.wait_address_and_get_div(page)

        # иницализация всех объектов на странице 
        self.init_object_from_page(page)


    def wait_address_and_get_div(self, page): 
        
        page.goto("http://localhost/institution/departments/create")

        page.wait_for_selector("div.fias_background.fias_address >> div.justify-content-center", state='visible', timeout=5000) # 

        divs = page.query_selector_all('div') 

        return divs
    
    def init_object_from_page(self, page):

        self.Code_FRMO = CodeFRMO(self.divs)

        self.Full_Name = FullName(self.divs)

        self.Short_Name = ShortName(self.divs)

        self.Type_Department = TypeDepartment(self.divs)

        self.Director_Of_Structure = DirectorOfStructure(self.divs)

        self.Name_And_Patronymic = NameAndPatronymic(self.divs)

        self.Select_Institution_Branch = SelectInstitutionBranch(self.divs)

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

        self.Date_Creation = DateCreation(self.divs, page)