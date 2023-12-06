import networkx as nx
import matplotlib.pyplot as plt
import math
from datetime import datetime, timedelta


distancias = {
    ("Curitiba/PR", "Londrina/PR"): 380,
    ("Londrina/PR", "Curitiba/PR"): 380,

    ("Foz do Iguaçu/PR", "União da Vitória/PR"): 450,
    ("União da Vitória/PR", "Foz do Iguaçu/PR"): 450,
    ("União da Vitória/PR", "Curitiba/PR"): 250,
    ("Curitiba/PR", "União da Vitória/PR"): 250,

    ("Joinville/SC", "Curitiba/PR"): 130,
    ("Curitiba/PR", "Joinville/SC"): 130,

    ("Joinville/SC", "União da Vitória/PR"): 280,
    ("União da Vitória/PR", "Joinville/SC"): 280,

    ("Joinville/SC", "Curitiba/PR"): 130,
    ("Curitiba/PR", "Joinville/SC"): 130,

    ("Joinville/SC", "Londrina/PR"): 520,
    ("Londrina/PR", "Joinville/SC"): 520,


    ("Joinville/SC", "Chapecó/SC"): 500,
    ("Chapecó/SC", "Joinville/SC"): 500,

    ("Porto Alegre/RS", "Chapecó/SC"): 450,
    ("Chapecó/SC", "Porto Alegre/RS"): 450,

    ("Porto Alegre/RS", "Uruguaiana/RS"): 630,
    ("Uruguaiana/RS", "Porto Alegre/RS"): 630,

    ("Porto Alegre/RS", "Pelotas/RS"): 260,
    ("Pelotas/RS", "Porto Alegre/RS"): 260,

    ("Uruguaiana/RS", "Pelotas/RS"): 550,
    ("Pelotas/RS", "Uruguaiana/RS"): 550,
}

custo_por_km = 20 
km_por_dia = 500   



G = nx.DiGraph()

for (cidade_origem, cidade_destino), distancia in distancias.items():
    G.add_edge(cidade_origem, cidade_destino, weight=distancia)

def encontrar_menor_caminho(grafo, origem, destino):
    try:
        caminho = nx.shortest_path(grafo, source=origem, target=destino, weight='weight')
        distancia = nx.shortest_path_length(grafo, source=origem, target=destino, weight='weight')
        return caminho, distancia
    except nx.NetworkXNoPath:
        return None, None

def calcular_distancia(grafo, origem, destino):
    _, distancia = encontrar_menor_caminho(grafo, origem, destino)
    return distancia

def calcular_custo(grafo, origem, destino, custo_por_km):
    distancia = calcular_distancia(grafo, origem, destino)
    if distancia is not None:
        custo = distancia * custo_por_km
        return custo
    else:
        return None

def calcular_dias_viagem(grafo, origem, destino, km_por_dia):
    distancia = calcular_distancia(grafo, origem, destino)
    if distancia is not None:
        dias = math.ceil(distancia / km_por_dia)
        return dias
    else:
        return None


def calcular_tempo_chegada(origem, destino, km_por_dia):
    distancia = calcular_distancia(G, origem, destino)
    if distancia is not None:
        dias_viagem = math.ceil(distancia / km_por_dia)
        agora = datetime.now()
        chegada = agora + timedelta(days=dias_viagem)
        return chegada
    else:
        return None

def exibir_caminho(grafo, caminho):

    subgrafo = grafo.edge_subgraph(zip(caminho, caminho[1:]))
    

    plt.figure(figsize=(10, 6))
    pos = nx.spring_layout(subgrafo)
    labels = nx.get_edge_attributes(subgrafo, 'weight')
    nx.draw_networkx_edge_labels(subgrafo, pos, edge_labels=labels)
    nx.draw(subgrafo, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=8, font_color='black', arrows=True)

    plt.title(f"Mapa do Caminho de {caminho[0]} para {caminho[-1]} (em km)")
    plt.show()

cidades_info = {
    "Curitiba/PR": {
        "nome": "Curitiba",
        "cd": "Rua Azul Royal 982",
        "la": """25°26'12.8"S""",
        "lo": """49°15'51.8"W"""
    },
    "Londrina/PR": {
        "nome": "Londrina",
        "cd": "Rua Verde Radiante 123",
        "la": """23°18'36.8"S""",
        "lo": """51°10'56.1"W"""
    },
    "Foz do Iguaçu/PR": {
        "nome": "Foz do Iguaçu",
        "cd": "Avenida Laranja Doce 445",
        "la": """25°31'19.3"S""",
        "lo": """54°35'08.5"W"""
    },
    "União da Vitória/PR": {
        "nome": "União da Vitória",
        "cd": "Rua Amarelo Dourado 7515",
        "la": """26°13'36.2"S""",
        "lo": """51°05'28.8"W"""
    },
    "Joinville/SC": {
        "nome": "Joinville",
        "cd": "Rua Roxo Negro 150",
        "la": """26°18'42.9"S""",
        "lo": """48°50'33.8"W"""
    },
    "Chapecó/SC": {
        "nome": "Chapecó",
        "cd": "Rua Branco Azulado 15",
        "la": """27°06'40.8"S""",
        "lo": """52°36'28.4"W"""
    },
    "Porto Alegre/RS": {
        "nome": "Porto Alegre",
        "cd": "Rua Doce Laranja 689",
        "la": """30°04'12.6"S""",
        "lo": """51°13'04.4"W"""
    },
    "Uruguaiana/RS": {
        "nome": "Uruguaiana",
        "cd": "Rua Verde Creme 515",
        "la": """29°46'01.6"S""",
        "lo": """57°05'10.5"W"""
    },
    "Pelotas/RS": {
        "nome": "Pelotas",
        "cd": "Rua Fim do Mundo 9999",
        "la": """31°46'50.7"S""",
        "lo": """52°20'40.5"W"""
    },
}


def exibir_informacoes_cidade(cidade):
    if cidade in cidades_info:
        info = cidades_info[cidade]
        result = (
            f"Informações sobre {cidade}:\n"
            f"Nome: {info['nome']}\n"
            f"Centro de Distribuição: {info['cd']}\n"
            f"Latitude: {info['la']}\n"
            f"Longitude: {info['lo']}\n"
        )
        return result
    else:
        return f"Informações sobre {cidade} não encontradas.\n"




def maps(origemc, destinoc):
    origem = origemc
    destino = destinoc

    caminho, distancia = encontrar_menor_caminho(G, origem, destino)
    custo = calcular_custo(G, origem, destino, custo_por_km)
    dias_viagem = calcular_dias_viagem(G, origem, destino, km_por_dia)
    chegada = calcular_tempo_chegada(origem, destino, km_por_dia)

    if caminho and distancia is not None and custo is not None and dias_viagem is not None and chegada is not None:

        print(exibir_informacoes_cidade(origem))
        
        print(exibir_informacoes_cidade(destino))

        print(f"Caminho de {origem} para {destino}:\n{', '.join(caminho)}\n")

        print(f"Distância total percorrida: {distancia} km")
        print(f"Custo total: R${custo:.2f}")
        print(f"Total de dias gastos na viagem: {dias_viagem} dias")
        print(f"Previsão de chegada: {chegada.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        

        exibir_caminho(G, caminho)
    else:
        print(f"Caminho de {origem} para {destino} não encontrado.")