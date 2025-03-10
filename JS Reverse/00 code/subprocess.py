# -*- coding: utf-8 -*-
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs
num = 12
ret = subprocess.check_output(f'node "subprocess.js" {num}',shell=True)
print(ret)
