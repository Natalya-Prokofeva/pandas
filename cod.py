import pandas as pd
import random

# Генерация исходного DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Преобразование столбца в one hot вид без использования get_dummies
one_hot_encoded = data['whoAmI'].apply(lambda x: pd.Series({'robot': 1 if x == 'robot' else 0, 
                                                            'human': 1 if x == 'human' else 0}))

# Объединяем с исходным DataFrame
final_data = pd.concat([data, one_hot_encoded], axis=1)

# Печатаем результат первые пять строк
print("\nOne Hot Encoded данные:")
print(final_data.head())
  
