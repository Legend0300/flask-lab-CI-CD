import pytest
from unittest.mock import MagicMock
from app import app as flask_app

@pytest.fixture
def client():
    flask_app.testing = True
    with flask_app.test_client() as client:
        yield client

def test_health_endpoint_returns_ok_json(client):
    resp = client.get('/health')
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.get_json() == {'status': 'ok'}

def test_home_renders_home_template(monkeypatch, client):
    mock_render = MagicMock(return_value='<html>home</html>')
    monkeypatch.setattr('app.render_template', mock_render)
    resp = client.get('/')
    assert resp.status_code == 200
    assert resp.data.decode() == '<html>home</html>'
    mock_render.assert_called_once_with('home.html')

def test_data_renders_data_template_with_expected_context(monkeypatch, client):
    mock_render = MagicMock(return_value='<html>data</html>')
    monkeypatch.setattr('app.render_template', mock_render)
    resp = client.get('/data')
    assert resp.status_code == 200
    assert resp.data.decode() == '<html>data</html>'
    mock_render.assert_called_once()
    args, kwargs = mock_render.call_args
    assert args[0] == 'data.html'
    assert 'data' in kwargs
    data = kwargs['data']
    assert isinstance(data, dict)
    assert data.get('count') == 3
    assert isinstance(data.get('items'), list)
    assert any(item.get('name') == 'Alice' for item in data['items'])