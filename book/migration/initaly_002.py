from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='created_date',
            new_name='created_dates',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='description',
            new_name='descriptions',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='image',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='title',
            new_name='titles',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='updated_date',
            new_name='updated_dates',
        ),
    ]