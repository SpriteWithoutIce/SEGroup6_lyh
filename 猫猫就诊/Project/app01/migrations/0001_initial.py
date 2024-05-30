# Generated by Django 5.0.4 on 2024-05-30 03:18

import django.db.models.deletion
import django.utils.timezone
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
        migrations.CreateModel(
            name="Patients",
            fields=[
                (
                    "identity",
                    models.SmallIntegerField(
                        choices=[
                            (1, "身份证"),
                            (2, "医保卡"),
                            (3, "诊疗卡"),
                            (4, "护照"),
                            (5, "军官证"),
                            (6, "港澳通行证"),
                        ],
                        default=1,
                        verbose_name="身份证明",
                    ),
                ),
                (
                    "identity_num",
                    models.CharField(
                        max_length=64,
                        primary_key=True,
                        serialize=False,
                        verbose_name="证件号",
                    ),
                ),
                ("name", models.CharField(max_length=20, verbose_name="患者姓名")),
                (
                    "health_insurance",
                    models.SmallIntegerField(
                        choices=[(1, "医保"), (2, "非医保")],
                        default=1,
                        verbose_name="医保情况",
                    ),
                ),
                (
                    "gender",
                    models.SmallIntegerField(
                        choices=[(1, "男"), (2, "女")], verbose_name="患者性别"
                    ),
                ),
                (
                    "birthday",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="患者生日"
                    ),
                ),
                (
                    "phone_num",
                    models.CharField(
                        default="", max_length=15, verbose_name="患者电话"
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        default="", max_length=128, verbose_name="患者住址"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "type",
                    models.SmallIntegerField(
                        choices=[(1, "医生"), (2, "普通用户"), (3, "管理员")],
                        default=2,
                        verbose_name="用户类型",
                    ),
                ),
                (
                    "identity_num",
                    models.CharField(
                        max_length=64,
                        primary_key=True,
                        serialize=False,
                        verbose_name="证件号",
                    ),
                ),
                ("password", models.CharField(max_length=64, verbose_name="用户密码")),
            ],
        ),
        migrations.CreateModel(
            name="OnDuty",
            fields=[
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to="app01.doctors",
                        verbose_name="医生编号",
                    ),
                ),
                (
                    "date",
                    models.DateField(
                        default=django.utils.timezone.now, verbose_name="值班日期"
                    ),
                ),
                (
                    "time",
                    models.SmallIntegerField(
                        choices=[(1, "上午"), (2, "下午"), (3, "晚上")],
                        default=1,
                        verbose_name="值班时间",
                    ),
                ),
                ("state", models.IntegerField(verbose_name="预约状态")),
            ],
        ),
        migrations.CreateModel(
            name="Register",
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
                ("queue_id", models.IntegerField(default=1, verbose_name="排队号")),
                ("time", models.DateTimeField(verbose_name="挂号时间")),
                ("position", models.CharField(max_length=128, verbose_name="门诊位置")),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app01.doctors",
                        verbose_name="医生编号",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient_registers",
                        to="app01.patients",
                        verbose_name="患者证件号",
                    ),
                ),
                (
                    "register",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="register_registers",
                        to="app01.patients",
                        verbose_name="挂号者证件号",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Treatment",
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
                ("queue_id", models.IntegerField(default=1, verbose_name="排队号")),
                ("time", models.DateTimeField(verbose_name="挂号时间")),
                ("advice", models.CharField(max_length=256, verbose_name="诊断结果")),
                ("medicine", models.TextField(verbose_name="开具药物")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="处方总价"
                    ),
                ),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app01.doctors",
                        verbose_name="医生编号",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app01.patients",
                        verbose_name="患者证件号",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notice",
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
                    "msg_type",
                    models.SmallIntegerField(
                        choices=[
                            (1, "预约成功"),
                            (2, "取消预约"),
                            (3, "处方缴费提醒"),
                            (4, "处方缴费成功"),
                        ],
                        verbose_name="消息类型",
                    ),
                ),
                ("time", models.DateTimeField(verbose_name="通知日期")),
                ("isRead", models.BooleanField(default=False, verbose_name="已读未读")),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app01.doctors",
                        verbose_name="医生编号",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="patient_notices",
                        to="app01.patients",
                        verbose_name="患者证件号",
                    ),
                ),
                (
                    "register",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app01.register",
                        verbose_name="挂号编号",
                    ),
                ),
                (
                    "treatment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app01.treatment",
                        verbose_name="处方编号",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Bill",
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
                    "type",
                    models.SmallIntegerField(
                        choices=[(1, "挂号"), (2, "处方")], verbose_name="账单类型"
                    ),
                ),
                ("state", models.BooleanField(verbose_name="账单状态")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="账单金额"
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app01.patients",
                        verbose_name="患者证件号",
                    ),
                ),
                (
                    "register",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app01.register",
                        verbose_name="挂号编号",
                    ),
                ),
                (
                    "treatment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app01.treatment",
                        verbose_name="处方编号",
                    ),
                ),
            ],
        ),
    ]
