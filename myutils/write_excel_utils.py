# /usr/bin/python
# -*- coding:utf-8 -*-
"""
    Created by qinshuang on 6/7/16.
"""

import xlsxwriter

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO


class WriterXLSX(object):
    """ 使用自定义 Writer XLSX """

    def __init__(self, output_type='io', file_name=""):
        """
            :param output_type:  输出类型，'io' ---  文件流; 'file' --- 文件;
        """
        if output_type == 'io':
            self.f = StringIO.StringIO()
        elif output_type == 'file':
            self.f = open(file_name, 'w')

        self.workbook = xlsxwriter.Workbook(self.f)

    def add_sheet(self, *args, **kwargs):
        return self.workbook.add_worksheet(*args, **kwargs)

    @property
    def bold_format(self):
        """ 粗体 """
        return self.workbook.add_format({'bold': True})

    @property
    def merge_format(self):
        """  """
        # 合并单元格格式化
        return self.workbook.add_format({'align': 'center', 'valign': 'vcenter'})

    @property
    def backgroup_color(self):
        """  """
        return self.workbook.add_format({'bg_color': 'cccccc'})

    def add_format(self, kwargs):
        """  """
        return self.workbook.add_format(kwargs)

    def close(self):
        self.workbook.close()
        return self.f


if __name__ == "__main__":
    a = WriterXLSX('file', 'safass.xlsx')
    workbook = a.workbook

    worksheet = workbook.add_worksheet()

    # Widen the first column to make the text clearer.
    worksheet.set_column('A:A', 20)

    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': True})

    # Write some simple text.
    worksheet.write('A1', 'Hello')

    # Text with formatting.
    worksheet.write('A2', 'World', bold)

    # Write the data to a sequence of cells.
    data = ('Foo', 'Bar', 'Baz')
    worksheet.write_column('B1', data)

    # 合并单元格
    worksheet.merge_range(3, 3, 1, 5, 'test1',
                          a.add_format({'align': 'center', 'valign': 'vcenter', 'bg_color': 'cccccc'}))

    # Write some numbers, with row/column notation.
    worksheet.write(2, 0, 123)
    worksheet.write(3, 0, 123.456)

    a.close()
