
import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect

from class_departments import Departments, CodeFRMO, FullNameDepartments, ShortNameDepartments, TypeDepartment, DirectorOfDepartment, NameAndPatronymic


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://davinci/login")
    page.get_by_placeholder("Введите Email").click()
    page.get_by_placeholder("Введите Email").fill("admin@mirmis.ru")
    page.get_by_placeholder("Введите пароль").click()
    page.get_by_placeholder("Введите пароль").fill("12345678")
    page.get_by_role("button", name="Войти").click()
    # page.get_by_role("link", name="Отделения").click()

    page.goto("http://davinci/institution/departments/create")

    # Найдём все элементы div, содержащие span и input
    divs = page.query_selector_all('div')
    field_found = False

    departments = Departments(divs = divs)

    # Рабочие 

    # departments.Code_FRMO.target()
    # departments.Code_FRMO.fill(text = "1.2.643.5.1.13.13.12.2.24.2081")
    # departments.Code_FRMO.clear()

    # departments.Full_Name_Departments.target()
    # departments.Full_Name_Departments.fill(text = "ПОЛНОЕ НАЗВАНИЕ")
    # departments.Full_Name_Departments.clear()

    # departments.Short_Name_Departments.target()
    # departments.Short_Name_Departments.fill(text = "КОРОТКОЕ НАЗВАНИЕ")
    # departments.Short_Name_Departments.clear()

    # departments.Type_Department.target()
    # time.sleep(1)
    # departments.Type_Department.fill(text = "Отделение лабораторное")
    # time.sleep(1)
    # departments.Type_Department.clear()
    # time.sleep(1)
    # departments.Type_Department.fill_not_selected(text = "Отделение")
    # time.sleep(1)

    # departments.Director_Of_Department.target()
    # time.sleep(1)
    # departments.Director_Of_Department.fill(text = "Админ")
    # time.sleep(1)
    # departments.Director_Of_Department.clear()
    # time.sleep(1)
    # departments.Director_Of_Department.fill_not_selected(text = "Адм")
    # time.sleep(1)

    # departments.Name_And_Patronymic.target()
    # time.sleep(1)
    # departments.Name_And_Patronymic.fill(text = "Админ")
    # time.sleep(1)
    # departments.Name_And_Patronymic.clear()
    # time.sleep(1)
    # departments.Name_And_Patronymic.fill_not_selected(text = "Адм")
    # time.sleep(1)

    # Рабочие 

    departments.Select_Department.target()
    time.sleep(1)
    # # departments.Select_Department.fill(text = "Админ")
    # time.sleep(1)
    # # departments.Select_Department.clear()
    # time.sleep(1)
    # # departments.Select_Department.fill_not_selected(text = "Адм")
    # time.sleep(1)



    # code_frmo = CodeFRMO(page_departments)
    # code_frmo.target()
    # code_frmo.fill(text = "1.2.643.5.1.13.13.12.2.24.2081")
    # code_frmo.clear()

    # full_name_departments = FullNameDepartments(page_departments)
    # full_name_departments.target()
    # full_name_departments.fill(text = "Наименование отделения")
    # full_name_departments.clear()

    # short_name_departments = ShortNameDepartments(page_departments)
    # short_name_departments.target()
    # short_name_departments.fill(text = "Краткое наименование")
    # short_name_departments.clear()

    # type_department = TypeDepartment(page_departments)
    # type_department.target()
    # type_department.fill(text = "Отделение лабораторное")
    # type_department.clear()
    # type_department.fill_not_selected(text = "Отделение")

    # type_department = DirectorOfDepartment(page_departments)
    # type_department.target()
    # type_department.fill(text = "Админ")
    # type_department.clear()
    # type_department.fill_not_selected(text = "Адм")

    # type_department = NameAndPatronymic(page_departments)
    # type_department.target()
    # type_department.fill(text = "Админ")
    # type_department.clear()
    # type_department.fill_not_selected(text = "Адм")


    context.close()

    browser.close()


with sync_playwright() as playwright:
    run(playwright)

