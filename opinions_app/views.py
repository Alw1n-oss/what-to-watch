from random import randrange

from flask import abort, redirect, render_template, url_for

from opinions_app import app, db
from opinions_app.forms import OpinionForm
from opinions_app.models import Opinion


@app.route("/")
def index_view():
    quantity = Opinion.query.count()
    if not quantity:
        abort(500)
    offset_value = randrange(quantity)
    opinion = Opinion.query.offset(offset_value).first()
    # Вот он — возврат функции.
    return render_template("opinion.html", opinion=opinion)


@app.route("/add", methods=["GET", "POST"])
def add_opinion_view():
    form = OpinionForm()
    # Если ошибок не возникло...
    if form.validate_on_submit():
        # ...то нужно создать новый экземпляр класса Opinion...
        opinion = Opinion(
            # ...и передать в него данные, полученные из формы.
            title=form.title.data,
            text=form.text.data,
            source=form.source.data,
        )
        # Затем добавить его в сессию работы с базой данных...
        db.session.add(opinion)
        # ...и зафиксировать изменения.
        db.session.commit()
        # Затем переадресовать пользователя на страницу добавленного мнения.
        return redirect(url_for("opinion_view", id=opinion.id))
    # Если валидация не пройдена - просто отрисовать страницу с формой.
    return render_template("add_opinion.html", form=form)


# Тут указывается конвертер пути для id.
@app.route("/opinions/<int:id>")
# Параметром указывается имя переменной.
def opinion_view(id):
    # Теперь можно запросить нужный объект по id...
    opinion = Opinion.query.get_or_404(id)
    # ...и передать его в шаблон (шаблон - тот же, что и для главной страницы).
    return render_template("opinion.html", opinion=opinion)
