from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "клиента"
        verbose_name_plural = "клиенты"

    def __str__(self):
        return str(self.name + " - " + self.phone)


class Good(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/", blank=True)

    @property
    def all_fields(self):
        return {
            "title": self.title,
            "description": self.description,
            "price": self.price,
            "quantity": self.quantity,
            "date": self.date,
            "image": self.image,
        }

    class Meta:
        verbose_name = "товара"
        verbose_name_plural = "товары"

    def __str__(self):
        return str(self.title)


class Order(models.Model):
    client = models.ForeignKey(
        to=Client, on_delete=models.CASCADE, related_name="orders"
    )
    goods = models.ManyToManyField(to=Good, related_name="goods")
    total = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    date_edit = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "заказа"
        verbose_name_plural = "заказы"

    def __str__(self):
        return str(f"Заказ No{self.pk}")
