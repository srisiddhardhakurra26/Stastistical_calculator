from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required

from application.bp.sample_calc.forms import SampleForm
from application.database import User, SampleCalc

sample_size = Blueprint('sample_size', __name__, template_folder='templates')


@sample_size.route('/sample_size', methods=['POST', 'GET'])
@login_required
def sample_size_page():
    form = SampleForm()
    if form.validate_on_submit():
        sample_calc = SampleCalc(z_score=form.z_score.data, margin_error=form.margin_error.data, std=form.std.data,
                                 population_size=form.population_size.data)
        current_user.sample_calcs.append(sample_calc)
        current_user.save()
        return redirect(url_for('sample_size.my_sample_calcs'))

    return render_template('sample_form.html', form=form)


@sample_size.route('/my_sample_calcs')
@login_required
def my_sample_calcs():
    calculations = current_user.sample_calcs
    results = []
    titles = [('z_score', 'Z Score'), ('margin_error', 'Margin Error'), ('standard_deviation', 'Std Dev'), ('population', 'Population'), ('sample_size', 'Sample Size')]
    for result in calculations:
        formatted_result = {
            "z_score": result.z_score,
            "margin_error": result.margin_error,
            "standard_deviation": result.std,
            "population": result.population_size,
            "sample_size": result.calc_sample_size
        }
        results.append(formatted_result)
    return render_template('my_sample_calcs.html', results=results, titles=titles)

