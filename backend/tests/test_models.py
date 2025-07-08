def test_list_models():
    from backend.api.models import service
    models = service.list_models()
    assert isinstance(models, list)
