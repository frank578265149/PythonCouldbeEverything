# -*- coding: utf-8 -*-
"""
Created by hushiwei on 2017/7/20
"""

import re


arr='''
tmp_publisher_type201707191500508355
tmp_publisher_type201707201500480001
tmp_publisher_type201707201500481801
tmp_publisher_type201707201500483601
tmp_publisher_type201707201500485401
tmp_publisher_type201707201500487201
tmp_publisher_type201707201500489001
tmp_publisher_type201707201500490801
tmp_publisher_type201707201500492601
tmp_publisher_type201707201500494401
tmp_publisher_type201707201500496201
tmp_publisher_type201707201500498001
tmp_publisher_type201707201500499801
tmp_publisher_type201707201500501601
tmp_publisher_type201707201500503401
tmp_publisher_type201707201500505201
tmp_publisher_type201707201500507001
tmp_publisher_type201707201500508801
tmp_publisher_type201707201500510601
tmp_publisher_type201707201500512401
tmp_publisher_type201707201500514201
tmp_publisher_type201707201500517801
tmp_publisher_type201707201500523201
tmp_publisher_type201707201500525001
tmp_publisher_type201707201500528601
tmp_publisher_type201707201500530401
tmp_publisher_type201707201500532201
tmp_publisher_type201707201500534001
tmp_publisher_type201707201500535801
tmp_publisher_type201707301501410601
tmp_publisher_type201707301501491873
tmp_publisher_type201707311501504201
tmp_publisher_type201708091502256601
tmp_publisher_type201708091502258401
tmp_publisher_type201708091502330548'''
pattern=re.compile(r"tmp.*")

m=pattern.findall(arr)

print m