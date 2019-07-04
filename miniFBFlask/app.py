from flask import Flask, render_template, request
from queries import get_user_data_based_on_user_id, \
    get_user_fans_by_user_id, \
    get_who_user_dates_by_user_id, get_who_user_marries_by_user_id, get_user_data_based_on_user_name

app = Flask(__name__)

@app.route('/')
@app.route('/<user_id>')
def show_user(user_id=614754689):
    get_user_data()

    # ID = 1
    #
    # age = 2
    #
    # income = 3

    # fans = ["fan1", "fan2", "fan3"]

    dates = ["date1", "date2", "date3"]

    marriages = ["marriage1", "marriage2", "marriage3"]

    user_query_result = get_user_data_based_on_user_id(user_id)

    ID = user_query_result[0]

    age = user_query_result[3]

    income = user_query_result[4]

    name = user_query_result[2]

    fan_query_result = get_user_fans_by_user_id(user_id)

    dates_query_result = get_who_user_dates_by_user_id(user_id)

    marriage_query_result = get_who_user_marries_by_user_id(user_id)



    return render_template("index.html", name = name ,ID = ID,
                           age=age, income=income, fans=fan_query_result,
                           dates=dates_query_result, marriages=marriage_query_result)


@app.route("/search", methods = ['POST', 'GET'])
def search():
    name = None
    if request.method == 'POST':
        name = request.form
        user_query_result = get_user_data_based_on_user_name(name)
        ID = user_query_result[0]

        age = user_query_result[3]

        income = user_query_result[4]

        name = user_query_result[2]
        fan_query_result = get_user_fans_by_user_id(ID)

        dates_query_result = get_who_user_dates_by_user_id(ID)

        marriage_query_result = get_who_user_marries_by_user_id(ID)
        if user_query_result is not None:
            return render_template("index.html", name = name ,ID = ID,
                           age=age, income=income, fans=fan_query_result,
                           dates=dates_query_result, marriages=marriage_query_result)
        else:
            return render_template("search.html", screenName = name)

def get_user_data():
    name = request.args.get('name')

    id = request.args.get('ID')
    age = request.args.get('age')
    income = request.args.get('income')
    print(name, id, age, income)

if __name__ == '__main__':
    app.run(debug=True)