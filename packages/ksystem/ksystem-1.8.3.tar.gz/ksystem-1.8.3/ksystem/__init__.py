# Copyright (c) 2019-2020 ZouMingzhe <zoumingzhe@qq.com>
# This module is part of the k-system package, which is released under a MIT licence.

"""
for core
"""
from  ksystem.core.warehouse        import  (stock, entry)
from  ksystem.core.report           import  (report)

"""
for database
"""
from  ksystem.database.codeDB       import  (sizeDB, classDB, supplierDB)
from  ksystem.database.productDB    import  (productDB)

"""
for process
"""
from  ksystem.process.code          import  (code)
