from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='category/images/%Y/%m/%d/',
        null=True,
        blank=True,
        help_text="An optional image representing the category."
    )
    parent = models.ForeignKey(
        to='self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children',
        related_query_name='category',
        help_text="The parent category for nested categories (optional)."
    )

    def __str__(self):
        return self.name

    def clean(self):
        """
        Custom validation to ensure categories have no more than two levels.

        Raises:
            ValidationError: If a category has more than two levels (parent and grandparent).
        """
        try:
            if not self.pk and self.parent and self.parent.parent:
                raise ValidationError("You can create only two levels of categories.")
        except AttributeError:
            pass
