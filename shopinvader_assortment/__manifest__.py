# Copyright 2018 ACSONE SA/NV
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Shopinvader Assortment",
    "version": "14.0.1.2.0",
    "license": "AGPL-3",
    "author": "ACSONE SA/NV",
    "website": "https://github.com/shopinvader/odoo-shopinvader",
    "depends": [
        "product_assortment",
        "shopinvader",
        "shopinvader_search_engine",
    ],
    "data": ["data/ir_cron.xml", "views/shopinvader_backend.xml"],
    "demo": ["demo/shopinvader_assortment_demo.xml"],
    "installable": True,
}
