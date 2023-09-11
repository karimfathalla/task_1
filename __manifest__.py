{
    'name': 'Purchase Request Training Task',
    # 'author': '',
    'summary': 'purchase request',
    'sequence': 1,
    'depends': ['base', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'wizards/cancel_wizard.xml',
        'views/purchase.xml',
        'data/email_templet.xml'
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
