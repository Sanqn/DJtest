# import psycopg2
# from psycopg2 import OperationalError
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
#
# a = 'testperson'
#
#
# def create_connection(db_name, db_user, db_password, db_host, db_port):
#     connection = None
#     try:
#         connection = psycopg2.connect(
#             database=db_name,
#             user=db_user,
#             password=db_password,
#             host=db_host,
#             port=db_port,
#         )
#         print('Connection to PosrgresQL DB successfull')
#         cursor = connection.cursor()
#         # print(connection.get_dsn_parameters(), "\n")
#         # Выполнение SQL-запроса
#         cursor.execute(
#             "SELECT table_name FROM information_schema.tables WHERE table_schema NOT IN ('information_schema', 'pg_catalog')")
#         # Получить результатn
#         for x in cursor:
#             print(x)
#         # Получить результат
#         # cursor.execute("SELECT * from test3")
#         # record = cursor.fetchall()
#         # print("Результат", record)
#
#         # cursor.execute("DROP TABLE test8")
#         # connection.commit()
#
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#     return connection
# #
# #
# # # con = create_connection("DB1", "postgres", "root", "127.0.0.1", "5432")
# con = create_connection("dc81ggqrnpkve6", "qkaxzsjgiqguhb", "8192f49013a9aa4af326f7b1bb58c32ba4afec96bb149e5e07cbef072591a47e",
#                         "ec2-18-204-142-254.compute-1.amazonaws.com", "5432")
#
#
# def execute_query_users(connection):
#     users = [
#         ("Col", "Cam"),
#     ]
#     user_records = ", ".join(["%s"] * len(users))
#     insert_query = (
#         f"INSERT INTO test (name, last_name) VALUES {user_records}"
#     )
#     connection.autocommit = True
#     cursor = connection.cursor()
#     cursor.execute(insert_query, users)
#
#
# execute_query_users(con)
#
#
# # def create_table(connection, query):
# #     connection.autocommit = True
# #     cursor = connection.cursor()
# #     try:
# #         cursor.execute(query)
# #     except OperationalError as e:
# #         print(f"The error '{e}' occurred")
# #
# # create_test_table = """
# # CREATE TABLE IF NOT EXISTS test (
# #   id SERIAL PRIMARY KEY,
# #   name VARCHAR(100),
# #   last_name VARCHAR(100)
# # )
# # """
# #
# # create_table(con, create_test_table)

# a = {'name': 'vasia', 'last': 'kim'}
# c = [v for k, v in a.items()]
# c = [tuple(c)]
# print(c)

# def dec_func(func):
#     def wrapper(*args):
#         print(args)
#         for i in args:
#             print(i * 5)
#
#         func(*args)
#
#     return wrapper
#
#
# @dec_func
# def test_fun(x, y, z):
#     pass
#
#
# test_fun(4, 5, 6)
# def big_dec(a, b):
#     print('Big_dec', a + b)
#
#     def dec_func(func):
#         print('dec_func', a * b)
#
#         def wrapper(*args):
#             for i in args:
#                 print('Умножим аргументы: ', i * 5)
#             print('Это из big_dec', a * 2, b * 2)
#             func(*args)
#
#         return wrapper
#
#     return dec_func
#
#
# @big_dec(5, 6)
# def new_fun(a, b, c):
#     pass


# new_fun(1, 2, 3)
# import datetime
# import time
#
# a = ('Alex6', 'Alex6', 'dada@6mail.com', '+375291811450')
# b = datetime.datetime.now()
# a = a + (str(b),)

# b = [[0 for _ in range(5)] for _ in range(5)]
# for i in b:
#     print(*i)

