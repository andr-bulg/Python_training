from pytest_bdd import given, when, then, parsers
from model.group import Group
import random

@given('a group list', target_fixture='group_list')
def group_list(db):
    return db.get_group_list()

@given(parsers.parse('a group with {name}, {header} and {footer}'), target_fixture='new_group')
def new_group(name, header, footer):
    return Group(name=name, header=header, footer=footer)

@when('I add the group to the list')
def add_new_group(app, new_group):
    app.group.create(new_group)

@then('the new group list is equal to the old list with the added group')
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    new_groups = db.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

@given('a non-empty group list', target_fixture='non_empty_group_list')
def non_empty_group_list(app, db):
    if not db.get_group_list():
        app.group.create(Group(name="temp_group", header="temp_header", footer="temp_footer"))
    return db.get_group_list()

@given('a random group from the list', target_fixture='random_group')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)

@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id_group)

@then('the new group list is equal to the old list without the deleted group')
def verify_group_deleted(app, db, check_ui, non_empty_group_list, random_group):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        new_groups = map(app.group.clean, new_groups)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

@when('I modify the group from the list', target_fixture='modified_group')
def modified_group(app, random_group):
    group = Group(name="new_group", header="new_header", footer="new_footer")
    group.id_group = random_group.id_group
    app.group.modify_group_by_id(random_group.id_group, group)
    return group

@then('the new group list is equal to the old list without the modified group')
def verify_group_modified(app, db, check_ui, non_empty_group_list, random_group, modified_group):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    old_groups.remove(random_group)
    old_groups.append(modified_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        new_groups = map(app.group.clean, new_groups)
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

