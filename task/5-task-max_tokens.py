from task.app.main import run
from task.app.utils import get_model_name_from_input, get_max_tokens_from_input


#  User massage example: What is token when we are working with LLM?

model = get_model_name_from_input()
max_tokens = get_max_tokens_from_input()

run(
    deployment_name=model.value,
    max_tokens=max_tokens,
)
