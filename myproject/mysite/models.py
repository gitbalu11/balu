from django.db import models


class Demo(models.Model):
	name = models.CharField(max_lenth=100)
