import pickle
database = {'gordon': {'6attempted': 5, '5attempted': 5, 'logins': 17, '9attempted': 5, '4attempted': 5, '1attempted': 8, '8attempted': 6, '0attempted': 3, '3attempted': 2, '2attempted': 5, '7attempted': 5}}
pickle.dump(database, open('userData/database.p', 'wb'))
