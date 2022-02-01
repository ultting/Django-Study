# git 설치 후 내 git id와 name 을 입력
# 명령어는 git config -- global user.email "my email @ xxxx.com"
# git config -- global user.name "my nick"

# git에 push 하는 법
# Source Control -> + 클릭 -> Commit 메세지 -> Check 표시 

# 장고 서버 실행할떈 python manage.py runserver
# 서버를 멈추고 싶을땐 Ctrl+c
# 서버의 포트를 바꾸고 싶을땐 python manage.py runserver ####

# 표준 라이브러리 import
from __future__ import absolute_import
from math import sqrt
from os.path import abspath
# 코어 장고 임포트
import Django
print(Django.__path__)