import jwt
jwt_fb = 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImJmMWMyNzQzYTJhZmY3YmZmZDBmODRhODY0ZTljMjc4ZjMxYmM2NTQiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoi0KjQsNC70LjQvNC-INCd0LjQutC40YLQsCIsInBpY3R1cmUiOiJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDM1OTQ5NTI0MzkwNTIvcGljdHVyZSIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS96bnMtYXV0aCIsImF1ZCI6Inpucy1hdXRoIiwiYXV0aF90aW1lIjoxNjU4Mzk4MTI4LCJ1c2VyX2lkIjoiOHNxd3puU2RFZ2dxM0hOcEd3ZmtXTmJyRDBkMiIsInN1YiI6IjhzcXd6blNkRWdncTNITnBHd2ZrV05ickQwZDIiLCJpYXQiOjE2NTgzOTgxMjgsImV4cCI6MTY1ODQwMTcyOCwiZW1haWwiOiJtZWdhZnJvc3RiYWxsQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJmYWNlYm9vay5jb20iOlsiMTAzNTk0OTUyNDM5MDUyIl0sImVtYWlsIjpbIm1lZ2Fmcm9zdGJhbGxAZ21haWwuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiZmFjZWJvb2suY29tIn19.TmhKNZu1uGDrzwuAiiDaMQTVSk9A_d4fGi_6q4-Nj2p4-dz1IZlELmf9D0mAXnX4Ik98sR3gsBMiJbwWwx4m8WMD_pjWP_Pox9LgiLIgqJVYw2U4nuhr3QwOC5gSImS-j2aNHGK-mFS0hYZN6pWxCOxs9J2VKaAgSjmqtIKMF1hQgyp0TB41F67ORUgcT2D38eqL8zPaOXDDr_Q_tq600kl6D35Fz7-QyCQ3VhTP1OdTZx9ac7KTMjDtfoXXUWCqaIKwBrWQFczKv-T8Z_jFzSFABJ2EquPzP99Sq8Y-OjpKu6Ru32-JJphvuINLlyeGukA7jkijQmoUEoxDQQaEDQ'
# __jwt = 'eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICIyMVRaNkI1RUItWUgyR0hqYlhNRFktdGVPQ3dwS2ZaR0FpZjhESkI2VDBzIn0.' \
#         'eyJleHAiOjE2NTc3MzkzNDAsImlhdCI6MTY1NzczOTA0MCwianRpIjoiMDUwN2U0NjAtNzhjYi00YzgzLWFhMmUtNzdjNzcyYjAxOGZjIiwiaXNzIj' \
#         'oiaHR0cHM6Ly9pZC5waXhvbW5pYS5jb20vcmVhbG1zL2RlZmF1bHQiLCJhdWQiOiJhY2NvdW50Iiwic3ViIjoiOWY3NjNjOGEtODc5MC00NTc0LTg5Nzc' \
#         'tYzA4NjgxN2Y4OTQ3IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoicGl4b21uaWEtYXBwLWlvcyIsInNlc3Npb25fc3RhdGUiOiJhM2QzYWRhMy0zODA3LTQ1' \
#         'ZmUtODczNS00ODFmNWFiYzZjYTUiLCJhY3IiOiIxIiwicmVhbG1fYWNjZXNzIjp7InJvbGVzIjpbIm9mZmxpbmVfYWNjZXNzIiwiZGVmYXVsdC1yb2xlcy' \
#         '1kZWZhdWx0IiwidW1hX2F1dGhvcml6YXRpb24iXX0sInJlc291cmNlX2FjY2VzcyI6eyJhY2NvdW50Ijp7InJvbGVzIjpbInZpZXctYXBwbGljYXRpb25z' \
#         'Iiwidmlldy1jb25zZW50Iiwidmlldy1wcm9maWxlIl19fSwic2NvcGUiOiJwcm9maWxlIGVtYWlsIiwic2lkIjoiYTNkM2FkYTMtMzgwNy00NWZlLTg' \
#         '3MzUtNDgxZjVhYmM2Y2E1IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJuYW1lIjoicGl4b21uaWEgcGl4b21uaWEiLCJwcmVmZXJyZWRfdXNlcm5hbWU' \
#         'iOiJwaXhvbW5pYWRldkBnbWFpbC5jb20iLCJnaXZlbl9uYW1lIjoicGl4b21uaWEiLCJmYW1pbHlfbmFtZSI6InBpeG9tbmlhIiwiZW1haWwiOiJwaXh' \
#         'vbW5pYWRldkBnbWFpbC5jb20ifQ.ePCga8iaqAtiB5AvGtSFii4nz70J4mzdRvpbrI064_4sJrje2oWn15-Sg9OsCEzkUYVah9a8obYvccUE_ASkfpRZH' \
#         'rlgTseKksw4hynuKX17Kjw_uQKdWAEemJoEpFTtzj7SOBezEC7vhKl0EELSvcJ4AcWtp2Wosego0EDfy-LO_160-BpMyuZZG-vTw0jVTmhfjwOkmoeae' \
#         'us0q6D6LBZt9ntUpsdXBXRq-CmAB8AI9TN1_Y1Jx7BU0tWkQ3RtTyISiNvMK8PyWQibZwcJe7iA0YHwK_hfpYNVTj5dPbCrBev0neAICA85Z3gWPGCNmS' \
#         'kTng0MPzaqiv15ld68uw'

