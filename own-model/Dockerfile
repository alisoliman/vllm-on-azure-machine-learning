FROM vllm/vllm-openai:latest

ENV MODEL_PATH /model/opt-125m

ENTRYPOINT python3 -m vllm.entrypoints.openai.api_server --model $MODEL_PATH $VLLM_ARGS
