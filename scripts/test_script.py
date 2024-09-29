from pages.Departments import Departments
from pages.InstitutionBranch import InstitutionBranch

import time

def test_institution_branch(page):
    institution_branch = InstitutionBranch(page = page)

    # institution_branch.Btn_Back_And_Save_Form.click_btn_save()
    # time.sleep(3)
    # institution_branch.Btn_Back_And_Save_Form.click_btn_back()
    # time.sleep(3)

    institution_branch.Code_FRMO.target()
    institution_branch.Code_FRMO.fill(text = "1.2.643.5.1.13.13.12.2.24.2081")
    institution_branch.Code_FRMO.clear()

    institution_branch.Full_Name.target()
    institution_branch.Full_Name.fill(text = "ПОЛНОЕ НАЗВАНИЕ")
    institution_branch.Full_Name.clear()

    institution_branch.Short_Name.target()
    institution_branch.Short_Name.fill(text = "КОРОТКОЕ НАЗВАНИЕ")
    institution_branch.Short_Name.clear()

    institution_branch.Director_Of_Structure.target()
    # time.sleep(1)
    institution_branch.Director_Of_Structure.fill(text = "Админ")
    # time.sleep(1)
    institution_branch.Director_Of_Structure.clear()
    # time.sleep(1)
    institution_branch.Director_Of_Structure.fill_not_selected(text = "Адм")
    # time.sleep(1)

    institution_branch.Name_And_Patronymic.target()
    # time.sleep(1)
    institution_branch.Name_And_Patronymic.fill(text = "Админ")
    # time.sleep(1)
    institution_branch.Name_And_Patronymic.clear()
    # time.sleep(1)
    institution_branch.Name_And_Patronymic.fill_not_selected(text = "Адм")
    # time.sleep(1)


#     institution_branch.Addr_Postal_Code.target()
#     # time.sleep(1)
#     institution_branch.Addr_Postal_Code.fill(text = "659220")
#     # time.sleep(1)
#     institution_branch.Addr_Postal_Code.clear()
#     # time.sleep(1)


#     institution_branch.Addr_Region.clear_button()
#     # time.sleep(1)
#     institution_branch.Addr_Region.target()
#     # time.sleep(1)
#     institution_branch.Addr_Region.fill(text = "Алтайский край")
#     # time.sleep(1)
#     institution_branch.Addr_Region.clear()
#     # time.sleep(1)
#     institution_branch.Addr_Region.fill_not_selected(text = "Барнаул")
#     # time.sleep(1)

#     institution_branch.Addr_District.target()
#     # time.sleep(1)
#     institution_branch.Addr_Region.fill(text = "Алтайский край")
#     # time.sleep(1)
#     institution_branch.Addr_District.fill(text = "р-н Бийский")
#     # time.sleep(1)
#     institution_branch.Addr_District.clear()
#     # time.sleep(1)
#     institution_branch.Addr_District.fill_not_selected(text = "Барнаул")
#     # time.sleep(1)

#     institution_branch.Addr_Region.fill(text = "Алтайский край")
#     # time.sleep(1)
#     institution_branch.Addr_District.fill(text = "р-н Бийский")
#     # time.sleep(1)
#     institution_branch.Addr_City.target()
#     # time.sleep(1)
#     institution_branch.Addr_City.fill_not_selected(text = "Бийск")
#     # time.sleep(1)

#     institution_branch.Addr_City.clear()
#     # time.sleep(1)
#     institution_branch.Addr_District.clear()
#     time.sleep(1)
#     institution_branch.Addr_City.fill(text = "Барнаул")
#     # time.sleep(1)
#     institution_branch.Addr_City.clear_button()
#     # time.sleep(1)

#     institution_branch.Addr_District.fill(text = "р-н Бийский")
#     time.sleep(1)
#     institution_branch.Addr_Settlement.fill(text = "снт Радуга")
#     time.sleep(1)
#     institution_branch.Addr_Settlement.clear_button()
#     time.sleep(1)

#     institution_branch.Addr_Settlement.fill_not_selected(text = "Нас пункт")
#     time.sleep(1)
#     institution_branch.Addr_Settlement.clear()
#     time.sleep(1)


#     institution_branch.Addr_Settlement_Second.target()
#     time.sleep(1)
#     institution_branch.Addr_Settlement_Second.fill_not_selected(text = "Второй населенный пункт")
#     time.sleep(1)
#     institution_branch.Addr_Settlement_Second.clear()
#     time.sleep(1)


#     institution_branch.Addr_District.clear()
#     time.sleep(1)
#     institution_branch.Addr_City.fill(text = "Барнаул")
#     time.sleep(1)
#     institution_branch.Addr_Street.fill(text = "ул Модельная")
#     time.sleep(1)
#     institution_branch.Addr_Street.clear_button()
#     time.sleep(1)

