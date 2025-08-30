from playwright.sync_api import Page

# get Veg - Rice and Price 37
#identify

def test_webtable_handle(page : Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    row_Text1 = page.locator("//table[@name='BookTable']/tbody/tr[6]/td[1]").inner_text()
    print(row_Text1)

    row_Text4 = page.locator("//table[@name='BookTable']/tbody/tr[6]/td[4]").inner_text()
    print(row_Text4)

def test_all_rowsCompare(page:Page):
    global book_name
    page.goto("https://testautomationpractice.blogspot.com/")

    # Get all rows
    all_rows = page.locator("//table[@name='BookTable']/tbody/tr").count()
    for i in range(all_rows):
    # Get text from the 2nd column (Book Name column)
        book_name = page.locator(f"//table[@name='BookTable']/tbody/tr[{i + 1}]/td[1]").inner_text()
    if book_name == "Master In Java":
        print("Found:", book_name)





