from django.urls import path

from products.views import (
                        JobNoticeView,
                        )

"""url
    Note:
        JobNoticeView     : 채용 공고 등록, 수정, 삭제
        
"""

urlpatterns = [
    path('/jobnotice', JobNoticeView.as_view()),
]
