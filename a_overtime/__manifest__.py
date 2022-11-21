# dodyakj --- dodyakj
{
    'name': "Overtime",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or dodyakj""",

    'description': """
        Long description of module's purpose
    """,

    'author': "dodyakj",
    'website': "dodyakj",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','ohrms_overtime','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/menu.xml',
        'report/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
    ],
    "sequence": 0,
    "application": True,
    "installable": True,
    "auto_install": False,
}
