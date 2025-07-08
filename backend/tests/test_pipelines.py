def test_pipeline_crud():
    from backend.api.pipelines import service
    service.create_pipeline("test", {"steps": []})
    data = service.get_pipeline("test")
    assert "steps" in data
    service.delete_pipeline("test")
