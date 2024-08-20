# Generated by Django 5.0.4 on 2024-08-20 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Doctors",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "identity_num",
                    models.CharField(max_length=64, verbose_name="证件号"),
                ),
                ("name", models.CharField(max_length=20, verbose_name="医生姓名")),
                ("title", models.CharField(max_length=50, verbose_name="医生职称")),
                (
                    "department",
                    models.CharField(max_length=20, verbose_name="医生科室"),
                ),
                (
                    "research",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="研究方向"
                    ),
                ),
                (
                    "cost",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="出诊费"
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="doctor/",
                        verbose_name="医生头像",
                    ),
                ),
                (
                    "avatar_name",
                    models.CharField(
                        default="img", max_length=128, verbose_name="图片名字"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Medicine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="药物名字")),
                (
                    "medicine_type",
                    models.SmallIntegerField(
                        choices=[(1, "中药"), (2, "中成药"), (3, "西药")],
                        verbose_name="药物种类",
                    ),
                ),
                ("symptom", models.CharField(max_length=200, verbose_name="适应症状")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="药物价格"
                    ),
                ),
                ("quantity", models.IntegerField(default=0, verbose_name="药物库存")),
                (
                    "photo_name",
                    models.CharField(
                        default="img", max_length=128, verbose_name="图片名字"
                    ),
                ),
            ],
        ),
    ]
