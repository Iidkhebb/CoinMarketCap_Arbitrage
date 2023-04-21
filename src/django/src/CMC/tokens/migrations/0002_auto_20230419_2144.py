

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tokens', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tokens',
            old_name='token_id',
            new_name='tokenID',
        ),
        migrations.AddField(
            model_name='tokens',
            name='audit',
            field=models.CharField(default='walou', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tokens',
            name='dextoolslink',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tokens',
            name='img_path',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tokens',
            name='tokensnifferlink',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
