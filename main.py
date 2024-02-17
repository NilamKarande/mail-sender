from flask import Flask,render_template,request
from flask_mail import Mail,Message

app=Flask(__name__)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='nilam@devangles.com'
app.config['MAIL_PASSWORD']='Nilam@1497'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)

@app.route('/home', methods=['GET','POST'])
@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        form_name = request.form["name"]
        form_email = request.form["email"]
        form_subject = request.form["subject"]
        form_message =request.form["message"]

        msg=Message("hey",sender=form_email,recipients=['nilam@devangles.com'])
        msg.subject=form_subject
        msg.body=form_message
        mail.send(msg)

        return "sent mail"
    return render_template('index.html')

if __name__=='__main__':
    app.run(host="127.0.0.6", port=8080,debug=True)

