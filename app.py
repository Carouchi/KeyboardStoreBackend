import imp
from flask import Flask
from flask import Flask, json, request, jsonify


shopping_items = [
    {
        "id":1,
        "title":"White Generic Keyboard",
        "price":55,"description":"Solid white keyboard",
        "image":"https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
    },
        {
        "id":2,
        "title":"Custom Black And Red Keyboard",
        "price":55,"description":"Black keyboard with red keycaps",
        "image":"https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
    },
        {
        "id":3,
        "title":"Custom Black And Yellow Keyboard",
        "price":55,"description":"Black keyboard with yellow keycaps",
        "image":"https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
    },
]

print(shopping_items)