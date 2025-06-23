# -*- coding: utf-8 -*-
{
    "name": "itl HRM",
    "version": "1.0",
    "category": "Tests",
    "description": """A module to test the Group functionality.""",
    "depends": ["base"],
    "installable": True,
    "data": [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/menu_view.xml',
        'views/employee_view.xml',
        'views/department_view.xml',
    ],
    'license': 'LGPL-3',
    "application": True,
}