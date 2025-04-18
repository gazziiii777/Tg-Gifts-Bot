from tortoise import fields, models

class Gifts(models.Model):
    id = fields.IntField(pk=True)
    gift_id = fields.BigIntField()
    convert_stars= fields.BigIntField()
    sold_out = fields.BooleanField()  
    limited = fields.BooleanField()  
    gift_id = fields.BigIntField()
    # logo = fields.TextField()
    availability_remains = fields.BigIntField()
    availability_total = fields.BigIntField()
    # created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "gifts"