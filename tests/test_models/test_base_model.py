#!/usr/bin/python3
"""define unittests for base_model.py.

unittest classes:
    TestBaseModel_instantiation
    TestBaseModel_save
    TestBaseModel_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """unittest for the basemodel class instantiation"""

    def test_no_args_instantiates(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_two_models_unique_ids(self):
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_two_models_different_created_at(self):
        base1 = BaseModel()
        sleep(0.05)
        base2 = BaseModel()
        self.assertLess(base1.created_at, base2.created_at)

    def test_two_models_different_updated_at(self):
        base1 = BaseModel()
        sleep(0.05)
        base2 = BaseModel()
        self.assertLess(base1.updated_at, base2.updated_at)

    def test_args_unused(self):
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_instantiation_with_kwargs(self):
        date = datetime.today()
        date_iso = date.isoformat()
        base = BaseModel(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(base.id, "345")
        self.assertEqual(base.created_at, date)
        self.assertEqual(base.updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)


class TestBaseModel_save(unittest.TestCase):
    """unittest for the saving method of BaseModel"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        base = BaseModel()
        sleep(0.05)
        first_updated_at = base.updated_at
        base.save()
        self.assertLess(first_updated_at, base.updated_at)

    def test_two_saves(self):
        base = BaseModel()
        sleep(0.05)
        first_updated_at = base.updated_at
        base.save()
        second_updated_at = base.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        base.save()
        self.assertLess(second_updated_at, base.updated_at)

    def test_save_updates_file(self):
        base = BaseModel()
        base.save()
        baseid = "BaseModel." + base.id
        with open("file.json", "r") as file:
            self.assertIn(baseid, file.read())


class TestBaseModel_to_dict(unittest.TestCase):
    """text to_dict method from the baseModel class"""

    def test_to_dict_type(self):
        base = BaseModel()
        self.assertTrue(dict, type(base.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        base = BaseModel()
        self.assertIn("id", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())
        self.assertIn("__class__", base.to_dict())

    def test_to_dict_contains_added_attributes(self):
        base = BaseModel()
        base.name = "model's name"
        bm.my_number = 50
        self.assertIn("name", base.to_dict())
        self.assertIn("my_number", base.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(str, type(base_dict["created_at"]))
        self.assertEqual(str, type(base_dict["updated_at"]))

    def test_contrast_to_dict_dunder_dict(self):
        base = BaseModel()
        self.assertNotEqual(base.to_dict(), base.__dict__)


if __name__ == "__main__":
    unittest.main()
