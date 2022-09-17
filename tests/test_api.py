import os

import allure
import requests
from api.utils import request_body
from api.utils.session import reqres

reqres_url = os.getenv('reqres_url')

@allure.parent_suite('List User')
@allure.suite(f'API List User {reqres_url}')
@allure.title(f"API List User {reqres_url} page 2")
def test_list_users():
    with allure.step(f'List user ID 2'):
        r = reqres().get('/api/users?page=2')
        # r = requests.get('https://reqres.in')
    with allure.step(f'Assert {reqres_url} page = 2'):
        assert r.json()['page'] == 2


@allure.parent_suite('Single user')
@allure.suite(f'API Single user {reqres_url}')
@allure.title(f"API Single user {reqres_url} 2")
def test_single_user():
    with allure.step(f'Watch user ID 2'):
        r = reqres().get('/api/users/2')
        # r = requests.get('https://reqres.in')
    with allure.step(f'Assert {reqres_url} user ID = 2'):
        assert r.json()['data']['id'] == 2
        assert r.json()['data']['email'] == "janet.weaver@reqres.in"

@allure.parent_suite('Create user')
@allure.suite(f'API Create user {reqres_url}')
@allure.title(f"API Create user {reqres_url} 2")
def test_create_user():
    user = request_body.create_user('Sam', 'Nope')
    with allure.step(f'Create user {user}'):
        r = reqres().post('/api/users', json=user)
        # r = requests.post('https://reqres.in/api/users', json=user)
    with allure.step(f'Assert {user}'):
        assert r.status_code == 201
        assert r.json()['name'] >= user['name']
        assert r.json()['job'] >= user['job']

@allure.parent_suite('Update user')
@allure.suite(f'API Update user {reqres_url}')
@allure.title(f"API Update user {reqres_url} 2")
def test_update_user():
    user = request_body.create_user('Sammm', 'Nopeee')
    with allure.step(f'Update user {user}'):
        r = reqres().put('/api/users/2', json=user)
        # r = requests.put('https://reqres.in/api/users/2', json=user)
    with allure.step(f'Assert Update {user}'):
        assert r.status_code == 200
        assert r.json()['name'] >= user['name']
        assert r.json()['job'] >= user['job']


