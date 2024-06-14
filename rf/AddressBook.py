from fixture.application import Application
from fixture.db import DbFixture
import json
import os.path
from model.group import Group
from model.contact import Contact


class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST_SUITE'

    def __init__(self, browser="firefox", config="target.json"):
        self.browser = browser
        config_file = os.path.abspath(f'{config}')
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target['web']
        self.fixture = Application(browser=self.browser, base_url=web_config["baseUrl"])
        self.fixture.session.ensure_login(username=web_config["username"], password=web_config["password"])
        db_config = self.target['db']
        self.dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                              password=db_config['password'])

    def destroy_fixtures(self):
        self.dbfixture.destroy()
        self.fixture.destroy()

    def create_group(self, group):
        self.fixture.group.create(group)

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id_group)

    def modify_group(self, modified_group, group):
        group.id_group = modified_group.id_group
        self.fixture.group.modify_group_by_id(modified_group.id_group, group)


    def create_contact(self, contact):
        self.fixture.contact.create(contact)

    def get_contact_list(self):
        return self.dbfixture.get_contact_list()

    def new_contact(self, first_name, last_name, address):
        return Contact(first_name=first_name, last_name=last_name, address=address)

    def contact_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Contact.id_or_max) == sorted(list2, key=Contact.id_or_max)

    def delete_contact(self, contact):
        self.fixture.contact.delete_contact_by_id(contact.id_contact)

    def modify_contact(self, modified_contact, contact):
        contact.id_contact = modified_contact.id_contact
        self.fixture.contact.modify_contact_by_id(modified_contact.id_contact, contact)

