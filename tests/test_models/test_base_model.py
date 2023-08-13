#!/usr/bin/python3
"""
    - id is unique
    - creation time is well documented
    - update time varies properly
    - adding new attribute is found both in the dict and str repr
"""


import datetime
from models.base_model import BaseModel
import uuid
from unittest import TestCase, mock


class TestBaseModel(TestCase):
    """
    """
    def test_isinstance(self):
        """
        """
        base_obj = BaseModel()
        self.assertIsInstance(base_obj, BaseModel)

    def test_id(self):
        """
        """
        base_obj1 = BaseModel()
        test_uuid = str(uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}'))
        with mock.patch('uuid.uuid4') as mock_uuid:
            mock_uuid.return_value = test_uuid
            base_obj2 = BaseModel()
        self.assertNotEqual(base_obj1.id, base_obj2.id)
        self.assertEqual(base_obj2.id, test_uuid)

    def test_creationUpdate(self):
        """
        """
        test_date1 = datetime.datetime(2023, 8, 9, 9, 5, 0, 123456)
        with mock.patch('datetime.datetime') as mock_time:
            mock_time.now.return_value = test_date1
            base_obj1 = BaseModel()
        self.assertEqual(base_obj1.created_at, test_date1)
        self.assertEqual(base_obj1.created_at, base_obj1.updated_at)
        test_date2 = datetime.datetime(2024, 9, 10, 10, 6, 1, 789101)
        with mock.patch('datetime.datetime') as mock_update:
            mock_update.now.return_value = test_date2
            base_obj1.save()
        self.assertNotEqual(base_obj1.updated_at, base_obj1.created_at)
        self.assertEqual(base_obj1.updated_at, test_date2)

    def test_dict(self):
        """
        """
        test_date = datetime.datetime(2023, 8, 9, 9, 5, 0, 123456)
        test_date_iso = test_date.isoformat()
        with mock.patch('datetime.datetime') as mock_time:
            mock_time.now.return_value = test_date
            base_obj = BaseModel()
            base_obj.str_attr = "some string"
            base_obj.int_attr = 1234
            obj_dict = base_obj.to_dict()
            self.assertEqual(obj_dict['created_at'], test_date_iso)
            self.assertEqual(obj_dict['updated_at'], test_date_iso)
        self.assertIn('str_attr', obj_dict)
        self.assertIn('int_attr', obj_dict)


if __name__ == '__main__':
    unittest.main()
