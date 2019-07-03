# Generated by Django 2.1.7 on 2019-07-02 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ac',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tail_number', models.CharField(max_length=100, verbose_name='注册号')),
            ],
            options={
                'verbose_name': '航空器注册信息',
                'verbose_name_plural': '航空器注册信息',
                'ordering': ('tail_number',),
            },
        ),
        migrations.CreateModel(
            name='acmodels',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('basic_acmodels', models.CharField(max_length=100, verbose_name='基本型号')),
                ('expanded_acmodels', models.CharField(max_length=100, verbose_name='系列号')),
                ('if_intra_ac', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '飞机型号',
                'verbose_name_plural': '飞机型号',
                'ordering': ('basic_acmodels',),
            },
        ),
        migrations.CreateModel(
            name='aputime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('apu_pn', models.CharField(max_length=20, verbose_name='APU件号')),
                ('meth', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='月使用时间')),
                ('metc', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='月使用循环')),
                ('ceth', models.FloatField(verbose_name='总使用时间')),
                ('cetc', models.FloatField(verbose_name='总使用循环')),
                ('csr', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='计划拆换数')),
                ('cuc', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='非计划拆换数')),
                ('re_date', models.DateField(verbose_name='记录时间')),
            ],
        ),
        migrations.CreateModel(
            name='ata',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('chapter', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='章')),
                ('section', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='节')),
                ('subject', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='题')),
                ('title', models.CharField(max_length=100, verbose_name='系统名称')),
                ('zh_title', models.CharField(max_length=100, verbose_name='系统名称(中)')),
            ],
            options={
                'verbose_name': 'ATA章节号',
                'verbose_name_plural': 'ATA章节号',
                'ordering': ('chapter',),
            },
        ),
        migrations.CreateModel(
            name='engine_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('en_models', models.CharField(max_length=100, verbose_name='发动机型号')),
                ('en_sn', models.CharField(max_length=100, verbose_name='发动机序号')),
                ('ac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engine_info_ac', to='reac.ac')),
            ],
            options={
                'verbose_name': '发动机信息',
                'verbose_name_plural': '发动机信息',
                'ordering': ('en_models',),
            },
        ),
        migrations.CreateModel(
            name='entime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('epc', models.CharField(max_length=4, verbose_name='装机位置')),
                ('meth', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='月使用时间')),
                ('metc', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='月使用循环')),
                ('if_overhaul', models.BooleanField(default=False)),
                ('eth_aoh', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='修后使用时间')),
                ('etc_aoh', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='修后使用循环')),
                ('ceth', models.FloatField(verbose_name='总使用时间')),
                ('cetc', models.FloatField(verbose_name='总使用循环')),
                ('re_date', models.DateField(verbose_name='记录时间')),
                ('remove_reson', models.TextField(verbose_name='拆换原因')),
                ('maintance', models.TextField(verbose_name='维修')),
                ('maintance_range', models.TextField(verbose_name='工作范围')),
                ('en_sn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='engine_info_time', to='reac.engine_info')),
            ],
        ),
        migrations.CreateModel(
            name='flytime',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ana', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='可用架日')),
                ('mth', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='月飞行时间')),
                ('mtc', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='月起落架次')),
                ('mdf', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='月营运飞行时间')),
                ('mdr', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='月营运起落架次')),
                ('cth', models.FloatField(verbose_name='总飞行时间')),
                ('cty', models.FloatField(verbose_name='总起落架次')),
                ('date', models.DateField(verbose_name='发生时间')),
                ('mfr', models.CharField(max_length=100, verbose_name='制造商')),
                ('ac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flytime_ac', to='reac.ac')),
            ],
        ),
        migrations.CreateModel(
            name='fm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fm', models.TextField(verbose_name='故障模式')),
                ('fe', models.TextField(verbose_name='故障影响')),
                ('ru', models.TextField(verbose_name='故障原因')),
                ('re', models.TextField(verbose_name='解决措施')),
                ('ata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ata_fm', to='reac.ata')),
            ],
            options={
                'verbose_name': '故障模式库',
                'verbose_name_plural': '故障模式库',
                'ordering': ('fm',),
            },
        ),
        migrations.AddField(
            model_name='ac',
            name='acmodels',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ac_acmodels', to='reac.acmodels'),
        ),
    ]
