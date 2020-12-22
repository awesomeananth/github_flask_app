try:
    from run import app
    import unittest
    from flask import json
except Exception as e:
    print("import error {}".format(e))

class FlaskTest(unittest.TestCase):

    #check for response 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.post(
            '/post',
            data=json.dumps({'repository_name': ["danistefanovic/build-your-own-x"]}),
            content_type='application/json',
        )
        #data = json.loads(response.get_data(as_text=True)
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_negative_index(self):
        tester = app.test_client(self)
        response = tester.post(
            '/post',
            data=json.dumps({'repository_name': ["danistefanovic/build-your-own-x"]}),
            content_type='application/json',
        )
        statuscode = response.status_code
        self.assertNotEqual(statuscode, 400)

    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.post(
            '/post',
            data=json.dumps({'repository_name': ["danistefanovic/build-your-own-x"]}),
            content_type='application/json',
        )
        self.assertEqual(response.content_type, 'application/json')

    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.post(
            '/post',
            data=json.dumps({'repository_name': ["danistefanovic/build-your-own-x"]}),
            content_type='application/json',
        )
        self.assertTrue(b'Stargazer Count' in response.data)


if __name__ == "__main__":
    unittest.main()
