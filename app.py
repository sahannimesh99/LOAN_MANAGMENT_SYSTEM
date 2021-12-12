import uuid

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

accounts = [
    {'id': uuid.uuid4().hex, 'username': 'Santha', 'password': 'test', 'amount': 100},
    {'id': uuid.uuid4().hex, 'username': 'Chaminda', 'password': 'test1', 'amount': 200},
   
]
loans = []


@app.route('/')
def landingpage():
    return render_template('landingpage.html')


def add_loans_to_context(context, account):
    context['loans'] = loans
    total_loans = 0
    my_loan = None
    for i in loans:
        total_loans = total_loans + i['amount']
        if i['account']['id'] == account['id']:
            my_loan = i
    context['total_loans'] = total_loans
    context['my_loan'] = my_loan
    return context


@app.route('/home', methods=['GET', 'POST'])
def home():
    context = {
        'accounts': accounts,
        'loans': loans
    }
    uid = request.values.get('id')
    if uid is None:
        return redirect('/')
    account = None
    bulk_amount = 0
    for acc in accounts:
        if uid == acc['id']:
            account = acc
        bulk_amount = bulk_amount + acc['amount']
    if account is None:
        return redirect('/')
    context['account'] = account
    context['bulk_amount'] = bulk_amount
    form = request.values
    context = add_loans_to_context(context, account)
    if form.get('type') == 'pay':
        idx = 0
        for i in loans:
            if i['account']['id'] == uid:
                loans.pop(idx)
                break
            idx = idx + 1
        context = add_loans_to_context(context, account)
        return render_template('home.html', **context)
    if form.get('approved_person') is None:
        return render_template('home.html', **context)
    check_duplicate = False
    for i in loans:
        if i['account']['id'] == account['id']:
            check_duplicate = True
            break
    if check_duplicate:
        return render_template('home.html', **context)
    if form['approved_person'] == account['id']:
        if int(form['amount']) > account['amount']:
            context['error'] = 'Amount is not compatible with our policy. Please select a correct Candidate person'
        else:
            loans.append({
                'id': uuid.uuid4().hex,
                'account': account,
                'amount': int(form.get('amount')),
                'approved_account': account
            })
    else:
        approved_account = None
        for i in accounts:
            if i['id'] == form.get('approved_person'):
                approved_account = i
                break
        if approved_account is None:
            context['error'] = 'Invalid Candidate person'
        else:
            for i in loans:
                if i['account']['id'] == approved_account['id']:
                    context['error'] = 'Candidate person is on another loan. Please choose another candidate person'
                    context = add_loans_to_context(context, account)
                    return render_template('home.html', **context)
            if int(form['amount']) > (account['amount'] + approved_account['amount']):
                context['error'] = 'Amount is high. Please select a different approved person'
            else:
                loans.append({
                    'id': uuid.uuid4().hex,
                    'account': account,
                    'amount': int(form.get('amount')),
                    'approved_account': approved_account
                })
    context = add_loans_to_context(context, account)
    return render_template('home.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = request.form
    for account in accounts:
        if form['username'] == account['username'] and form['password'] == account['password']:
            return redirect('/home?id=' + account['id'])
    context = {
        'error': 'Invalid username or password.'
    }
    return render_template('landingpage.html', **context)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    context = {}
    form = request.form
    for account in accounts:
        if form['username'] == account['username']:
            context['error'] = 'Username already exists'
            return render_template('landingpage.html', **context)
    if form['username'] is None:
        context['error'] = 'Invalid username'
        return render_template('landingpage.html', **context)
    if form['password'] is None:
        context['error'] = 'Invalid password'
        return render_template('landingpage.html', **context)
    if form['amount'] is None:
        context['error'] = 'Invalid amount'
        return render_template('landingpage.html', **context)
    uid = uuid.uuid4().hex
    accounts.append({
        'id': uid,
        'username': form['username'],
        'password': form['password'],
        'amount': int(form['amount'])
    })
    return redirect('/home?id=' + uid)


if __name__ == '_main_':
    app.run(debug=True)