decoded = jwt.decode(jwt_fb, options={"verify_signature": False})
print(decoded)
email = decoded['email']
username = decoded['name']
print(email, username)
# from auth_project.auth_project.settings import SECRET_KEY
# encoded_jwt = jwt.encode({'exp': 1657739340, 'iat': 1657739040, 'jti': '0507e460-78cb-4c83-aa2e-77c772b018fc', 'iss': 'https://id.pixomnia.com/realms/default'}, SECRET_KEY, algorithm="HS256", headers={"kid": "230498151c214b788dd97f22b85410a5"})
# print(encoded_jwt)
# a = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NTc3MzkzNDAsImlhdCI6MTY1NzczOTA0MCwianRpIjoiMDUwN2U0NjAtNzhjYi00YzgzLWFhMmUtNzdjNzcyYjAxOGZjIiwiaXNzIjoiaHR0cHM6Ly9pZC5waXhvbW5pYS5jb20vcmVhbG1zL2RlZmF1bHQifQ.5pliMDBvC2F_O1BHYtQdtB7JBLCtuDRTjN-gC0rSoMQ'
# decoded_jwt = jwt.decode(a, options={"verify_signature": False})
# print(decoded_jwt)
# token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ik5FRTFRVVJCT1RNNE16STVSa0ZETlRZeE9UVTFNRGcyT0Rnd1EwVXpNVGsxUWpZeVJrUkZRdyJ9.eyJpc3MiOiJodHRwczovL2Rldi04N2V2eDlydS5hdXRoMC5jb20vIiwic3ViIjoiYVc0Q2NhNzl4UmVMV1V6MGFFMkg2a0QwTzNjWEJWdENAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZXhwZW5zZXMtYXBpIiwiaWF0IjoxNTcyMDA2OTU0LCJleHAiOjE1NzIwMDY5NjQsImF6cCI6ImFXNENjYTc5eFJlTFdVejBhRTJINmtEME8zY1hCVnRDIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.PUxE7xn52aTCohGiWoSdMBZGiYAHwE5FYie0Y1qUT68IHSTXwXVd6hn02HTah6epvHHVKA2FqcFZ4GGv5VTHEvYpeggiiZMgbxFrmTEY0csL6VNkX1eaJGcuehwQCRBKRLL3zKmA5IKGy5GeUnIbpPHLHDxr-GXvgFzsdsyWlVQvPX2xjeaQ217r2PtxDeqjlf66UYl6oY6AqNS8DH3iryCvIfCcybRZkc_hdy-6ZMoKT6Piijvk_aXdm7-QQqKJFHLuEqrVSOuBqqiNfVrG27QzAPuPOxvfXTVLXL2jek5meH6n-VWgrBdoMFH93QEszEDowDAEhQPHVs0xj7SIzA"
# token_jwt = jwt.decode(token, options={"verify_signature": False})
# print(token_jwt)
# new_request = {}
# a = ['email', 'given_name', 'sid']
# for k, v in decoded.items():
#     if k in [i for i in a]:
#             if k == 'given_name':
#                 print(k)
#                 new_request['username'] = new_request.get('username', v)
#             else:
#                     new_request[k] = new_request.get(k, v)
# print(new_request)

# class PageNumberSetPagination(pagination.PageNumberPagination):
#     page_size = 5
#     page_size_query_param = 'page_size'
#     ordering = 'date_added_post_db'
#
#
# class NewView(APIView):
#     pagination_class = PageNumberSetPagination
#
#     def get(self, request):
#
#         link = f'https://tlgrm.ru/channels/@showtimeinfo'
#         browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
#         browser.get(link)
#         time.sleep(1)
#         for i in range(2):
#             botton_next = browser.find_element(By.CLASS_NAME, "cfeed-loadmore-tear__button")
#             browser.execute_script("return arguments[0].scrollIntoView(true);", botton_next)
#             botton_next.click()
#             time.sleep(1)
#         time_create_post = browser.find_elements(By.XPATH, '//div[@channel_id="1143557060"]/header/section/footer/time')
#         title_post = browser.find_elements(By.CSS_SELECTOR, ".cpost-wt-text > b")
#         dick_post = browser.find_elements(By.CSS_SELECTOR, ".cpost-wt-text")
#         print(len(time_create_post), len(title_post), len(dick_post))
#         for i in range(len(time_create_post)):
#             time_cr = time_create_post[i].text
#             # print(i, '---------', time_create_post[i].text, title_post[i].text, dick_post[i].text)
#             old_create_time = ''
#             for k, v in data_time.items():
#                 if k == time_cr:
#                     old_create_time = datetime.now() - timedelta(minutes=v)
#             om = title_post[i].text
#             di_post = dick_post[i].text
#             di_post = (di_post.split('\n\n'))[1:-1]
#             di_post1 = ''.join(di_post)
#             check = New.objects.filter(name_public=om)
#             if not check:
#                 New.objects.create(name_public=om, information_post=di_post1, date_create_post=old_create_time)
#         all_news = New.objects.all()
#         serializer = NewSerializer(all_news, many=True)
#         return Response({'news': serializer.data})
# import time
# import datetime
# from datetime import datetime, timedelta
# a = '56 минут назад'
# if 'мин' in a:
#     min = int(a.split()[0])
#     old_create_time = datetime.now() - timedelta(minutes=min)
#     print(old_create_time)



