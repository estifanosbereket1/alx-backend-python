#!/usr/bin/env python3

import unittest
from parameterized import parameterized
from utils import access_nested_map

class TestAccessNestedMap(unittest.TestCase):
  

    @parameterized.expand([
    ({"a": 1}, ("a",), 1),                       
    ({"a": {"b": 2}}, ("a",), {"b": 2}),       
    ({"a": {"b": 2}}, ("a", "b"), 2), 
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), repr(path[len(context.exception.args[0].split('.') if '.' in context.exception.args[0] else path) - 1]))


