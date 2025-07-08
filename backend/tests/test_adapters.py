def test_adapter_schema():
    from backend.schemas.adapter import AdapterSpec
    adapter = AdapterSpec(
        adapter_name="png_to_bmp",
        description="Convert PNG to BMP",
        input_keys=["image"],
        output_keys=["result"],
        version="1.0"
    )
    assert adapter.adapter_name == "png_to_bmp"
