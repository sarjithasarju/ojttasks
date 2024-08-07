import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

#create sample data
reviews=[
    "i love the movie,it was good",
    "i hate the movie,it was bad",
    "excellent movie avtors done well",
    "i love the movie,it was good",

    

]
labels=[1,0,1,2]
vectorizer=CountVectorizer()
x=vectorizer.fit_transform(reviews)
y=np.array(labels)
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)

#create our model
model=LogisticRegression()
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print(f"accuracy:{accuracy*100:.2f}%")

new_review=["it was a good movie"]
new_review_vectorized=vectorizer.transform(new_review)
prediction=model.predict(new_review_vectorized)
print(f"Prediction: {prediction}")



