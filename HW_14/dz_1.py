# 📌На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# 📌Напишите 3-7 тестов unittest для данного проекта.
# 📌Используйте setUp





import re
import pytest
import unittest
from os import path
from Project import Project
from User import User
import Excep as Ex

@pytest.fixture
def project():
    return Project.load_users('users.json')

@pytest.fixture
def admin(project):
    project.enter('Piter', 114)
    return project.admin

def test_enter(project):
    project.enter('Jack', 105)
    assert project.admin.name == 'Jack' and \
            project.admin.uid == 105

def test_enter_error(project):
    with pytest.raises(Ex.ErrorAcsess, match="Пользователя Иван с ID-10 не существует!"):
        project.enter('Иван', 10)

def test_add_user(project, admin):
    new_user = User('Иван', 105, 7)
    project.add_user('Иван', 105, 7)
    assert new_user in project.users

def test_add_user_error_level(project, admin):
    with pytest.raises(Ex.ErrorLevel, match=re.escape("Операция для пользователя Иван не может быть выполнена, \
т.к. его уровень доступа (1) выше, чем уровень администратора (4)!")):
        project.add_user('Иван', 105, 1)

def test_add_user_error_user(project, admin):

    with pytest.raises(Ex.ErrorUser, match="Пользователь Tom с ID-106 уже существует!"):
        project.add_user('Tom', 106, 6)

def test_del_user(project, admin):
    new_user = User('Jack', 105, 5)
    project.del_user('Jack', 105)
    assert not new_user in project.users

def test_del_user_error_user(project, admin):
    with pytest.raises(Ex.ErrorAcsess, match="Пользователя Иван с ID-105 не существует!"):
        project.del_user('Иван', 105)

def test_del_user_error_level(project, admin):
    with pytest.raises(Ex.ErrorLevel, match=re.escape("Операция для пользователя Rudyard не может быть выполнена, \
т.к. его уровень доступа (1) выше, чем уровень администратора (4)!")):
        project.del_user('Rudyard', 104)

def test_file_not_exist(project, tmp_path):
    f_name = tmp_path / 'result.json'
    project.write_to_json(f_name)
    assert path.exists(f_name) == True and path.getsize(f_name) != 0


if __name__ == '__main__':
    pytest.main()

if __name__ == '__main__':
    unittest.main()
