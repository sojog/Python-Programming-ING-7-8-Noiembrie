
# varsta = 18
# # In ce interval este  0-18, 18-35, 35-50, 50-100

# if varsta < 18:
#     print("minor")
# else:
#     if varsta < 35:
#         print("major pana in 35")
#     else:
#         if varsta < 50:
#             print("major intre 35 si 50")
#         else:
#             print("peste 50 de ani")

varsta = 18

if varsta < 18:
    print("minor")
elif varsta >=18 and varsta < 35:
    print("major pana in 35")
elif varsta >=35 and varsta < 50:
    print("major intre 35 si 50")
else:
    print("peste 50 de ani")
