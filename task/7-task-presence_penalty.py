from task.app.main import run
from task.app.utils import get_penalty_from_input, get_model_name_from_input


#  User massage example: What is an entropy in LLM's responses?

model = get_model_name_from_input()
presence_penalty = get_penalty_from_input()

run(
    deployment_name=model.value,
    print_only_content=True,
    presence_penalty=presence_penalty,
)
