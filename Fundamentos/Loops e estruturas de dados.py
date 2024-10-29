
# TEXTOS FORNECIDOS
texto1 = "1 - Uma infecção curada de dengue confere ao paciente imunidade contra o tipo de vírus responsável. Por existirem quatro tipos diferentes de vírus, para estar totalmente imunizado, é necessário ter tido contato com todos eles. Caso contrário, a cada contágio com um novo tipo de vírus, os sintomas são mais intensos e o risco de desenvolver a dengue grave é mais alto."
texto2 = "2 - Já num sentido amplo, lei é somente a regra jurídica escrita, excluindo-se dessa aceção, portanto, o costume jurídico. Por fim, numa aceção técnica e específica, a palavra lei designa uma modalidade de regra escrita, que apresenta determinadas características; no direito brasileiro, são técnicas apenas a lei complementar e a lei ordinária."
texto3 = "3 - Na linha do tempo do futebol feminino brasileiro, ele passou tanto tempo proibido quanto regulamentado: 38 anos. De 1941 a 1979, a lei nacional não permitia a prática do esporte por mulheres devido às “condições da sua natureza”. Já o regulamento da modalidade, que permanece válido até 2021, só foi feito em 1983. "
texto4 = "4 - A lei dos cossenos é uma expressão matemática que relaciona os três lados de um triângulo qualquer. Por não estar restrita ao triângulo retângulo, a lei dos cossenos pode ser entendida como uma generalização do teorema de Pitágoras."

# LISTA
textos = [texto1, texto2, texto3, texto4]


def apresentacao():

    print("📝⚙️  Vamos descobrir juntos qual dos seguintes textos é sobre direito, iremos analisar 4 textos. 👩‍💻🛠️ \n")

    print("-"*90,"\n")

def contemlei(texto, palavra):
    palavras_separadas = texto.split(" ")
    quantidade = 0
    for i in palavras_separadas:
        if i.lower() == palavra.lower():
            quantidade += 1

    print(f'🔍 No texto "{texto}" a palavra "{palavra}" se repete {quantidade} vezes. 📝 \n')


apresentacao()

contemlei(texto1, "lei")
contemlei(texto2, "lei")
contemlei(texto3, "lei")
contemlei(texto4, "lei")


def texto_direito_constitucional(textos, palavra):
    textos_contados = []
    for texto_possivel in textos:
        palavras_separadas = texto_possivel.split(" ")
        quantidade = 0

        for i in palavras_separadas:
            if i.lower() == palavra.lower():
                quantidade += 1

        textos_contados.append(quantidade)

    texto_escolhido = textos_contados.index(max(textos_contados))
    print(f'⚙️  RESPOSTA = O texto 💡 "{textos[texto_escolhido]}" é o que mais houve a recorrência da palavra "{palavra}" 📝.')


texto_direito_constitucional(textos, "lei")
