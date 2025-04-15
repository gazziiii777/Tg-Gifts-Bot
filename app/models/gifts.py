from tortoise import fields, models

class Message(models.Model):
    id = fields.IntField(pk=True)
    user_id = fields.BigIntField()
    text = fields.TextField()
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "messages"