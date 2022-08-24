from django.urls import path

from products.views import (
                        JobNoticeView,
                        JobNoticeListView,
                        JobNoticeDetailView,
                        JobNoticeSearchView,
                        )

"""url
    Note:
        JobNoticeView       : 채용 공고 등록, 수정, 삭제
        JobNoticeListView   : 채용 공고 리스트
        JobNoticeDetailView : 채용 공고 상세페이지
        JobNoticeSearchView : 채용 공고 검색 기능
"""

urlpatterns = [
    path('/jobnotice', JobNoticeView.as_view()),
    path('/jobnoticelist', JobNoticeListView.as_view()),
    path('/jobnotice/<int:job_notice_id>', JobNoticeDetailView.as_view()),
    path('/search', JobNoticeSearchView.as_view()),
]
