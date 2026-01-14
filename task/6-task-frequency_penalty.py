from task.app.main import run
from task.app.utils import get_model_name_from_input, get_penalty_from_input


#  User massage example: Explain the water cycle in simple terms for children

model = get_model_name_from_input()
frequency_penalty = get_penalty_from_input()

run(
    deployment_name=model.value,
    print_only_content=True,
    frequency_penalty=frequency_penalty,
)
