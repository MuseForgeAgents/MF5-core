def test_step_format():
    from backend.schemas.pipeline import PipelineStep
    step = PipelineStep(
        step_id="step1",
        type="adapter",
        adapter_name="images_to_video",
        input_keys=["img1", "img2"],
        output_keys=["video"]
    )
    assert step.step_id == "step1"
