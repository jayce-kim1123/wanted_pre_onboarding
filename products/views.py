import json,traceback

from django.http  import JsonResponse
from django.views import View
from django.db    import transaction

from db_models.models import User, Company, RecruitmentStatus, JobNotice, District, Position, Skill, NoticeDistrict, NoticePosition, NoticeSkill  
from common.errors    import NoneFieldError, NoneObjectsError

class JobNoticeView(View):
    def post(self, request):
        try:
            """ 채용공고를 등록
            Note:
                1. 근무지, 채용 포지션, 사용기술은 복수 요청이 가능한 기획이며
                    해당 내용들은 각각 notice_districts, notice_positions, notice_skills 중간 테이블에 저장함
                2. 채용 공고 작성, 근무지, 채용 포지션, 사용기술을 create하는 기능은 transaction으로 원자성 부여
            Todo:
                
            Key:
                title          : 채용공고의 제목
                reward         : 채용보상금
                description    : 공고 내용
                company_name   : 회사 이름
                district_names : 근무 지역 (복수 입력 가능)
                position_names : 채용 포지션 (복수 입력 가능)
                skill_names    : 사용 기술 (복수 입력 가능)
                
            History:
                2022-08-24(김지성): 초기 작성
            """
            data         = json.loads(request.body)
            title        = data['title']
            reward       = data['reward']
            description  = data['description']
            company_name = data['company_name']
            company_id   = Company.objects.get(name=company_name)
            
            with transaction.atomic():
                notice = JobNotice.objects.create(
                    title       = title,
                    reward      = reward,
                    description = description,
                    company_id  = company_id
                )
                
                district_names  = data['district_names']
                districts       = District.objects.filter(name__in=district_names)
                notice_district = [NoticeDistrict(
                    notice_id   = notice.id,
                    district_id = district.id,
                )for district in districts]
                
                NoticeDistrict.objects.bulk_create(notice_district)
                
                position_names  = data['position_names']
                positions       = Position.objects.filter(name__in=position_names)
                notice_position = [NoticePosition(
                    notice_id   = notice.id,
                    position_id = position.id,
                )for position in positions]
                
                NoticePosition.objects.bulk_create(notice_position)
                
                skill_names  = data['skill_names']
                skills       = Skill.objects.filter(name__in=skill_names)
                notice_skill = [NoticeSkill(
                    notice_id = notice.id,
                    skill_id  = skill.id,
                )for skill in skills]
                
                NoticeSkill.objects.bulk_create(notice_skill)
            
            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message':e.message}, status=e.status)
        except NoneFieldError as e:
            return JsonResponse({'message':e.message}, status=e.status)
        except NoneObjectsError as e:
            return JsonResponse({'message':e.message}, status=e.status)
        except Exception as e:
            traceback.print_exc()

class JobNoticeListView(View):
    def get(self, request):
        try:
            """ 채용공고의 리스트를 엔드포인트로 전달
            Note:
                
            Todo:
                1. annotate, aggregate를 사용하여 context의 nested 구조 해결할 수 있는지 확인하기
                
            Return:
                id           : 채용 공고의 id
                company_name : 채용 공고의 채용사
                title        : 채용 공고 제목
                reward       : 채용보상금
                district     : 지역
                position     : 채용포지션
                skill        : 시용기술
                
            History:
                2022-08-24(김지성): 초기 작성
            """
            
            offset = int(request.GET.get('offset', 0))
            limit  = int(request.GET.get('limit', 9)) 
            
            notice_qs   = JobNotice.objects.select_related('company').all()
            
            context = {
                'notice_list': [{
                    'id'          : notice.id,
                    'company_name': notice.company.name,
                    'title'       : notice.title,
                    'district'    : NoticeDistrict.objects.filter(notice_id=notice.id).district.name,
                    'position'    : NoticePosition.objects.filter(notice_id=notice.id).position.name,
                    'skill'       : NoticeSkill.objects.filter(notice_id=notice.id).skill.name,
                    'reward'      : notice.reward,
                } for notice in notice_qs[offset:offset+limit]]
            }
            
            return JsonResponse({'result': context}, status=200)
        except NoneFieldError as e:
            return JsonResponse({'message':e.message}, status=e.status)
        except Exception as e:
            traceback.print_exc()