#     institution_branch.Addr_Street.fill_not_selected(text = "Название улицы")
#     time.sleep(1)
#     institution_branch.Addr_Street.clear()
#     time.sleep(1)


#     institution_branch.Addr_Region.fill(text = "Алтайский край")
#     time.sleep(1)
#     institution_branch.Addr_City.fill(text = "Барнаул")
#     time.sleep(1)
#     institution_branch.Addr_Street.fill(text = "ул Модельная")
#     time.sleep(1)
#     institution_branch.Addr_House.fill(text = "9")
#     time.sleep(1)
#     institution_branch.Addr_House.clear_button()
#     time.sleep(1)

#     institution_branch.Addr_House.fill_not_selected(text = "ДОМ 10")
#     time.sleep(1)
#     institution_branch.Addr_House.clear()
#     time.sleep(1)

#     institution_branch.Addr_Structure.target()
#     time.sleep(1)
#     institution_branch.Addr_Structure.fill(text = "Строение")
#     time.sleep(1)
#     institution_branch.Addr_Structure.clear()
#     time.sleep(1)

#     institution_branch.Addr_Frame.target()
#     time.sleep(1)
#     institution_branch.Addr_Frame.fill(text = "Корпус")
#     time.sleep(1)
#     institution_branch.Addr_Frame.clear()


#     institution_branch.Phone_Str.target()
#     time.sleep(1)
#     institution_branch.Phone_Str.fill(text = "89994769999")
#     time.sleep(1)
#     institution_branch.Phone_Str.clear()
#     time.sleep(1)

#     institution_branch.Describe_Phone.target()
#     time.sleep(1)
#     institution_branch.Describe_Phone.fill(text = "Описание телефона")
#     time.sleep(1)
#     institution_branch.Describe_Phone.clear()
#     time.sleep(1)

#     institution_branch.Districts_Mo.target()
#     # time.sleep(3)
#     institution_branch.Districts_Mo.select("Бийск")
#     # time.sleep(3)
#     institution_branch.Districts_Mo.clear_button()
#     # time.sleep(3)

#     institution_branch.Subordination_Mo.target()
#     # time.sleep(3)
#     institution_branch.Subordination_Mo.select("Федеральная")
#     # time.sleep(3)
#     institution_branch.Subordination_Mo.clear_button()
#     # time.sleep(3)




# def test_departments(page):
#     departments = Departments(page = page)

#     departments.Date_Creation.target()
#     time.sleep(2)
#     departments.Date_Creation.target_icon()
#     time.sleep(2)
#     departments.Date_Creation.fill(text = "12.12.1999")
#     time.sleep(2)
#     departments.Date_Creation.clear()
#     time.sleep(2)
#     departments.Date_Creation.select_datepicker_target_date("05.01.2030")
#     time.sleep(2)
#     departments.Date_Creation.select_datepicker_today()
#     time.sleep(2)
    

#     # Рабочие 

#     departments.Code_FRMO.target()
#     departments.Code_FRMO.fill(text = "1.2.643.5.1.13.13.12.2.24.2081")
#     departments.Code_FRMO.clear()

#     departments.Full_Name.target()
#     departments.Full_Name.fill(text = "ПОЛНОЕ НАЗВАНИЕ")
#     departments.Full_Name.clear()

#     departments.Short_Name.target()
#     departments.Short_Name.fill(text = "КОРОТКОЕ НАЗВАНИЕ")
#     departments.Short_Name.clear()

#     departments.Type_Department.target()
#     # time.sleep(1)
#     departments.Type_Department.fill(text = "Отделение лабораторное")
#     # time.sleep(1)
#     departments.Type_Department.clear()
#     # time.sleep(1)
#     departments.Type_Department.fill_not_selected(text = "Отделение")
#     # time.sleep(1)

#     departments.Director_Of_Structure.target()
#     # time.sleep(1)
#     departments.Director_Of_Structure.fill(text = "Админ")
#     # time.sleep(1)
#     departments.Director_Of_Structure.clear()
#     # time.sleep(1)
#     departments.Director_Of_Structure.fill_not_selected(text = "Адм")
#     # time.sleep(1)

#     departments.Name_And_Patronymic.target()
#     # time.sleep(1)
#     departments.Name_And_Patronymic.fill(text = "Админ")
#     # time.sleep(1)
#     departments.Name_And_Patronymic.clear()
#     # time.sleep(1)
#     departments.Name_And_Patronymic.fill_not_selected(text = "Адм")
#     # time.sleep(1)

