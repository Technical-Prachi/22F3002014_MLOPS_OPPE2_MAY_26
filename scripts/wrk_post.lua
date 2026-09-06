wrk.method = "POST"
wrk.headers["Content-Type"] = "application/json"

wrk.body = '{"sno":1000,"age":55,"gender":"male","cp":1,"trestbps":130,"chol":250,"fbs":0,"restecg":1,"thalach":150,"exang":0,"oldpeak":1.0,"slope":2,"ca":0,"thal":2}'

request = function()
    return wrk.format(nil, "/predict")
end
