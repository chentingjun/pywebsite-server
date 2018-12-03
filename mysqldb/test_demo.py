# -*- coding: utf-8 -*-
from comm_functions import OpSql
opsql = OpSql()
res = opsql.selectSql('SELECT * FROM user_info')
print(res)