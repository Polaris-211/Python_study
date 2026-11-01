#单继承
# class Phone:
#     IMEI = None
#     producer = "APPL"
#
#     def call_by_4g(self):
#         print("4g通话")
#
# class Phone2022(Phone):
#     face_id = "10001"
#
#     def call_by_5g(self):
#         print("2022年新功能")
#
# phone = Phone2022()
# print(phone.producer)
# phone.call_by_4g()
# phone.call_by_5g()
#
# #多继承
# class NFCReader:
#     nfc_type = "第五代"
#     producer = "HM"
#
#     def read_card(self):
#         print("NFC读卡")
#
#     def write_card(self):
#         print("NFC写卡")
#
# class RemoteControl:
#     rc_type = "红外遥控"
#
#     def control(self):
#         print("红外遥控开启")
#
# class MyPhone(Phone, NFCReader, RemoteControl):
#     pass
#
# phone = MyPhone()
# phone.call_by_4g()
# phone.read_card()
# phone.write_card()
# phone.control()
# print(phone.producer) #同名成员左边的优先级最高

class Phone:
    IMEI = None
    producer = "APPL"

    def call_by_5g(self):
        print("使用5g通话")

class MyPhone(Phone):
    producer = "HM"

    def call_by_5g(self):
        # print("开启单核模式")
        #
        # print("使用5g通话")
        # print("关闭单核模式")
        # Phone.call_by_5g(self)
        print(f"父类：{super().producer}")
        super().call_by_5g()

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)



