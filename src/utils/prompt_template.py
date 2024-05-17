from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
import streamlit as st

# On définit notre template
template = """
Tu es un assistant IA avancé, et ta mission est de raffiner le message marketing ci-dessous pour qu'il résonne spécifiquement avec le segment des {segment}. Ce groupe a les caractéristiques suivantes : {caracs_segments} Le message doit communiquer notre compréhension de leurs besoins uniques et notre engagement à offrir des solutions qui respectent leur mode de vie tout en leur fournissant sécurité et facilité.
Instructions supplémentaires pour l'adaptation du message:
Canal Digital Spécifié: Le message doit être adapté pour être diffusé via le canal digital spécifié : {canal}. Cela peut inclure des ajustements de ton ou de format pour s'assurer qu'il est approprié pour ce canal et qu'il capte l'attention de notre segment cible dans cet environnement.
Services Offerts: Assure-toi d'inclure des références spécifiques aux services offerts : {service}, en soulignant comment ces services répondent directement aux besoins et préférences des "Humble Elders".
Objectif de la Compagne: Le message doit être conçu pour atteindre l'objectif de la compagne : {objectif_campagne}.
Format du Message: Adapte le message pour qu'il corresponde au format spécifié : {format}.
Message original:
{prompt_de_specification}
"""


def generate_crea(segment,caracs_segments,canal,prompt_de_specification):
    # On crée un PromptTemplate
    prompt = PromptTemplate.from_template(template)

    # On initialise le modèle OpenAI avec notre clef
    llm = OpenAI(openai_api_key=st.secrets["openai_key"])
    llm_chain = prompt | llm

    # On définit le dictionnaire d'entrée avec les valeurs pour chaque placeholder
    input_data = {
        "caracs_segments" : caracs_segments,
        "segment": segment,
        "canal": canal,
        "service": "Accessible healthcare plans",
        "objectif_campagne": "Increase enrollment among seniors",
        "format": "Plain text email",
        "prompt_de_specification": prompt_de_specification,
    }

    # On invoque la chaine avec le dictionnaire
    result = llm_chain.invoke(input_data)

    return result
