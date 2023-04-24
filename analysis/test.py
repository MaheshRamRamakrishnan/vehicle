import rsa
# from analysis.models import *

publicKey, privateKey = rsa.newkeys(512)

# message = mechanical_analysis.objects.all()
# print(message.car_name)
message = ["mahesh", "ram","20000"]
for i in message:
    encMessage = rsa.encrypt(i.encode(), publicKey)
    print("original string: ", i)
    print("encrypted string: ", encMessage)

    decMessage = rsa.decrypt(encMessage, privateKey).decode()
    print("decrypted string: ", decMessage)
