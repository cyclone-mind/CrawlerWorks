from DrissionPage import ChromiumPage, ChromiumOptions


co = ChromiumOptions()
co.headless(False)
browser = ChromiumPage(co)
tab = browser.new_tab()
tab.get('https://www.ccprec.com/projectSecPage/#/cqzspl')

button = tab.ele('.btn-next')
# page = tab.save()
# page_list = [page]
# for i in range(2):
#     button.click()
#     new_page = tab.save()
#     page_list.append(new_page)


def get_data():
    names_list = tab.eles('.el-table_1_column_1  bdName el-table__cell')
    start_end_date_list = tab.eles('.el-table_1_column_2   el-table__cell')
    print(names_list,start_end_date_list)
    for name,date in zip(names_list,start_end_date_list):
        title = name.text
        date = date.text
        start_date = date.split('--')[0]
        end_date = date.split('--')[1]
        print(title,start_date,end_date)

get_data()

for i in range(2):
    button.click()
    get_data()
