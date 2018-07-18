import unittest
from graphene.test import Client

from tests import schema

class TestPeopleRoute(unittest.TestCase):
    def setUp(self):
        self.client = Client(schema)

    def test_getAllPeople(self):
        query = """{
            people {
                firstname
                lastname
            }
        }"""
        
        executed = self.client.execute(query)
        assert type(executed) == dict

    def test_getPeopleByPeopleCode(self):
        query = """{
            peopleByPeopleCode(peopleCode: "aot12345") {
                people {
                    peopleCode
                }
                status
                msg
            }
        }"""

        executed = self.client.execute(query)
        data = executed['data']

        peopleByPcode = data['peopleByPeopleCode']
        status = peopleByPcode['status']
        if status:
            assert peopleByPcode == {
                'people': {
                    'peopleCode': 'aot12345'
                },
                'status': True
            }
        else:
            msg = peopleByPcode['msg']
            assert msg is not None

    def test_createPeopleWithPeopleCode(self):
        pCode = 'aot1234'
        mutation = """mutation {
            createPeople(peopleData: { peopleCode: "aot1234" }) { 
                ok
                msg    
            }
        }"""

        result = schema.execute(mutation)
        assert not result.errors

        status = dict(result.data)['createPeople']['ok']
        msg = dict(result.data)['createPeople']['msg']

        if status:
            assert status == True
        else:
            assert msg == 'The pCode: {} is already exist.'.format(pCode)

    def test_editPeopleWithPcode(self):

        pCode = 'aot1234'
        edittedFname = 'edittedFirstname'
        ediitedLname = 'edittedLastname'

        mutation = """mutation {
            editPeople(editData: { 
                peopleCode: "%s", 
                firstname: "%s",
                lastname: "%s" }) {
                    people {
                        firstname
                        lastname
                    }
                    status
                    msg
                }
        }""" % (pCode, edittedFname, ediitedLname)

        result = schema.execute(mutation)
        assert not result.errors

        data = dict(result.data)['editPeople']
        status = data['status']
        msg = data['msg']

        if status:
            assert status == True

            people = data['people']
            firstname = people['firstname']
            lastname  = people['lastname']

            assert firstname == edittedFname
            assert lastname  == ediitedLname
        else:
            assert msg == 'This pCode\'s {} is not exist'.format(pCode)

    def test_deletePeopleByPCode(self):
        pCode = 'aot1234'

        mutation = """mutation {
            deletePeople(peopleCode: "%s") {
                peopleCode
                status
                msg
            }
        }""" % (pCode)

        result = schema.execute(mutation)
        assert not result.errors

        data = dict(result.data)['deletePeople']

