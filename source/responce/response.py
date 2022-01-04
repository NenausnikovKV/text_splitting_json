import json



from source.responce.json_parts.final_component import FinalComponent
from source.responce.json_parts.found_component import FoundComponent
from source.responce.json_parts.unfound_component import UnfoundComponent
from source.responce.json_processing import MyJSONEncoder

description = dict()
description["name"] = "Наименование документа"
description["introduction"] = "Введение"
description["main_text"] = "Основной текст"
description["conclusion"] = "Заключение"



class Response:


    def __init__(self, text, found_components = None, unfound_components = None):
        self.text = text
        self.found_components = found_components
        self.unfound_components = unfound_components
        self.description = description

    @classmethod
    def get_json_responce(cls, text, final_components):
        """
        расчитываем и собираем json_responce
        """

        found_components = FoundComponent.get_found_components(text, final_components)

        unfound_components = UnfoundComponent.get_unfound_components(found_components)

        responce = Response(text, found_components, unfound_components)

        return responce


if __name__ == '__main__':

    text_address = "in\\text_property\\text"
    with open(text_address, "r", encoding="utf-8") as read_file:
        text = read_file.read()

    categpries_address = "in\\text_property\\categories\\json_categories"
    with open(categpries_address, "r", encoding="utf-8") as file:
        components = json.load(file)

    # Переписваем рабочие компоненты на договорные с фронтом
    final_components = {name:FinalComponent(name, excerts) for name, excerts in components.items()}

    responce = Response.get_json_responce(text, final_components)

    with open("out/test_responce", "w", encoding="utf-8") as file:
        json.dump(responce, file, ensure_ascii=False, cls=MyJSONEncoder)