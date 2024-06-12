from pytest_bdd import given, when, then, parsers
from model.contact import Contact
import random

@given('a contact list', target_fixture='contact_list')
def contact_list(db):
    return db.get_contact_list()

@given(parsers.parse('a contact with {first_name}, {last_name} and {address}'), target_fixture='new_contact')
def new_contact(first_name, last_name, address):
    return Contact(first_name=first_name, last_name=last_name, address=address)

@when('I add the contact to the list')
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)

@then('the new contact list is equal to the old list with the added contact')
def verify_contact_added(db, contact_list, new_contact):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

@given('a non-empty contact list', target_fixture='non_empty_contact_list')
def non_empty_contact_list(app, db):
    if not db.get_contact_list():
        app.contact.create(Contact(first_name="temp_first_name", last_name="temp_last_name", address="temp_address"))
    return db.get_contact_list()

@given('a random contact from the list', target_fixture='random_contact')
def random_contact(non_empty_contact_list):
    return random.choice(non_empty_contact_list)

@when('I delete the contact from the list')
def delete_contact(app, random_contact):
    app.contact.delete_contact_by_id(random_contact.id_contact)

@then('the new contact list is equal to the old list without the deleted contact')
def verify_contact_deleted(app, db, check_ui, non_empty_contact_list, random_contact):
    old_contacts = non_empty_contact_list
    new_contacts = db.get_contact_list()
    old_contacts.remove(random_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

@when('I modify the contact from the list', target_fixture='modified_contact')
def modified_contact(app, random_contact):
        contact = Contact(first_name="new_first_name", last_name="new_last_name", address="new_address")
        contact.id_contact = random_contact.id_contact
        app.contact.modify_contact_by_id(random_contact.id_contact, contact)
        return contact

@then('the new contact list is equal to the old list without the modified contact')
def verify_contact_modified(app, db, check_ui, non_empty_contact_list, random_contact, modified_contact):
        old_contacts = non_empty_contact_list
        new_contacts = db.get_contact_list()
        old_contacts.remove(random_contact)
        old_contacts.append(modified_contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

