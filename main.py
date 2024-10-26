from flask import Flask, render_template, request, redirect, url_for
import tool # Actual Encryption Tool
from werkzeug.utils import secure_filename

# Initialise the tool ui
TOOL = Flask(__name__)

@TOOL.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        GIVEN_DATA = {
            "Text_To_Cipher": request.form['user_text'],
            "Req_Type": request.form['oprt'],
            "Key_Image": request.files['image']
        }

        if GIVEN_DATA['Text_To_Cipher'] and GIVEN_DATA["Key_Image"].filename != '':
            # Secure the image
            secure_filename(GIVEN_DATA["Key_Image"].filename)

            if GIVEN_DATA["Req_Type"] == "ENCR":
                # Perform the encryption
                resulted_encryption = tool.Encryption_Algorithm(GIVEN_DATA["Text_To_Cipher"], GIVEN_DATA["Key_Image"])
                return redirect(url_for('result', result=resulted_encryption))

            elif GIVEN_DATA["Req_Type"] == "DECR":
                # Perform the decryption
                plain_txt = tool.Unecryption_Algorithm(GIVEN_DATA["Text_To_Cipher"], GIVEN_DATA["Key_Image"])
                return redirect(url_for('result', result=plain_txt))

        return redirect(url_for('result', result="No file uploaded or text entered."))

    # Render the main form page
    return render_template('main.html')

# Route for result
@TOOL.route('/result')
def result():
    result_text = request.args.get('result', '')
    # Pass down result to html page, where it will be used during the rendering
    return render_template('ending.html', result=result_text)


if __name__ == '__main__':
    TOOL.run(debug=True)
