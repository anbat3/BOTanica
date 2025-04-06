# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import json
from rasa_sdk import Action

class ActionRequestInfoFlower(Action):
    def name(self):
        return "action_request_info_flower"

    def run(self, dispatcher, tracker, domain):
        user_flower = tracker.get_slot("flower")
        attribute = tracker.get_slot("atribute")

        if not user_flower:
            dispatcher.utter_message(text="¿Qué flor te interesa?")
            return []

        # Manejo de posibles errores al abrir el archivo
        try:
            with open("flowers.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            dispatcher.utter_message(text="Hubo un problema al leer la información de las flores.")
            return []

        # Crear un diccionario para acceder fácilmente a cada flor
        flowers = {item["name"].lower(): item for item in data}
        flower_info = flowers.get(user_flower.lower())

        if not flower_info:
            dispatcher.utter_message(text="No encontré información sobre esa flor.")
            return []

        if not attribute:
            # Si no se especifica un atributo, devolvemos toda la información
            respuesta = (
                f"🌸 {flower_info['name']}:\n"
                f"Temporada: {flower_info['season']}\n"
                f"Cuidado: {flower_info['care']}\n"
                f"Simbolismo: {flower_info['symbolism']}\n"
                f"Toxicidad: {flower_info['toxicity']}\n"
                f"Descripción: {flower_info['description']}"
            )
        else:
            attribute = attribute.lower()
            # Mapeo de posibles palabras clave a los atributos del JSON
            mapping = {
                "cuidado": "care",
                "cuidados": "care",                
                "cuida": "care",
                "simbolismo": "symbolism",
                "simbolice": "symbolism",
                "simboliza": "symbolism",
                "significado": "symbolism",
                "significa": "symbolism",
                "temporada": "season",
                "descripción": "description",
                "descripcion": "description",
                "toxico": "toxicity",
                "tóxico": "toxicity",
                "toxicidad": "toxicity",
                "tóxica": "toxicity",
                "toxica": "toxicity"
            }
            clave = mapping.get(attribute)
            if clave and clave in flower_info:
                respuesta = f"{clave.capitalize()}: {flower_info[clave]}"
            else:
                respuesta = "No entiendo qué aspecto quieres saber de esa flor."

        dispatcher.utter_message(text=respuesta)
        return []

