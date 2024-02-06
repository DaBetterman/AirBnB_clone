import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.my_model = BaseModel()

    def test_attributes_existence(self):
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))

    def test_str_representation(self):
        expected_str = "[BaseModel] ({}) {}".format(self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected_str)

    def test_save_updates_updated_at(self):
        original_updated_at = self.my_model.updated_at
        self.my_model.save()
        new_updated_at = self.my_model.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

    def test_to_dict_structure(self):
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        my_model_dict = self.my_model.to_dict()
        self.assertCountEqual(my_model_dict.keys(), expected_keys)

    def test_to_dict_values(self):
        my_model_dict = self.my_model.to_dict()
        self.assertEqual(my_model_dict['id'], self.my_model.id)
        self.assertEqual(my_model_dict['created_at'], self.my_model.created_at.isoformat())
        self.assertEqual(my_model_dict['updated_at'], self.my_model.updated_at.isoformat())
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()
