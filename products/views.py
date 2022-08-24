import json,traceback

from django.http       import HttpResponse, JsonResponse
from django.views      import View
from django.db         import transaction

from db_models.models import Company,RecruitmentStatus, JobNotice, District, Position, Skill, NoticeDistrict, NoticePosition, NoticeSkill  
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
            company_id   = Company.objects.get(name=company_name).id
            
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
                    job_notice_id = notice.id,
                    district_id   = district.id,
                )for district in districts]
                
                NoticeDistrict.objects.bulk_create(notice_district)
                
                position_names  = data['position_names']
                positions       = Position.objects.filter(name__in=position_names)
                notice_position = [NoticePosition(
                    job_notice_id = notice.id,
                    position_id   = position.id,
                )for position in positions]
                
                NoticePosition.objects.bulk_create(notice_position)
                
                skill_names  = data['skill_names']
                skills       = Skill.objects.filter(name__in=skill_names)
                notice_skill = [NoticeSkill(
                    job_notice_id = notice.id,
                    skill_id      = skill.id,
                )for skill in skills]
                
                NoticeSkill.objects.bulk_create(notice_skill)
            
            return HttpResponse(status=201)
        except KeyError:
            return JsonResponse({'message':"KeyError"}, status=400)
        except NoneFieldError as e:
            return JsonResponse({'message':e.message}, status=e.status)
        except NoneObjectsError as e:
            return JsonResponse({'message':e.message}, status=e.status)
        except Exception as e:
            traceback.print_exc()
    
    def patch(self, ):
        try:
            """ 채용공고를 수정
            Note:
                1. 근무지, 채용 포지션, 사용기술은 복수 요청이 가능함
                
            Todo:
                1. 다대다 관계에 있는 지역, 포지션, 사용기술을 일괄 수정할 수 있게 할 것
                    bulk_update를 쓴다면 기존에 없던 값이 추가가 되는 경우는 어떻게 처리할 것인가
                
            Key:
                job_notice_id  : 채용공고의 아이디
                title          : 채용공고의 제목
                reward         : 채용보상금
                description    : 공고 내용
                district_names : 근무 지역 (복수 입력 가능)
                position_names : 채용 포지션 (복수 입력 가능)
                skill_names    : 사용 기술 (복수 입력 가능)
                
            History:
                2022-08-24(김지성): 초기 작성
            """
            data           = json.loads(request.body)
            notice_id      = data["job_notice_id"]
            title          = data["title"]
            reward         = data["reward"]
            description    = data["description"]
            district_names = data["district_names"]
            position_names = data["position_names"]
            skill_names    = data["skill_names"]
            
            notice = JobNotice.objects.get(id=notice_id)
            
            districts       = District.objects.filter(name__in=district_names)
            positions       = Position.objects.filter(name__in=position_names)
            skills          = Skill.objects.filter(name__in=skill_names)
            notice_district = [district.id for district in districts]
            notice_position = [position.id for position in positions]
            notice_skill    = [skill.id for skill in skills]
            
            with transaction.atomic():
                notice.title = title
                notice.reward = reward
                notice.description = description
                notice.save()
                NoticeDistrict.objects.filter(job_notice_id=notice_id)\
                            .bulk_update(notice_district,'district_id')
                NoticePosition.objects.filter(job_notice_id=notice_id)\
                            .bulk_update(notice_position,'position_id')
                NoticeSkill.objects.filter(job_notice_id=notice_id)\
                            .bulk_update(notice_skill,'skill_id')
            
            return HttpResponse(status=200)
        except KeyError:
            return JsonResponse({'message':"KeyError"}, status=400)
        except NoneFieldError as e:
            return JsonResponse({'message':e.message}, status=e.status)
        except NoneObjectsError as e:
            return JsonResponse({'message':e.message}, status=e.status)
        except Exception as e:
            traceback.print_exc()
    
    def delete(self, request):
        try:
            """ 채용공고를 삭제
            Note:
                
            Todo:
                
            Key:
                job_notice_ids  : 채용공고의 아이디(다수 입력 가능)
                
            History:
                2022-08-24(김지성): 초기 작성
            """
            notice_ids  = request.GET.get('job_notice_ids').split(',')
            notice_qs   = JobNotice.objects.filter(id__in=notice_ids)
            district_qs = NoticeDistrict.objects.filter(job_notice_id__in=notice_ids)
            position_qs = NoticePosition.objects.filter(job_notice_id__in=notice_ids)
            skill_qs    = NoticeSkill.objects.filter(job_notice_id__in=notice_ids)
            
            if not notice_qs:
                return JsonResponse({"message" : "JOB_NOTICES_DOES_NOT_EXIST"}, status=404)
            
            notice_qs.delete()
            district_qs.delete() 
            position_qs.delete() 
            skill_qs.delete()    
            
            return HttpResponse(status=200)
        except NoneFieldError as e:
            return JsonResponse({'message':e.message}, status=e.status)
        except NoneObjectsError as e:
            return JsonResponse({'message':e.message}, status=e.status)
        except Exception as e:
            traceback.print_exc()



