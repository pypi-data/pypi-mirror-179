typeguards
==========

A library of ``bool`` and TypeGuard_ functions that can be used for runtime checks
and static type narrowing.

.. code-block:: python

  is_json(
      {
          "str_key": "str_val",
          "int_key": 1,
          "float_key": 1.0,
          "bool_key": True,
          "none_key": None,
          "list_key": [1, 2, "3", {"foo": "bar"}],
          "dict_key": {"foo": "bar"},
      },
  )  # True

.. _TypeGuard:
   https://docs.python.org/3/library/typing.html?highlight=typeguard#typing.TypeGuard

Usage
-----

Assert that an ``object`` is valid JSON, or not.

.. code-block:: python

  from typeguards.json import is_json

  assert is_json(
      {
          "str_key": "str_val",
          "int_key": 1,
          "float_key": 1.0,
          "bool_key": True,
          "none_key": None,
          "list_key": [1, 2, "3", {"foo": "bar"}],
          "dict_key": {  # dict values can be nested infinitely
                  "foo": "bar",
          },
      },
  )  # OK

  assert is_json("a string")  # AssertionError
  assert is_json([1, 2, 3])  # AssertionError

Assert that an ``object`` conforms to a JSON schema, or not.

.. code-block:: python

  from typing import List, TypedDict

  from typeguards.json import is_json_schema


  class HobbySchema(TypedDict):
     name: str
     is_fun: bool


  class UserSchema(TypedDict):
     id: int
     username: str
     hobbies: List[HobbySchema]  # Nested schema


  assert is_json_schema(
      {
          "id": 7,
          "username": "charlotte",
          "hobbies": [{"name": "Hyrule Warriors: Age of Calamity", "is_fun": True}],
      },
      UserSchema,
  )  # OK

  assert is_json_schema(
      {
          # No id, but still conforms to schema
          "username": "oscar",
          "hobbies": [{"name": "Whacking things", "is_fun": True}],
      },
      UserSchema,
  )  # OK

  assert is_json_schema(
      {
          "bad-id": 123,  # Doesn't conform to schema
          "username": "narvin",
          "hobbies": [{"name": "Watching coding videos", "is_fun": False}],
      },
      UserSchema,
  )  # AssertionError
