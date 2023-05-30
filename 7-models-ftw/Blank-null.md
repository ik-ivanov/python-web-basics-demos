```python 
class NullBlankDemo(models.Model):
    # can be blank, but can't be null
    blank = models.IntegerField(blank=True, null=False)
    # can't be blank, can be null
    null = models.IntegerField(blank=False, null=True)
    # can be blank, can be null
    blank_null = models.IntegerField(blank=True, null=True)
    # can't be blank, can't be null
    default = models.IntegerField(blank=False, null=False)


class NullBlankDemoAdmin(admin.ModelAdmin):
    pass   
```

In other words (as table)
+-----------+---------+---------+------------+
|  field    |  blank  |  null   |  default   |
+-----------+---------+---------+------------+
| blank     |   True  |  False  |    needed  |
| null      |  False  |   True  |            |
| blank_null|   True  |   True  |   possible |
| default   |  False  |  False  |            |
+-----------+---------+---------+------------+

In other words as flow:
1. blank=True, null=False - Can skip the form, but the DB requires a value
2. blank=False, null=True - Can't skip the form, but the DB allows a NULL value (we can hack it with JS)
3. blank=True, null=True - Can skip the form, and the DB allows a NULL value
4. blank=False, null=False - Can't skip the form, and the DB requires a value
