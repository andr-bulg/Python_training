import re
from random import randrange
from model.contact import Contact

def test_all_contact_fields_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_all_contacts_on_home_page(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    assert len(contact_from_home_page) == len(contact_from_db)

    contact_from_home_page = sorted(contact_from_home_page, key=Contact.id_or_max)
    contact_from_db = sorted(contact_from_db, key=Contact.id_or_max)
    assert contact_from_home_page == contact_from_db

    for i in range(len(contact_from_db)):
        assert contact_from_home_page[i].first_name == contact_from_db[i].first_name
        assert contact_from_home_page[i].last_name == contact_from_db[i].last_name
        assert contact_from_home_page[i].address == contact_from_db[i].address
        assert contact_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db[i])
        assert contact_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db[i])

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                    [contact.home_phone, contact.mobile_phone, contact.work_phone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                [contact.email_1, contact.email_2, contact.email_3])))

