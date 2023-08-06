"""
# BaseAdmin控制选项

> 这里应该用装饰器模式的... 后续改进.
> 导入功能要求用户必须拥有对应的add权限.

- stop_field_ls                                         # 停用词列表, 字段名包含该词的字段将不展示.

- move_id_to_tail = False                               # id移到最后一列去

- origin_list = False                                   # 展示原str

- `ExcelImportExportAdmin`选项
    - default_export_action = True                      # 默认增加导出按钮
    - `ExportExcelMixin`导出选项
        - export_asc = False                            # 按id升序导出
        - add_index = False                             # 导出时是否增加index列

- orm_executor = True                                   # 使用orm过滤器

- `ImportAdmin`导入导出选项
    - change_list_template = CHANGE_LIST_HTML_PATH      # 模板路径, 一般CHANGE_LIST_HTML_PATH的路径在'~bddjango/templates/entities/...'中

    - custom_import_and_export_buttons = True           # 是否显示自定义的导入导出按钮
    - has_import_perm = True                            # 导入数据
    - has_export_perm = True                            # 全部导出
    - check_import_and_export_perm = True               # 是否检查导入导出按钮的权限

"""

import csv
import datetime
import threading
import numpy as np
import pandas as pd
import xlrd
import os
from openpyxl import Workbook
from bdtime import Time
from django import forms
from django.shortcuts import render, redirect, HttpResponse
from django.urls import path
from django.contrib import admin
from django.contrib import messages
from django.utils.http import urlquote

from .. import get_model_max_id_in_db
from .. import reset_db_sequence
from ..pure import remove_temp_file

import shutil
# --- 初始化环境 ---
from .admin_env_init import CHANGE_LIST_HTML_PATH, TEMPDIR, BD_USE_GUARDIAN, CHANGE_FORM_TEMPLATE, BD_USE_SIMPLEUI
from tqdm import tqdm
from pandas._libs.tslibs.timestamps import Timestamp
from bddjango import get_base_model, get_model_max_id_in_db, old_get_model_max_id_in_db
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
import datetime as dt
from bdtime import tt
import time
import pandas as pd
from django.contrib.auth import get_permission_codename
import re
import html


IAdmin = admin.ModelAdmin


if BD_USE_SIMPLEUI:
    from simpleui.admin import AjaxAdmin
    IAdmin = AjaxAdmin


# if BD_USE_GUARDIAN:
#     from guardian.admin import GuardedModelAdmin
#
#     IAdmin = GuardedModelAdmin
#     IAdmin.change_form_template = CHANGE_FORM_TEMPLATE


# region # --- 处理df中的特殊格式
def conv_date_field_str_format(ts):
    """
    DateField的格式转换

    - 将csv中的时间字符转为符合django的时间格式
    """
    if isinstance(ts, Timestamp):
        return ts

    if isinstance(ts, datetime.datetime):
        return ts

    if not ts or ts == 'None':
        return None

    if isinstance(ts, float) and np.isnan(ts):
        return None

    if '/' in ts:
        ts = datetime.datetime.strptime(ts, '%Y/%m/%d')
        ts = datetime.datetime.strftime(ts, '%Y-%m-%d')
    # elif '.' in ts:
    #     print('11111111')
    else:
        try:
            # 若匹配得到， 说明格式不用换
            datetime.datetime.strptime(ts, '%Y-%m-%d')
        except:
            ts = None
    return ts


