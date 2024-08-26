from django.test import TestCase

# Create your tests here.
from django.urls import reverse
import requests
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import date
from django.utils import timezone
from .models import *
import json

client = APIClient()


# class PatientViewTest(APITestCase):
#     def setUp(self):
#         self.existing_patient = Patients.objects.create(
#             identity_num='123456',
#             identity=1,
#             name='Existing Patient',
#             health_insurance=1,
#             gender=1,
#             birthday=date.today(),
#             phone_num='1234567890',
#             address='Existing Address'
#         )
#         self.valid_data = {
#             'number': '654321',
#             'idType': '身份证',
#             'name': 'New Patient',
#             'paymentType': '非医保',
#             'gender': '女',
#             'birthday': '1985-06-12',
#             'phone': '0987654321',
#             'addr': 'New Address'
#         }

#     # 正向测试：成功添加患者信息
#     def test_successful_patient_addition(self):
#         url = reverse('patient_add')
#         response = self.client.post(url, self.valid_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.json(), {'msg': 'Successfully add patient'})
#         patient = Patients.objects.filter(
#             identity_num=self.valid_data['number']).first()
#         self.assertIsNotNone(patient)

#     # 负向测试：尝试用已存在的证件号码添加患者信息（增加了view.py内返回报错）
#     def test_patient_addition_with_existing_number(self):
#         url = reverse('patient_add')
#         invalid_data = self.valid_data.copy()
#         invalid_data['number'] = self.existing_patient.identity_num
#         response = self.client.post(url, invalid_data, format='json')
#         self.assertEqual(response.status_code, 400)
#         self.assertEqual(response.json(), {
#                          'msg': 'Patient already exists'})


# class RegisterViewTest(APITestCase):
#     def setUp(self):
#         # 准备测试数据
#         # API 服务器地址
#         api_url = 'http://nginx:80/api/administrator_service/test/addDoctor/'
#         # 请求数据（如果需要的话）
#         requestData = {
#             'identity_num': '1234567890',  # 证件号
#             'name': '张三',                # 医生姓名
#             'title': '主任医师',           # 医生职称
#             'department': '内科',          # 医生科室
#             'research': '心脏病研究',     # 研究方向，如果不需要可以省略或设置为None
#             'cost': 200,                   # 出诊费，例如200元
#             'avatar': 'path/to/avatar.jpg',  # 头像图片路径，如果不需要可以省略或设置为None
#             'avatar_name': 'dr_zhang_san.jpg',  # 图片名字
#             'action': 'testAddDoctor'
#         }
#         requests.post(api_url, json=requestData)
#         api_url = "http://nginx:80/api/administrator_service/doctors/getDoctor/"
#         requestData = {
#             'identity_num': '1234567890',  # 证件号
#             'action': 'getDoctor'
#         }
#         respond = requests.post(api_url, json=requestData)
#         self.doctor = respond.json()['doctor']

#         self.patient = Patients.objects.create(
#             identity_num='123456',
#             identity=1,
#             name='Existing Patient',
#             health_insurance=1,
#             gender=1,
#             birthday=date.today(),
#             phone_num='1234567890',
#             address='Existing Address'
#         )

#     def test_add_register_data_success(self):
#         # 正向测试用例：成功添加挂号信息
#         response = self.client.post(reverse('appointment_add'), json.dumps({
#             'action': 'addRegisterData',
#             'number': 1,
#             'inumber': self.patient.identity_num,
#             'identity_num': self.patient.identity_num,
#             'doctorId': self.doctor[0]['id'],
#             'time': "08-20-2024",
#             'starttime': '09:00',
#             'department': 'cat',
#             'cost': 100
#         }), content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('registers', response.json())

#     def test_get_registers_data_success(self):
#         # 正向测试用例：成功获取挂号信息
#         response = self.client.post(reverse('register_list'), json.dumps(
#             {'action': 'getRegistersData', 'identity_num': self.doctor[0]['identity_num']}), content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('registers', response.json())

#     def test_get_registers_data_invalid_action(self):
#         # 负向测试用例：无效的 action 参数
#         response = self.client.post(reverse('register_list'), json.dumps(
#             {'action': 'invalid_action'}), content_type='application/json')
#         self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
#         self.assertEqual(response.json(), {'error': 'Invalid action'})


# class BillViewTestCase(APITestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.patient = Patients.objects.create(
#             identity_num='1234567',
#             identity=1,
#             name='Existing Patient',
#             health_insurance=1,
#             gender=1,
#             birthday=date.today(),
#             phone_num='1234567890',
#             address='Existing Address'
#         )
#         self.patient2 = Patients.objects.create(
#             identity_num='123456',
#             identity=1,
#             name='Existing Patient',
#             health_insurance=1,
#             gender=1,
#             birthday=date.today(),
#             phone_num='1234567890',
#             address='Existing Address'
#         )
#         # API 服务器地址
#         api_url = 'http://nginx:80/api/administrator_service/test/addDoctor/'
#         # 请求数据（如果需要的话）
#         requestData = {
#             'identity_num': '1234567890',  # 证件号
#             'name': '张三',                # 医生姓名
#             'title': '主任医师',           # 医生职称
#             'department': '内科',          # 医生科室
#             'research': '心脏病研究',     # 研究方向，如果不需要可以省略或设置为None
#             'cost': 200,                   # 出诊费，例如200元
#             'avatar': 'path/to/avatar.jpg',  # 头像图片路径，如果不需要可以省略或设置为None
#             'avatar_name': 'dr_zhang_san.jpg',  # 图片名字
#             'action': 'testAddDoctor'
#         }
#         requests.post(api_url, json=requestData)
#         api_url = "http://nginx:80/api/administrator_service/doctors/getDoctor/"
#         requestData = {
#             'identity_num': '1234567890',  # 证件号
#             'action': 'getDoctor'
#         }
#         respond = requests.post(api_url, json=requestData)
#         self.doctor = respond.json()['doctor']

