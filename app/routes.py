from flask import render_template, flash, redirect
from app import app
from app.forms import EnterNumberForm
from app.wan_wangEN import wanWang

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():

    form = EnterNumberForm()

    if form.validate_on_submit():

        result = wanWang(form.arabicNumber.data)

        arabic_number = result[0]
        pinyin_number = result[1]
        character_number = result[2]

        return render_template('index.html', title = "Chinese number converter", form = form, arabic_number = arabic_number, pinyin_number = pinyin_number, character_number = character_number)


    return render_template('index.html', title = "Chinese number converter", form = form)
