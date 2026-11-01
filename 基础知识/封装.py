# class Phone:
#     __current_voltage = 0#私有成员变量
#
#     def __keep_single_core(self): #私有成员方法
#         print("让CPU以单核模式运行")
#
#     def call_by_5G(self):
#         if self.__current_voltage >= 1: #私有成员/方法可以在类中使用
#             print("5G通话已开启")
#         else:
#             self.__keep_single_core()
#             print("电量不足")
# phone = Phone()
# # phone.__keep_single_core()
# # print(__current_voltage)
#
# phone.call_by_5G ()

class Phone:
    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭，使用4g网络")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()
phone.call_by_5g()
