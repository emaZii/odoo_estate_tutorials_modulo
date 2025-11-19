from odoo import models, fields

"""Model definition for MODELNAME."""
class EstateProperty (models.Model):
    
    # TODO: Define fields here
    _name = 'estate.property'
    _description = "Real Estate Property"
    
    name = fields.Char(required=True)
    description = fields.Text()
    expected_price = fields.Float(required=True)
    bedrooms = fields.Integer()
    postcode = fields.Char() 
    
