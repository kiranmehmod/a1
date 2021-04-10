from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def add2logFile(string2add):
    f = open("logs.txt", "a")
    f.write(str(string2add))
    f.close()

@app.route('/')
def main():
    return render_template('app.html')

@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if operation == 'add':
            sum = float(num1) + float(num2)
            ip_address = request.remote_addr
            log = "TimeStamp " + str(datetime.datetime.now()) + " Requester IP Address = " + str(ip_address) + " Sum performaned " + "\n"
            add2logFile(log)
            return render_template('app.html',sum=sum)

        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            ip_address = request.remote_addr
            log = "TimeStamp " + str(datetime.datetime.now()) + " Requester IP Address = " + str(ip_address) + " Subtract performaned " + "\n"
            add2logFile(log)
            return render_template('app.html', sum=sum)

        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            ip_address = request.remote_addr
            log = "TimeStamp " + str(datetime.datetime.now()) + " Requester IP Address = " + str(ip_address) + " Multiply performaned" + "\n"
            add2logFile(log)
            return render_template('app.html', sum=sum)

        elif operation == 'divide':
            sum = float(num1) / float(num2)
            ip_address = request.remote_addr
            log = "TimeStamp " + str(datetime.datetime.now()) + " Requester IP Address = " + str(ip_address) + " Divide  performaned" + "\n"
            add2logFile(log)
            return render_template('app.html', sum=sum)
        else:
            return render_template('app.html')
        
if __name__ == ' __main__':
    app.debug = True
    app.run()
