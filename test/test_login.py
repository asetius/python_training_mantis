

def test_login(app):
    app.session.login("administrator", "Astana08")
    assert app.session.is_logged_in_as("administrator")