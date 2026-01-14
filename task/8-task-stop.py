from task.app.main import run
from task.app.utils import get_model_name_from_input, get_stop_from_input


#  User massage example: Explain the key components of a Large Language Model architecture
#  Stop examples: "\n\n", ["**Embedding Layer**", "**Transformer Blocks**", "**Training**"]

model = get_model_name_from_input()
stop = get_stop_from_input()

run(
    deployment_name=model.value,
    print_only_content=False,
    stop=stop,
)
