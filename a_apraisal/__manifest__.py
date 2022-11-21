# dodyakj --- dodyakj
{
    'name': "Penilaian Kinerja",

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
    'depends': ['base','hr_disciplinary_tracking','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'report/report_peremployee.xml',
        'views/views.xml',
        'views/menu.xml',
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
