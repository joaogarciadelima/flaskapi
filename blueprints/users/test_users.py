from blueprints.users.models import User


def test_save_user(client, db_session):
    resp = client.get('/usuarios/joao')
    assert resp.status_code == 200


def test_save_user_model(client, db_session):
    client.get('/usuarios/joao')
    assert User.query.count() == 1


def test_session_access(flask_session):
    flask_session['a_key'] = 'a value'
    assert flask_session['a_key'] == 'a value'
