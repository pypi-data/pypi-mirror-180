#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
from .warehouse import stock as s
import re
# ----------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------
# 类 rstock
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2021-04-11 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)           | 版本显示
# ----------------------------------------------------------------------------------------------------
class rstock():
    """
    rstock类，库存报表。
    """
    def __init__(self, dict):
        self.__version = "0.1"
        self.__dict = dict
        self.__stock = {}
# ----------------------------------------------------------------------------------------------------
    def __recode2define(self, item):
        """
        重新编码，从官方库存数据编码转换成自定义编码。
        """
        info = {}
        info['分类'] = item['分类（必填）']
        info['名称'] = item['名称（必填）']
        #info['条码'] = item['条码']
        info['进货价'] = int(float(item['进货价（必填）']))
        info['销售价'] = int(float(item['销售价（必填）']))
        info['毛利率'] = item['毛利率']
        info['批发价'] = int(float(item['批发价']))
        info['会员价'] = int(float(item['会员价']))
        info['会员折扣'] = item['会员折扣']
        info['积分商品'] = item['积分商品']
        info['供货商'] = item['供货商']
        info['拼音码'] = item['拼音码']
        info['商品状态'] = item['商品状态']
        info['商品描述'] = item['商品描述']
        size = item['尺码']
        num  = int(item['库存量'])
        return info,size,num
# ----------------------------------------------------------------------------------------------------
    def build(self, path):
        """
        库存总表。
        """
        errors = []
        rstock = {}
        stock = s().build(path)
        # 逐条读取库存信息
        for barcode in stock:
            item = stock[barcode]
            info,size,num = self.__recode2define(item)
            supplier = info['供货商']
            article  = info['名称']
            # 商品不存在需初始化
            if article not in rstock:
                rstock[article] = [info, 0, {}]
            # 与已记录商品信息是否一致？
            if rstock[article][0] != info:
                # 出现不一致信息，记录错误
                errors.append([barcode])
                errors.append(list(rstock[article][0].keys()))
                errors.append(list(rstock[article][0].values()))
                errors.append(list(info.keys()))
                errors.append(list(info.values()))
                errors.append([])
                continue
            # 尺码是否还未记录？
            if size not in rstock[article][2]:
                sum = rstock[article][1]
                rstock[article][1] = sum + num
                rstock[article][2][size] = num
            else:
                raise Exception('尺码{0}已存在:{1}'.format(size, rstock[article][2]))
        # 处理同一商品的不同尺码信息
        sizes = self.__dict['size'].keys()
        for article in rstock:
            item = rstock[article]
            info = item[0]
            info['总库存'] = item[1]
            # 所有已知尺码
            for size in sizes:
                info[size] = None
            # 所有存在尺码
            for size in item[2]:
                # 尺码必须已知
                if size not in info:
                    continue
                info[size] = item[2][size]
            self.__stock[article] = info
        # 汇总成表
        form = []
        for article in self.__stock:
            keys   = list(self.__stock[article].keys())
            values = list(self.__stock[article].values())
            if form != []:
                if keys != form[0]:
                    raise Exception('标题不一致:\n{0}\n{1}'.format(keys, form[0]))
                form.append(values)
            else:
                form.append(keys)
                form.append(values)
        return form,errors
# ----------------------------------------------------------------------------------------------------
    def abstract(self):
        """
        库存摘要。
        """
        # 逐条扫描商品记录并按分类汇总
        suppliers = {}
        for article in self.__stock:
            item   = self.__stock[article]
            title  = item['分类']
            price  = int(item['销售价'])
            number = int(item['总库存'])
            if title in suppliers:
                info = suppliers[title]
                suppliers[title]['款数'] = info['款数'] + 1
                suppliers[title]['件数'] = info['件数'] + number
                suppliers[title]['总价'] = info['总价'] + number * price
            else:
                suppliers[title] = {}
                suppliers[title]['款数'] = 1
                suppliers[title]['件数'] = number
                suppliers[title]['总价'] = number * price
        # 汇总分类并输出成表
        all = {'款数':0, '件数':0, '总价':0}
        abstract = [['分类', '款数', '件数', '总价']]
        for title in sorted(suppliers.keys()):
            one = suppliers[title]
            all['款数'] = all['款数'] + one['款数']
            all['件数'] = all['件数'] + one['件数']
            all['总价'] = all['总价'] + one['总价']
            abstract.append([title, one['款数'], one['件数'], one['总价']])
        abstract.append(['总计', all['款数'], all['件数'], all['总价']])
        return abstract
# ----------------------------------------------------------------------------------------------------
    def classify(self):
        """
        库存分类。
        """
        sizes = self.__dict['size'].keys()
        # 逐条扫描商品记录并按分类归并
        suppliers = {}
        for article in self.__stock:
            item   = self.__stock[article]
            title  = item['分类']
            if title not in suppliers:
                suppliers[title] = [dict.fromkeys(sizes, 0)]
            suppliers[title].append(item)
            # 标记非空白尺码
            for size in sizes:
                if item[size] != None:
                    suppliers[title][0][size] = 1
        # 汇总分类并输出成表
        classify = {}
        for key in sorted(suppliers.keys()):
            no = re.search('\d+', key).group()
            classify[no] = []
            # 处理空白尺码
            deletes = ['批发价']
            for size in sizes:
                if suppliers[key][0][size] <= 0:
                    deletes.append(size)
            # 按分类逐条扫描
            for item in suppliers[key][1:]:
                for d in deletes:
                    del item[d]
                keys   = list(item.keys())
                values = list(item.values())
                if classify[no] == []:
                    classify[no] = [keys]
                elif keys != classify[no][0]:
                    raise Exception('标题不一致:\n{0}\n{1}'.format(keys, classify[no][0]))
                classify[no].append(values)
        return classify
# ----------------------------------------------------------------------------------------------------



# ----------------------------------------------------------------------------------------------------
# 类 report
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2021-04-11 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 已测试 | Version(self, ...)           | 版本显示
# ----------------------------------------------------------------------------------------------------
class report():
    """
    report类，报表处理。
    """
    def __init__(self):
        self.__version = "0.1"
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def stock(dict, path):
        """
        库存报表。
        """
        names = []
        forms = []
        r = rstock(dict)

        stock,error = r.build(path)
        names.append('总库存')
        forms.append(stock)
        if error:
            names.append('错误')
            forms.append(error)
        
        abstract = r.abstract()
        names.append('摘要')
        forms.append(abstract)

        classify = r.classify()
        for key in classify:
            names.append(key)
            forms.append(classify[key])

        return names,forms
# ----------------------------------------------------------------------------------------------------
