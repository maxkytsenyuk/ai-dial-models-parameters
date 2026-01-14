from task.app.main import run
from task.app.utils import get_model_name_from_input, get_choices_from_input, get_seed_from_input


#  User massage example: Name a random animal

model = get_model_name_from_input()
n = get_choices_from_input()
seed = get_seed_from_input()

run(
    deployment_name=model.value,
    n=n,
    seed=seed,
)