def conv_date_time_field_str_format(ts):
    """
    DateTimeField的格式转换

    - 将csv中的时间字符转为符合django的时间格式
    """
    if isinstance(ts, Timestamp):
        return ts

    if not ts or ts == 'None':
        return None

    if isinstance(ts, float) and np.isnan(ts):
        return None

    if '.' in ts:
        # 毫秒级
        if '/' in ts:
            ts = datetime.datetime.strptime(ts, "%Y/%m/%d %H:%M:%S.%f")
            ts = datetime.datetime.strftime(ts, '%Y-%m-%d %H:%M:%S.%f')
        else:
            try:
                # 若匹配得到， 说明格式不用换
                datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M:%S.%f')
            except:
                ts = None
        return ts

    if '/' in ts:
        ts = datetime.datetime.strptime(ts, '%Y/%m/%d %H:%M:%S')
        ts = datetime.datetime.strftime(ts, '%Y-%m-%d %H:%M:%S')
    else:
        try:
            # 若匹配得到， 说明格式不用换
            datetime.datetime.strptime(ts, '%Y-%m-%d %H:%M:%S')
        except:
            ts = None
    return ts


def format_time_column(df1, column_name):
        # 多行一起处理
        ts_ls = df1[column_name]
        ts_ls = [datetime.datetime.strptime(ts, '%Y/%m/%d') for ts in ts_ls]
        ts_ls = [datetime.datetime.strftime(ts, '%Y-%m-%d') for ts in ts_ls]
        df1[column_name] = ts_ls


def conv_nan(xx):
    # df中的特殊字符nan处理
    if xx == 'None' or (isinstance(xx, float) and np.isnan(xx)):
        return None
    else:
        return xx

# endregion


class BulkDeleteMixin:
    """
    批量删除

    - django自带的删除法太慢了, 弄个批量删除

    - django的actions文档: https://docs.djangoproject.com/en/3.2/ref/contrib/admin/actions/
    """

    @admin.action(permissions=['delete'])
    def bulk_delete(self, request, queryset=None, model=None):
        t_delete = Time()
        count = queryset.count()
        queryset.delete()
        self.message_user(request, f"成功删除{count}条数据, 耗时: {t_delete.now(1)}秒.")

    bulk_delete.short_description = "批量删除"
    bulk_delete.icon = 'el-icon-delete'
    bulk_delete.confirm = "确定要批量删除选中的数据么?"


class ExportExcelMixin:
    export_asc = False  # 按id升序导出
    add_index = False

    def export_as_excel(self, request, queryset=None, model=None, extra_fields_dc=None, add_index_column=0,
                        ordering=None):
        if model is None:
            # 如果没有指定model, 则采用默认的model, 并导出全部
            if hasattr(self, 'model'):
                base_model = self.model
            else:
                base_model = get_base_model(queryset)
            meta = base_model._meta
        else:
            meta = model._meta
            queryset = model.objects.all()

        # md = get_base_model(queryset)
        field_names = [field.name for field in meta.fields]
        verbose_names = [field.verbose_name for field in meta.fields]
        conv_name_to_verbose_dc = dict(zip(field_names, verbose_names))
        if extra_fields_dc:
            conv_name_to_verbose_dc.update(extra_fields_dc)

        if model is None:
            """
            导出全部的时候, 大文件用流媒体传输, 并分批次读入, 防止超过云服务器带宽.
            未完待续...
            """
            from django.http import StreamingHttpResponse
            from django_pandas import io
            from bdtime import tt
            from django.db import models as m
            # print('~~~~~~~~~~~~ queryset.count():', queryset.count())
            qs: m.QuerySet = queryset

            tt.__init__()

            # print('开始读入sql...')
            qs: m.QuerySet
            # import pandas as pd
            # from django.db import connection
            # df = pd.concat([df for df in pd.read_sql(f'SELECT * FROM {meta.db_table}', connection, chunksize=100)], axis=0)
            df = io.read_frame(qs=qs)
            df.columns = [conv_name_to_verbose_dc.get(col) if conv_name_to_verbose_dc.get(col) else col for col in
                          df.columns]
            # print('df读入成功: ', tt.now(2))

            if add_index_column:
                # 增加一个序号列, start为 add_index_column - 1
                index = pd.Series(df.index) + int(add_index_column) - 1  # add_index_column为2, 则从1开始
                df.insert(loc=0, column='序号', value=index, allow_duplicates=False)

            if ordering:
                df = df[ordering]

            # print('开始保存为excel...', tt.now(2))
            time_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            tmp_file_name = f"{meta.verbose_name}_{time_str}.xlsx"
            fpath = os.path.join(TEMPDIR, tmp_file_name)
            # df.to_excel(fpath, index=False, encoding='unicode_escape')       # unicode_escape
            df.to_excel(fpath, index=self.add_index)  # unicode_escape
            # print('保存为Excel成功!', tt.now(2))
            del df

            # big file download
            def file_iterator(file_name, open_model='rb', chunk_size=512):
                with open(file_name, open_model) as f:  # , encoding=encoding
                    while True:
                        c = f.read(chunk_size)
                        if c:
                            yield c
                        else:
                            break

            # print('write response', tt.now(2))
            response = StreamingHttpResponse(file_iterator(fpath))
            # response['Content-Type'] = 'application/octet-stream'
            filename = urlquote(f"{meta.verbose_name}.xlsx")
            response['Content-Type'] = 'application/msexcel'
            response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)

            print('return response', tt.now(2))
            return response
        else:
            response = HttpResponse(content_type='application/msexcel')
            filename = urlquote(f"{meta.verbose_name}.xlsx")
            response['Content-Disposition'] = f'attachment; filename={filename}'
            wb = Workbook()
            ws = wb.active

            if self.export_asc:
                if queryset.count() and hasattr(queryset[0], 'id'):
                    queryset = queryset.order_by('id')
            ws.append(verbose_names)

            total = queryset.count()
            tq = tqdm(total=total)
            for obj in queryset:
                tq.update(1)
                data = [f'{getattr(obj, field)}' for field in field_names]
                try:
                    ws.append(data)
                except Exception as e:
                    print(data)
                    raise e
            wb.save(response)
            return response

    export_as_excel.short_description = "导出所选数据"
    # export_as_excel.acts_on_all = True
    # export_as_excel.type = 'success'
    # export_as_excel.icon = 'el-icon-upload'
    export_as_excel.icon = 'el-icon-download'


