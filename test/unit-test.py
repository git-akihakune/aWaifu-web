import unittest
import os
import requests
import waifulabs

class configurationTest(unittest.TestCase):
    def importDependencies(self):
        from flask import request
        import waifulabs
        import aWaifu
        from flask_cors import CORS

    def testDependency(self):
        try:
            self.importDependencies()
            print(waifulabs.__version__)
        except AttributeError:
            pass
        except ModuleNotFoundError:
            self.fail('Dependencies not installed')
                

class webPageTest(unittest.TestCase):
    def testEnvironmentVariable(self):
        self.assertTrue(os.environ['FLASK_APP'] and os.environ['FLASK_ENV'], msg='Ensure environment variables set')
    
    def testApi(self, host:str = 'http://127.0.0.1:5000', endpoint:str = '/api/profile') -> bool:
        data = {
            "api_key": 'test',
            "number_of_profiles": 1,
            "multiCultures": False,
            "bigWaifu": False,
            "faster": True,
        }
        response = requests.post(host + endpoint, data)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('Traceback', response.text)

if __name__ == '__main__':
    unittest.main()