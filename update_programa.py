import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

head_end = html.find('</head>')
head = html[:head_end + 7]

nav_start = html.find('<nav class="nav"')
nav_end = html.find('<!-- HERO -->')
nav = html[nav_start:nav_end]

# Update nav links to point to index.html sections
nav = nav.replace('href="#inicio"', 'href="index.html#inicio"')
nav = nav.replace('href="#sobre"', 'href="index.html#sobre"')
nav = nav.replace('href="#servicos"', 'href="index.html#servicos"')
nav = nav.replace('href="#depoimentos"', 'href="index.html#depoimentos"')
nav = nav.replace('href="#contato"', 'href="index.html#contato"')

footer_start = html.find('<footer>')
footer_end = html.find('</footer>') + 9
footer = html[footer_start:footer_end]

# Update footer links
footer = footer.replace('href="#servicos"', 'href="index.html#servicos"')
footer = footer.replace('href="#contato"', 'href="index.html#contato"')
footer = footer.replace('href="#sobre"', 'href="index.html#sobre"')
footer = footer.replace('href="#depoimentos"', 'href="index.html#depoimentos"')

scripts_start = html.find('<script>')
scripts = html[scripts_start:]

content_html = """
    <main style="padding-top: 120px; padding-bottom: 80px; min-height: 70vh;">
      <div class="container" style="background: var(--white); padding: 60px; border-radius: 8px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); max-width: 800px;">
        <h1 style="font-family: var(--ff-head); color: var(--ink); font-size: 2rem; margin-bottom: 10px; border-bottom: 2px solid var(--gold); padding-bottom: 10px;">
          PROGRAMA DE ASSESSORIA DE GESTÃO INTEGRADA
        </h1>
        <p style="color: var(--ink3); font-family: var(--ff-mono); font-size: 0.85rem; margin-bottom: 40px; text-transform: uppercase; letter-spacing: 0.05em;">
          Estrutura da Página do Site – Graficosnet
        </p>

        <h2 style="font-family: var(--ff-head); color: var(--ink); font-size: 1.5rem; margin-top: 30px; margin-bottom: 15px;">
          1. ABERTURA DA PÁGINA
        </h2>
        <p style="color: var(--ink); font-weight: 600; margin-bottom: 5px;">Programa de Assessoria de Gestão Integrada</p>
        <p style="color: var(--ink3); margin-bottom: 20px;">Desenvolvimento contínuo para empresas que querem evoluir de forma estruturada.</p>

        <h2 style="font-family: var(--ff-head); color: var(--ink); font-size: 1.5rem; margin-top: 40px; margin-bottom: 15px;">
          2. APRESENTAÇÃO DO PROGRAMA
        </h2>
        <p style="color: var(--ink); font-weight: 600; margin-bottom: 5px;">Objetivo da seção:</p>
        <p style="color: var(--ink3); margin-bottom: 15px;">Explicar o conceito do programa.</p>
        
        <p style="color: var(--ink); font-weight: 600; margin-bottom: 10px;">Pontos principais:</p>
        <ul style="color: var(--ink3); list-style-type: disc; padding-left: 20px; line-height: 1.8;">
          <li>Programa de acompanhamento contínuo</li>
          <li>Formato trimestral, semestral ou anual</li>
          <li>Integração entre finanças, comercial, produção e gestão de pessoas</li>
          <li>Desenvolvimento contínuo da equipe de gestores</li>
          <li>Modelo híbrido: treinamentos + reuniões privadas + suporte consultivo</li>
        </ul>
      </div>
    </main>
"""

new_html = head + '\n<body>\n' + nav + '\n' + content_html + '\n' + footer + '\n' + scripts

with open('programa.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