#         self.register = Register.objects.create(
#             queue_id=1,
#             patient=self.patient,
#             register=self.patient,
#             doctor=self.doctor[0]['id'],
#             time=timezone.now(),
#             position="门诊大楼1楼内科"
#         )
#         # API 服务器地址
#         api_url = 'http://nginx:80/api/doctor_service/test/addTreatment'
#         requestData = {
#             'action': 'testAddTreatment',
#             'id': self.register.id,
#             'suggestion': 'Take a rest',
#             'medicines': ['Aspirin', 'Paracetamol'],
#             'totalPrice': 100
#         }
#         respond = requests.post(api_url, json=requestData)

#         self.bill = Bill.objects.create(
#             register=self.register,
#             state=False,
#             patient=self.patient,
#             treatment=respond.json()['treatment_id'],
#             price=100,
#             type=2
#         )

#     def test_get_bills_data_success(self):
#         # 正向测试用例：成功的获取账单数据
#         url = reverse('bill_list')  # 确保使用正确的 URL 名称
#         response = self.client.post(url, {
#             'action': 'getBillsData',
#             'identity_num': self.patient.identity_num
#         }, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertIn('bill', response.json())

#     def test_change_bill_status_success(self):
#         # 正向测试用例：成功的更改账单状态
#         url = reverse('bill_list')
#         self.client.post(url, {
#             'action': 'changeBillStatus',
#             'item_id': self.bill.id
#         }, format='json')
#         self.assertTrue(Bill.objects.get(id=self.bill.id).state)


class NoticeViewTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.patient = Patients.objects.create(
            identity_num='123456',
            identity=1,
            name='Existing Patient',
            health_insurance=1,
            gender=1,
            birthday=date.today(),
            phone_num='1234567890',
            address='Existing Address'
        )
        # API 服务器地址
        api_url = 'http://nginx:80/api/administrator_service/test/addDoctor/'
        # 请求数据（如果需要的话）
        requestData = {
            'identity_num': '1234567890',  # 证件号
            'name': '张三',                # 医生姓名
            'title': '主任医师',           # 医生职称
            'department': '内科',          # 医生科室
            'research': '心脏病研究',     # 研究方向，如果不需要可以省略或设置为None
            'cost': 200,                   # 出诊费，例如200元
            'avatar': 'path/to/avatar.jpg',  # 头像图片路径，如果不需要可以省略或设置为None
            'avatar_name': 'dr_zhang_san.jpg',  # 图片名字
            'action': 'testAddDoctor'
        }
        requests.post(api_url, json=requestData)
        api_url = "http://nginx:80/api/administrator_service/doctors/getDoctor/"
        requestData = {
            'identity_num': '1234567890',  # 证件号
            'action': 'getDoctor'
        }
        respond = requests.post(api_url, json=requestData)
        self.doctor = respond.json()['doctor']

        self.register = Register.objects.create(
            queue_id=1,
            patient=self.patient,
            register=self.patient,
            doctor=self.doctor[0]['id'],
            time=timezone.now(),
            position="门诊大楼1楼内科"
        )
        # API 服务器地址
        api_url = 'http://nginx:80/api/doctor_service/test/addTreatment'
        requestData = {
            'action': 'testAddTreatment',
            'id': self.register.id,
            'suggestion': 'Take a rest',
            'medicines': ['Aspirin', 'Paracetamol'],
            'totalPrice': 100
        }
        respond = requests.post(api_url, json=requestData)

        self.bill = Bill.objects.create(
            register=self.register,
            state=False,
            patient=self.patient,
            treatment=respond.json()['treatment_id'],
            price=100,
            type=2
        )
        self.notice_unread = Notice.objects.create(
            id=1,
            patient=self.patient, doctor=self.doctor[0]['id'], msg_type=1, time=timezone.now(), isRead=False)
        self.notice_read = Notice.objects.create(
            id=2,
            patient=self.patient, doctor=self.doctor[0]['id'], msg_type=2, time=timezone.now(), isRead=True)

    def test_get_notice_data_success(self):
        # 正向测试用例：成功的获取通知数据
        url = reverse('notice_list')  # 确保使用正确的 URL 名称
        response = self.client.post(url, {
            'action': 'getMesData',
            'identity_num': self.patient.identity_num
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('resMes', response.json())
        self.assertIn('billMes', response.json())

    def test_read_notice_success(self):
        # 正向测试用例：成功的标记通知为已读
        url = reverse('add_notice')
        response = self.client.post(url, {
            'action': 'readMes',
            'item_id': self.notice_unread.id
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'msg': 'Successfully read'})