#     departments.Select_Institution_Branch.target()
#     # time.sleep(3)
#     departments.Select_Institution_Branch.select("Подразделение новое 1 полное ред")
#     # time.sleep(3)
#     departments.Select_Institution_Branch.clear_button()
#     # time.sleep(3)


#     departments.Addr_Postal_Code.target()
#     # time.sleep(1)
#     departments.Addr_Postal_Code.fill(text = "659220")
#     # time.sleep(1)
#     departments.Addr_Postal_Code.clear()
#     # time.sleep(1)


#     departments.Addr_Region.clear_button()
#     # time.sleep(1)
#     departments.Addr_Region.target()
#     # time.sleep(1)
#     departments.Addr_Region.fill(text = "Алтайский край")
#     # time.sleep(1)
#     departments.Addr_Region.clear()
#     # time.sleep(1)
#     departments.Addr_Region.fill_not_selected(text = "Барнаул")
#     # time.sleep(1)

#     departments.Addr_District.target()
#     # time.sleep(1)
#     departments.Addr_Region.fill(text = "Алтайский край")
#     # time.sleep(1)
#     departments.Addr_District.fill(text = "р-н Бийский")
#     # time.sleep(1)
#     departments.Addr_District.clear()
#     # time.sleep(1)
#     departments.Addr_District.fill_not_selected(text = "Барнаул")
#     # time.sleep(1)

#     departments.Addr_Region.fill(text = "Алтайский край")
#     # time.sleep(1)
#     departments.Addr_District.fill(text = "р-н Бийский")
#     # time.sleep(1)
#     departments.Addr_City.target()
#     # time.sleep(1)
#     departments.Addr_City.fill_not_selected(text = "Бийск")
#     # time.sleep(1)

#     departments.Addr_City.clear()
#     # time.sleep(1)
#     departments.Addr_District.clear()
#     time.sleep(1)
#     departments.Addr_City.fill(text = "Барнаул")
#     # time.sleep(1)
#     departments.Addr_City.clear_button()
#     # time.sleep(1)

#     departments.Addr_District.fill(text = "р-н Бийский")
#     time.sleep(1)
#     departments.Addr_Settlement.fill(text = "снт Радуга")
#     time.sleep(1)
#     departments.Addr_Settlement.clear_button()
#     time.sleep(1)

#     departments.Addr_Settlement.fill_not_selected(text = "Нас пункт")
#     time.sleep(1)
#     departments.Addr_Settlement.clear()
#     time.sleep(1)


#     departments.Addr_Settlement_Second.target()
#     time.sleep(1)
#     departments.Addr_Settlement_Second.fill_not_selected(text = "Второй населенный пункт")
#     time.sleep(1)
#     departments.Addr_Settlement_Second.clear()
#     time.sleep(1)


#     departments.Addr_District.clear()
#     time.sleep(1)
#     departments.Addr_City.fill(text = "Барнаул")
#     time.sleep(1)
#     departments.Addr_Street.fill(text = "ул Модельная")
#     time.sleep(1)
#     departments.Addr_Street.clear_button()
#     time.sleep(1)

#     departments.Addr_Street.fill_not_selected(text = "Название улицы")
#     time.sleep(1)
#     departments.Addr_Street.clear()
#     time.sleep(1)


#     departments.Addr_Region.fill(text = "Алтайский край")
#     time.sleep(1)
#     departments.Addr_City.fill(text = "Барнаул")
#     time.sleep(1)
#     departments.Addr_Street.fill(text = "ул Модельная")
#     time.sleep(1)
#     departments.Addr_House.fill(text = "9")
#     time.sleep(1)
#     departments.Addr_House.clear_button()
#     time.sleep(1)

#     departments.Addr_House.fill_not_selected(text = "ДОМ 10")
#     time.sleep(1)
#     departments.Addr_House.clear()
#     time.sleep(1)

#     departments.Addr_Structure.target()
#     time.sleep(1)
#     departments.Addr_Structure.fill(text = "Строение")
#     time.sleep(1)
#     departments.Addr_Structure.clear()
#     time.sleep(1)

#     departments.Addr_Frame.target()
#     time.sleep(1)
#     departments.Addr_Frame.fill(text = "Корпус")
#     time.sleep(1)
#     departments.Addr_Frame.clear()


#     departments.Phone_Str.target()
#     time.sleep(1)
#     departments.Phone_Str.fill(text = "89994769999")
#     time.sleep(1)
#     departments.Phone_Str.clear()
#     time.sleep(1)

#     departments.Describe_Phone.target()
#     time.sleep(1)
#     departments.Describe_Phone.fill(text = "Описание телефона")
#     time.sleep(1)
#     departments.Describe_Phone.clear()
#     time.sleep(1)


    # Рабочие 