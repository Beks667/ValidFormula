
def is_balanced(text):
    text = "".join(el for el in text if el in "〈({[]})〉")

    while text:
        flag = True
        for el in  "〈〉", "()", "{}", "[]":
            if el in text:
                text = text.replace(el, "")
                flag = False
        if flag:
            return False
    return True


y=is_balanced('((A + B) * [C / D])/{W + K}')
print(y)

# ip_client = self.get_client_ip(request)
# request.data['ip_client'] = ip_client
#
# text = request.data['formula']
#
# text = "".join(el for el in text if el in "〈({[]})〉")
# while text:
#     flag = True
#     for el in "〈〉", "()", "{}", "[]":
#         if el in text:
#             text = text.replace(el, "")
#             flag = False
#     if flag:
#         request.data['status'] = False
#         return Response('error !!!!')
#
# if 'status' not in request.data:
#     request.data['status'] = True
#
# serializer = FormulaValidatorSerializers(data=request.data)
# if serializer.is_valid():
#     serializer.save()
#     return Response(serializer.data)
# else:
#     return Response(serializer.errors, status=400)