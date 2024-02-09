import unittest
# from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.BaseModel = BaseModel()

    def test_attributes_existence(self):
        self.assertTrue(hasattr(self.BaseModel, 'id'))
        self.assertTrue(hasattr(self.BaseModel, 'created_at'))
        self.assertTrue(hasattr(self.BaseModel, 'updated_at'))

    def test_str_representation(self):
        expected_str = "[BaseModel] ({}) {}".format(self.BaseModel.id, self.BaseModel.__dict__)
        self.assertEqual(str(self.BaseModel), expected_str)

    def test_save_updates_updated_at(self):
        original_updated_at = self.BaseModel.updated_at
        self.BaseModel.save()
        new_updated_at = self.BaseModel.updated_at
        self.assertNotEqual(original_updated_at, new_updated_at)

    def test_to_dict_structure(self):
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        BaseModel_dict = self.BaseModel.to_dict()
        self.assertCountEqual(BaseModel_dict.keys(), expected_keys)

    def test_to_dict_values(self):
        BaseModel_dict = self.BaseModel.to_dict()
        self.assertEqual(BaseModel_dict['id'], self.BaseModel.id)
        self.assertEqual(BaseModel_dict['created_at'], self.BaseModel.created_at.isoformat())
        self.assertEqual(BaseModel_dict['updated_at'], self.BaseModel.updated_at.isoformat())
        self.assertEqual(BaseModel_dict['__class__'], 'BaseModel')

    def test_from_dict(self):
        BaseModel_dict = self.BaseModel.to_dict()
        new_model = BaseModel(**BaseModel_dict)
        self.assertEqual(new_model.id, self.BaseModel.id)
        self.assertEqual(new_model.created_at, self.BaseModel.created_at)
        self.assertEqual(new_model.updated_at, self.BaseModel.updated_at)


if __name__ == '__main__':
    unittest.main()
