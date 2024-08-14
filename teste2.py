import subprocess
import xml.etree.ElementTree as ET

def stl_to_gdml(stl_file, gdml_file):
    """Converte um arquivo STL para GDML usando o Geant4."""
    subprocess.run(["gmsh", "-3", stl_file, "-o", gdml_file])

def read_gdml(gdml_file):
    """Lê um arquivo GDML e extrai suas propriedades."""
    properties = {}
    tree = ET.parse(gdml_file)
    root = tree.getroot()

    # Exemplo de extração de propriedades (a serem adaptadas conforme necessário)
    for material in root.iter("material"):
        material_name = material.attrib["name"]
        properties[material_name] = {}
        for prop in material.iter("D"):
            properties[material_name]["density"] = float(prop.attrib["value"])
        # Adicione mais propriedades conforme necessário

    return properties

def generate_simulation_config(properties):
    """Gera o arquivo de configuração para o ambiente de simulação."""
    # Aqui você pode usar as propriedades extraídas para gerar o arquivo de configuração
    # Como exemplo, aqui está a impressão das propriedades
    for material, props in properties.items():
        print(f"Material: {material}")
        for prop, value in props.items():
            print(f"- {prop}: {value}")

if __name__ == "__main__":
    stl_file = r"C:\Users\gusta\OneDrive\Área de Trabalho\Nova pasta\esfera.stl"
    gdml_file = "esfera.gdml"

    # Convertendo o arquivo STL para GDML
    stl_to_gdml(stl_file, gdml_file)

    # Lendo o arquivo GDML e extraindo suas propriedades
    properties = read_gdml(gdml_file)

    # Gerando o arquivo de configuração para o ambiente de simulação
    generate_simulation_config(properties)
