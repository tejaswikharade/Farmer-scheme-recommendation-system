

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import seaborn as sns
import pickle
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
def data():

    schemes_df = pd.read_csv("schemes.csv",usecols=['schemeid','title'],dtype={'schemeid': 'int32', 'title': 'str'})
    ratings_df=pd.read_csv("ratings.csv",usecols=['userid', 'schemeid', 'rating'],
        dtype={'userid': 'int32', 'schemeid': 'int32', 'rating': 'float32'})

    df = pd.merge(ratings_df,schemes_df,on='schemeid')



    df.tail(), ratings_df.tail(),schemes_df.tail()

    combine_scheme_rating = df.dropna(axis = 0, subset = ['title'])
    scheme_ratingCount = (combine_scheme_rating.
         groupby(by = ['title'])['rating'].
         count().
         reset_index().
         rename(columns = {'rating': 'totalRatingCount'})
         [['title', 'totalRatingCount']]
        )




    rating_with_totalRatingCount = combine_scheme_rating.merge(scheme_ratingCount, left_on = 'title', right_on = 'title', how = 'left')


    (rating_with_totalRatingCount)




    pd.set_option('display.float_format', lambda x: '%.3f' % x)

    popularity_threshold = 0
    rating_popular_scheme= rating_with_totalRatingCount.query('totalRatingCount >= @popularity_threshold')
    scheme_features_df=rating_popular_scheme.pivot_table(index='title',columns='userid',values='rating').fillna(0)
    scheme_features_df_matrix = csr_matrix(scheme_features_df.values)
    model_knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute')
    model_knn.fit(scheme_features_df_matrix)
    return model_knn,scheme_features_df


def predict(query_index):
    model_knn,scheme_features_df=data()

    #print(query_index)
    distances, indices = model_knn.kneighbors(scheme_features_df.iloc[query_index,:].values.reshape(1, -1), n_neighbors = 5)


    # In[90]:
    ans=[]



    for i in range(0, len(distances.flatten())):
        if i == 0:
            print('Recommendations for {0}:\n'.format(scheme_features_df.index[query_index]))
            ans.append('Recommendations for {0}:\n'.format(scheme_features_df.index[query_index]))
        else:
            print('{0}: {1}'.format(i, scheme_features_df.index[indices.flatten()[i]]))
            ans.append('{0}: {1}'.format(i, scheme_features_df.index[indices.flatten()[i]]))
    return ans

    