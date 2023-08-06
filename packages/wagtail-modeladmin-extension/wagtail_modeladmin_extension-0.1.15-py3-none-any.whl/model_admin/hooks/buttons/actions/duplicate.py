from re import search
from typing import Type, List, Union

from django.db.models import Model
from django.utils.text import slugify
from model_admin.hooks.buttons.handlers import FieldHandler


class DuplicateObject:
    """
        This class hold all the logic to duplicate a given object
    """

    @classmethod
    def _field_max_length(cls, obj: Type[Model], field: str) -> Union[int, None]:
        """Return text according to the max_length defined in Django field

        Args:
            obj (Model): A Django model
            field (str): The field name that will want to be found

        Returns:
            int: The maximum length of field
            None: If field has no maximum length
        """
        max_length = None
        django_field = obj._meta.get_field(field) # noqa
        if hasattr(django_field, "max_length"):
            max_length = django_field.max_length

        return max_length

    @classmethod
    def _set_copy_to_text(cls, obj: Type[Model], field: str) -> str:
        """Set the string `COPY` to the field.

        Args:
            obj (Model): A Django model
            field (str): The field name that will want to be found

        Returns:
            str: The string with COPY concatenated

        """
        final_text = f"COPY {getattr(obj, field)}"
        if search("slug", field):
            final_text = slugify(final_text)
        max_length = cls._field_max_length(obj, field)
        return final_text[0:max_length]

    @classmethod
    def _remove_duplicates(cls, lists: List[List[str]]) -> List[str]:
        """Auto retrieve all unique fields defined in model

        Args:
            lists (List[List[str]]): A list of lists with all fields to 
            create a only one list

        Returns:
            List[str]: A list containing all fields (without duplicates)
        """
        all_lists = []
        for li in lists:
            all_lists = all_lists + li
        return list(set(all_lists))

    @classmethod
    def _auto_import_unique_fields(cls, obj: Type[Model]) -> List[str]:
        """Auto retrieve all unique fields defined in model

        Args:
            obj (Model): A Django model

        Returns:
            List[str]: A list with all fields to modify
        """
        fields = []
        for field in obj._meta.get_fields():  # noqa
            if (
                (hasattr(field, "unique") and field.unique) 
                and "id" not in field.name
            ):
                fields.append(FieldHandler(field.name))
        return fields

    @classmethod
    def _get_fields(cls, obj: Type[Model]) -> List[str]:
        """Get all fields to concatenate the text COPY.

        Args:
            obj (Model): A Django model

        Returns
        """
        unique_fields = cls._auto_import_unique_fields(obj)

        if hasattr(obj, "TO_DUPLICATE"):
            unique_fields = cls._remove_duplicates([
                unique_fields,
                obj.TO_DUPLICATE,
            ])
        return unique_fields

    @classmethod
    def do(cls, obj: Type[Model]) -> None:
        """Just execute the action"""
        obj.pk = None

        for field in cls._get_fields(obj):
            setattr(obj, field.name, field.handle(obj))
        obj.save()
