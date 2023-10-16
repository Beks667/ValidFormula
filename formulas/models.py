from django.db import models


class FormulaValidator(models.Model):
	formula = models.TextField()
	date_of_create = models.DateTimeField(auto_now_add=True)
	result = models.BooleanField(default=True)
	ip_client=models.CharField(max_length=100)

	def __str__(self):
		return self.formula


	class Meta:
		verbose_name = "Формула"
		verbose_name_plural = "Формулы"
		ordering = ('-id',)