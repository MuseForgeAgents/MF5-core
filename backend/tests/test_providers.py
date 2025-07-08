def test_replicate_sync():
    from backend.api.providers.replicate import service
    result = service.get_cached_collections()
    assert isinstance(result, list)
