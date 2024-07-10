from flask import Flask, render_template, request , redirect, url_for , jsonify
## request library chahiye kyonki agar hume pata lagana hain ki koi bhi request get hain yaa post hain 

## create a simple flask application
app = Flask(__name__)

## __name__ is an entry point for the application
## we have given debug=True, because agar hum aage kuch code change karnege to hume phir baar baar local host ko stop karke dobara port karna padgea baar baar 
# if __name__ == "__main__":
#     app.run(debug=True)


## the app route decorator takes 2 values . The first one takes the value after which the page runs(after the local host(5000 default) address)

## Flask App Routing (important)
@app.route("/", methods=["GET"])
def welcome():
    return "<h1>Welcome to meet Yash</h1>"



@app.route("/index", methods=["GET"])
def index():
    return "<h2>Welcome to the Index page</h2>"


# if __name__ == "__main__":
#     app.run(debug=True)

## Jab humne for examplr ek url hit kiya google.com kaa . Yeh ab server par gya aur ek webpage aa gya .Toh yeh jo request hain isko hum bolte hain GET request
# So jab bhi hum kisi url par hit maarte hain toh woh by default leta hain get request . 
# Ab agar hum kuch search karenge jaise India (google search mein). So humne ek information post kardi hain server par and then according to this keyword kuch content aa gya haim . Isko hum bolte hain post request 


## Variable rule    
@app.route('/success/<score>')    ## The score here is a parameter 
def success(score):
    return "The person has passed and the score is: "+ score


@app.route('/fail/<score>')
def fail(score):
    return "The person has failed and the score is: "+ score


@app.route('/form', methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks = (maths+science+history)/3
        res=""

        if average_marks>=50:
            res="success"
        else:
            res="fail"

        return redirect(url_for(res,score=average_marks))

       # return render_template('form.html', score=average_marks)


## Apis ko hit karne ke liye hum log generally Postman use karte hain
@app.route('/api', method=['POST'])
def calculate_sum():
    data=request.get_json()
    a_val=float(dict(data)['a'])
    b_val=float(dict(data)['b'])
    return jsonify(a_val+b_val)





if __name__=="__main__":
    app.run(debug=True)