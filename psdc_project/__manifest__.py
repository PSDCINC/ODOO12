# -*- coding: utf-8 -*-
{
    "name": "PSDC - Ajustes para Proyectos y Contactos",
    "summary": "Ajustes al módulo de proyectos y contactos",
    "description": """
        PSDC - proyectos y contactos, contiene información para:
            - Definir contactos como residentes
            - Agregar residentes en los proyectos
            - Agregar adendas
            - Agregar fianzas
            - Agregar pólizas
    """,
    "author": "PSDC Innova",
    "website": "https://psdc.com.pa/",
    "category": "Projects",
    "version": "1.0.2",
    "depends": ['base', 'contacts', 'project'],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/project_views.xml',
        'views/addendum_views.xml',
        'views/endorsement_views.xml',
        'views/bail_views.xml',
        'views/policy_views.xml',
        'data/addendum_descriptions.xml',
        'data/endorsement_reasons.xml',
        'data/policy_types.xml',
    ],
    "demo": []
}
