from django.db import models
from accounts.models import CustomUser


class AttentionData(models.Model):
    attention_position = models.IntegerField(default=0)
    stay_time = models.IntegerField(default=0)

    def __str__(self):
        return f"Attention Position: {self.attention_position}, Stay Time: {self.stay_time}"

class ScrollData(models.Model):
    max_scroll_position = models.IntegerField(default=0)
    max_scroll_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Scroll Position:{self.max_scroll_position},Max Count:{self.max_scroll_count}"

    

class ClickData(models.Model):
    click_position_x = models.IntegerField(default=0)
    click_position_y = models.IntegerField(default=0)
    click_count = models.IntegerField(default=0)

    def __str__(self):
        return f"Click Position:({self.click_position_x},{self.click_position_y}),Click_count:{self.click_count}"

    
class Url_Form(models.Model):
    web_site = models.URLField(max_length=200)
    
    def __str__(self):
        return self.web_site
    
class Data_Search(models.Model):
    date_field = models.DateField()
    datetime_field = models.DateTimeField()
    
    def __str__(self):
        return self.date_field