class ExportCsvMixin:
    def export_as_csv(self, request, queryset, model=None):
        if model is None:
            meta = self.model._meta
        else:
            meta = model._meta
        field_names = [field.name for field in meta.fields]
        verbose_names = [field.verbose_name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(verbose_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        return response

    export_as_csv.short_description = "  导出选中数据"  # 有图标的话要空俩格, 不然太近了
    # export_as_csv.acts_on_all = True
    # export_as_csv.icon = 'fas fa-audio-description'
    # export_as_csv.icon = 'fas fa-download'
    export_as_csv.icon = 'fas fa-download'


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


def _get_base_admin_dc_by_iadmin(iadmin):       # 类似装饰器模式, 通过IAdmin来获取装饰后的BaseAmin
    if BD_USE_GUARDIAN:
        from guardian.admin import GuardedModelAdminMixin

        class iadmin(GuardedModelAdminMixin, iadmin):
            change_form_template = CHANGE_FORM_TEMPLATE

    class IDAdmin(iadmin):
        """
        * 保存时自动处理id, 解决postgre在批量导入数据后的主键冲突问题.

        - 该方法仅对admin界面手动保存时调用的save_model()方法生效, 不影响obj.save()方法效率.
        """

        def save_model(self, request, obj, form, change):
            """
            参数change分辨保存or修改.
            若为保存, 则model的id值自动更新为数据库中最大id+1.
            """
            # if change is False:
            #     # meta = obj._meta
            #     # obj.id = get_model_max_id_in_db(model=None, meta=meta)
            #     obj.id = get_model_max_id_in_db(model=obj)
            # obj.save()

            try:
                obj.save()
            except Exception as e:
                msg = f'可能为pgsql的id引起的错误:' + str(e)

                print(msg)
                reset_db_sequence(obj)
                # obj.id = get_model_max_id_in_db(get_base_model(obj))
                obj.save()

    class ImportAdmin(IDAdmin):
        """
        导入类, CSV和Excel通用

        - 不能与admin.ModelAdmin一起用!
        """
        change_list_template = CHANGE_LIST_HTML_PATH

        custom_import_and_export_buttons = True
        has_import_perm = True      # 导入数据
        has_export_perm = True      # 全部导出
        check_import_and_export_perm = True     # 是否检查导入导出按钮的权限

        def import_csv(self, request):
            t_import = Time()
            index = 0
            try:
                if request.method == "POST":
                    csv_file = request.FILES.get("csv_file")
                    assert csv_file, '文件不能为空!'
                    assert csv_file._name and csv_file._name.__contains__('.'), '文件名不能为空, 且必须有后缀名!'
                    f_format = csv_file._name.rsplit('.', 1)[-1]
                    format_ls = ['xls', 'xlsx', 'csv']
                    assert f_format in format_ls, f'不支持的文件类型! 目前仅支持{format_ls}.'

                    read_data = csv_file.read()

                    time_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

                    tempdir = 'tempdir'
                    if not os.path.exists(tempdir):
                        os.mkdir(tempdir)

                    if f_format == 'csv':
                        try:
                            encoding = 'utf-8'
                            file_data = read_data.decode(encoding)
                        except Exception as e:
                            print('-- 尝试用gbk编码 --')
                            encoding = 'gbk'
                            file_data = read_data.decode(encoding)

                        fname = f'f_{time_str}.csv'
                        fname = os.path.join(tempdir, fname)

                        with open(fname, 'w', encoding=encoding) as f:
                            f.write(file_data)

                        # 为解决字段内有逗号导致分割错误问题, 只能采用pd了
                        df = pd.read_csv(fname, encoding=encoding)
                    elif f_format in ['xlsx', 'xls']:
                        wb = xlrd.open_workbook(file_contents=read_data)
                        df = pd.read_excel(wb)
                    else:
                        df = None

                    df_rows = df.shape[0]        # 一共多少行数据

                    # 删除Unnamed列
                    df = df.loc[:, ~df.columns.str.match('Unnamed')]

                    # 找出在model定义的列
                    meta = self.model._meta
                    field_names = [field.name for field in meta.fields]
                    verbose_names = [field.verbose_name for field in meta.fields]
                    field_dc = dict(zip(verbose_names, field_names))
                    valid_columns = [column_i in field_names or column_i in verbose_names for column_i in df.columns]
                    df = df.loc[:, valid_columns]
                    titles = df.columns.tolist()
                    title_ls = [field_dc.get(title_i) if field_dc.get(title_i) else title_i for title_i in titles]
                    curr_id = get_model_max_id_in_db(self.model)

                    df1 = df.copy()
                    df1.columns = title_ls

                    # 这里有问题, 服务器带宽太小的话, 一次性bulk_update会造成tcp拥塞, 从而导致服务器瘫痪!
                    # 必须仿照navicat的处理方式, 设置batch_size, 小批量处理数据.
                    # 同时出现问题, 如何让用户看到进度条? 用异步的方式, 或者websocket?
                    md_ls = []
                    my_tqdm = tqdm(total=df_rows)
                    for index, row in df1.iterrows():
                        content_ls = row.values.tolist()

                        # 处理DateField字段
                        for i in range(len(title_ls)):
                            title_i = title_ls[i]
                            content_ls[i] = conv_nan(content_ls[i])

                            attr = getattr(self.model, title_i)
                            if not hasattr(attr, 'field'):
                                continue
                            attr_field_name = attr.field.__class__.__name__

                            if attr_field_name in ['DateField', 'DateTimeField']:
                                # print(i, title_i, content_ls[i])
                                if attr_field_name == 'DateTimeField':
                                    res = conv_date_time_field_str_format(ts=content_ls[i])
                                    # if res is None:
                                    #     print(content_ls[i])
                                    content_ls[i] = res
                                else:
                                    ts = content_ls[i]
                                    res = conv_date_field_str_format(ts=ts)
                                    # if res is None:
                                    #     print(content_ls[i])
                                    content_ls[i] = res

                        dc = dict(zip(title_ls, content_ls))
                        dc.update({'id': curr_id})
                        curr_id += 1
                        md = self.model(**dc)
                        md_ls.append(md)
                        my_tqdm.update(1)
                        # self.model.objects.create(**dc)

                    self.model.objects.bulk_create(md_ls,batch_size=100)
                    reset_db_sequence(self.model)
                    self.message_user(request, f"{f_format}文件导入成功! 一共导入{df_rows}条数据, 耗时: {t_import.now(1)}秒.")
                    self.remove_temp_file(tempdir)

                    return redirect("..")
            except Exception as e:
                self.message_user(request, f"第 {index+1} 条数据导入失败!</br>错误信息：&nbsp;" + str(e), level=messages.ERROR)
                return redirect("..")

            form = CsvImportForm()
            payload = {"form": form}
            return render(request, "admin/csv_form.html", payload)

        def bulk_save(self, request, md_ls, f_format, df_rows, t_import, tempdir, batch_size=100):
            def _bulk_save():
                self.model.objects.bulk_create(md_ls, batch_size=batch_size)
                reset_db_sequence(self.model)
                self.message_user(request, f"{f_format}文件导入成功! 一共导入{df_rows}条数据, 耗时: {t_import.now(1)}秒.")
                self.remove_temp_file(tempdir)

            if df_rows < 3000:
                return _bulk_save()
            else:
                print('~~~ 多线程_bulk_save')
                self.message_user(request, f"{f_format}文件的{df_rows}条数据格式正确, 正在后台导入中, 请稍后查看...")
                t1 = threading.Thread(target=_bulk_save, args=())
                t1.start()

        def export_all_csv(self, request):
            # self.message_user(request, "成功导出全部数据为csv文件")
            return ExportCsvMixin().export_as_csv(request, queryset=self.model.objects.all(), model=self.model)

        def export_all_excel(self, request):
            # self.message_user(request, "成功导出全部数据为csv文件")
            ret = ExportExcelMixin().export_as_excel(request, queryset=self.model.objects.all(), model=self.model)
            self.remove_temp_file(TEMPDIR)
            return ret

        def get_urls(self):
            my_urls = [
                path('import-csv/', self.import_csv),
                path('export_all_csv/', self.export_all_csv),
                path('export_all_excel/', self.export_all_excel),
            ]
            return my_urls + super().get_urls()

        def remove_temp_file(self, tempdir):
            return remove_temp_file(tempdir)

        def changelist_view(self, request, extra_context=None):
            if not self.check_import_and_export_perm:
                has_import_perm = has_export_perm = True
            else:
                opts = self.opts

                def has_action_permission(opts, action):
                    codename = get_permission_codename(action, opts)
                    has_perm = request.user.has_perm('%s.%s' % (opts.app_label, codename))
                    return has_perm

                has_add_perm = has_action_permission(opts, 'add')
                has_change_perm = has_action_permission(opts, 'change')
                has_view_perm = has_action_permission(opts, 'view')

                has_import_perm = self.has_import_perm and has_add_perm and has_change_perm
                has_export_perm = self.has_export_perm and has_view_perm

            if extra_context is None:
                extra_context = {}
            extra_context.update({
                'custom_import_and_export_buttons': self.custom_import_and_export_buttons,
                'has_import_perm': has_import_perm,
                'has_export_perm': has_export_perm,
            })

            ret = super().changelist_view(request, extra_context=extra_context)
            return ret

    class CsvImportExportAdmin(ImportAdmin, ExportCsvMixin):
        """
        CSV导入/导出Admin类

        - 不能与admin.ModelAdmin一起用!
        """

        actions = ['export_as_csv']

    class ExcelImportExportAdmin(ImportAdmin, ExportExcelMixin):
        """
        Excel导入/导出Admin类

        - 不能与admin.ModelAdmin一起用!
        """
        default_export_action = True        # 默认增加导出按钮

        def get_actions(self, request):
            ACTION_NAME = 'export_as_excel'
            if self.default_export_action and ACTION_NAME not in self.actions:
                if self.actions is None:
                    self.actions = []
                self.actions.append(ACTION_NAME)
            ret = super().get_actions(request)
            return ret

    class ListDisplayAdmin(ExcelImportExportAdmin):
        """
        * admin展示界面

        - 展示所有字段, 默认前两列为点击链接. 并去除'stop_field_ls'中的字段

        - stop_field_ls: 停用词列表, 字段名包含该词的字段将不展示.
            - 注意url和href的区别: url为本地路由; href超链接, 不显示
        """
        list_display = '__all__'        # 默认展示全部
        stop_field_ls = []              # 停用字段
        move_id_to_tail = False      # id移到最后一列去

        origin_list = False     # 展示原str

        def __init__(self, *args, **kwargs):
            """
            增加一个可点击字段
            """
            super().__init__(*args, **kwargs)

            meta = self.model._meta
            field_names = [field.name for field in meta.fields]

            if self.list_display == [] or self.list_display is None:
                self.list_display = ('__str__', )
                self.origin_list = True
                return

            if not self.list_display_links and len(field_names) >= 2:
                if field_names[0] == 'id':
                    self.list_display_links = ('id', field_names[1])

            if (isinstance(self.list_display, str) and self.list_display == '__all__') or '__all__' in self.list_display:
                res = []
                for f in field_names:
                    if f not in self.stop_field_ls:
                        res.append(f)
                self.list_display = res

            return

        def get_list_display(self, request):
            ret = super().get_list_display(request)
            meta = self.model._meta
            field_names = [field.name for field in meta.fields]

            # model_str = self.model.__str__(self.model)
            # if not self.origin_list and ret == ('__str__',) and isinstance(model_str, str) and model_str.__contains__('ModelBase'):
            #     """如果用户没对list_display进行变更的话, 则自定义list_display字段"""
            #     meta = self.model._meta
            #     field_names = [field.name for field in meta.fields]
            #
            #     ret = []
            #     for f in field_names:
            #         if isinstance(f, str):
            #             # 如果有停用词, 则不加入ret中
            #             flag = False
            #             for r in self.stop_field_ls:
            #                 if f.__contains__(r):
            #                     flag = True
            #                     break
            #             if flag:
            #                 continue
            #         ret.append(f)

            if self.move_id_to_tail and 'id' in field_names and id not in self.stop_field_ls:
                ret.remove('id')
                ret.append('id')
            return ret

    class ForceRunActionsAdmin(ListDisplayAdmin):
        """
        增加强制运行actions功能
        """
        def changelist_view(self, request, extra_context=None):
            """
            这里想跳过"必须选择一个数据"的确认框,
            但django原生admin可以, 而simpleui无法实现,
            经过改进后, 以"fc_"开头的方法将强制运行

            - https://stackoverflow.com/questions/4500924/django-admin-action-without-selecting-objects
            """
            MyModel = self.model

            # 强制运行以"fc_"开头的action
            if 'action' in request.POST and request.POST['action'].startswith('fc_'):
                if not request.POST.getlist(ACTION_CHECKBOX_NAME):
                    post = request.POST.copy()
                    for u in MyModel.objects.all():
                        post.update({ACTION_CHECKBOX_NAME: str(u.id)})
                    request._set_post(post)
            return super().changelist_view(request, extra_context)

    class BaseAdmin(ForceRunActionsAdmin):
        """
        # 若search_term以变量prefix的值开头, 则检索最近xx条记录.
            - 如'~10'代表检索最近10条记录

        # 支持orm检索
        > 使用反引号[`]来替代引号["]
            - .filter(id__lt=20, wiki_id="asd")
            - .filter(wiki_id=`asd`).order_by(`-id`)[:3]
        """
        _tmp = None
        orm_executor = True  # 使用orm过滤器

        _ajax_search_term = None  # 用来ajax过滤
        _ajax_return_qs_ls = None  # 以便使用ajax方法返回的qs_ls

        def get_search_results(self, request, queryset, search_term):
            if not self.orm_executor:
                ret = super().get_search_results(request, queryset, search_term)
                return ret

            # --- 根据ajax方法返回qs_ls
            bd_ajax_return_qs_ls = '_ajax_return_qs_ls'
            if hasattr(self, bd_ajax_return_qs_ls) and getattr(self, bd_ajax_return_qs_ls) is not None:
                queryset = getattr(self, bd_ajax_return_qs_ls)
                setattr(self, bd_ajax_return_qs_ls, None)
                ret = (queryset, False)
                return ret

            # --- 根据orm语句进行过滤
            prefix = '~'  # 反向过滤~pk

            reg = re.compile(r'^\..*?[\)\]]$')  # 让.filter(xxx), .order_by(xxx)等orm语句可以执行

            if hasattr(self, '_ajax_search_term') and getattr(self, '_ajax_search_term'):
                search_term = self._ajax_search_term
                self._ajax_search_term = None

            if search_term and reg.match(search_term):
                print('search_term: ', search_term)

                # html转义
                search_term = search_term.replace('`', '"')
                while ('=&' in search_term):     search_term = html.unescape(search_term)
                try:
                    self._tmp = queryset
                    exec(f'self._tmp = self._tmp{search_term}')
                    queryset = self._tmp
                    # exec(f'queryset = queryset{search_term}')     # 局部变量无法用exec赋值!
                except Exception as e:
                    msg = f'orm语句执行出错! <br> search_term: {search_term},<br>  error: {e}'
                    self.message_user(request, msg)
                ret = (queryset, False)
            elif search_term.startswith(prefix):
                try:
                    if search_term.startswith(prefix):
                        search_term = search_term
                        search_term = int(search_term[len(prefix):])
                except Exception as e:
                    raise TypeError(f'pk必须为整数! {e}')
                id_qsv_ls = queryset.values('pk')[:search_term]
                queryset = queryset.filter(pk__in=id_qsv_ls)
                ret = (queryset, False)
            else:
                ret = super().get_search_results(request, queryset, search_term)

            return ret

    ret = {
        'IDAdmin': IDAdmin,
        'ImportAdmin': ImportAdmin,
        'CsvImportExportAdmin': CsvImportExportAdmin,
        'ExcelImportExportAdmin': ExcelImportExportAdmin,
        'ListDisplayAdmin': ListDisplayAdmin,
        'ForceRunActionsAdmin': ForceRunActionsAdmin,
        'BaseAdmin': BaseAdmin,
    }
    return ret


from . import adminclass


# decorator, 装饰器模式, 给admin_class附加额外的功能
def get_base_admin_dc_by_iadmin(iadmin=IAdmin, key='BaseAdmin') -> adminclass.BaseAdmin:
    admin_dc = _get_base_admin_dc_by_iadmin(iadmin)
    admin_class = admin_dc.get(key)
    return admin_class


if BD_USE_SIMPLEUI:
    MyAjaxAdmin: adminclass.BaseAdmin = get_base_admin_dc_by_iadmin(AjaxAdmin)


class CustomIAdmin:
    def __init__(self, iadmin):
        self.iadmin = iadmin

    def get_base_admin_dc_by_iadmin(self, key):
        return get_base_admin_dc_by_iadmin(key, iadmin=self.iadmin)

    @property
    def IDAdmin(self)->adminclass.IDAdmin:
        ret = self.get_base_admin_dc_by_iadmin('IDAdmin')
        return ret

    @property
    def BaseAdmin(self) -> adminclass.BaseAdmin:
        ret = self.get_base_admin_dc_by_iadmin('BaseAdmin')
        return ret

    @property
    def CsvImportExportAdmin(self):
        ret = get_base_admin_dc_by_iadmin('CsvImportExportAdmin')
        return ret


