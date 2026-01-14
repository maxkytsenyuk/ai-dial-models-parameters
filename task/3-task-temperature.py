from task.app.main import run
from task.app.utils import get_model_name_from_input, get_temperature_from_input

#  User massage example: Describe the sound that the color purple makes when it's angry

model = get_model_name_from_input()
temperature = get_temperature_from_input()

run(
    deployment_name=model.value,
    temperature=temperature,
    print_only_content=True,
)