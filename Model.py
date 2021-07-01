import pickle as pk
model=pk.load(open('model','rb'))
age=int(input("Age of the person:"))
gender=int(input("gender of the person(Male=1 & Female=0):"))
predict=model.predict([[age,gender]])
print(predict)