# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (c) 2016 brain-tec AG (http://www.braintec-group.com)
#    All Right Reserved
#
#    See LICENSE file for full licensing details.
##############################################################################
{
    'name': "Configure and Test",
    'author': "brain-tec AG",
    'license': 'LGPL-3',
    'version': '1.0',
    'summary': "Configure and Test",
    'category': 'Base',
    'website': 'http://www.braintec-group.com',
    'images': [
    ],
    'depends': [],
    'data': ['config_settings/_load_configuration_settings.yml',
             'config_settings/res.company.csv',
             ],
    'qweb': [
    ],
    'test': [
    ],
    'js': [
    ],
    'external_dependencies': {
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
