import model as db


page = db.CMS.get_by_slug('/')
print(page)
print(page.text)