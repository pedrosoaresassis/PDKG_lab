from django.db import models

class Product(models.Model):
    # Campo obrigatorio
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    image_url = models.URLField()
    
    # Campo adicional
    tags = models.JSONField(default=list) 
    brand = models.CharField(max_length=255, null=True, blank=True)
    
    # Campos de tempo
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    valid_until = models.DateTimeField(null=True, blank=True)
    expiration_date = models.DateTimeField(null=True, blank=True)  # data de validade se for alimento nesse garai V -v 
    
    def __str__(self):
        return self.name
